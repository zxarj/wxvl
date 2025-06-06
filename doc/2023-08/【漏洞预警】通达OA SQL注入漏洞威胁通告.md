#  【漏洞预警】通达OA SQL注入漏洞威胁通告   
安识科技  SecPulse安全脉搏   2023-08-10 09:59  
  
##   
  
1. **通告信息**  
  
  
  
近日，安识科技  
A-Team团队监测到通达OA存在两个SQL注入漏洞（CVE-2023-4165和CVE-2023-4166），CVSSv3评分均为5.5，目前这些漏洞的PoC已公开。  
  
对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。  
##   
  
2. **漏洞概述**  
  
  
  
漏洞名称：通达  
OA SQL注入漏洞  
  
CVE编号：  
CVE-2023-4165/CVE-2023-4166  
  
简述：通达  
OA（Office Anywhere网络智能办公系统）是由北京通达信科科技有限公司自主研发的协同办公自动化软件，是适合各个行业用户的综合管理办公平台。  
  
CVE-2023-4165：通达OA SQL注入漏洞  
  
通达  
OA版本11.10之前，/general/system/seal_manage/iweboffice/delete_seal.php路径下的DELETE_STR参数存在SQL注入漏洞，可能导致通过SQL盲注（延时注入）获取数据库中的敏感信息。  
  
CVE-2023-4166：通达OA SQL注入漏洞  
  
通达  
OA版本11.10之前，/general/system/seal_manage/dianju/delete_log.php路径下的$DELETE_STR参数存在SQL注入漏洞，可能导致通过SQL盲注（延时注入）获取数据库中的敏感信息。  
##   
  
3. **漏洞危害**  
  
  
  
由于参数存在  
SQL注入漏洞，可能导致通过SQL盲注（延时注入）获取数据库中的敏感信息。  
##   
  
4. **影响版本**  
  
  
  
目前受影响的通达  
OA版本：  
  
通达  
OA < v11.10  
##   
  
5. **解决方案**  
  
  
  
目前这些漏洞已经修复，受影响用户可升级到以下版本：  
  
通达  
OA >= v11.10  
  
下载链接：  
  
https://www.tongda2000.com/index.php  
##   
  
6. **时间轴**  
  
  
  
【-】2023年0  
8  
月  
07  
日 安识科技A-Team团队监测到漏洞公布信息  
  
【  
-】2023年0  
8  
月  
08  
日   
安识科技  
A-Team团队根据漏洞信息分析  
  
【  
-】2023年0  
8  
月  
09  
日   
安识科技  
A-Team团队发布安全通告  
  
  
  
