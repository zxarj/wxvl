#  无补丁，I-O Data路由器0Day漏洞被利用   
老布  FreeBuf   2024-12-07 02:04  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38G1nYUFhMulWK7EEiadWOtSMbaUhibhicibCR4h2q0PCrFcFaW99iaQYZiaJkVG66pJGc0APk9ooAic3icgQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
日本计算机紧急响应小组（CERT）警告称 ，黑客正在利用I-O Data路由器设备中的零日漏洞来修改设备设置、执行命令，甚至关闭防火墙。  
  
  
I-O Data在其网站上发布的安全公告中承认确实存在三个零日漏洞，但目前暂无完整的修复补丁，预计将在2024年12月18日发布，因此在此之前用户将面临比较严重的风险。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38G1nYUFhMulWK7EEiadWOtSy0Dvo5PEJUw3eHyJktvEO0cEOdhoYva6vuZy6s8JP9v3aEDKau4ZPQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
上述三个零日漏洞在2024年11月13日被发现，包括信息泄露、远程任意操作系统命令执行和导致防火墙禁用的漏洞。  
  
  
具体如下：  
- CVE-2024-45841：敏感资源上的不当权限配置，导致低权限用户可以访问关键文件。  
  
- CVE-2024-47133：认证的管理员用户可以在设备上注入并执行任意操作系统命令，利用配置管理中的输入验证不充分漏洞。  
  
- CVE-2024-52464：固件中的未记录特性或后门可导致远程攻击者在无需认证的情况下，关闭设备防火墙并修改设置。  
  
****  
**受影响的设备**：这些漏洞影响UD-LT1和UD-LT1/EX设备，前者是为多功能连接解决方案设计的混合LTE路由器，而后者是工业级版本。  
  
  
最新可用的固件版本v2.1.9仅解决了CVE-2024-52564漏洞，I-O Data表示其他两个漏洞的修复将在计划于2024年12月18日发布的v2.2.0版本中提供。比较糟糕的消息是，已经有客户因为这些漏洞而遭到黑客攻击。  
  
  
I-O Data安全公告指出，“已收到使用混合LTE路由器UD-LT1和UD-LT1/EX的客户的咨询，这些客户报告了来自外部来源的潜在未经授权访问。”  
  
  
在安全更新发布之前，I-O Data 建议用户实施以下缓解措施：  
  
- 禁用所有互联网连接方式的远程管理功能，包括WAN端口、调制解调器和VPN设置。  
  
- 仅限VPN连接的网络访问，以防止未经授权的外部访问。  
  
- 将默认的“访客”用户的密码更改为超过10个字符的更复杂的密码。  
  
- 定期监控和验证设备设置，以尽早检测未经授权的更改，并在检测到泄露时将设备重置为出厂默认设置并重新配置。  
  
不过国内的企业用户不需要太过担心，因为I-O DATA UD-LT1和UD-LT1/EX LTE路由器主要在日本市场销售，旨在支持NTT Docomo和KDDI等多个运营商，并兼容该国的主要MVNO SIM卡。  
  
  
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
  
> https://www.bleepingcomputer.com/news/security/japan-warns-of-io-data-zero-day-router-flaws-exploited-in-attacks/  
  
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
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
