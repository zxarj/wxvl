#  12年来最严重的 WordPress 漏洞，可大规模接管管理员权限   
 WIN哥学安全   2024-11-18 13:58  
  
点击上方  
蓝字关注我们  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qLaXsGgOwmOFETMqV9DfenGIAx8BfvBotFhJrgP7IG9WkIkgCP1Q1DDIVsZVqTiasAS9CT66RJrq9Gj0ibkpdeew/640?&random=0.10577231121717623&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=png&random=0.7851078959349969&tp=webp&random=0.3158067333367687 "")  
  
  
  
免责声明：  
  
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
**转自奇安信代码卫士，编译：代码卫士**  
  
**WordPress 插件 “Really Simple Security”（此前被称为 “Really Simple SSL”）的免费和专业版本均受一个严重的认证绕过漏洞影响。**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibvxd5tc1COE4kUV1E9ZmEQiaHvJ1Wicapmnu7L9zKeSN2xB8WnBrRMYJg/640?wx_fmt=gif&from=appmsg "")  
  
  
Really Simple Security 是 WordPress 平台的一个安全插件，提供SSL配置、登录暴露、双因素认证层以及实时漏洞检测服务。其免费版本已用于超过400多万个网站上。  
  
Wordfence 公司公开披露了该漏洞，称其为12年来报送的最严重的漏洞，并提醒称该漏洞可导致远程攻击者获得对受影响网站的完整管理员访问权限。更糟糕的是，可通过自动化脚本大规模利用该漏洞，从而可能导致大规模网站遭接管后果。  
  
而这也是Wordfence 提醒托管提供商更新客户网站上的插件并扫描数据库以确保未运行易受攻击版本的原因所在。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibI1DRe3GvlbfrWtHb3ZAlNLSsZZJ2IqdOZ4NaxjmzFL6B1KzYobmjew/640?wx_fmt=gif&from=appmsg "")  
  
  
**2FA导致更脆弱的安全性**  
  
  
该漏洞的编号是CVE-2024-10924，是由 Wordfence 公司的研究员 István Márton 在2024年11月6日发现的。该漏洞由该插件的双因素REST API 操作中的用户认证处理不当造成的，可导致任何用户账户包括管理员在内的账户遭越权访问。  
  
具体而言，漏洞位于 “check_login_and_get_user()”函数中。该函数通过检查 “user_id”和 “login_nonce” 参数对用户身份进行验证。当 “login_nonce” 不合法时，该请求本应但并未遭到拒绝，而是调用“authenticate_and_redirect()” 只基于 “user_id” 对用户进行认证，从而导致认证绕过后沟。  
  
当双因素认证启用时，该漏洞可遭利用，而且即使默认是禁用状态，很多管理员将允许启用以便获得更强的账户安全性。该漏洞影响Really Simple Security 9.0.0至9.1.1.1的免费、专业以及多网站专业 (Pro Multisite) 版本。  
  
目前，开发人员已经正确处理 “login_nonce” 验证失败情况，即会立即退出 “check_login_and_get_user()” 函数。该修复方案已经应用到该插件的9.1.2版本，已在11月12日发布在Pro版本以及在11月14日为免费用户发布。厂商与 WordPress.org 协作，强制用户进行安全更新，不过网站管理员仍然应当检查并确保自己运行的是最新版本9.1.2。专业版用户在许可过期时已禁用自动更新功能，因此必须手动更新至9.1.2。  
  
截止到昨天，WordPress.org 数据显示，该插件的免费版本的下载次数约为45万次，即350万个网站易受攻击。  
  
  
**原文链接**  
  
  
https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/  
  
  
题图：  
Pixabay  
 License  
  
****  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  

								  

									  

										  

											  
往期推荐  

										  

									  

									  

								[ 比较有意思的几个漏洞挖掘记录 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247502125&idx=1&sn=15f4d48305c47b6a699973c871f1cca0&chksm=c0c868d9f7bfe1cf87cd0eea2b0fe635af7c9ff29d604544b162d17cad57ab3da3ceb45a0b03&scene=21#wechat_redirect)  

							  
  

								[ 惊喜，GPT4o可接入个人微信了！ ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247502119&idx=1&sn=16b547ead14bd0305be520de5d33d840&chksm=c0c868d3f7bfe1c57d400776ef36be40bbcd5ec5f93da38376e715d2bfdc5ef3767b4486c1f7&scene=21#wechat_redirect)  

							  
  

								[ 分享某单位众测项目漏洞挖掘中的一些手法 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247502084&idx=1&sn=d48d54097881a0bd3c994c3d816bb50b&chksm=c0c868f0f7bfe1e617bd8b582860051b3a23f3f7b281943bde2953d490765b13d216d6b3ea50&scene=21#wechat_redirect)  

							  
  

								[ 从404到RCE，挖洞像喝水一样简单 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501990&idx=1&sn=cb10031d31e76ad2a3161edd1b0ae150&chksm=c0c86952f7bfe044a7ca1c516fc7f3622935eb3465254d668faa81f2f08b7bc834755788c98b&scene=21#wechat_redirect)  

							  
  

								[ 一款针对Burp Suite Pro的安全扫描增强工具 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501958&idx=1&sn=c379d63c4be459123cee9b08089e522a&chksm=c0c86972f7bfe064ca6a3367bb823295789d0c298c46bc7a9f7b50985036ed396b238a86629b&scene=21#wechat_redirect)  

							  
  

								[ DudeSuite Web Security Tools 渗透测试工具集 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501938&idx=1&sn=e1a7953ca4719b400b2dd6011482996d&chksm=c0c86986f7bfe09019b5e8608ff79a6fe1e44dcd4b6a9acadd57d09ef84b615abf2c12139c2a&scene=21#wechat_redirect)  

							  
  

								[ 无影(TscanPlus) v2.6发布：弱口令连接校验 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501910&idx=1&sn=48bb76542e5a88c3fbd623fe387e32f5&chksm=c0c869a2f7bfe0b45c85c623f9a521ff19b006449f832d3799c39abae03daaac3471e77c8f26&scene=21#wechat_redirect)  

							  
  

								[ 一次看个爽——攻防演练合集篇 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501889&idx=1&sn=750feacfaa2b710f1fda9c266efc5098&chksm=c0c869b5f7bfe0a331c351f54e8adcefdcbbe45a157989e9321fb7af86ae5ab8ecede810edff&scene=21#wechat_redirect)  

							  
  

								[ 小记一次逆向分析 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501882&idx=1&sn=f81013e8a09e890275367a7efe7e8fdc&chksm=c0c869cef7bfe0d81b92a28f2e98af26c8dd45ff5475e58317f93792b423f51cc3786bd50aed&scene=21#wechat_redirect)  

							  
  

								[ 红队武器库2.0版本，内含数百款渗透工具 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501849&idx=1&sn=cfa9166999f9242eaac57c9a74b46b74&chksm=c0c869edf7bfe0fb821f3117f5d519e02bc681ee7448562f2164dec9bc430af66fb807ff6584&scene=21#wechat_redirect)  

							  
  

								[ SSRF打穿内网 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501833&idx=1&sn=650a086ea1158057dec8d9fd714b2ade&chksm=c0c869fdf7bfe0eb3ba649469fdffed70500b9acee8bb8e0b81b98b62879b3f441f884b7c56c&scene=21#wechat_redirect)  

							  
  

								[ 货拉拉在逻辑漏洞自动化检测的实践 ](http://mp.weixin.qq.com/s?__biz=MzkwODM3NjIxOQ==&mid=2247501830&idx=1&sn=752ab849a1a431aaaa222c3ca3e1f203&chksm=c0c869f2f7bfe0e448f27d906992c10e9ef360481cdca045ff059220ffa21e4354b2d5ac6e90&scene=21#wechat_redirect)  

							  
  
  
   
  
![](https://mmbiz.qpic.cn/mmbiz_png/Ngu0cYa5JdjQIPE8G8k6vwgYicqnqMH1w5pcv9o54qTO9gEWA9HCpZZ8zljsa1UTHTg3bS6WjbRoSaOibMv5pIMw/640? "")  
  
点个  
在看你最好看  
  
