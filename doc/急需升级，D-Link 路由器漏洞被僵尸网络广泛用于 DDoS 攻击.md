#  急需升级，D-Link 路由器漏洞被僵尸网络广泛用于 DDoS 攻击   
龙猫  星尘安全   2024-12-30 02:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qTcIBaTRMWdjcGWCVUAKtpd05lBUJo0eJ4bg9ujlbhoFeMUcSBFia6tzfs0GPK3RRcLC8vysusEFvqicJ0VGicMtA/640 "")  
  
点击上方  
蓝字  
关注我们  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibV6vqVQpnKD9eLpCQAf69UFrxu8NdzsuFfBDKuKia0X9xJm2mFicP6xnfvpUSafPWB448zx1apYe9Tt76TgsJ12Q/640 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/JmssGpneVHK2aNAIsS7yQ1icFsQMnHqJhsY5gGWBhGwlDF4mVgbdT6WG0ialZ1GdFOYblVeBCAQzTQhYbBFS7Wog/640 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jDxr6RVaB7uMUZsmHvlRS4lPKuiaFhr7T2qJAJiavGZDsg68iauiaK3M09dKgCX0WdDBGH0HH7Ucf1fDt6PiaGGJjLw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XUVHsLAnCiafbNPpza417U8rdne5tbVd9KQrpXMgerhxuOdxpe1NTP8ibibYicvsWVonDKMgNJ2GkXkuQ6ajkzBDSw/640?from=appmsg "")  
  
**僵尸网络活动增加**  
  
：新的“FICORA”和“CAPSAICIN”僵尸网络（Mirai 和 Kaiten 的变体）的活动激增。  
  
**被利用的漏洞**  
  
：攻击者利用已知的 D-Link 路由器漏洞（例如 CVE-2015-2051、CVE-2024-33112）来执行恶意命令。  
  
**僵尸网络功能**  
  
：两种僵尸网络都使用 shell 脚本，以 Linux 系统为目标，杀死恶意软件进程，并进行 DDoS 攻击。  
  
**全球影响**  
  
：FICORA 针对多个国家，而 CAPSAICIN 专注于东亚，东亚的活动持续了两天多。  
  
**缓解措施**  
  
：建议定期更新固件和强大的网络监控，以防止漏洞利用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QRNCxNSF1Ek3FfftEd3BO1pdbPC6odcYIbbKlyfHJkUo0scyyzibZIeN8l44S6lAOpHAddQsic1qczYERFrUGCPw/640?from=appmsg "")  
  
  
FortiGuard Labs 观察到，“FICORA”和“CAPSAICIN”这两个僵尸网络在 2024 年 10 月和 11 月的活动激增。FortiGuard Labs 的威胁研究团队在其与 Hackread.com 独家分享的博客文章中解释说，这些僵尸网络是著名的   
Mirai  
 和   
Kaiten  
 僵尸网络的变体，可以执行恶意命令。  
  
进一步的调查显示，这些  
僵尸网络  
的分发涉及利用 D-Link 漏洞，这些漏洞允许远程攻击者通过家庭网络管理协议 （HNAP） 接口上的 GetDeviceSettings 操作执行恶意命令。  
  
这些漏洞包括   
CVE-2015-2051  
、  
CVE-2019-10891  
、  
CVE-2022-37056  
 和   
CVE-2024-33112  
。这些 CVE 代表攻击者利用的 D-Link 路由器中的特定漏洞实例。它们通常涉及 HNAP 处理用户输入和身份验证方式的缺陷。攻击者使用 HNAP 接口来传播恶意软件，而这一弱点在近十年前首次暴露出来。  
  
受影响的平台包括   
D-Link  
 DIR-645 有线/无线路由器 Rev. Ax、D-Link DIR-806 设备以及 D-Link GO-RT-AC750 GORTAC750_revA_v101b03 和 GO-RT-AC750_revB_FWv200b02。根据 FortiGuard Labs IPS 遥测数据，该僵尸网络具有很高的威胁级别，并通过较旧的攻击方式进行传播。  
  
FICORA 僵尸网络是一种恶意软件，它以多种 Linux 架构为目标，并使用   
ChaCha20  
 加密算法对其配置进行加密。此外，它的功能还包括暴力破解，嵌入带有十六进制 ASCII 字符的 shell 脚本以识别和杀死其他恶意软件进程，以及使用 UDP、TCP 和 DNS 等协议的 DDoS 攻击功能。  
  
根据 FortiGuard Labs 威胁研究团队的  
博客文章  
，这个僵尸网络会下载一个名为“multi”的 shell 脚本，该脚本使用包括 wget、ftpget、curl 和 tftp 在内的各种方法来下载实际的恶意软件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jDxr6RVaB7uMUZsmHvlRS4lPKuiaFhr7Te6QWBXKCPIQp4JicduDLrzpaia4hGe91OVFpA203ZbTIAA2Mpk7WJUMQ/640?wx_fmt=jpeg&from=appmsg "")  
![]( "")  
  
使用 “curl” 命令的下载器脚本 “multi”   
  
FICORA 僵尸网络攻击针对全球许多国家，由来自荷兰的攻击者触发。但与 FICORA 不同的是，CAPSAICIN 攻击仅在 2024 年 10 月 21 日至 22 日的两天内非常活跃，并以东亚国家为目标。  
  
然而，与 FICORA 一样，它也展示了多种功能，包括下载名为“bins.sh”的 shell 脚本、针对多个 Linux 架构、杀死已知的僵尸网络进程、与其 C2 服务器建立连接、发送受害者主机信息以及提供   
DDoS 攻击  
功能。  
  
尽管这种攻击中利用的漏洞已经为人所知近十年，但这些攻击仍然普遍存在，这令人担忧。尽管如此，为了降低   
D-Link 设备  
被僵尸网络入侵的风险，建议定期更新固件并保持全面的网络监控。  
  
[锐捷网络云平台漏洞使大量设备面临远程攻击风险2024-12-27 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247485287&idx=1&sn=dbe25435ade82a813000e9e81a9c5e80&scene=21#wechat_redirect)  
  
  
[黑客利用 Linux eBPF 技术传播恶意软件2024-12-20 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247485202&idx=1&sn=36f8e4353e3d739848dd7493ced629ac&scene=21#wechat_redirect)  
  
  
[Bing搜索引擎爆出严重XSS漏洞2024-11-28 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247484954&idx=1&sn=10bb386657c8c1482377a8a4c8c31464&scene=21#wechat_redirect)  
  
  
[新的 Xiū gǒu 网络钓鱼工具席卷多个国家2024-11-08 ](https://mp.weixin.qq.com/s?__biz=Mzg3NTY0MjIwNg==&mid=2247484880&idx=1&sn=9182c4b20407a75464274f113edf8d58&scene=21#wechat_redirect)  
  
  
**喜欢此文的话，可以点赞、转发、在看 一键三连哦！**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7vglcuxSMkmalibicmpOSAop2ebtW81WD17lIoywzweqOrtD2C7MiaU003Cdo8F8ZpWTqvY50VeDja9w/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
