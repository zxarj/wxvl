#  Windows存储系统现0day漏洞，攻击者可远程删除目标文件   
邑安科技  邑安全   2025-02-13 02:20  
  
更多全球网络安全资讯尽在邑安全  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1N39PtINn8uwv9BCGszjEJ2xicYjQguFQIyAic2aaFmZTVicwydrDDpr1kVibq62mJ1UOBLETXAhoE9bjsSqiadd5ibQ/640?wx_fmt=png&from=appmsg "")  
  
  
Windows系统近日被曝出一个重大安全漏洞，攻击者可利用该漏洞远程删除受影响系统上的目标文件。该漏洞编号为CVE-2025-21391，于2025年2月11日披露，属于权限提升漏洞，严重性被评定为"重要"级别。  
## 漏洞详情与风险分析  
  
CVE-2025-21391利用了一个被称为"文件访问前链接解析不当"（CWE-59）的缺陷，使攻击者能够操纵文件访问权限。该漏洞的CVSS评分为7.1，属于中高风险的漏洞。  
  
攻击向量为本地（AV:L），攻击复杂度低（AC:L），所需权限也较低（PR:L），这意味着攻击者无需大量资源或高权限即可利用该漏洞。微软研究人员指出，CVSS评分显示该漏洞不会导致机密性丧失（C:N），但对完整性（I:H）和可用性（A:H）的影响重大。换句话说，虽然无法窃取敏感信息，但攻击者可以删除重要文件，可能导致系统运行中断。  
## 影响范围与缓解措施  
  
该漏洞已在野被利用，状态显示为"已检测到利用"。成功利用该漏洞的攻击者可以删除目标文件，如果关键系统文件受到影响，可能导致服务不可用。受影响的Windows版本包括Windows Server 2016、Windows Server 2019、Windows Server 2022、Windows 10（版本1607、1809、21H2和22H2）以及Windows 11（版本22H2）。x64和ARM64架构的系统均受到影响。  
  
为防范该漏洞，建议用户尽快应用微软2025年2月发布的月度安全更新。用户应优先更新系统，以防潜在攻击，确保数据的完整性和可用性。  
  
原文来自:   
cybersecuritynews.com  
  
原文链接: https://cybersecuritynews.com/windows-storage-0-day-vulnerability/  
  
欢迎收藏并分享朋友圈，让五邑人网络更安全  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1N39PtINn8tD9ic928O6vIrMg4fuib48e1TsRj9K9Cz7RZBD2jjVZcKm1N4QrZ4bwBKZic5crOdItOcdDicPd3yBSg/640?wx_fmt=jpeg "")  
  
欢迎扫描关注我们，及时了解最新安全动态、学习最潮流的安全姿势！  
  
推荐文章  
  
1  
  
[新永恒之蓝？微软SMBv3高危漏洞（CVE-2020-0796）分析复现](http://mp.weixin.qq.com/s?__biz=MzUyMzczNzUyNQ==&mid=2247488913&idx=1&sn=acbf595a4a80dcaba647c7a32fe5e06b&chksm=fa39554bcd4edc5dc90019f33746404ab7593dd9d90109b1076a4a73f2be0cb6fa90e8743b50&scene=21#wechat_redirect)  
  
  
2  
  
[重大漏洞预警：ubuntu最新版本存在本地提权漏洞（已有EXP）　](http://mp.weixin.qq.com/s?__biz=MzUyMzczNzUyNQ==&mid=2247483652&idx=1&sn=b2f2ec90db499e23cfa252e9ee743265&chksm=fa3941decd4ec8c83a268c3480c354a621d515262bcbb5f35e1a2dde8c828bdc7b9011cb5072&scene=21#wechat_redirect)  
  
  
  
  
  
