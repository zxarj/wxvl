#  漏洞预警 | 红帆HFOffice SQL注入漏洞   
浅安  浅安安全   2025-04-22 00:02  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
红帆HFOffice是由广州红帆科技有限公司开发的医院智慧管理云平台，旨在为医院各行政科室提供高效的办公工具。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SWjP6kdhjibnhNYQQ7ibGoNqaibE27cvOiabfDKbtmpJMn9tib23D0YRNaxib3FH0IujjkANlGrMMroAvCg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**0x03 漏洞详情**  
  
**漏洞类型：**  
SQL注入  
  
**影响：**  
  
获取敏感信息  
  
**简述：**  
红帆HFOffice的/ioffice/prg/set/wss/MobileOA.asmx接口存在SQL注入漏洞，未经身份验证的攻击者可以通过该漏洞获取数据库敏感信息。  
  
**0x04 影响版本**  
- 红帆HFOffice  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.ioffice.cn/  
  
  
  
