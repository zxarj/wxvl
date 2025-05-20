#  Mongoose 搜索注入漏洞复现与修复   
 蚁景网安   2025-05-20 08:31  
  
## 漏洞简介  
  
CVE-2024-53900  
 Mongoose 8.8.3、7.8.3 和 6.13.5 之前的版本容易受到 $where 运算符不当使用的影响。此漏洞源于 $where 子句能够在 MongoDB 查询中执行任意 JavaScript 代码，这可能导致代码注入攻击以及未经授权的数据库数据访问或操纵。  
  
CVE-2025-23061  
 Mongoose 8.9.5、7.8.4 和 6.13.6 之前的版本容易受到 $where 运算符不当使用的影响。此漏洞源于 $where 子句能够在 MongoDB 查询中执行任意 JavaScript 代码，可能导致代码注入攻击以及未经授权的数据库数据访问或操纵。该问题的存在是因为CVE-2024-53900的修复不完整。  
  
Mongoose 是一个用于 Node.js 的 MongoDB 对象建模工具，它使得与 MongoDB 数据库交互变得更加简单和高效。我们可以看到这两个漏洞描述大体相同，都是因为在使用 $where 运算符时出现了问题。  
## 环境搭建  
  
<span data-type="text">安装 MongoDB</span>  
  
不知道是不是本地环境的问题，错误百出，于是还是采用 docker 来安装  
  
docker pull mongo  
  
docker run —name mongodb -d -p 27017:27017 mongo  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6ypjenaic1Zxs7wXCL1bsAK7xZaOONibk4RXicfB09R4TXWNEJJ9NiciaSHzQ/640?wx_fmt=other&from=appmsg "")  
  
快速创建一个项目并指定 mongoose 版本  
```
npm init -y
npm install mongoose@6.13.4--save
node test.js
```  
## 漏洞复现  
  
根据漏洞特点我编写了一个 js 脚本，在不同版本下执行，比较不同情况对应的结果  
```
const mongoose = require("mongoose");

// 连接 MongoDB
const MONGO_URI ="mongodb://localhost:27017/testdb";

async function testWhereInjection(){
  await mongoose.connect(MONGO_URI,{ useNewUrlParser:true, useUnifiedTopology:true});

// 定义 User 模型和 Post 模型
constUserSchema=new mongoose.Schema({
    username:String,
    isAdmin:Boolean,
    password:String
});

constPostSchema=new mongoose.Schema({
    title:String,
    content:String,
    author:{ type: mongoose.Schema.Types.ObjectId, ref:'User'}
});

constUser= mongoose.model("User",UserSchema);
constPost= mongoose.model("Post",PostSchema);

// 插入测试数据
  await User.deleteMany({});
  await Post.deleteMany({});

const users = await User.insertMany([
{ username:"admin", isAdmin:true, password:"admin123"},
{ username:"user1", isAdmin:false, password:"user123"},
{ username:"user2", isAdmin:false, password:"user456"}
]);

  await Post.insertMany([
{ title:"Post 1", content:"Content 1", author: users[0]._id },
{ title:"Post 2", content:"Content 2", author: users[1]._id }
]);

  console.log("√ 已插入测试数据");

// 1. 正常的 populate 查询
try{
const result = await Post.findOne().populate({
      path:'author',
      match:{ username:"admin"}
});
    console.log("√ 正常 populate 查询结果:", result);
}catch(err){
    console.error("× 正常 populate 查询失败:", err.message);
}

// 2. 测试 populate match 中的 $where 注入
try{
const result = await Post.findOne().populate({
      path:'author',
      match:{ $where:"this.isAdmin"}// 修改这里，去掉 return
});
    console.log("√ `$where` populate 查询成功，说明可能存在漏洞:", result);
}catch(err){
    console.error("× `$where` populate 查询被拦截:", err.message);
}

// 3. 测试深层嵌套的 $where 注入
try{
const result = await Post.findOne().populate({
      path:'author',
      match:{
        $and:[
{ nested:{ $where:"this.isAdmin"}}// 修改这里，去掉 return
]
}
});
    console.log("√ 嵌套 `$where` populate 查询成功，说明可能存在漏洞:", result);
}catch(err){
    console.error("× 嵌套 `$where` populate 查询被拦截:", err.message);
}

// 4. 测试数组中的 $where 注入
try{
const result = await Post.findOne().populate({
      path:'author',
      match:[{ $where:"this.isAdmin"}]// 修改这里，去掉 return
});
    console.log("√ 数组中的 `$where` populate 查询成功，说明可能存在漏洞:", result);
}catch(err){
    console.error("× 数组中的 `$where` populate 查询被拦截:", err.message);
}

  await mongoose.disconnect();
}

testWhereInjection().catch(console.error);
```  
### mongoose@6.13.4  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6yyibiaLibPhdSnxeK67YBav5aWdtW2FlKfcVzDfHfGiaWicBddytN4tzeo5A/640?wx_fmt=other&from=appmsg "")  
### mongoose@6.13.5  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6yXh5BeWgib4ts1uzQjqgL1dIftyAibsZXzEmIxKPkE5gWsWg0xDdDZTSA/640?wx_fmt=other&from=appmsg "")  
### mongoose@6.13.6  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6yDlw1ia0MABHIV2eibFsia6lxcWOtWJIshAB6ed2mKfibZRTkHxs2HczGng/640?wx_fmt=other&from=appmsg "")  
  
‍  
  
通过执行结果我们发现，在   
mongoose@6.13.4  
 中，$where 语句可以任意执行语句，经过修复后的   
mongoose@6.13.5  
 中，只能通过嵌套来执行插入的语句，  
mongoose@6.13.6  
 已经修复了通过嵌套执行插入语句的问题。  
## 漏洞分析  
  
https://github.com/Automattic/mongoose/compare/6.13.4...6.13.5?diff=split&w=  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6y2VGwkZiazu5ppRgpPlaITZtfh1libBibib1BFW8ManvNg1E6JTDXS8VCUg/640?wx_fmt=other&from=appmsg "")  
  
第一次进行修复  
- 首先判断 match 是否为一个数组,使用 Array.isArray(match) 进行检查。  
  
- 如果 match 是一个数组,则使用 for…of 循环遍历数组中的每个元素 item。  
  
- 对于每个 item,进行以下检查：  
  
- 如果 item 不为 null (item !\= null),并且 item 对象中存在 \$where 属性 (item.\$where),则抛出一个 MongooseError 异常,错误信息为 “Cannot use \$where filter with populate() match”。这是因为在 populate() 查询中不允许使用 \$where 操作符。  
  
- 如果 match 不是一个数组,则进行另一个判断:  
  
- 如果 match 不为 null (match !\= null),并且 match 对象中存在 \$where 属性 (match.\$where !\= null),同样抛出一个 MongooseError 异常,错误信息为 “Cannot use \$where filter with populate() match”。  
  
‍  
  
进行 populate() 查询时,防止使用 \$where 操作符，检查传入的 match 参数是否包含 \$where 属性,无论 match 是一个数组还是一个对象。如果发现 match 中存在 \$where 属性,就会抛出一个 MongooseError 异常,提示不能在 populate() 查询中使用 \$where 过滤器  
  
https://github.com/Automattic/mongoose/compare/6.13.5...6.13.6?diff=split&w=  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6ybpkdxfx3ZLicp6FpCSK4iciaG5L7C0sWx090JGHmIuVJS78YcGdxUz7kQ/640?wx_fmt=other&from=appmsg "")  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwncZ4I1yEUNbicXtkknST6yeAZjia6UIAIlzV9ORA1ar8MJgvWKfgnxLUMibByZHXicNNOaPSEqQiaaAA/640?wx_fmt=other&from=appmsg "")  
  
第二次修复  
1. 函数接受一个参数 match  
,表示要检查的对象。  
  
1. 首先进行两个条件判断:  
  
1. 如果 match  
 为 null 或 undefined,直接返回,不进行后续检查。  
  
1. 如果 match  
 的类型不是对象,也直接返回,不进行后续检查。这两个判断是为了避免对非对象类型进行遍历和递归。  
  
1. 使用 Object.keys(match)  
 获取 match  
 对象的所有属性键,并使用 for...of  
 循环遍历每个属性键 key  
。  
  
1. 对于每个属性键 key  
,进行以下检查:  
  
1. 如果 key  
 等于 ‘\$where’,表示在 match  
 对象中发现了 \$where 操作符,抛出一个 MongooseError 异常,错误信息为 “Cannot use \$where filter with populate() match”。  
  
1. 如果当前属性的值 match[key]  
 不为 null 或 undefined,并且其类型为对象,则递归调用 throwOn$where  
 函数,将 match[key]  
 作为参数传入,对嵌套的对象进行相同的检查。  
  
通过递归调用 throwOn$where  
 函数,可以对 match  
 对象进行深度遍历,检查其中是否包含 \$where 操作符,无论 \$where 操作符位于对象的哪个层级。  
<table><thead><tr style="background-color: rgb(248, 248, 248);border-top: 1px solid rgb(204, 204, 204);"><th style="text-align: -webkit-match-parent;padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">阶段</span></span></th><th style="text-align: -webkit-match-parent;padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">分析</span></span></th></tr></thead><tbody><tr style="background-color: rgb(255, 255, 255);border-top: 1px solid rgb(204, 204, 204);"><td style="padding: 6px 13px;"><section><span leaf=""><br/></span></section></td><td style="padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">在最初状态下,没有对 populate() 查询中的 \$where 操作符进行任何检查和限制。这意味着用户可以在 match 参数中自由使用 \$where 操作符,但这可能会导致一些安全和性能问题。</span></span></td></tr><tr style="background-color: rgb(248, 248, 248);border-top: 1px solid rgb(204, 204, 204);"><td style="padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">CVE-2024-53900</span></span></td><td style="padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">第一次修复引入了代码来检查 match 参数是否包含 \$where 操作符。代码首先判断 match 是否为数组,如果是,则遍历数组的每个元素,检查是否包含 \$where 属性;如果 match 是一个对象,则直接检查其 \$where 属性。如果发现 \$where 操作符,就抛出一个 MongooseError 异常。这样可以在 populate() 查询中禁止使用 \$where 操作符,提高了安全性。但是,这种方式只能检查一层嵌套,对于更深层次的嵌套对象,可能无法完全检查到。</span></span></td></tr><tr style="background-color: rgb(255, 255, 255);border-top: 1px solid rgb(204, 204, 204);"><td style="padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">CVE-2025-23061</span></span></td><td style="padding: 6px 13px;"><span style="font-size: 12px;"><span leaf="">第二次修复对代码进行了重构,引入了一个单独的函数 throwOn\$where。该函数接受 match 对象作为参数,并递归地检查其中是否包含 \$where 操作符。函数首先对 match 进行类型检查,如果不是对象类型则直接返回。然后遍历 match 对象的属性键,如果发现 \$where 键,则抛出异常;对于嵌套的对象,函数会递归调用自身进行检查。这种递归的方式可以对任意深度嵌套的对象进行全面检查,提供了更完善的 \$where 操作符限制。同时,代码的可读性和可维护性也得到了提高。</span></span></td></tr></tbody></table>  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
学习  
网安实战技能课程  
，戳  
“阅读原文”  
  
