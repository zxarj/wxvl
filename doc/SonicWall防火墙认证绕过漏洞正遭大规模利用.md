#  SonicWall防火墙认证绕过漏洞正遭大规模利用   
AI小蜜蜂  FreeBuf   2025-02-17 10:34  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
网络安全公司警告称，SonicWall防火墙中存在的一个严重认证绕过漏洞正在被积极利用，该漏洞编号为CVE-2024-53704 。随着Bishop Fox的研究人员公开发布了概念验证（PoC）漏洞利用代码，未修补设备组织面临的风险大大增加。  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ic1eod6DUAUiaOACznmS3Y8NNcxaIMJreElNT6ISIOxLz0ZjXkEpp6ohX45iaUico9CbB2gX0wOCtzGQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
**洞详情与攻击方式**  
  
  
  
CVE-2024-53704是一个存在于SonicOS SSL VPN认证机制中的高危漏洞，影响SonicWall Gen 6、Gen 7和TZ80系列防火墙。攻击者可以通过向/cgi-bin/sslvpnclient  
端点发送包含base64编码的空字节字符串的特制会话cookie，从而远程劫持活动的VPN会话。  
  
  
成功利用该漏洞可以绕过多因素认证（MFA），暴露私有网络路由，并允许未经授权的用户访问内部资源。此外，被劫持的会话还可用于终止合法用户连接。  
  
  
**漏洞被快速武器化**  
  
  
  
SonicWall最初于2025年1月7日披露了该漏洞，并敦促用户立即修补。当时厂商并未报告漏洞被实际利用的证据。然而，随着Bishop Fox在2月10日发布PoC代码，攻击门槛大幅降低。2月12日，Arctic Wolf观察到源自不到十个不同IP地址的攻击尝试，这些IP主要托管在虚拟私有服务器（VPS）上。  
  
  
安全分析师认为，漏洞被快速武器化是因为其严重性和SonicWall设备曾被Akira和Fog等勒索软件组织针对性攻击的历史。截至2月7日，Bishop Fox统计发现仍有超过4,500台暴露于互联网的SonicWall SSL VPN（Virtual Private Network）服务器未修补。  
  
  
受影响的固件版本包括：  
- SonicOS 7.1.x（最高到7.1.1-7058）  
  
- SonicOS 7.1.2-7019  
  
- SonicOS 8.0.0-8035  
  
修复版本（如SonicOS 8.0.0-8037和7.1.3-7015）已于2025年1月发布。  
  
漏洞利用模式与此前的攻击活动类似。2024年底，Akira勒索软件组织利用被攻破的SonicWall VPN账户渗透网络，通常在初始访问后的几小时内加密数据。  
  
  
**风险与应对建议**  
  
  
  
Arctic Wolf警告称，CVE-2024-53704可能成为勒索软件部署、凭证窃取或间谍活动的入口。SonicWall和网络安全机构强调，用户需采取以下紧急措施：  
1. 升级固件到修复版本（如8.0.0-8037或7.1.3-7015）。  
  
1. 在无法立即修补的情况下，关闭公共接口的SSL VPN功能。  
  
1. 限制VPN访问到受信任的IP范围，并为剩余用户强制启用MFA。  
  
随着漏洞被大规模利用，组织必须优先修补以降低风险。PoC代码公开、攻击可行性高以及SonicWall在企业网络中的广泛应用，都凸显了问题的紧迫性。  
  
正如Arctic Wolf所警告的那样，鉴于漏洞严重性和勒索软件攻击者的敏捷性，拖延修补可能导致“灾难性的网络入侵”。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ic5icaZr7IGkVcd3DT6vXW4B4LOZ1M7YkTPhS1AT2DQJaicFjtCxt5BRO7p5AOJqvH3EJABCd0BFqYQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651312407&idx=1&sn=60289b6b056aee1df1685230aa453829&token=1964067027&lang=zh_CN&scene=21#wechat_redirect)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
