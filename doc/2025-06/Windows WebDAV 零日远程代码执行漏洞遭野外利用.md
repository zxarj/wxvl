#  Windows WebDAV 零日远程代码执行漏洞遭野外利用  
 FreeBuf   2025-06-11 10:57  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38jklsSv8Tzqr96KnnDUsKC5hf45tTnBj1CS1690dn3GPMOfzlxVIbYJHq9qVnkiaMsA5Eibk4ZGYXA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
微软已确认其Web分布式创作和版本控制（WebDAV）实现中存在一个严重的零日漏洞正遭攻击者野外利用，这促使微软在2025年6月的补丁星期二发布紧急安全更新。  
  
### Part01  
### 漏洞简介  
  
  
该漏洞编号为CVE-2025-33053，属于严重的远程代码执行（RCE）缺陷，允许未经授权的攻击者通过外部控制WebDAV中的文件名或路径，通过网络执行任意代码。此安全漏洞影响所有受支持的微软Windows版本，使其成为当前补丁周期中修复范围最广的漏洞之一。  
  
  
微软在安全公告中表示："WebDAV中文件名或路径的外部控制允许未经授权的攻击者通过网络执行代码。"该漏洞被评定为"重要"严重等级，成功利用需要用户交互。  
  
### Part02  
### 野外活跃利用现状  
###   
  
Check Point Research的安全研究人员发现该漏洞并报告了野外活跃利用的证据。攻击媒介要求受害者点击特制的WebDAV URL，从而触发远程代码执行漏洞。  
微软在解释利用方法时表示：“用户需要点击特制的URL才会被攻击者入侵。” 尽管需要用户交互，但由于该漏洞可能导致整个系统沦陷，仍构成重大风险。  
  
### Part03  
### 影响范围和补丁发布  
###   
  
该漏洞影响广泛的微软系统，微软已为Windows 10、Windows 11和各种Windows Server版本分发补丁。微软2025年6月的补丁星期二共修复了66个漏洞，CVE-2025-33053是本次修复的两个零日漏洞之一。  
  
  
**Part04**  
### 攻击面扩大与遗留风险  
  
  
WebDAV组件通过与Microsoft Edge中的Internet Explorer模式以及其他应用程序中的WebBrowser控件集成，显著扩大了攻击面。微软指出，虽然Internet Explorer 11在某些平台上已停用，但底层的MSHTML平台仍受支持且存在漏洞。此外，鉴于已确认野外利用，安全专家强烈建议立即部署可用补丁。  
  
  
该漏洞延续了近年来威胁行为体日益针对WebDAV相关安全问题的趋势。使用旧版Windows系统和启用Internet Explorer兼容模式的机构面临更高风险。  
微软建议安装仅安全更新的客户同时安装相应的IE累积更新，以确保完全防范此漏洞。  
  
  
**参考来源：**  
  
Windows WEBDAV 0-Day RCE Vulnerability Actively Exploited in the Wild – All Versions Affected  
  
https://cybersecuritynews.com/windows-webdav-0-day-actively-exploited/  
  
  
###   
###   
###   
### 推荐阅读  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651322750&idx=1&sn=a3c131230639a0c28b18a4475b631066&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
