#  iOS和macOS系统曝关键漏洞，可破坏TCC框架   
天唯科技  天唯信息安全   2024-12-17 02:35  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNbU68NXCNH8sw9R1wBYiaT6icvH7moZbnkDB7UPWcP57YnEr5sDNDh6pssbCmuxvzQERZeMhN6Dknw/640?wx_fmt=png "")  
  
近日，苹果iOS和macOS系统中被曝光一个关键的安全漏洞，若被成功利用，可能会绕过透明度、同意和控制（TCC）框架，导致用户敏感信息被未经授权访问。漏洞编号CVE-2024-44131，存在于文件提供组件中，苹果通过在iOS 18、iPadOS 18和macOS Sequoia 15中增强符号链接的验证来修复此问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PZibWfCgzicQN4E1zGIRYEEzuknObD2ZCOeRPuepf2RxB9Kj4g8OO03AlklHe35bDkAibxSrmPhJEKfc6wJCAQaUg/640?wx_fmt=jpeg "")  
  
TCC作为苹果设备上的一项关键安全功能，允许用户对应用程序访问敏感数据的请求进行授权或拒绝，如GPS位置、联系人和照片等。  
  
Jamf Threat Labs发现并报告该漏洞，该公司指出，“这种TCC绕过允许未经授权地访问文件和文件夹、健康数据、麦克风或摄像头等，而不会通知用户，这削弱了用户对iOS设备安全性的信任，并使个人数据面临风险。”  
  
漏洞允许恶意应用在后台运行时，拦截用户在文件应用中复制或移动文件的操作，并将它们重定向到其控制的位置。这种劫持行为利用了fileproviderd的高权限，这是一个处理与iCloud和其他第三方云文件管理器相关的文件操作的守护进程，它移动文件后可以将它们上传到远程服务器。  
  
Jamf进一步解释：“具体来说，当用户在后台运行恶意应用可访问的目录内使用Files.app移动或复制文件或目录时，攻击者可以操纵符号链接欺骗文件应用。新的符号链接攻击方法是，首先复制一个正常的文件，为恶意进程复制已开始的可检测信号。然后在复制过程已经开始后插入一个符号链接，有效地绕过符号链接检查。”  
  
因此，攻击者可以利用这种方法复制、移动甚至删除路径“/var/mobile/Library/Mobile Documents/”下的各个文件和目录，以访问与第一方和第三方应用相关的iCloud备份数据，并将它们窃取。这个漏洞的严重之处在于它完全破坏了TCC框架，并且不会向用户触发任何提示。尽管如此，可以访问的数据类型取决于执行文件操作的系统进程。  
  
Jamf表示：“这些漏洞的严重性取决于目标进程的权限，这揭示了对某些数据类型的访问控制执行存在差距，由于这种竞态条件，并非所有数据都可以在不发出警报的情况下提取。例如，由随机分配的UUID保护的文件夹中的数据，以及通过特定API检索的数据不受这种类型的攻击影响。”  
  
与此同时，苹果发布了软件更新，以修复包括  
WebKit  
中的四个漏洞在内的多个问题，这些漏洞可能导致内存损坏或进程崩溃，以及音频中的一个逻辑漏洞（CVE-2024-54529），该漏洞可能允许应用程序执行具有内核权限的任意代码。  
  
iPhone制造商还修复了Safari中的一个漏洞（CVE-2024-44246），该漏洞可能允许网站在启用私人中继的设备上将其添加到阅读列表时获取原始IP地址。苹果表示，它通过“改进Safari发起请求的路由”来解决这个问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNbU68NXCNH8sw9R1wBYiaT6icvH7moZbnkDB7UPWcP57YnEr5sDNDh6pssbCmuxvzQERZeMhN6Dknw/640?wx_fmt=png "")  
  
  
天唯科技专注于大型组织信息安全领域及IT基础设施解决方案的规划、建设与持续运维服务。帮助客户提高IT基础设施及信息安全管控水平和安全运营能力，使客户在激烈的市场环境中保持竞争力。  
  
我们一直秉承“精兵强将，专业专注”的发展理念。  
先后在江门、深圳成立分公司，在武汉、长沙成立办事处以及成立广州的服务支撑中心。公司已获得高新技术企业认证、已通过IS09001、IS027001、CCRC信息安全集成服务、CCRC信息安全风险评估、CCRC信息安全应急处理等认证。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZibWfCgzicQNRytkPMNOKYRW452LxR5Ez5Wee8X6KlbhoUMt9XyhhbRxHafKcCLWJic3ib0umJiaH3fl6sOx8KMBiaQ/640?wx_fmt=png "盾牌单图.png")  
  
**END**  
  
  
  
**往期推荐:**  
  
  
  
  
  
[新型攻击技术曝光：通过二维码实现命令与控制操作](https://mp.weixin.qq.com/s?__biz=MzkzMjE5MTY5NQ==&mid=2247503123&idx=1&sn=38975a0c60dbc007b55dea3ad456cadc&scene=21#wechat_redirect)  
  
  
  
[利用GitLab漏洞，美国比特币ATM巨头Byte Federal数据泄露](https://mp.weixin.qq.com/s?__biz=MzkzMjE5MTY5NQ==&mid=2247503123&idx=2&sn=5dd8d8ef12e293191bd286b255519a79&scene=21#wechat_redirect)  
  
  
  
[警惕！新一届特朗普政府将开展更多攻击性网络行动](https://mp.weixin.qq.com/s?__biz=MzkzMjE5MTY5NQ==&mid=2247503097&idx=1&sn=2f894a8b3ac95a63df71406787f9b974&scene=21#wechat_redirect)  
  
  
  
**征文通道:**  
  
  
  
  
  
[发钱！征文！让真诚的分享更有价值](http://mp.weixin.qq.com/s?__biz=MzkzMjE5MTY5NQ==&mid=2247490310&idx=1&sn=db4b524d1d9f5aabb4af2184dd831de3&chksm=c25ed7a6f5295eb053d3f90e2dc8cd22a2d8ce1a62561ffa62966340ee563734cd4fd32045f3&scene=21#wechat_redirect)  
  
  
