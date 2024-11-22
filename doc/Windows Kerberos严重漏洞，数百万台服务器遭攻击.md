#  Windows Kerberos严重漏洞，数百万台服务器遭攻击   
 E安全   2024-11-22 01:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6ylOmP5V7JstQwqRc78nIGth6tqjJElaxeKZ4l6nSSyvZntciaUjic7OwjyBdMHca1fHic6icQqX4xbQQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6ylOmP5V7JstQwqRc78nIGtGf3dcKEM6TjsMhDPZNoiaOa5Z93fwmrvu441OQ8aQ6wjgO7VADO35zA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**E安全消息，Windows Kerberos身份认证协议中存在一个严重漏洞，对数百万服务器构成了重大威胁。微软在11月补丁星期二更新中解决了此问题。**  
  
  
Microsoft Kerberos是一种广泛使用的用于验证主机或用户身份的身份验证协议。为了利用这个漏洞，未经身份验证的行为者必须利用密码协议漏洞来实现RCE，微软在其“补丁星期二”中解释道。  
  
  
**该漏洞被追踪为CVE-2024-43639，CVSS得分为9.8（严重）。**此漏洞允许攻击者向易受攻击的系统发送精心设计的请求，以获得未经授权的访问和远程代码执行(RCE)。  
  
  
如果不及时修补，可能会导致各种规模的组织遭受严重后果，包括数据盗窃、系统中断，甚至整个系统被破坏。由于Windows Server的广泛使用和攻击者可以轻易利用，这个漏洞尤其令人担忧。  
  
  
**根据Censys调查结果，有超过两百万（2274340）个暴露的Windows Server实例，其中1211834个可能易受攻击。**  
  
  
不过，Censys研究称，并非所有这些实例都易受攻击，只有配置了Kerberos KDC代理的服务器才会受到影响。  
  
  
“请注意，显示的设备只有在配置为Kerberos KDC代理协议服务器时，才易受攻击。”Censys博客文章写道。  
  
  
这些设备中有一半以上被发现TCP/443端口开放，这是KDC代理协议服务器的默认端口，研究人员敦促管理员确认他们系统上该协议的存在。  
  
  
**供您参考，KDC代理协议服务器**允许客户端通过HTTPS与KDC服务器通信，使用Kerberos协议（例如用于Kerberos身份验证服务和票证光栅服务交换的UDP/TCP 88，以及用于Kerberos密码更改的TCP 464）。这些协议假设可以直接、可靠地访问KDC服务器，通常在同一网络或VPN内，并通常用于远程桌面网关和DirectAccess等服务。  
  
  
**关于受影响最严重的地区，**Censys指出，这些易受攻击的服务器中有34%位于美国，11%与Armstrong Enterprise Communications相关联，后者是一家托管IT提供商。  
  
  
系统管理员应该修补所有配置为KDC代理服务器的Windows服务器，禁用不必要的KDC代理服务，并实施安全措施如网络分段和防火墙，以最小化网络攻击的风险。  
  
  
鉴于许多服务器易受攻击，攻击者不断利用这些弱点。建议快速修补和采取额外的安全措施，以降低网络攻击的风险。  
  
  
  
**精彩推荐**  
  
  
微软11月补丁星期二：修复91个漏洞，包含4个零日漏洞  
2024.11.15  
  
[](http://mp.weixin.qq.com/s?__biz=MzI4MjA1MzkyNA==&mid=2655347993&idx=1&sn=029f276994bab0e5572dded3d81f223c&chksm=f02e1952c75990441ba555d82104c4a49a754017b7a324c29c1f426b0ba9b2c5532f2309e0dd&scene=21#wechat_redirect)  
  
  
五眼联盟警告，零日漏洞利用正在成为“新常态”  
2024.11.14  
  
[](http://mp.weixin.qq.com/s?__biz=MzI4MjA1MzkyNA==&mid=2655347981&idx=1&sn=4ea51d5d9163381c229194d6dcce6833&chksm=f02e1946c75990504d5c8aba874223a013df25f97a7399a96e053033c4a67526600c836b13c1&scene=21#wechat_redirect)  
  
  
Palo Alto警告，防火墙管理界面RCE漏洞被攻击者利用  
  
2024.11.19  
  
[](http://mp.weixin.qq.com/s?__biz=MzI4MjA1MzkyNA==&mid=2655348005&idx=1&sn=4c930728fafc77e04d44557a763f493e&chksm=f02e196ec759907822c3df98a751c7bd50774a2c551f4cf92f721b23e9006f74c8ca72995f99&scene=21#wechat_redirect)  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6xuwKC3XZa5PZwOfyW4oy9y2uKJLHcg0LnRAXiaicvdMTgLgKoxoVJZfmQxUensppSZJSmnIbX3dNiaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6xuwKC3XZa5PZwOfyW4oy9ypIV3ItH0hiazjtk1Qe8wQJHLiaMTtfDZD9UnHrctGwbbbx9NLsQibCa0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6xuwKC3XZa5PZwOfyW4oy9ynjicbtVrTnA8w5v2sLoAjkictk1u5uVGJZ9MMouKDLUqsqXRZjkhU84A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
注：本文由E安全编译报道，转载请联系授权并注明来源。  
  
