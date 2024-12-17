#  最新的Windows内核漏洞，可获system权限   
老布  FreeBuf   2024-12-17 11:09  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
网络安全和基础设施安全局（CISA）已将两个新的漏洞添加到其已知被利用漏洞目录中，其中一个是涉及 Windows 内核的漏洞，目前正被用于攻击。  
  
  
该漏洞编号为CVE-2024-35250，具体是在 Windows 的 ks.sys 驱动中存在的“不受信任的指针解引用”。这个漏洞可以通过利用未受信任的指针，来进行任意内存读写，最终实现权限提升。这种问题可能导致系统崩溃或使攻击者能够执行任意代码，对安全专业人员来说是一个重要关注点。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icpa18eT1YlRU4d2KsyaE4yjtmDvS5FImKkegAqZs2NtOgic01mkdQIzia2v0lASz6E6NibicLSzzibfEQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
微软已在最近的12月星期二补丁中修复了该漏洞 ，并表示“成功利用这一漏洞的攻击者可能获得 system权限。”该公司在6月发布的安全公告中仅提供了有限的细节，不过发现该漏洞的 DEVCORE 研究团队通过趋势科技的零日计划（Zero Day Initiative）将其报告给微软，并确定受影响的系统组件为 Microsoft Kernel Streaming Service (MSKSSRV.SYS)。  
  
****  
**影响版本：**  
- Windows 10 20H2 Build 19042    
  
- Windows 11 22H2 Build 22621    
  
- VMWare Workstation 17 Pro 环境下也可被利用  
  
****  
**漏洞细节：**  
  
攻击者可以通过发送特制的 IOCTL 请求触发 ks.sys 驱动中的漏洞，利用不可信指针的解引用，最终对系统内存进行任意读写操作。  
  
  
**限制条件：**  
- 实测该漏洞无法在 Hyper-V 环境中成功利用；  
  
- 攻击者需要拥有中等权限（Medium Integrity Level，通常为普通用户权限），才能触发漏洞进行提权。      
  
当前大部分 XDR（扩展检测和响应）解决方案能够检测并阻止该漏洞的利用行为。  
  
  
另外一个漏洞编号是CVE-2024-20767：此漏洞影响 Adobe ColdFusion，涉及不当的访问控制。攻击者可以利用此类漏洞来获取敏感信息或系统的未经授权访问，对网络安全构成重大威胁。对此，CISA 的操作指令（BOD）22-01，题为“减少已知被利用漏洞的重大风险”，要求联邦政府行政部门（FCEB）机构在指定的截止日期前修补这些漏洞，并表示“此类漏洞是一种常见的攻击途径，对联邦企业构成重大风险。”  
  
  
虽然 BOD 22-01 明确针对 FCEB 机构，但CISA 依旧强烈建议所有组织采取积极措施，以减少其网络攻击的暴露面。  
  
  
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
> https://cybersecuritynews.com/windows-kernal-vulnerability-actively-exploits-in-attacks/  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
