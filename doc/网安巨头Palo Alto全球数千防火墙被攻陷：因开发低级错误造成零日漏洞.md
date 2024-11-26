#  网安巨头Palo Alto全球数千防火墙被攻陷：因开发低级错误造成零日漏洞   
 网安百色   2024-11-26 11:30  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vK9ZGS15PBzhF8gRBMk6V7TXMVsSxyqn3vpLuXTg82nHzLRYicg7QtVJQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
点击上方  
蓝字  
关注我们吧~  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sCJ9An5FeDcUKJA1xL2QdPJVK970AnWEKrIdG8dHcGVicLOBLzrSsIHpxZ6rWB8N1cV3ibV4iauyvsw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
安全内参11月26日消息，国际网络安全巨头  
Palo Alto Networks  
日前修复了两个被积极利用的漏洞，这些漏洞影响其防火墙及虚拟化安全设备。攻击者可以利用这些漏洞，在安全设备操作系统PAN-OS上以最高权限执行恶意代码，从而完全控制设备。  
  
Palo Alto Networks在18日发布公告，警告客户其正在调查PAN-OS的Web管理界面可能存在远程代码执行漏洞，并建议用户按推荐步骤限制对该界面的访问。  
  
经过调查，公司确认远程代码执行攻击并非源于单一漏洞，而是通过组合利用两个漏洞实现攻击。这些漏洞已被攻击者在部分暴露于互联网的管理界面设备中利用。  
  
  
Palo Alto Networks表示，此次攻击仅影响“极少数的PAN-OS”防火墙。但威胁监控平台Shadowserver在20日报告称，全球范围内至少有超过2700台易受攻击的PAN-OS设备。Shadowserver还发现，自攻击活动开始以来，已有约2000台设备被入侵。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sCJ9An5FeDcUKJA1xL2QdPWDAOYDl950BbNecqnHE34ZlVkIueodtbnVr3iavicEcdLeOAZXzIojEg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图：美印等国的PAN-OS设备受攻击最多  
  
  
**身份验证绕过与权限提升**  
  
  
  
第一个漏洞（CVE-2024-0012）被评为严重级别，评分高达9.3（满分10）。攻击者可以利用该漏洞绕过身份验证，获取Web管理界面的管理员权限，从而执行管理操作或更改设备配置。  
  
尽管这一漏洞已非常严重，但如果攻击者不能进一步在底层操作系统上执行恶意代码，就无法完全攻陷系统。  
  
然而，攻击者通过第二个漏洞（CVE-2024-9474）达到了这一目的。该漏洞允许拥有Web管理界面管理员权限的用户，在类Linux操作系统上以root最高权限执行代码。  
  
这些漏洞影响PAN-OS 10.2、11.0、11.1和11.2版本，目前所有受影响的版本均已发布补丁。  
  
  
**漏洞源自开发低级错误**  
  
  
  
安全公司watchTowr研究人员对Palo Alto修复补丁进行逆向工程，发现这些漏洞源于开发中的基础性错误。  
  
为了验证用户访问某页面是否需要身份验证，PAN-OS管理界面会检查请求中的X-Pan-Authcheck头部值是否设置为on或off。Nginx代理服务器负责将请求转发至托管Web应用的Apache服务器，并根据请求路径自动将X-Pan-Authcheck设置为on。在某些情况下（例如访问/unauth/目录），X-Pan-Authcheck会被设置为off，以允许无需身份验证访问。然而，除了/unauth/之外的所有路径，其头部值均应为on，以确保用户被重定向至登录页面。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7sCJ9An5FeDcUKJA1xL2QdPfTqFbiaVRe1YXdnrLEGibvYaVB8LAvUiblGTCx5QmaBCCAxfJXzJ5YGKw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
但watchTowr的研究人员发现，uiEnvSetup.php的一个重定向脚本期望HTTP_X_PAN_AUTHCHECK值为off。如果请求中主动设置该值，服务器将直接接受。  
  
研究人员在报告中写道：“只需要将X-PAN-AUTHCHECKHTTP请求头部值设置为off，服务器就会轻松绕过身份验证？！面对这样的设计，谁还能不感到震惊？”  
  
第二个漏洞同样简单。攻击者可以将shell命令作为用户名传递至名为AuditLog.write()的函数，而该函数会将注入的命令传递至pexecute()执行。    
  
实际上，这一问题的核心在于另一个功能，而研究人员认为这个功能本身极为危险。  
  
该功能允许Palo Alto Panorama设备指定要模拟的用户和角色，无需提供密码或通过双因素身份验证，即可生成一个完全认证的PHP会话ID。    
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7sCJ9An5FeDcUKJA1xL2QdPPysH0icNAX99leXLUrABOrLHgppw3UQvicCD0ADkCVcwespnTLb8RgIw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
综合来看，这一设计使攻击者可以将shell代码作为用户名字段的一部分，模拟特定用户和角色，然后通过AuditLog.write()传递至pexecute()，最终在底层操作系统上执行代码。  
  
研究人员总结道：“**令人震惊的是，这两个漏洞竟然存在于生产设备中，且通过Palo Alto设备内部复杂的shell脚本拼凑形成。**”  
  
**缓解措施**  
  
  
  
除了及时更新防火墙至最新补丁版本外，管理员还应限制对管理界面的访问，仅允许可信的内部IP地址访问。管理界面也可以隔离至专用管理VLAN，或通过配置跳板服务器访问，这需要额外的身份验证。  
  
将PAN-OS管理界面暴露于互联网是极高风险的行为。这并非第一次在此类设备中发现远程代码执行漏洞，也可能不是最后一次。今年早些时候，Palo Alto Networks修复了另一个PAN-OS远程代码执行零日漏洞（CVE-2024-3400），该漏洞遭到国家级威胁行为者利用。  
  
Palo Alto Networks的威胁狩猎团队正追踪CVE-2024-0012和CVE-2024-9474的攻击活动，并将其命名为“月顶行动”（Operation Lunar Peak）。  
  
该团队指出：“主要攻击流量来自一些已知用于代理/隧道匿名 VPN 服务的 IP 地址。后续利用活动包括交互式命令执行以及在防火墙上部署恶意软件（例如 webshell）。”  
  
**免责声明**  
：  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
