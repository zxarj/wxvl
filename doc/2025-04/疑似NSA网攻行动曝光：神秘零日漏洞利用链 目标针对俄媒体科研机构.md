#  疑似NSA网攻行动曝光：神秘零日漏洞利用链 目标针对俄媒体科研机构   
安全内参编译  安全内参   2025-04-01 16:05  
  
**关注我们**  
  
  
**带你读懂网络安全**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sP0gnXja5nqqWgaFv3Jlyq2fiaRvWmo80eAibFZHug2XZ7Xo2pc9ekzQib2TKsZgB0EygK0QR2wnWQg/640?wx_fmt=webp&from=appmsg "")  
  
  
卡巴斯基日前披露一起尖端的网攻行动，受害者点击定向钓鱼邮件中的链接，该页面暗藏零日漏洞利用代码，可远程绕过Chrome浏览器的沙盒保护机制，结合另一个未知漏洞即可实现远程代码执行，控制受害者的设备；  
  
  
根据该行动非常隐蔽和技艺高超的特征，卡巴斯基认为攻击者具有国家背景，参考此前披露的三角行动，这起事件也很可能是NSA的网络间谍活动。  
  
  
前情回顾·  
抓住NSA的网攻痕迹  
- [巅峰对抗：卡巴斯基曝光疑遭NSA利用的苹果处理器“神秘后门”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510707&idx=1&sn=d2bdd4b2a1d4b929e8f2fce7ac93f01b&scene=21#wechat_redirect)  
  
  
- [俄罗斯指责NSA利用苹果后门监控境内iPhone，中国大使馆亦受影响](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508762&idx=1&sn=ecb77e1320915baf82559f7e7571755f&scene=21#wechat_redirect)  
  
  
- [攻击渗透我国基础设施！美国NSA网络攻击西工大更多细节公布](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247506172&idx=2&sn=c38fbc67445ed3b9d911d2b3e37a1f64&scene=21#wechat_redirect)  
  
  
  
  
安全内参4月1日消息，俄罗斯安全研究人员近日发现了一种复杂的新型恶意软件，该软件被用于针对国内媒体机构和教育机构的间谍活动。  
  
此次攻击利用了谷歌Chrome浏览器中的一个零日漏洞，这一情况令网络安全公司卡巴斯基的研究人员感到震惊。他们指出，黑客在未执行任何明显的恶意或违规行为的情况下，成功绕过了Chrome的沙盒保护机制，“仿佛它根本不存在”。  
  
研究人员在3月25日发布的分析报告中表示：“我们已经发现并报告了数十个在攻击中被积极利用的零日漏洞，但这个特定的漏洞无疑是我们遇到的最有趣的之一。”  
  
  
**点击链接即被控，隐蔽性极高**  
  
  
这场疑似间谍行动被卡巴斯基命名为“论坛巨魔行动”（Operation ForumTroll）。该公司在3月中旬发现了相关攻击。他们检测到一波网络钓鱼邮件，发信人伪装成俄罗斯知名科学和专家论坛的组织者。  
  
邮件内嵌入了针对特定目标定制的恶意链接，且这些链接仅在短时间内有效，可能是为了增加调查人员的分析难度。据研究人员透露，在所有攻击案例中，受害者只需点击链接，访问黑客设下的网站（该网站会在谷歌Chrome中加载），设备即刻感染，无需任何额外操作。  
  
鉴于此次攻击的复杂性及所使用的工具，卡巴斯基认为，这一行动极有可能由某个国家支持的黑客组织发起，但目前尚未将其归因于任何具体国家。  
  
在攻击过程中，攻击者利用CVE-2025-2783漏洞，突破了Chrome的保护系统，该系统原本应该确保网页内容与计算机的其他部分隔离。卡巴斯基指出，漏洞的根本原因在于Chrome的安全机制在与Windows操作系统交互时存在“逻辑错误”，这使攻击者能够绕过关键的安全防护措施。  
  
谷歌已证实该漏洞的存在，并于3月25日发布了安全更新以修复该问题。该公司承认该漏洞已被积极利用，但为了在全球补丁推送期间保护用户，暂未透露更多技术细节。  
  
此外，卡巴斯基表示，该漏洞可能与另一个尚未被发现的漏洞结合使用，从而实现远程代码执行（RCE）。  
  
目前，攻击者使用的恶意链接已不再携带可执行漏洞代码，而是会将用户重定向至合法的科学论坛网站。不过，网络安全专家警告称，应对可疑邮件保持警惕，因为攻击者可能会利用新的漏洞重新发动攻击。  
  
  
**卡巴斯基曾发现多起疑似NSA攻击事件**  
  
  
早在2024年8月，卡巴斯基就曾发现一种此前未见的间谍软件，该软件专门针对俄罗斯安卓用户。这一恶意软件被命名为LianSpy，并伪装成金融服务应用或其他系统应用，例如支付宝等数字支付软件。  
  
卡巴斯基表示，他们在俄罗斯境内检测到10名LianSpy受害者，但拒绝透露具体受害者的身份信息。  
  
此外，在去年6月，卡巴斯基还揭露了另一场间谍行动，代号为“三角行动”(Operation Triangulation）。该行动利用了苹果设备中的两个漏洞，并至少自2019年以来一直活跃，主要攻击手段是向目标设备发送带有恶意附件的iMessage。  
  
俄罗斯政府曾指责美国策划了这场行动，称其攻击了“数千部苹果手机”，以此监视俄罗斯外交官。然而，苹果否认了这一指控，而卡巴斯基也未将“三角定位”行动归因于任何特定政府或已知黑客组织。  
  
  
**参考资料：therecord.media**  
  
  
**推荐阅读**  
- [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)  
  
  
- [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)  
  
  
  
  
  
  
  
点击下方卡片关注我们，  
  
带你一起读懂网络安全 ↓  
  
  
  
  
