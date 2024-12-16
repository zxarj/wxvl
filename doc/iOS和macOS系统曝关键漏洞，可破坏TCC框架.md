#  iOS和macOS系统曝关键漏洞，可破坏TCC框架   
知知  FreeBuf   2024-12-16 11:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
近日，苹果iOS和macOS系统中被曝光一个关键的安全漏洞，若被成功利用，可能会绕过透明度、同意和控制（TCC）框架，导致用户敏感信息被未经授权访问。漏洞编号CVE-2024-44131，存在于文件提供组件中，苹果通过在iOS 18、iPadOS 18和macOS Sequoia 15中增强符号链接的验证来修复此问题。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3iczI6SxGibvHhibWTfyRLOPsicwNgJibV55oFHtQUiawOYAl43icZZ0YI1kmGSAfKGIq1kpoTxFPNeD5mMw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
TCC作为苹果设备上的一项关键安全功能，允许用户对应用程序访问敏感数据的请求进行授权或拒绝，如GPS位置、联系人和照片等。  
  
  
Jamf Threat Labs发现并报告该漏洞，该公司指出，“这种TCC绕过允许未经授权地访问文件和文件夹、健康数据、麦克风或摄像头等，而不会通知用户，这削弱了用户对iOS设备安全性的信任，并使个人数据面临风险。”  
  
  
漏洞允许恶意应用在后台运行时，拦截用户在文件应用中复制或移动文件的操作，并将它们重定向到其控制的位置。这种劫持行为利用了fileproviderd的高权限，这是一个处理与iCloud和其他第三方云文件管理器相关的文件操作的守护进程，它移动文件后可以将它们上传到远程服务器。  
  
  
Jamf进一步解释：“具体来说，当用户在后台运行恶意应用可访问的目录内使用Files.app移动或复制文件或目录时，攻击者可以操纵符号链接欺骗文件应用。新的符号链接攻击方法是，首先复制一个正常的文件，为恶意进程复制已开始的可检测信号。然后在复制过程已经开始后插入一个符号链接，有效地绕过符号链接检查。”  
  
  
因此，攻击者可以利用这种方法复制、移动甚至删除路径“/var/mobile/Library/Mobile Documents/”下的各个文件和目录，以访问与第一方和第三方应用相关的iCloud备份数据，并将它们窃取。这个漏洞的严重之处在于它完全破坏了TCC框架，并且不会向用户触发任何提示。尽管如此，可以访问的数据类型取决于执行文件操作的系统进程。  
  
  
Jamf表示：“这些漏洞的严重性取决于目标进程的权限，这揭示了对某些数据类型的访问控制执行存在差距，由于这种竞态条件，并非所有数据都可以在不发出警报的情况下提取。例如，由随机分配的UUID保护的文件夹中的数据，以及通过特定API检索的数据不受这种类型的攻击影响。”  
  
  
与此同时，苹果发布了软件更新，以修复包括WebKit中的四个漏洞在内的多个问题，这些漏洞可能导致内存损坏或进程崩溃，以及音频中的一个逻辑漏洞（CVE-2024-54529），该漏洞可能允许应用程序执行具有内核权限的任意代码。  
  
  
iPhone制造商还修复了Safari中的一个漏洞（CVE-2024-44246），该漏洞可能允许网站在启用私人中继的设备上将其添加到阅读列表时获取原始IP地址。苹果表示，它通过“改进Safari发起请求的路由”来解决这个问题。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ61icYlLmBLDpdYEZ7nIzpGovpHjtxITB6ibiaC3R5hoibVkQsVLQfdK57w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
> https://thehackernews.com/2024/12/researchers-uncover-symlink-exploit.html  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
