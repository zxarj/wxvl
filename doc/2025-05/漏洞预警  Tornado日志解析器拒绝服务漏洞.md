#  漏洞预警 | Tornado日志解析器拒绝服务漏洞   
浅安  浅安安全   2025-05-19 00:00  
  
**0x00 漏洞编号**  
- # CVE-2025-47287  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Tornado是一个高性能的Web框架和异步网络库，专为处理大规模并发连接设计。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SUdHXWiahFfxqaJBQ1ocAIXicSnOwhEPLficjPkUV1mDdciaDict3NpqQiaSKOWmicJZC8xHAgfUAtbYdchQ/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2025-47287**  
  
**漏洞类型：**  
拒绝服务  
  
**影响：**  
资源耗尽  
  
**简述：**  
Tornado的multipart/form-data解析器存在日志拒绝服务漏洞，该解析器在默认启用的情况下，当遇到特定错误时，会记录警告信息并继续解析后续数据。这种处理方式使攻击者能够发送恶意请求，生成大量警告日志，从而消耗系统资源并导致拒绝服务攻击。  
  
**0x04 影响版本**  
- Tornado <= 6.4.2  
  
**0x05 POC状态**  
- **未公开**  
  
**0x06 修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.tornadoweb.org/  
  
  
  
