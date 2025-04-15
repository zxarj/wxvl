#  SRC舔狗日常   
原创 A2Cai  隐雾安全   2025-04-15 01:05  
  
**No.0**  
  
**起源**  
  
  
某月某日 星期二 天气多云转暴雨  
  
我刚冒雨给心仪的女神小彤  
  
送上了杯热腾腾的一点点奶茶  
  
"波霸椰果四季奶青要热的不另外加糖，谢谢"  
  
在得到了她包含爱意的背影后  
  
我决定奋发图强，挖洞赚钱  
  
争取早日和她成双成对、喜结良缘！  
  
**No.1**  
  
**找目标**  
  
  
这是件技术活吗？  
  
对你来说或许是，但我这儿就是抽奖  
  
fofa 一开，title="公司" && body="注册" 就开始抽奖了  
  
(PS：一般来说，这个地方容易出货...)  
  
fofa_viewer 真好用，同时也感谢 Sheen 师傅给我提供的技术支持  
  
抽啊抽，抽啊抽  
  
诶，就这家了，前端做这么丑，爱企查2900万+资产  
  
开始干活！  
  
  
**No.2**  
  
**开测**  
  
  
一开始随便注册了个号  
  
进了我的个人页面，看看有没啥越权的  
  
结果是个没有任何参数的 GET 请求...  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWRzibhkicgZQlt5xeVribl1xnnlXrj4m2x3DFmGIx9KJEpz5wF4y7e9YKg/640?wx_fmt=png&from=appmsg "")  
  
  
不经意间，我瞥到 Cookie 中有几个有意思的字段  
  
(这里码死了，就看我写的吧...)  
  
  
AccountID=12345; UserName=hacker  
  
  
脑子里又回想起以前学的那个传说中的 “篡改Cookie造成任意身份伪造”  
  
！！！！  
  
一下子就激灵起来了  
  
然后我就试着改了下，发现不行  
  
于是我就尝试着逐个删除 Cookie 的值，看看哪个是真正决定登陆状态的  
  
？，竟然是你！？  
  
真正决定登陆状态的，竟然是一个短短的，像 Base64 的 Cookie 值？  
  
  
SUID=diFX0gBXXXXXXXXXXXXx7A==  
  
  
后来又经过了几次删 Cookie 登陆之后，发现这个 Cookie 还是这个值  
  
我擦，静态的会话 Cookie，有戏！  
  
我第一反应，就是 base64 解密出来啥可读的信息  
  
然后直接遍历实现任意身份伪造  
  
但事情远没有那么简单...  
  
这个加密，我 base64 解不开...  
  
然后我又进行了很多尝试，可都不行  
  
可恶啊！！这么危险的配置我竟然对它没有办法吗？？？  
  
难道真的要让大家的数据都暴露在风险之中嘛？！？！  
  
难道我真的没办法挖洞赚钱迎娶小彤走向巅峰嘛...  
  
难道，就到此为止了吗.....  
  
  
**No.3**  
  
**车道山前必有路，有路必有小菜哥**  
  
  
没办法，已经很晚了  
  
我怕打扰舍友睡觉，放弃了继续破解加密字符串的想法了...  
  
这个夜晚，有点失眠  
  
也不知道是在回味小彤那深情的背影呢..  
  
还是在想那个差一点点的 Cookie 呢..  
  
这一切不得而知，但唯一知道的是  
  
我睡得很香，香到我的呼噜声吵醒了隔壁床的两个舍友...  
  
  
一觉过后，我又重拾信心  
  
开始对这个系统的另外一个网站下手  
  
简单的测了一下，又发现了个篡改 Cookie 可以出信息的地方  
  
这个地方，原本是用来投诉的  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWBPXaLHxVRbPpvN8Ggj4WKic5c15GdnN2nqBeqbt8DLXKbgI3t46tOwg/640?wx_fmt=png&from=appmsg "")  
  
  
而如果你是登陆了的用户，它会给你自动填上你的一些个人信息  
  
又经过我删删减减 Cookie 值...  
  
发现它竟然是依据 AccountID 给你自动补充的个人信息..  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWGY0JeYHVBkBbjIsJp0GB14l2BZgplx94NmoHnbYmiaibeEdX4oXXsk3w/640?wx_fmt=png&from=appmsg "")  
  
  
改个 AccountID 试试  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWf831wZI3M66xEC9mBcPd6Qxjzsibpq5yXb3yyicfBjLXJh1178ukHscA/640?wx_fmt=png&from=appmsg "")  
  
  
发现它给自动补充了别人的一些个人信息  
  
除此之外，留意到头上的那个欢迎语句嘛...  
  
"您好，dgzhonglian" 这句话让我感觉....  
  
这个网站可能还会有更多的 Cookie 伪造的点  
  
果不其然，让我发现了又有个确定登录状态的接口  
  
/HXXXXXX/ComXXXXXXXXXle.ashx?method=loadloginstatus  
  
而这个接口只需要 AccountID，就可以得到所有人的 UserName、头像地址之类的  
  
(PS：AccountName 得存在，但它的值对查询结果无影响)  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWmHCgOwsBxLnzZHOicicn8HVlBvibLQPkEUqgsDGN7GI0kqcxicLDy8HK3w/640?wx_fmt=png&from=appmsg "")  
  
  
听起来很鸡肋对吧...但最牛逼的地方来了....  
  
这个响应包...  
  
它 给 我 Set-Cookie 啦！！！！！！！  
  
而且这个 Cookie 还和我本身的 Cookie 是不一样的  
  
再加上之前我找到的那个点：Cookie 是静态不改变的  
  
这意味着什么？  
  
这意味着我可以仅仅根据遍历 UserId，就拿到所有人的 Cookie 值  
  
然后伪装成任何人来操作这个系统  
  
多说无益，快来试试  
  
先拿个 Cookie  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWMe6YXIIxkb6GTDdMOqO6mGZT6iav5S7aDeD0mayd6Vib9IkxIKjXUfiaQ/640?wx_fmt=png&from=appmsg "")  
  
  
拿这个Cookie去访问个人页面  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWPPT2bffkRl7OcBW1SvvRwXwbh8WCwgG0j5rILG0icftZnDSQvNdIrRA/640?wx_fmt=png&from=appmsg "")  
  
  
成功伪装成这个用户然后读取到他的个人信息啦！！  
  
后面用 Firefox 的插件 Cookie Manager  
  
尝试说带着这个 Cookie 去系统里做一些操作  
  
然后畅通无阻...  
  
接着，就火急火燎地去交补天啦！  
  
希望这家公司能够给点 money 给我  
  
我都快请不起小彤吃早餐和下午茶了呜呜呜呜呜  
  
  
  
**No.4**  
  
**网安沟通交流群**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ELQKhUzr34wXviaZKH7WMYicpk18XwVqkWGXIOmKb5bicCRbMak13AibldBwOc1YRAkKiadibgdqLiaD9RsgeCXqkOdDQ/640?wx_fmt=jpeg&from=appmsg "")  
  
**扫码加客服小姐姐拉群**  
  
  
  
