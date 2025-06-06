#  Wireshark漏洞可通过恶意数据包注入引发拒绝服务攻击  
FreeBuf  FreeBuf   2025-06-06 10:20  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3iblc7WcME2ohpibXziarQaghTVMr2rR56bsAFLiaGrRQ7zJdH4WveHOo5QUxemwQOcHVvsyRaUQiaf1xw/640?wx_fmt=png&from=appmsg "")  
  
  
### Part01  
### 高危漏洞影响全球用户  
  
  
知名网络协议分析工具Wireshark近日曝出高危漏洞（CVE-2025-5601），攻击者可通过注入数据包或使用畸形抓包文件触发拒绝服务（DoS）攻击。该漏洞由Wireshark基金会编号为wnpa-sec-2025-02，于2025年6月4日披露，CVSS评分为7.8（高危级别），影响全球数百万使用Wireshark进行网络故障排查和分析的用户。  
  
  
漏洞源于Wireshark列工具模块的缺陷，当处理畸形网络流量时会导致特定解析器崩溃。受影响版本包括Wireshark 4.4.0至4.4.6以及4.2.0至4.2.12，该漏洞被归类为CWE-120类型，即典型的"缓冲区复制未检查输入大小"导致的缓冲区溢出问题。  
  
  
**Part02**  
### 双重攻击路径威胁企业安全  
  
  
安全研究人员确认该漏洞存在两种主要攻击方式：攻击者可直接向Wireshark监控的网络基础设施注入畸形数据包；或制作损坏的抓包文件诱骗用户打开。Wireshark基金会表示该漏洞是在内部测试环境中发现，目前尚未发现实际攻击案例，但安全专家警告称，鉴于Wireshark在企业环境中的广泛部署，其潜在威胁不容忽视。  
  
  
成功利用该漏洞将导致Wireshark应用程序崩溃，中断关键的网络分析和监控操作，对依赖Wireshark进行实时网络安全监控和事件响应的组织造成严重影响。  
  
  
**Part03**  
### 修复方法与防护建议  
  
  
Wireshark基金会已发布补丁修复该漏洞，强烈建议用户立即升级至4.4.7或4.2.12版本。安全专家还建议采取以下额外防护措施：  
  
**•**  
在Wireshark中打开抓包文件前验证来源可靠性  
  
**•**  
仅从可信来源进行网络数据包捕获  
  
**•**  
实施网络分段以降低暴露风险  
  
  
**Part04**  
### 解析器模块安全问题频发  
###   
  
这是Wireshark解析器模块系列安全问题的最新案例，此前Bundle Protocol、CBOR解析器曾出现CVE-2025-1492漏洞，蓝牙ATT、Radiotap等协议解析器也曝出过类似问题。该事件凸显了复杂网络分析工具在解析多样化且可能恶意的网络流量时面临的安全挑战。由于Wireshark需要处理来自不可信网络的流量，它始终是攻击者试图破坏网络监控能力的重点目标。建议生产环境中使用Wireshark的组织优先实施补丁更新，并全面审查网络监控安全协议以防范潜在威胁。  
  
  
**参考来源：**  
  
Wireshark Vulnerability Enables DoS Attack Through Malicious Packet Injection  
  
https://cybersecuritynews.com/wireshark-vulnerability-enables-dos-attack/  
  
  
###   
###   
###   
### 推荐阅读  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651322416&idx=1&sn=f496ad76672dc84007c77a588480096b&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
