#  FortiWLM 曝关键漏洞，攻击者可获得管理员权限   
Zicheng  FreeBuf   2024-12-21 02:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR389GQon9kaib6xcIzm7t0JKibxcfXyCA2mO6H5TiapjZVCD9pInUfMfykhkxRSRLeOx4WMDsLjer2C1g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Fortinet 披露了 Fortinet Wireless Manager （FortiWLM） 中的一个严重漏洞，该漏洞允许远程攻击者通过特制的 Web 请求执行未经授权的代码或命令来接管设备。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR389GQon9kaib6xcIzm7t0JKib8U98Q3eop7c9gpx74rlU2PRa4FIjLicqbmkeh1HKO0JGTudpsHxyy3g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
FortiWLM 是一种集中式管理工具，用于监控、管理和优化无线网络，被政府机构、医疗保健组织、教育机构和大型企业使用。  
  
  
该漏洞被跟踪为 CVE-2023-34990，是一个相对路径遍历缺陷，评分高达 9.6。Horizon3 研究员 Zach Hanley 于 2023 年 5 月发现并披露了该漏洞。但在数月后仍未修复。于是 Hanley 决定于 2024 年 3 月 14 日在一篇关于他发现的其他 Fortinet 漏洞的技术文章中披露相关信息和 POC。尽管研究人员公开警告，但缺少 CVE编号以及安全公告意味着大多数用户没有充分意识到风险。  
  
  
该漏洞会影响 FortiWLM 8.6.0 到 8.6.5 和 8.5.0 到 8.5.4 版本 。当 'op_type' 设置为 'upgradelogs' 时，通过在 'imagename' 参数中使用目录遍历技术，攻击者可以从系统中读取敏感的日志文件。这些日志通常包含管理员会话 ID，可用于劫持管理员会话并获得特权访问权限，从而允许威胁行为者接管设备。  
  
  
根据12月18日发布的安全公告，漏洞已在 2023 年 9 月底发布的 FortiWLM 版本 8.6.6 和 8.5.5 中修复。但Fortinet直到最近才正式发布该漏洞的安全通告。  
  
  
换言之，该漏洞作为零日漏洞持续了大约四个月的时间，鉴于 FortiWLM 部署在关键环境中，可能成为攻击者的目标，通过远程入侵导致整个网络中断和敏感数据泄露。因此，强烈建议 FortiWLM 管理员在可用更新可用时应用所有可用更新。  
  
  
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
> https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortiwlm-bug-giving-hackers-admin-privileges/  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
