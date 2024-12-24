#  Adobe最新漏洞被披露，已有PoC代码流出   
老布  FreeBuf   2024-12-24 10:50  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
Adobe近期发布了紧急安全更新，针对ColdFusion中的一个关键漏洞，该漏洞已有概念验证（PoC）代码流出。根据周一的公告，这个编号为CVE-2024-53961的漏洞源于路径遍历弱点，影响了Adobe ColdFusion 2023和2021版本，攻击者可借此读取易受攻击服务器上的任意文件。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibSxDsItbp8q2DaEq4dPM5diaPXKBIn2uUtNWFiaftDLmuh61s3Bm8MCEcFQ4dgyK4G69fLj8KDiaibDg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Adobe指出，鉴于该漏洞已有可用的PoC代码，可能导致任意文件系统读取，因此将其评为“优先级1”严重等级，警示用户该漏洞面临更高的被攻击风险。  
  
  
Adobe建议管理员尽快安装当天发布的紧急安全补丁（ColdFusion 2021更新18和ColdFusion 2023更新12），最好在72小时内完成，并按照ColdFusion 2023和ColdFusion 2021锁定指南中的安全配置设置进行操作。  
  
  
尽管Adobe尚未透露该漏洞是否已在野外被利用，但建议客户查阅更新的串行过滤文档，了解更多关于阻止不安全Wddx反序列化攻击的信息。  
  
  
今年5月，美国网络安全与基础设施安全局（CISA）曾警告软件公司，在产品发布前应消除路径遍历安全漏洞，因为攻击者可利用这类漏洞访问敏感数据，包括可用于暴力破解现有账户和入侵系统的凭证。  
  
  
去年7月，CISA还要求联邦机构在8月10日前保护其Adobe ColdFusion服务器，防范两个被利用的关键安全漏洞（CVE-2023-29298和CVE-2023-38205），其中一个为零日漏洞。  
  
  
一年前，美国网络安全局还披露，自2023年6月以来，黑客一直利用另一个关键的ColdFusion漏洞（CVE-2023-26360）入侵过时的政府服务器。从2023年3月起，该漏洞在“非常有限的攻击”中被作为零日漏洞积极利用。  
  
  
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
> https://www.bleepingcomputer.com/news/security/adobe-warns-of-critical-coldfusion-bug-with-poc-exploit-code/  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
