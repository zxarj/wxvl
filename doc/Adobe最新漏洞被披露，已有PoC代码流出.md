#  Adobe最新漏洞被披露，已有PoC代码流出   
 网安百色   2024-12-25 11:29  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vK9ZGS15PBzhF8gRBMk6V7TXMVsSxyqn3vpLuXTg82nHzLRYicg7QtVJQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
点击上方  
蓝字  
关注我们吧~  
  
Adobe近期发布了紧急安全更新，针对ColdFusion中的一个关键漏洞，该漏洞已有概念验证（PoC）代码流出。根据周一的公告，这个编号为CVE-2024-53961的漏洞源于路径遍历弱点，影响了Adobe ColdFusion 2023和2021版本，攻击者可借此读取易受攻击服务器上的任意文件。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibSxDsItbp8q2DaEq4dPM5diaPXKBIn2uUtNWFiaftDLmuh61s3Bm8MCEcFQ4dgyK4G69fLj8KDiaibDg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
Adobe指出，鉴于该漏洞已有可用的  
PoC  
代码，可能导致任意文件系统读取，因此将其评为“优先级1”严重等级，警示用户该漏洞面临更高的被攻击风险。  
  
  
Adobe建议管理员尽快安装当天发布的紧急安全补丁（ColdFusion 2021更新18和ColdFusion 2023更新12），最好在72小时内完成，并按照ColdFusion 2023和ColdFusion 2021锁定指南中的安全配置设置进行操作。  
  
  
尽管Adobe尚未透露该漏洞是否已在野外被利用，但建议客户查阅更新的串行过滤文档，了解更多关于阻止不安全Wddx反序列化攻击的信息。  
  
  
今年5月，  
美国网络安全与基础设施安全局  
（CISA）曾警告软件公司，在产品发布前应消除路径遍历安全漏洞，因为攻击者可利用这类漏洞访问敏感数据，包括可用于暴力破解现有账户和入侵系统的凭证。  
  
  
去年7月，CISA还要求联邦机构在8月10日前保护其Adobe ColdFusion服务器，防范两个被利用的关键安全漏洞（CVE-2023-29298和CVE-2023-38205），其中一个为零日漏洞。  
  
  
一年前，美国网络安全局还披露，自2023年6月以来，黑客一直利用另一个关键的ColdFusion漏洞（CVE-2023-26360）入侵过时的政府服务器。从2023年3月起，该漏洞在“非常有限的攻击”中被作为  
零日漏洞  
积极利用。  
  
  
来源：  
FreeBuf  
  
**免责声明**  
：  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
