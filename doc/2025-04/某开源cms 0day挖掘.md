#  某开源cms 0day挖掘   
用户9528  神农Sec   2025-04-05 08:56  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
网络安全领域各种资源，EDUSRC证书站挖掘、红蓝攻防、渗透测试等优质文章，以及工具分享、前沿信息分享、POC、EXP分享。  
不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。  
#   
  
原文链接：  
https://xz.aliyun.com/news/17601  
  
作者：  
用户9528  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x1 简介**  
  
**简介**  
  
CicadasCMS是用springboot+mybatis+beetl开发的一款CMS，支持自定义内容模型、模板标签、全站静态化等功能。  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8PxvRXWM4SUrDLhjnPV56P59Mj6Ixobk23DZy4u0gpM7IULtX7X6Zjg/640?wx_fmt=png&from=appmsg "")  
  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8jucbCZInoYc1yxlQgMicarJOWarueibtiaNwdXaqmpiaicLc25jslDq5iazg/640?wx_fmt=png&from=appmsg "")  
  
  
   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x2 漏洞挖掘**  
  
  
****  
  
sql注入（成功）  
  
漏洞发生位置在com.zhiliao.module.web.cms.ContentController#save：  
```
```  
  
save方法接受了一个content对象为参数，这个content对象包含主键contentId等信息，formParam对象为一个新建的hashMap，用于保存表单数据的键值对，表示了一些扩展字段和其对应值，那么在这个逻辑中，如果contentId不为空，则调用com.zhiliao.module.web.cms.service.ContentService#update更新数据，否则调用com.zhiliao.module.web.cms.service.ContentService#save进行数据保存：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8DsWmltZwVsl09ehBYGicFjJSu0s0vc10ZELOZtocPicpibacpVOn4zgZQ/640?wx_fmt=png&from=appmsg "")  
  
  
com.zhiliao.module.web.cms.service.impl.ContentServiceImpl#update(com.zhiliao.mybatis.model.TCmsContent, java.lang.String, java.util.List<com.zhiliao.mybatis.model.TCmsModelFiled>, java.util.Map<java.lang.String,java.lang.Object>, java.lang.String[])：  
```
```  
  
又调用了com.zhiliao.module.web.cms.service.impl.ContentServiceImpl#SaveModelFiledParam进行数据保存：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8dUDBbEh65fNScyQt25pj0PRPq127sZSjVqCZVRyNheL6mtdkg3kpdg/640?wx_fmt=png&from=appmsg "")  
  
  
接着跟进com.zhiliao.module.web.cms.service.impl.ContentServiceImpl#SaveModelFiledParam方法：  
```
```  
  
那么这里执行的逻辑是：首先进行非空判断，接着遍历表单数据并且动态拼接到sql执行语句中，最后进行执行，显然这里是存在sql注入漏洞：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8YG53UQBHeNictQcKX5WCPXXicYSicAMicMFibOQEfUQzjU3RYgct11YtrNQ/640?wx_fmt=png&from=appmsg "")  
  
  
文件上传（失败）：  
  
com.zhiliao.common.upload.UploadComponent#uploadFile：  
```
```  
  
这里的newName是从this.getNewFileName(fileName);得到的，fileName又是通过this.getFileName(fileType) ;获得的：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8xfxwGGPsctxhJZZTJepC1pqt8drvH8E0DVF2PH0BH3XAeaicZA2nCrQ/640?wx_fmt=png&from=appmsg "")  
  
  
最开始fileType又是通过this.getFileType(attachment.getOriginalFilename());获得的：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW11L0Qwfx1ehYqNViagSco8RFRTQXTHj6duthrVibfwAaTVygsIeFwWuXCqqmeWsA2rmN57dw6CWQw/640?wx_fmt=png&from=appmsg "")  
  
  
那么跟进com.zhiliao.common.upload.UploadComponent#getFileType：  
```
```  
  
那么这里是使用了lastIndexof函数，这样的话看上去后文件的类型是不可控的。  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x3 总结**  
  
  
  
这套源码是很老了，整体难度不大，非常适合新手进行学习。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x4 内部圈子详情介绍**  
  
我们是  
神农安全  
，点赞 + 在看  
 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
```  
  
  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
  
**知识星球——**  
**神农安全**  
  
星球现价 ￥40元  
  
如果你觉得应该加入，就不要犹豫，价格只会上涨，不会下跌  
  
星球人数少于400人 40元/年  
  
星球人数少于600人 60元/年  
  
（新人优惠卷20，扫码或者私信我即可领取）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVuEXF1P2pJMs8L6hKKR5QFYFf8Xqj7SNtV9Xmb9tS7kvq0oRuoPMN6SdgfKIckL4OAHc7ZhrgNdA/640?wx_fmt=png&from=appmsg "")  
  
  
欢迎加入星球一起交流，券后价仅40元！！！ 即将满600人涨价  
  
长期  
更新，更多的0day/1day漏洞POC/EXP  
  
  
内部小圈子——  
圈友反馈  
（  
良心价格  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8Hviaqs0Uv6F4NTNkTKDictgOV445RLkia2rFg6s6eYTSaDunVaRF41qBibY1A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8HviaRhLXFayW3gyfu2eQDCicyctmplJfuMicVibquicNB3Bjdt0Ukhp8ib1G5aQ/640?wx_fmt=png&from=appmsg "")  
  
  
****  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWX4tdZp6r3Wmb4fm2sX7tMGzq4elfctXeqH9YOoqPkDQkJR4oiar5L4hQFNRUG4ozKyUtI2xQy3gqQ/640?wx_fmt=jpeg&from=appmsg "")  
  
****  
    
```
```  
  
