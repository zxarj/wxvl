#  AirBorne漏洞可导致苹果设备被完全劫持   
FreeBuf  商密君   2025-05-03 10:05  
  
**苹果AirPlay协议及SDK中的漏洞使苹果及第三方设备面临攻击风险，包括远程代码执行。**  
  
****  
网络安全公司  
Oligo  
在苹果AirPlay协议及软件开发套件（SDK）中发现一系列严重漏洞（统称为AirBorne），影响苹果及第三方设备。攻击者可利用这些漏洞实施零点击/单点击远程代码执行（RCE）、绕过访问控制列表（ACL）、读取本地文件、窃取数据，以及发起中间人（MITM）或拒绝服务（DoS）攻击。这些漏洞可被组合利用，通过无线或点对点连接完全劫持设备。  
  
  
**01**  
  
  
  
**漏洞影响范围广泛**  
  
  
AirBorne  
漏洞虽未影响所有苹果设备，但全球有23.5亿台活跃苹果设备（包括超1亿台Mac和数千万台支持AirPlay的第三方设备），潜在影响范围极大。研究人员发现编号为CVE-2025-24252和CVE-2025-24132的两个漏洞可实现可蠕虫传播的零点击RCE，攻击者不仅能劫持支持AirPlay的设备，还能通过本地网络传播恶意软件。由于AirPlay在苹果及第三方设备中的广泛存在，这些漏洞可能导致间谍活动、勒索软件和供应链攻击等风险。  
  
  
**02**  
  
  
  
**关键漏洞技术分析**  
  
  
CVE-2025-24252是macOS系统中的高危释放后使用（use-after-free）漏洞，远程攻击者可触发该漏洞执行任意代码。当与CVE-2025-24206组合利用时，可对网络设置开放的AirPlay设备发起零点击蠕虫攻击。攻击者无需用户交互即可通过公共WiFi等途径在网络间传播恶意软件。  
  
  
CVE-2025-24132是AirPlay SDK中的基于栈的  
缓冲区溢出漏洞  
，影响所有支持AirPlay的扬声器和接收器，同样可实现零点击蠕虫式RCE。利用该漏洞可从播放媒体内容到严重入侵（如在敏感环境中通过设备麦克风窃听）等多种攻击效果。  
  
  
**03**  
  
  
  
**漏洞修复与缓解措施**  
  
  
Oligo向苹果报告了23个漏洞，其中17个获得CVE编号。双方通过合作已识别并修复问题，遵循负责任的漏洞披露流程发布更新。为降低风险，用户应：  
  
- 及时更新设备系统  
  
- 停用不必要的AirPlay接收功能  
  
- 通过防火墙限制7000端口的AirPlay访问  
  
- 将"允许AirPlay访问"设置为"仅限当前用户"  
  
报告特别强调："企业必须立即更新所有支持AirPlay的公司设备，安全负责人还需明确告知员工及时更新个人设备。"  
  
  
编辑：陈十九  
  
审核：商密君  
  
**征文启事**  
  
大家好，为了更好地促进同业间学术交流，商密君现开启征文活动，只要你对商用密码、网络安全、数据加密等有自己的独到见解和想法，都可以积极向商密君投稿，商密君一定将您的声音传递给更多的人。  
  
  
[](https://mp.weixin.qq.com/s?__biz=MzI5NTM4OTQ5Mg==&mid=2247633989&idx=1&sn=cd6647451cec618b20dd28533702603b&scene=21#wechat_redirect)  
  
  
点击购买《2023-2024中国商用密码产业发展报告》  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXNcXmbiaiaCljdXpwzOEQ9QTBXMibM6rZTOnbTSwTmCXncQLria2vuLGxn8QPtznzBc0as8vBxWIjrWxQ/640?wx_fmt=jpeg "")  
  
来源：  
FreeBuf  
  
注：内容均来源于互联网，版权归作者所有，如有侵权，请联系告知，我们将尽快处理。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXOdeQx0thlyozF2swQTEN9iaaBNDG0jTKfAgqgdesve8x5IEWNvYxjF6sAWjO1TPCZVsWd0oiaDn3uw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMyyClGk1cttkSBbJicAn5drpXEbFIeChG9IkrslYEylRF4Z6KNaxNafDwr5ibcYaZXdnveQCNIr5kw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaMcJkA69QYZ9T4jmc3fdN6EA7Qq9A8E3RWcTKhxVEU1QjqOgrJMu2Qg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点分享  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaiaRXdw4BFsc7MxzkVZaKGgtjWA5GKtUfm3hlgzsBtjJ0mnh9QibeFOGQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点点赞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaeiaNlRO9954g4VS87icD7KQdxzokTGDIjmCJA563IwfStoFzPUaliauXg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点在看  
  
