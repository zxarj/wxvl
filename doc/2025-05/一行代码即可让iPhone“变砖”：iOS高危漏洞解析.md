#  一行代码即可让iPhone“变砖”：iOS高危漏洞解析   
 FreeBuf   2025-05-03 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
iOS系统存在一个高危漏洞（CVE-2025-24091），恶意应用仅需执行一行代码即可永久禁用iPhone。该漏洞通过操作系统的Darwin通知机制触发无限重启循环，导致设备"变砖"，必须通过完整系统恢复才能修复。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icbm1QXk9w6O9EM8c0VvZicmhia9IcxLTuqWX9ThtlxCgz4rYNZibwxibS9xyMQVOTxMR7RvexgQ5vpiag/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**01**  
  
  
  
**Darwin通知系统漏洞分析**  
  
  
该漏洞利用了CoreOS层的底层消息机制——Darwin通知。与常见的NSNotificationCenter或NSDistributedNotificationCenter不同，Darwin通知属于苹果操作系统的遗留API（应用程序接口），工作在系统底层。  
  
  
发现该漏洞的安全研究员Guilherme Rambo解释："Darwin通知更为基础，属于CoreOS层组件，为苹果系统进程间提供简单的底层消息交换机制。"  
  
  
漏洞的关键在于：iOS上的任何应用都无需特殊权限即可发送敏感的系统级Darwin通知。最危险的是，这些通知能触发包括"进入恢复模式"在内的强力系统功能。  
  
  
**02**  
  
  
  
**一行代码的攻击实现**  
  
  
攻击代码异常简单，仅需执行以下单行指令即可触发漏洞：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icbm1QXk9w6O9EM8c0VvZicmXgUCIwjgt36lEtoGqwMgWp0PRgqvr4nZJ8t4pHSbgFicyicfaaKx46YA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
执行后设备将强制进入"恢复中"状态。由于实际未进行恢复操作，该过程必然失败并提示用户重启设备。研究人员创建了名为"VeryEvilNotify"的概念验证攻击，将漏洞利用代码植入小组件扩展。  
  
  
研究员指出："iOS会定期在后台唤醒小组件扩展。由于小组件在系统中使用广泛，当安装并启动包含小组件扩展的新应用时，系统会非常积极地执行其小组件扩展。"  
  
  
通过将漏洞代码植入发送通知后反复崩溃的小组件，研究人员构建了持久性攻击——每次重启后都会触发攻击，形成使设备无法使用的无限循环。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icbm1QXk9w6O9EM8c0VvZicm5zJt6ppn4o8QnTVibPm9cJibP9UInsHRuBHN7ibGhuia3cgJB1jm3uhCPQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
**03**  
  
  
  
**修复方案**  
  
  
苹果在iOS 18.3中通过实施新的敏感Darwin通知授权机制修复该漏洞，并向研究员支付了7500美元漏洞赏金。  
具体措施包括：  
- 系统通知现在必须包含"com.apple.private.restrict-post."前缀  
  
- 发送进程需持有"com.apple.private.darwin-notification.restrict-post."格式的受限授权  
  
这并非苹果系统首次出现Darwin相关漏洞。此前卡巴斯基实验室曾发现"Darwin Nuke"漏洞，攻击者可通过特制网络数据包发起远程拒绝服务攻击。  
  
  
强烈建议所有iPhone用户立即升级至iOS 18.3或更高版本。早期版本设备仍面临攻击风险，攻击可能通过App Store或其他渠道分发的看似无害的应用或小组件实施。  
  
  
该案例凸显了移动操作系统持续面临的安全挑战——即使简单且被忽视的遗留API，若未妥善保护也可能构成重大风险。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR39ibFdyjP3Qp8CEJxFWljbW1y91mvSZuxibf3Q3g2rJ32FNzoYfx4yaBmWbfwcRaNicuMo3AxIck2bCw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319699&idx=1&sn=127e9ca1a8d55931beae293a68e3b706&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319086&idx=1&sn=e2ff862babd7662c4fa06b0e069c03f2&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319257&idx=1&sn=a603c646a53e3a242a2e79faf4f06239&scene=21#wechat_redirect)  
  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39ibFdyjP3Qp8CEJxFWljbW1uEIoRxNoqa17tBBrodHPbOERbZXdjFvNZC5uz0HtCfKbKx3o3XarGQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5KDnCKUfVLVQGsc9BiaQTUsrwzfcianumzeLVcmibOmm2FzUqef2V6WPQQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38mFMbqsUOVbBDicib7jSu7FfibBxO3LTiafGpMPic7a01jnxbnwOtajXvq5j2piaII2Knau7Av5Kxvp2wA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
