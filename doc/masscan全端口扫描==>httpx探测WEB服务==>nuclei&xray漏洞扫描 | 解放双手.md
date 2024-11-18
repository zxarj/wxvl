#  masscan全端口扫描==>httpx探测WEB服务==>nuclei&xray漏洞扫描 | 解放双手   
whoisavicii  夜组安全   2024-11-18 00:02  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**baobeiaini_ya**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xvvlzc5lra8XdgLYGCfX5ooaMiaUJy4vKvStTngQp4122jauXltltcCuYib5WBBdaXu5dh91dGvibyQ/640?wx_fmt=png&from=appmsg "")  
  
  
**01**  
  
**工具介绍**  
  
# Masscan2Httpx2Nuclei&xray  
  
****  
masscan全端口扫描==>httpx探测WEB服务==>nuclei&xray漏洞扫描 解放双手  
  
**02**  
  
**环境准备**  
  
  
- 自备nuclei\httpx\xray_linux_amd64放脚本同目录(文件名请保持不变)  
  
- 自备masscan python3环境  
  
- 将要扫描的资产放在ip.txt里面  
  
- python3 Masscan2Httpx2Nuclei.py -i ip.txt -p 1-65535 --rate 2000  
  
- nuclei默认只扫描medium,high,critical级别，方便打野，如有其他需求请自行更新  
  
- 睡一觉  
  
## 没啥技术含量的脚本，能用就行  
##   
##   
  
```
https://github.com/robertdavidgraham/masscan/
https://github.com/projectdiscovery/httpx/
https://github.com/projectdiscovery/nuclei/
https://github.com/chaitin/xray/
```  
  
**03**  
  
**工具下载**  
  
**点击关注下方名片****进入公众号**  
  
**回复关键字【241118****】获取**  
**下载链接**  
  
  
**04**  
  
**往期精彩**  
  
[ JavaSecLab 一款综合Java漏洞平台 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492733&idx=1&sn=d41a5ddfe26f0a9dfaa02fedafee911a&chksm=c36ba085f41c29939223545de63e6dd51eee2d1c2e76755a6f8d9ddcef40fece5748affa600a&scene=21#wechat_redirect)  

						  
  
  
[ 一款java漏洞集合工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492730&idx=1&sn=4830f7a0e4dfa7e50b8fb0ccc7e0e0b9&chksm=c36ba082f41c2994059ab6b2829b5188508869ea9726694e911078775c93f5343300a071a267&scene=21#wechat_redirect)  

						  
  
  
[ 一款集成高危漏洞exp的实用性工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492694&idx=1&sn=593e032dc17a72a4ca4250d4a3f210f1&chksm=c36ba0aef41c29b832e8f14aafe90179de166338058ad1d6096d5b9f956e771a308d9824db65&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557 "")  
  
  
  
