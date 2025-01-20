#  一个支持被动代理的调用 KIMI AI 进行越权漏洞检测的工具   
Ed1s0nZ  夜组安全   2025-01-20 00:00  
  
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
  
利用工作之余（摸鱼）时间花 2 小时完成的小工具，简易版支持通过被动代理调用 KIMI AI 进行越权漏洞检测，检测能力依赖 KIMI API 实现。目前功能较为基础，尚未优化输出，也未加入扫描失败后的重试机制等功能。  
## 工作流程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UkECj8peRvFCP3Hia0iatFVic7uAWNcibic4Ay92J8t7E7UHDsflmWYGfR0TV37XD2yGe3Nl6XfSibeMQQ/640?wx_fmt=png&from=appmsg "")  
## 使用方法  
1. 下载源代码；  
  
1. 编辑config.go文件，配置apiKey（Kimi的API秘钥） 和cookie2（响应2对应的cookie），可按需配置suffixes（接口后缀白名单，如.js）；  
  
1. go build编译项目，并运行二进制文件；  
  
1. BurpSuite 挂下级代理 127.0.0.1:9080（端口可在mitmproxy.go 的Addr:":9080", 中配置）即可开始扫描。  
  
## 效果  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UkECj8peRvFCP3Hia0iatFVic4kgVVPQOgbjscn2icUsv7QyRaTZxPOric3W5PLbCZvfd77RucW0tTfgg/640?wx_fmt=png&from=appmsg "")  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
250120  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
[ SimpleIAST- 基于污点追踪的灰盒漏洞扫描工具。 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493301&idx=1&sn=14d3843029a33e9ea975e81ed20fab0d&chksm=c36ba24df41c2b5bc59798d6290ae8a7eac9166f8af0864feb2966f5d730bd6449188ee8592f&scene=21#wechat_redirect)  

						  
  
  
[ 一款微信小程序源码包信息收集工具，根据已有项目改编 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493290&idx=1&sn=a995aeef1e1fcab2781421ef2ef70a1a&chksm=c36ba252f41c2b448c921c829cc0e7a118fe0acdc7dd58d3a8b8dd82673eb49d1b1942f5eb39&scene=21#wechat_redirect)  

						  
  
  
[ 专注于软件供应链安全，具备专业的软件成分分析（SCA）、漏洞检测、专业漏洞库。 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493280&idx=1&sn=0c9de072c4b55977c5623ecbd68293a6&chksm=c36ba258f41c2b4e58900d7f5a9b977fd20838adbc1ecc0caa94847b3ce869038b2466181c9c&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
