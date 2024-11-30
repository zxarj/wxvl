#  知名工业WiFi接入点被曝存在20多个漏洞   
老布  FreeBuf   2024-11-30 02:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
近期，Advantech工业级无线接入点设备被曝光存在近二十个安全漏洞，部分漏洞可被恶意利用以绕过身份验证并执行高权限代码。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibdicpTBMAWrconxBghTAHVMCNAcUWhtNcd8FYGRoYzQRmB1bPhwCm0NMH85nqB1piauL6JjibW8QI7w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
网络安全公司Nozomi Networks在周三发布的分析报告中警告称：“这些漏洞带来了严重的安全风险，它们允许未经身份验证的远程代码以根权限执行，全面威胁到受影响设备的保密性、完整性和可用性。”  
  
  
在负责任的披露流程之后，这些安全漏洞已在以下固件版本中得到修复：  
  
  
- 1.6.5版本，适用于EKI-6333AC-2G和EKI-6333AC-2GD型号；- 1.2.2版本，适用于EKI-6333AC-1GPO型号。  
  
  
在这些被识别的漏洞中，有六个被标记为关键漏洞，它们使得攻击者能够通过植入后门获得对内部资源的持续访问，触发拒绝服务（DoS）攻击，甚至将受感染的端点转变为Linux工作站，以实现网络内的横向移动和进一步渗透。  
  
  
在这六个关键漏洞中，有五个（CVE-2024-50370至CVE-2024-50374，CVSS评分为9.8）与操作系统命令中特殊元素的不当处理有关，而CVE-2024-50375（CVSS评分为9.8）则涉及关键功能缺乏身份验证的问题。  
  
  
特别值得关注的是CVE-2024-50376（CVSS评分为7.3），这是一个跨站脚本（XSS）漏洞，它可以与CVE-2024-50359（CVSS评分为7.2）相结合，后者是一个需要身份验证的操作系统命令注入漏洞，使得攻击者能够通过无线方式执行任意代码。  
  
  
为了成功实施这种攻击，外部恶意用户需要靠近Advantech的接入点并广播恶意信号。  
  
  
当管理员访问Web应用程序中的“Wi-Fi分析器”部分时，攻击就会被触发，导致页面自动嵌入攻击者广播的信标帧信息，而未进行任何消毒检查。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibdicpTBMAWrconxBghTAHVMgtrMWhzInTgVBTXf9HfkHPxgpuYCMv3mQp73RO2KYBPTYQ0R54NUIA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Nozomi Networks指出：“攻击者可以通过其恶意接入点广播SSID（即Wi-Fi网络名称）。”因此，攻击者可以在其恶意接入点的SSID中嵌入JavaScript有效载荷，利用CVE-2024-50376触发Web应用程序内的XSS漏洞。  
  
  
这将导致在受害者的Web浏览器上下文中执行任意JavaScript代码，进而可以与CVE-2024-50359结合，实现具有根权限的操作系统级别的命令注入。这种攻击可能以反向shell的形式出现，为攻击者提供持久的远程访问权限。  
  
  
该公司进一步解释道：“这将使攻击者能够远程控制受损设备，执行命令，并进一步渗透网络，提取数据或部署额外的恶意脚本。”  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊  
】  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ61icYlLmBLDpdYEZ7nIzpGovpHjtxITB6ibiaC3R5hoibVkQsVLQfdK57w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
> https://thehackernews.com/2024/11/over-two-dozen-flaws-identified-in.html  
  
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21&token=734903441&lang=zh_CN#wechat_redirect)  
  
