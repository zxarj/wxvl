#  Node.js 严重漏洞使数百万系统面临 RCE 攻击   
龙猫  星尘安全   2024-12-25 02:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qTcIBaTRMWdjcGWCVUAKtpd05lBUJo0eJ4bg9ujlbhoFeMUcSBFia6tzfs0GPK3RRcLC8vysusEFvqicJ0VGicMtA/640?wx_fmt=png "")  
  
点击上方  
蓝字  
关注我们  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibV6vqVQpnKD9eLpCQAf69UFrxu8NdzsuFfBDKuKia0X9xJm2mFicP6xnfvpUSafPWB448zx1apYe9Tt76TgsJ12Q/640?wx_fmt=png "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/JmssGpneVHK2aNAIsS7yQ1icFsQMnHqJhsY5gGWBhGwlDF4mVgbdT6WG0ialZ1GdFOYblVeBCAQzTQhYbBFS7Wog/640?wx_fmt=png "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7v2GzYiatfDGeOcvIoyDY8oC7tWXE1e4YWjTUcSic6pyOiavoc4gZS2xTZXnPDQeibbNsRTGQEXNpbbBw/640?wx_fmt=png&from=appmsg "")  
  
在广泛使用的Node.js包“systeminformation”中发现了一个严重的安全漏洞，可能会使数百万个系统面临远程代码执行 （RCE） 攻击。  
  
该漏洞被确定为   
CVE-2024-56334  
，影响该软件包 5.23.6 及以下的版本，该软件包每月下载量超过 800 万次，总下载量达到惊人的 3.3 亿次。  
  
该漏洞源于 getWindowsIEEE8021x 函数中的命令注入缺陷，该函数可检索网络 SSID 信息。  
  
此函数在讲 SSID 作为参数传递给 cmd.exe 之前无法正确清理 SSID。因此，攻击者可以在   
Wi-Fi 网络的 SSID  
 中嵌入恶意命令，然后在调用 getWindowsIEEE8021x 函数是在易受攻击的系统上执行这些命令。  
  
根据程序包的使用方式，此漏洞可能使攻击者能够执行远程代码执行或本地权限提升。该漏洞利用似乎相对简单，只需要本地访问权限即可解近攻击。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7v2GzYiatfDGeOcvIoyDY8oCgvibSRAI3Xw2cicmFGPQwP9lP21QSBfpxjGcicsZHNkcRx1iaej0GOhO0w/640?wx_fmt=png&from=appmsg "")  
  
PoC   
演示了  
两种可能的攻击场景：  
  
通过将 SSID 设置为以下方式无限期运行 ping 命令：  
```
a" | ping /t 127.0.0.1 &
```  
  
通过将 SSID 设置为以下方式，以root权限执行具有提升权限的任意可执行文件：  
```
a" | %SystemDrive%\a\a.exe &
```  
  
一旦连接到恶意构建的 Wi-Fi 网络，只需调用易受攻击的函数（例如 si.networkInterfaces() ）即可触发命令的执行。  
  
“systeminformation” 的维护者已在版本 5.23.7 中解决了这个问题。强烈建议此软件包的所有用户立即更新到最新版本。  
  
对于无法升级的开发人员，解决方法包括手动清理传递给特定函数的参数，包括si.inetLatency() 、si.inetChecksite()、si.services() 和 si.processLoad()。  
  
此漏洞凸显了 npm 生态系统中持续存在的安全挑战以及与广泛使用的软件包相关的潜在风险。它提醒开发人员：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XUVHsLAnCiafbNPpza417U8rdne5tbVd9KQrpXMgerhxuOdxpe1NTP8ibibYicvsWVonDKMgNJ2GkXkuQ6ajkzBDSw/640?from=appmsg "")  
  
· 定期更新依赖项并监控安全公告  
  
· 实施适当的输入清理，尤其是在处理系统级命令时  
  
· 对项目中使用的第三方软件包进行彻底的安全审计  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QRNCxNSF1Ek3FfftEd3BO1pdbPC6odcYIbbKlyfHJkUo0scyyzibZIeN8l44S6lAOpHAddQsic1qczYERFrUGCPw/640?from=appmsg "")  
  
  
在“systeminformation”包中发现 CVE-2024-56334 凸显了对软件安全保持警惕的极端重要性，尤其是对于广泛采用的开源库。  
  
随着 Node.js 生态系统的不断发展，开发人员和组织都必须优先考虑安全实践并随时了解可能影响其系统的潜在漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tLV8Gx8km9J2qtZb0RmrJTSUibpbnWUNaZnW7nRmmBic23KZkLCLiajggaRmtCTvK0IM5xyjFtDY8YNCx6dMdWFVQ/640 "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hox1KVQnzGiapffJhGLo1bjRHbxbLYV2cgd54VBV3aEnbiajibjaL4Ya1wz1zNibHzu08s45GibrEaUnQ65dLQawnibA/640 "")  
  
漏洞信息  
  
https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-cvv5-9h9w-qp2m  
  
[Wordpress 知名插件漏洞致百万网站面临接管风险2024-09-11 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247484685&idx=1&sn=e0df9898c7d75a5c15a0c69c477edec1&scene=21#wechat_redirect)  
  
  
[全球最大勒索组织 - LockBit 勒索软件开发人员在以色列被捕2024-12-23 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247485265&idx=1&sn=a155c57a73a4d74768b9dbbbbb658f60&scene=21#wechat_redirect)  
  
  
[全球供应链安全警钟：七大知名供应链攻击事件回顾2024-09-25 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247484779&idx=1&sn=b25b86ef9f5127d1b1ce26c2dc57b085&scene=21#wechat_redirect)  
  
  
[全球宕机：CrowdStrike事件始末2024-08-12 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247484503&idx=1&sn=0057b2f8403269432daa8a066d6d903f&scene=21#wechat_redirect)  
  
  
**喜欢此文的话，可以点赞、转发、在看 一键三连哦！**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7vglcuxSMkmalibicmpOSAop2ebtW81WD17lIoywzweqOrtD2C7MiaU003Cdo8F8ZpWTqvY50VeDja9w/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
