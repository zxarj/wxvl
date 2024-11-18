#  Palo Alto Networks确认0Day漏洞正在被黑客利用   
老布  FreeBuf   2024-11-18 11:12  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/oQ6bDiaGhdyoFWEgZIHic7sqnootFEuOic7RlQNGhKY6d2ZESG3WpiaTMRlD0z4xO6mQrTZjkWHCkMpO2QtCfUJH6g/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39tmyyDlVsmZoccz4K8eSN6RPRgib1aj9AdQYhvDeoDlBUnia4k5gJX8icJUxKnH8wfaDny2tFiad8yuw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
近日，全球网络巨头Palo Alto Networks确认旗下0Day漏洞正在被黑客利用。11月8日，Palo Alto Networks发布了一份安全通告  
，警告客户PAN-OS管理界面中存在一个远程代码执行漏洞，并建议客户确保PAN-OS管理界面访问的安全性。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39tmyyDlVsmZoccz4K8eSN6cHfohWMRZSkY8icEo6XAJ7QsGaGC2Dnia3076fNUJm4F5h7ibvq0ls6lw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
但随着该漏洞的曝光，Palo Alto Networks在11月15日发现已经有黑客/威胁组织正在利用该漏洞，对用户发起网络攻击，主要目标用户是那些暴露在互联网上防火墙管理界面。  
  
  
目前还不清楚该漏洞如何暴露，以及受影响的企业范围。该漏洞也还没有分配CVE标识符，CVSS评分9.3分。Palo Alto Networks表示，他们认为Prisma Access和Cloud NGFW产品不受此漏洞影响。  
  
  
**安全措施和建议**  
  
  
  
目前，Palo Alto Networks正在开发补丁和威胁预防签名，建议客户确保只有来自可信IP地址的访问才能访问防火墙管理界面，而不是从互联网访问。公司指出，大多数防火墙已经遵循了这一Palo Alto Networks和行业的安全最佳实践。  
  
  
其他受影响的产品：除了上述漏洞，美国网络安全机构CISA还表示，他们知道有三个影响Palo Alto Networks Expedition的漏洞在野外被利用。CISA警告，至少有两个影响Palo Alto Networks Expedition软件的漏洞正在被积极利用，并已将这些漏洞添加到其已知被利用漏洞(KEV)目录中，要求联邦文职行政部门机构在2024年12月5日之前应用必要的更新。  
  
  
**屡屡出现0Day漏洞**  
  
  
  
值得一提的是，在2024年3月，Palo Alto Networks防火墙产品也曾被曝存在严重安全漏洞，编号 CVE-2024-3400 ，CVSS 评分达10分，具体涉及PAN-OS 10.2、PAN-OS 11.0 和 PAN-OS 11.1 防火墙版本软件中的两个缺陷。  
  
  
在第一个缺陷中，GlobalProtect 服务在存储会话 ID 格式之前没有对其进行充分验证。Palo Alto Networks 产品安全高级总监 Chandan B. N. 表示，这使得攻击者能够用选择的文件名存储一个空文件。第二个缺陷被认为是系统生成的文件将文件名作为了命令的一部分。  
  
  
值得注意的是，虽然这两个缺陷本身都不够严重，但当它们组合在一起时，就可能导致未经验证的远程 shell 命令执行。  
  
  
Palo Alto Network表示，利用该漏洞实施零日攻击的攻击者实施了两阶段攻击，以便在易受影响的设备上执行命令。该活动被命名为Operation MidnightEclipse，涉及发送包含要执行命令的特制请求，然后通过名为 UPSTYLE 的后门运行。  
  
  
在攻击的第一阶段，攻击者向 GlobalProtect 发送精心制作的 shell 命令而非有效的会话 ID，导致在系统上创建一个空文件，文件名由攻击者命名为嵌入式命令；在第二阶段，定时运行系统作业会在命令中使用攻击者提供的文件名，进而让攻击者提供的命令能以更高的权限执行。利用这种方式，攻击者就能将该漏洞武器化，且不需要在设备上启用遥测功能就能对其进行渗透。  
  
  
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
> https://www.securityweek.com/palo-alto-networks-confirms-new-firewall-zero-day-exploitation/  
  
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
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651302087&idx=1&sn=29d91904d6471c4b09f4e574ba18a9b2&chksm=bd1c3a4c8a6bb35aa4ddffc0f3e2e6dad475257be18f96f5150c4e948b492f32b1911a6ea435&token=21436342&lang=zh_CN&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651302006&idx=1&sn=18f06c456804659378cf23a5c474e775&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
