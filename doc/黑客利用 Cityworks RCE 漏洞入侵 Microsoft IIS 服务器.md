#  黑客利用 Cityworks RCE 漏洞入侵 Microsoft IIS 服务器   
会杀毒的单反狗  军哥网络安全读报   2025-02-08 01:00  
  
**导****读**  
  
  
  
软件供应商 Trimble 警告  
(  
https://learn.assetlifecycle.trimble.com/i/1532182-cityworks-customer-communication-2025-02-06-docx/  
)  
称，黑客正在利用 Cityworks 反序列化漏洞在 IIS 服务器上远程执行命令并部署 Cobalt Strike 信标以进行初始网络访问。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGDMttlnBTje7VZiamyeDmdLI0nrK5OOMgiaqoSWcJyIxcacHvia9TsCDSgjEqLb31R0IwMW6RicSgKKA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Trimble Cityworks 是一款以地理信息系统 (GIS) 为中心的资产管理和工单管理软件，主要面向地方政府、公用事业和公共工程组织设计。  
  
  
该产品可帮助市政当局和基础设施机构管理公共资产、处理工作订单、办理许可和执照、资本规划和预算等。  
  
  
该漏洞的编号为CVE-2025-0994，是一个高严重性（CVSS v4.0 评分：8.6）反序列化问题，允许经过身份验证的用户对客户的 Microsoft Internet 信息服务 (IIS) 服务器执行 RCE 攻击。  
  
  
Trimble表示，已经调查了客户关于黑客利用该漏洞未经授权访问客户网络的报告，这表明攻击正在进行中。  
  
  
美国网络安全和基础设施安全局 (CISA) 发布了一份协调咨询报告（  
https://www.cisa.gov/news-events/ics-advisories/icsa-25-037-04），警告客户立即保护其网络免受攻击。  
  
  
CVE-2025-0994 漏洞影响 15.8.9 之前的 Cityworks 版本以及 23.10 之前的 Cityworks 办公配套版本。  
  
  
最新版本 15.8.9 和 23.10 分别于 2025 年 1 月 28 日和 29 日发布。  
  
  
管理员必须尽快应用安全更新，而云托管实例（CWOL）将自动接收更新。  
  
  
Trimble 表示，它发现一些内部部署可能具有过度特权的 IIS 身份权限，并警告这些部署不应以本地或域级管理权限运行。  
  
  
此外，一些部署的附件目录配置不正确。供应商建议限制附件根文件夹仅包含附件。  
  
  
完成所有三个操作后，客户即可恢复 Cityworks 的正常运营。  
  
  
虽然 CISA 尚未透露该漏洞是如何被利用的，但 Trimble 已经发布了利用该漏洞进行攻击的危害指标。  
  
  
这些 IOC 表明威胁行为者部署了各种远程访问工具，包括 WinPutty 和 Cobalt Strike 信标。  
  
  
新闻链接：  
  
https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
