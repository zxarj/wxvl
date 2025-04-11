#  新手小白如何挖掘cnvd通用漏洞之存储xss漏洞（利用xss钓鱼）   
原创 zkaq - 小博  掌控安全EDU   2025-02-16 04:00  
  
扫码领资料  
  
获网安教程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
# 本文由掌控安全学院 -   小博 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**  
## 一、XSS的三种类型：  
  
1.反射型XSS（Reflected XSS）：这是最常见的一种XSS类型。攻击者将恶意脚本注入到URL中，然后诱骗受害者点击该链接。当受害者的浏览器加载该URL时，恶意脚本会被执行。由于恶意脚本包含在URL中，因此仅当受害者点击或访问该URL时，才会发生攻击。  
  
2.存储型XSS（Stored XSS）：攻击者将恶意脚本注入到网站的数据库中，如评论、用户资料等，当其他用户浏览这些数据时，恶意脚本会在他们的浏览器上执行。这种类型的XSS攻击比反射型XSS更为持久和危险。  
  
3.基于DOM的XSS（DOM-based XSS）：这种XSS攻击与反射型和存储型不同，它主要依赖于客户端的DOM操作。攻击者通过修改网页的DOM结构，而不是通过服务器注入恶意脚本，来执行恶意代码。这种类型的XSS攻击更加难以防范，因为它不依赖于服务器端的代码或数据。  
## 二、XSS攻击的危害：  
  
1.窃取用户信息：通过读取用户的Cookie、Session Token等信息，攻击者可以假冒用户身份进行登录或其他操作。2.会话劫持：攻击者可以利用盗取的Cookie等会话信息，直接接管用户的会话。3.恶意重定向：将用户重定向到恶意网站。4.传播蠕虫：通过自动在用户浏览器中执行脚本，攻击者可以进一步传播恶意代码。5.篡改页面内容：在页面上展示广告、挂马链接或其他恶意内容。  
## 三、文件上传存储型xss：  
  
1.文件上传类型：pdf、js、html、css、svg2.漏洞点：招聘系统，文件上传点。  
## 四、实战演示：  
#### 1、在月黑风高的某一天晚上，我正在焦头烂额的努力寻找工作，疯狂的投递简历，突发奇想这个文件上传点可不可以试试传一些别的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlbGYiceAYm9q0ibGC4rLY8xp2icPR4yNdBnyKzEnO7H1mnpZktfO650jsQ/640?wx_fmt=png&from=appmsg "")  
#### 2.直接一手抓包，上传html文件，发现真的可以上传html文件，这存储xss不就来了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TllNP4liasEDicicdkPllfOB6JL9EuuCAOibGnnACekxvGaaeLW4q4zcBJBg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlQUFibxuPyS2Budbic4dyrpqZpUHtibbcDEcCHl7nmBdWFVbAI7qBQtXUw/640?wx_fmt=png&from=appmsg "")  
#### 3.通过查看招聘系统的链接不是招聘公司的地址，原来是一个供应商系统，而且还不小，通过寻找利用该招聘系统的公司一一去上传，发现了通用的xss。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlR5MhZyMtVPQollhtWf6GTTjZBgmp4ldm8jGFGNOw2Ff4QbOIf7ibsZA/640?wx_fmt=png&from=appmsg "")  
#### 4.通过上传的html进一步扩大危害，使用xss平台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlmHqibelsSWuNZHZDmLC8L1g1icjCuNKrvUeAAK6grNcwQib4yKUiaHPOJQ/640?wx_fmt=png&from=appmsg "")  
#### 5.思路一下子就上来了，可以伪造一个静态页面，让别人输入账号密码，我这边通过xss窃取键盘记录，说干就干，把供应商系统的登录页面的前端源码复制，伪造恶意网站，再把xss代码插进去。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2Tl11RnAWNzPdYF5M1EwS25poibgTKzqabLGxul3ibaIrtiaVHicLnuGJy7ug/640?wx_fmt=png&from=appmsg "")  
#### 6.这样的一个可以窃取键盘记录的页面就做好了，可以试试效果，上传恶意html页面。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlHjbo2iazZAbVLokiafgkh5a790fbe5SzSLTPcC3yibQAkZiaGdaTIjSPeg/640?wx_fmt=png&from=appmsg "")  
#### 7.成功窃取到键盘记录，打到了账号密码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TliaxVGvQ5icMydx0OofIoe6o4EoX6eOQcTcD4RgLZZZTFYtibGjV5IHTkw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2TlJvkwr1kltfM14VhDOYbQtv3jWaJ4iciaRrSK9iajiczD0Tus37lPJmgtew/640?wx_fmt=png&from=appmsg "")  
## 五、XSS漏洞修复：  
  
1.对所有用户输入进行严格的验证和清理，避免将用户输入直接嵌入到HTML、JavaScript等可执行代码中。2.使用安全的API和库，如HTML模板库，它们可以自动对输出进行编码，避免XSS攻击。3.设置合适的Content-Security-Policy（CSP），以减少XSS攻击的风险。4.对敏感信息进行加密存储和传输，以防止信息泄露。5.定期进行安全审计和漏洞扫描，及时发现并修复潜在的安全问题。  
## 六、经验总结：  
  
1.招聘系统简历上传点，招聘系统有概率会有让你上传你的作品或者成果的上传点，比如应聘程序员会让你上传你开发的作品，可以试试传一些别的文件上去。2.通过漏洞发现供应商寻找通用的漏洞。3.资产足够，一定要写满10个案例！！！！！可以的话一定要利用漏洞展示出最大的危害。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqhAic6ad7ID9FE1x2MDx2Tl4L5ic5TXeibglWwlLn0qCkNDtBohTYdGj99ib8w9Nic5b81BzVib6ibc5Jug/640?wx_fmt=png&from=appmsg "")  
  
  
  
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，  
  
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**没看够~？欢迎关注！**  
  
  
  
  
  
**分享本文到朋友圈，可以凭截图找老师领取**  
  
上千**教程+工具+交流群+靶场账号**哦  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
******分享后扫码加我！**  
  
  
  
**回顾往期内容**  
  
  
[零基础学黑客，该怎么学？](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247487576&idx=1&sn=3852f2221f6d1a492b94939f5f398034&chksm=fa686929cd1fe03fcb6d14a5a9d86c2ed750b3617bd55ad73134bd6d1397cc3ccf4a1b822bd4&scene=21#wechat_redirect)  
  
  
[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)  
  
  
[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)  
  
  
[记某地级市护网的攻防演练行动](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247543747&idx=1&sn=c7745ecb8b33401ae317c295bed41cc8&token=74838194&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&scene=21#wechat_redirect)  
[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)  
  
##     代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
点赞+在看支持一下吧~感谢看官老爷~   
  
你的点赞是我更新的动力  
  
  
```
```  
  
