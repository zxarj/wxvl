#  OpenSSL软件库曝高危漏洞，可实施中间人攻击   
AI小蜜蜂  FreeBuf   2025-02-12 10:53  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38LWZibRwEuPn9hEibyTcrpiaXJqMzhG3icReEqTv4yHG2D8dIPRMCF7Aric1pW8Nv8GyvFOgfRuibdYYEg/640?wx_fmt=jpeg&from=appmsg "")  
  
## OpenSSL 修补了由苹果发现的高严重性漏洞 CVE-2024-12797，该漏洞可能导致中间人攻击。  
  
  
OpenSSL 项目在其安全通信库中修复了一个高严重性漏洞，编号为 CVE-2024-12797。OpenSSL 软件库用于在计算机网络中实现安全通信，防止窃听并确保通信双方的认证。该库包含了安全套接层（SSL）和传输层安全（TLS）协议的开源实现。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38LWZibRwEuPn9hEibyTcrpiaXlwdZh17aXP1zGaszBeSjmM3utD1IgtTclgkjtx5vhoQTdqUVJZeFSA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**项目地址**  
  
  
  
该漏洞影响使用 RFC7250 原始公钥（RPK）的客户端 TLS/DTLS 连接。由于在 SSL_VERIFY_PEER 模式下服务器认证检查失败，攻击者可能利用此漏洞发起中间人攻击。苹果研究人员于 2024 年 12 月 18 日报告了该漏洞，并由 Viktor Dukhovni 修复。  
  
  
**影响范围**  
  
  
  
漏洞主要影响那些显式启用 RPK 并依赖 SSL_VERIFY_PEER 来检测认证失败的 TLS 客户端。OpenSSL 维护者指出，默认情况下，RPK 在 TLS 客户端和服务器中均为禁用状态。项目公告中明确表示：“只有在 TLS 客户端显式启用服务器端的 RPK，且服务器也发送 RPK 而非 X.509 证书链时，才会引发此问题。受影响的客户端通过设置验证模式为 SSL_VERIFY_PEER，期望在服务器的 RPK 与预期公钥不匹配时握手失败。”  
  
  
**修复建议**  
  
  
  
即便如此，启用服务器端原始公钥的客户端仍可通过调用 SSL_get_verify_result() 来检查原始公钥验证是否失败。该漏洞最初出现在 OpenSSL 3.2 版本的 RPK 支持实现中。受影响的版本包括 OpenSSL 3.4、3.3 和 3.2，此漏洞已在 3.4.1、3.3.2 和 3.2.4 版本中得到修复。  
  
  
**历史漏洞回顾**  
  
  
  
2022 年 11 月，OpenSSL 项目发布安全更新，修复了其加密库中的两个高严重性漏洞，编号分别为 CVE-2022-3602 和 CVE-2022-3786。这两个漏洞影响了 3.0.0 至 3.0.6 版本的库。  
  
  
这两个漏洞均为缓冲区溢出问题，攻击者可通过提供特制的电子邮件地址在 X.509 证书验证中触发。Censys 发布的一篇文章中提到：“第一个漏洞 CVE-2022-3786 允许攻击者‘在证书中构造恶意电子邮件地址，以溢出包含.  
字符的任意字节。第二个漏洞 CVE-2022-3602 类似，但攻击者可以通过恶意电子邮件溢出栈上的四个受控字节。’这可能导致服务拒绝或远程代码执行。”  
  
这种缓冲区溢出可能导致服务拒绝，甚至引发远程代码执行。  
  
  
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
  
