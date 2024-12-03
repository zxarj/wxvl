#  知名开源监控系统Zabbix存在SQL 注入漏洞   
老布  FreeBuf   2024-12-03 11:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38Ve7IOFZ6CP5p5MV7hJPibporZicKCX4Id2F2yzc6ObTNDfNjKz9gLTr9f2hVu8sSeQvcd2bIuS0NQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Zabbix 存在 SQL 注入漏洞（CVE-2024-42327），该漏洞是由于在 Zabbix前端的CUser类中的addRelatedObjects函数未对输入数据进行充分验证和转义，导致具有API访问权限的恶意用户可以通过user.get API传递特制输入触发SQL注入攻击，进而利用该漏洞实现权限提升或访问敏感数据。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38Ve7IOFZ6CP5p5MV7hJPibp5Ak0w7DiaLtw2VQh7uNKILibarHZ1Bmx0gdObvdVfJI3MMI0KcBHLV7Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Zabbix是一个基于WEB界面的提供分布式系统监视以及网络监视功能的企业级开源监控解决方案，可以用来监控服务器、硬件、网络等。  
  
  
该漏洞位于user.get API端点，任何具有API访问权限的非管理员用户均可利用，包括默认的“用户”角色。利用这一漏洞，攻击者可以通过操控特定的API调用，注入恶意SQL代码，从而获得未授权的访问和控制权限，进而完全控制Zabbix实例，导致敏感监控数据和连接系统的泄露。  
  
  
Qualys公司对于该漏洞进行分析，指出利用这个漏洞可能允许攻击者提升权限并获得对易受攻击的Zabbix服务器的完全控制，且目前已经发现，有超过83000个暴露在互联网上的Zabbix服务器。  
  
  
漏洞具体信息如下：  
###   
### 漏洞等级  
  
高危  
###   
### 受影响版本  
  
目前受影响的Zabbix版本：  
  
6.0.0 <= Zabbix < 6.0.32rc1  
  
6.4.0 <= Zabbix < 6.4.17rc1  
  
Zabbix 7.0.0  
###   
### 修复方案  
  
目前官方已发布新版本修复该漏洞，建议受影响用户升级到Zabbix 6.0.32rc1、Zabbix 6.4.17rc1、Zabbix 7.0.1rc1或更高版本。官网地址：  
https://www.zabbix.com/download  
  
  
尽管关于CVE-2024-42327的咨询仅在上周发布，但包含该问题补丁的版本6.0.32rc1、6.4.17rc1和7.0.1rc1已于7月发布。这些修补版本还解决了另外一个漏洞，编号为CVE-2024-36466（CVSS评分为8.8）。该漏洞存在认证绕过问题，可能允许攻击者签署伪造的zbx_session cookie并以管理员权限登录。  
  
  
Zabbix版本7.0.1rc1还修复了CVE-2024-36462，这是一个不受控制的资源消耗漏洞，可能允许攻击者造成拒绝服务（DoS）状态。目前没有发现该漏洞被公开利用的情况，强烈建议用户尽快安全最新版本，以修复上述漏洞。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊  
】  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ61icYlLmBLDpdYEZ7nIzpGovpHjtxITB6ibiaC3R5hoibVkQsVLQfdK57w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
> https://www.securityweek.com/critical-vulnerability-found-in-zabbix-network-monitoring-tool/  
  
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21&token=734903441&lang=zh_CN#wechat_redirect)  
  
