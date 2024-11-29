#  Burpsuite存储桶配置不当漏洞检测插件   
libaibaia  夜组安全   2024-11-29 00:02  
  
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
  
存储桶相关配置检测自动化，访问目标网站将会自动检测，如：访问的网站引用存储桶上的静态资源，就会触发检测逻辑,将指纹识别方式修改了下，通过server头及域名中的一个方式进行判断，另外由于敏感信息误报较多，已经取消了。  
## 导入burpsuite  
## 存储桶相关配置问题检测结果同步到bp的issue  
## 检测结果，目前支持阿里云，华为云，腾讯三个厂商的检测，存储桶文件遍历，acl读写，Policy读写及未授权上传  
  
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2XUsVf0BYHK9lBfjbr5JjHXEw6vxTHzQ4IpQmEf1AyAst0a2QTMe5ZG7E9BIwElrUY6VUA7dPHnTQ/640?wx_fmt=png&from=appmsg "")  
使用的新版bp接口，所以版本有要求，jdk17  
## 打包  
```
mvn package
```  
## 导入bp  
##   
## 敏感字段会在这个面板展示  
##   
  
  
**02**  
  
**工具下载**  
  
**点击关注下方名片****进入公众号**  
  
**回复关键字【241129****】获取**  
**下载链接**  
  
  
**03**  
  
**往期精彩**  
  
[ 一个好用的越权扫描工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492818&idx=1&sn=3e7742054baf1b71a35ffdd6ceac4290&chksm=c36ba02af41c293c833f2a13afadd3291199e7691cdf9d5990a7947c4b728887dd254432ac62&scene=21#wechat_redirect)  

						  
  
  
[ James_synthesis_tooL | 日常渗透测试或攻防演练中对于漏洞及指纹的积累工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492810&idx=1&sn=389a83e0263bfc916ef686658d7b17e3&chksm=c36ba032f41c2924c846ec04c4e7560c7b7863289d3125841faa7fce4e4be0943d21feb5ba8b&scene=21#wechat_redirect)  

						  
  
  
[ HeavenlyBypassAV免杀工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492795&idx=1&sn=26d535dd11cc123c4388efa29fa86285&chksm=c36ba043f41c295593eb76d4ba5acc284847585eb639ad43da91a0a8ab8840c529ab8b0a1d49&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557 "")  
  
