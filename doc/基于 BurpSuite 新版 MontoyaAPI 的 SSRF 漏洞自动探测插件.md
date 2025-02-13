#  基于 BurpSuite 新版 MontoyaAPI 的 SSRF 漏洞自动探测插件   
banchengkemeng  夜组安全   2025-02-13 00:01  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**baobeiaini_ya**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
## 工具介绍  
  
Auto-SSRF是一款基于BurpSuite MontoyaApi的自动SSRF漏洞探测插件, 捕获BurpSuite 流经Passive Audit、Proxy、Repeater的流量进行SSRF漏洞探测分析。  
## 运行原理  
1. 捕获参数中存在URL链接特征的请求包  
  
1. 参数值替换为BurpSuite Collaborator的payload(类似DNSLOG)  
  
1. 重新发包, 并监听BurpSuite Collaborator  
  
1. 如果BurpSuite Collaborator收到目标站点发出的请求(HTTP请求),则疑似存在SSRF漏洞  
  
1. 手动确认  
  
## 插件截图  
  
![img.png](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIBqamJRzd6WXRyyK0Wziaiah7C1MeMjUA90qJKnFLdolhjHOvIn0hKYxInH68eaTjcJWq3H3wNGKQ/640?wx_fmt=png&from=appmsg "")  
![img_1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIBqamJRzd6WXRyyK0WziaiaFrZ7YJCSYGlmfouibQE3tVbng56B2apB7MnAYgT02lf9bFMOSHBshvg/640?wx_fmt=png&from=appmsg "")  
![img.png](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UIBqamJRzd6WXRyyK0WziaiaSM48t8iblwOCVMzLPQfPmU4XVcicf0m6WXnjquatYGHhHT4HiaGrH08cg/640?wx_fmt=png&from=appmsg "")  
## Features  
- [x] 插件的启动/关闭取决于BurpSuite的被动扫描状态  
  
- [x] 支持扫描Proxy、Repeater  
  
- [x] 可疑点使用dnslog探测  
  
- [x] 线程池大小可配置  
  
- [x] 支持JSON请求体的扫描  
  
- [x] 支持XML请求体的扫描  
  
- [x] 重复流量过滤  
  
- [x] 重复流量过滤器的缓存持久化  
  
- [x] 配置持久化  
  
- [ ] 接入SRC厂商提供的SSRF靶子  
  
- [ ] 探测127.0.0.1消除误报  
  
- [ ] 自动 Bypass  
  
  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
250213  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[ 自动化扫描利器，指纹识别更精准，漏洞扫描更全面 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493547&idx=1&sn=155a6666a83262fde491030d6f110c94&chksm=c36ba353f41c2a459d800ba21108df90bc7b296a29b6cc20eb3266ca78a92be72964ae519983&scene=21#wechat_redirect)  

						  
  
  
[ Enhanced BurpGPT 是一个强大的 Burp Suite 插件 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493546&idx=1&sn=d97c9804a3e4b1d64a99736fda01598e&chksm=c36ba352f41c2a444428c6dbac6631a12a0b7cf2a87faf13be4aa95f566204d509e4d362fa16&scene=21#wechat_redirect)  

						  
  
  
[ 一款利用爬虫技术实现前端JS加密自动化绕过的渗透测试工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493527&idx=1&sn=26de8cb5a753d31961c39da9ca5aa811&chksm=c36ba36ff41c2a7926d0d349f5f4f6b650e079dd1d3479447992049e5ed5080f5933339e0a90&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
