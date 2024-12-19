#  Apache Tomcat新漏洞允许攻击者执行远程代码   
Zicheng  FreeBuf   2024-12-19 11:04  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
据Cyber Security News消息，安全研究人员在流行的开源 Web 服务器 Apache Tomcat和servlet 容器中发现了两个严重漏洞，可能允许攻击者执行远程代码并导致拒绝服务。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icherY4cPanJaomibfQGLiaY8v6AyRuaXIGicaicQ0qDA1muqfNckzOCgibibzOXBlZhlfPuxutJEwOmKrA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
第一个漏洞被追踪为 CVE-2024-50379， 影响 Apache Tomcat  11.0.0-M1 到 11.0.1、10.1.0-M1 到 10.1.33 和 9.0.0.M1 到 9.0.97版本 。如果默认 servlet 在不区分大小写的文件系统上配置了写入权限，攻击者可在并发读取和上传操作期间利用竞争条件。这种绕过 Tomcat 大小写敏感性检查的做法会导致上传的文件被视为 JSP，最终导致远程代码执行。  
  
  
第二个漏洞被追踪为 CVE-2024-54677，虽然严重性较低，但仍可能构成重大威胁。它影响相同版本的 Apache Tomcat，可使攻击者触发拒绝服务攻击。该漏洞源于 Tomcat 提供的 Web 应用程序示例，其中许多示例无法限制上传的数据大小，可能会导致 OutOfMemoryError，从而导致拒绝服务。  
  
值得注意的是，默认情况下，示例网络应用程序只能从 localhost 访问，这在一定程度上限制了潜在的攻击面。  
  
  
目前Apache 已经发布了解决这些安全漏洞的补丁，敦促用户立即升级：  
  
- Apache Tomcat 11.0.2 或更高版本  
  
- Apache Tomcat 10.1.34 或更高版本  
  
- Apache Tomcat 9.0.98 或更高版本  
  
这些漏洞的发现突显了在网络服务器环境中定期进行安全审计和及时打补丁的重要性。由于 Apache Tomcat 在企业环境中的广泛使用，因此这些漏洞的潜在影响十分巨大。  
  
  
最近，Apache还披露了一个CVSS 4.0 评分高达9.5的高危漏洞，影响Apache Struts 2.0.0 到 2.3.37、2.5.0 到 2.5.33 以及 6.0.0 到 6.3.0.2版本，攻击者可以操纵文件上传参数以启用路径遍历，在某些情况下，这可能导致上传可用于执行远程代码执行的恶意文件 。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ61icYlLmBLDpdYEZ7nIzpGovpHjtxITB6ibiaC3R5hoibVkQsVLQfdK57w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
> https://cybersecuritynews.com/apache-tomcat-rce-vulnerability/  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
