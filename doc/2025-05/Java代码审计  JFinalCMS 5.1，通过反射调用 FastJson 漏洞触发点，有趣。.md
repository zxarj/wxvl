#  Java代码审计 | JFinalCMS 5.1，通过反射调用 FastJson 漏洞触发点，有趣。   
原创 领家小明  闪石星曜CyberSecurity   2025-05-27 03:38  
  
内部学员投稿。  
  
首发于闪石星曜CyberSecurity。  
  
我公开了一份面向零基础小白的 JavaWeb代码审计入门文档。  
  
欢迎一起来学习，感觉不错别忘了分享给身边的好哥们。  
```
https://www.yuque.com/power7089/ekvyga
```  
  
  
# 正文  
  
  
JFinal_CMS 5.1 版本下面存在一个有趣的 Fastjson 漏洞触发点。  
  
Github 定位 Issues: https://github.com/jflyfox/jfinal_cms/issues/60  
  
下面我们通过上述 Issues，来进行代码分析。  
  
通过上面的漏洞Issues，明确的知道了漏洞点在哪。  
  
也就是这处 API 是有漏洞的，具体漏洞点事 P 参数。  
```
/api/action?version=1.0.1&apiNo=1000000&pageNo=1&pageSize=1&method=pageArticleSite&time=20170314160401&p={siteId:1}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5c4c0YkibALFbs9qu58qXUibibOibwic4YumOgnPYlPDdCHicQBR8KufibUFqw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5H0fQOmHEbnJFibT7t3sycuJdrFoB0xW0IbjmtbeK3yq04NBBbShVPIg/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞代码审计分析，核心流程如下： 1、正向：搜索JSON.parseObject  
可以找到getParams  
方法-----> get(String key)  
------> getInt(String key)  
-----> ApiV100Logic  
中，使用过form.getInt("siteId")  
的方法的全部都存在 Fastjson反序列化漏洞，ApiV100Logic  
向上找不到直接传参的入口，实际上是根据反射过来的。  
  
2、反射链条api.controller  
类中action  
方法，----> service.action(from)  
方法----> (ApiResp) ReflectionUtils.invokeMethod  
方法，根据action名  
称反射调用。  
  
代码审计分析：   
  
全局搜索 Fastjson 触发反序列化的漏洞点：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB50YiaoALXs867VUI4BSOJLSF5qMia2Y4xyvbiaetI0d5Miaeu0TUShSuJsw/640?wx_fmt=png&from=appmsg "")  
  
  
找到getParams方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5MN29Z1icEj3N0mibnpu83bhzNialyjcUsFG9RMyMFAofBJbWuG5KJlFNw/640?wx_fmt=png&from=appmsg "")  
  
  
向上找调用链发现get(String key)方法存在调用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5ibmdEj4Hkjulo8ialK6Upm46HNV0kImGhX7wYebcB7hC6QI0DjFwnfKw/640?wx_fmt=png&from=appmsg "")  
  
  
向上找调用链发现getInt(String key)方法存在调用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5NJHIslaTaWC5tdJPejHB2Jiceoq520nm2RrS3KaapHGxKV4JSva654A/640?wx_fmt=png&from=appmsg "")  
![]( "")  
  
  
搜索ApiV100Logic向上找不到调用链，进一步探索该系统架构，发现其实是根据反射过来的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5pflhYGsCl6ez9OP0J27CBPYzj9U8OLAWzWJ3bxyYuB3m9WxuIbbINQ/640?wx_fmt=png&from=appmsg "")  
  
  
下面分析反射调用链  
  
搜索/api/action  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5MvhLa9nP6oVxAonZBKibMnupax0m8qbwmw0HNKQPicGiaCY101YvFiaUIA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB50gLZXcL4ktHykeqhyYn91tEJdGCACJyH4eiaN30ib0SvOj0PcxdSLUIQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5rBwrqFnBhvuGNrzHjxdp9m5ZtqhpkSWhaGIiaq5yoHOeO3dc5yniaURQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FFcgFn6WVc2Zqes79oHX5yUqfVibajJB5olRFgPwQoD5jbFlXeCria3SiblXq1pHWryFlSllATpHIz3uWlCyxIxgA/640?wx_fmt=png&from=appmsg "")  
  
然后接下来就是走 form.getInt 的流程导致反序列化，衔接到了上面讲的 Fastjson 反序列化漏洞点触发。  
  
这个漏洞的本质在于入口非常规寻找接口的方式，而是使用的反射的形式获取到该接口，从而连接上了 Fastjson 漏洞点，构成了一条完整的漏洞触发链。  
  
所以，在寻找漏洞点到入口这个分析阶段，每个系统都有不同的情况，不同的场景，需要我们根据当下系统情况，进一步分析。不能完全一味地只看 Controller 层代码。  
  
# 更多内容  
  
  
> 学Java代码审计就找闪石星曜CyberSecurity，手把手带你！  
> 视频培训课程详情可点击下方链接了解，六十多节实战课，低至 499。  
> 2025 版部分课程进行了重新讲解，并新增了不少内容。  
  
  
[《JavaWeb代码审计企业级项目实战》课程2.0升级版，新增10节实战课！依旧低至499，加量不加价！招生！](https://mp.weixin.qq.com/s?__biz=Mzg3MDU1MjgwNA==&mid=2247487386&idx=2&sn=fc36f768e8715e1b0c291519e7dad584&scene=21#wechat_redirect)  
  
  
> 如果你想找个代码审计内部社区，欢迎加入【炼石计划@赛博代审之旅】以原创系列教程为主，代码审计资源为辅，打造一个专业的代码审计内部社区，已有 2000 多人加入！  
> 更多代码审计资料整理中，现在加入就能回本！  
> 仅需 99元一年，续费仅需 25元一年。  
> 两杯奶茶钱就能投资自己学习代码审计知识！  
  
  
[2025 年，炼石计划@赛博代审之旅又带来了什么好东西呢？](https://mp.weixin.qq.com/s?__biz=Mzg3MDU1MjgwNA==&mid=2247487164&idx=1&sn=ee4ecadbaa3c2616b6e600c1711926e0&scene=21#wechat_redirect)  
  
  
  
  
  
