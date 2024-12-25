#  Adobe最新漏洞被披露，已有PoC代码流出   
FreeBuf  商密君   2024-12-24 15:15  
  
Adobe近期发布了紧急安全更新，针对ColdFusion中的一个关键漏洞，该漏洞已有概念验证（PoC）代码流出。根据周一的公告，这个编号为CVE-2024-53961的漏洞源于路径遍历弱点，影响了Adobe ColdFusion 2023和2021版本，攻击者可借此读取易受攻击服务器上的任意文件。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibSxDsItbp8q2DaEq4dPM5diaPXKBIn2uUtNWFiaftDLmuh61s3Bm8MCEcFQ4dgyK4G69fLj8KDiaibDg/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic "")  
  
Adobe指出，鉴于该漏洞已有可用的PoC代码，可能导致任意文件系统读取，因此将其评为“优先级1”严重等级，警示用户该漏洞面临更高的被攻击风险。  
  
Adobe建议管理员尽快安装当天发布的紧急安全补丁（ColdFusion 2021更新18和ColdFusion 2023更新12），最好在72小时内完成，并按照ColdFusion 2023和ColdFusion 2021锁定指南中的安全配置设置进行操作。  
  
尽管Adobe尚未透露该漏洞是否已在野外被利用，但建议客户查阅更新的串行过滤文档，了解更多关于阻止不安全Wddx反序列化攻击的信息。  
  
今年5月，美国网络安全与基础设施安全局（CISA）曾警告软件公司，在产品发布前应消除路径遍历安全漏洞，因为攻击者可利用这类漏洞访问敏感数据，包括可用于暴力破解现有账户和入侵系统的凭证。  
  
去年7月，CISA还要求联邦机构在8月10日前保护其Adobe ColdFusion服务器，防范两个被利用的关键安全漏洞（CVE-2023-29298和CVE-2023-38205），其中一个为零日漏洞。  
  
一年前，美国网络安全局还披露，自2023年6月以来，黑客一直利用另一个关键的ColdFusion漏洞（CVE-2023-26360）入侵过时的政府服务器。从2023年3月起，该漏洞在“非常有限的攻击”中被作为零日漏洞积极利用。  
  
  
编辑：陈十九  
  
审核：商密君  
  
**征文启事**  
  
大家好，为了更好地促进同业间学术交流，商密君现开启征文活动，只要你对商用密码、网络安全、数据加密等有自己的独到见解和想法，都可以积极向商密君投稿，商密君一定将您的声音传递给更多的人。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXNcXmbiaiaCljdXpwzOEQ9QTBXMibM6rZTOnbTSwTmCXncQLria2vuLGxn8QPtznzBc0as8vBxWIjrWxQ/640?wx_fmt=jpeg "")  
  
来源：FreeBuf  
  
注：内容均来源于互联网，版权归作者所有，如有侵权，请联系告知，我们将尽快处理。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXOdeQx0thlyozF2swQTEN9iaaBNDG0jTKfAgqgdesve8x5IEWNvYxjF6sAWjO1TPCZVsWd0oiaDn3uw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMyyClGk1cttkSBbJicAn5drpXEbFIeChG9IkrslYEylRF4Z6KNaxNafDwr5ibcYaZXdnveQCNIr5kw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaMcJkA69QYZ9T4jmc3fdN6EA7Qq9A8E3RWcTKhxVEU1QjqOgrJMu2Qg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点分享  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaiaRXdw4BFsc7MxzkVZaKGgtjWA5GKtUfm3hlgzsBtjJ0mnh9QibeFOGQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点点赞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaeiaNlRO9954g4VS87icD7KQdxzokTGDIjmCJA563IwfStoFzPUaliauXg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点在看  
  
