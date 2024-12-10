#  Burpsuite存储桶配置不当漏洞检测插件   
 进击的HACK   2024-12-09 23:55  
  
Burpsuite存储桶配置不当漏洞检测插件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13 "")  
  
声明：  
文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！  
如有侵权烦请告知，我们会立即删除并致歉。谢谢  
！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13 "")  
  
  
## BucketVulTools  
  
项目地址：  
https://github.com/libaibaia/BucketVulTools  
  
Burpsuite存储桶配置不当漏洞检测插件  
## 用法  
  
存储桶相关配置检测自动化，访问目标网站将会自动检测，如：访问的网站引用存储桶上的静态资源，就会触发检测逻辑,将指纹识别方式修改了下，通过server头及域名中的一个方式进行判断，另外由于敏感信息误报较多，已经取消了。  
## 导入burpsuite  
  
检测结果，目前支持阿里云，华为云，腾讯三个厂商的检测，存储桶文件遍历，acl读写，Policy读写及未授权上传  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrianm0jqQrOB0bzaxGdOv2LQG3xzStQZmqMBG140icCuL30DaFeWP4HPaoMh5n0vnwiafiataSfOHKopQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrianm0jqQrOB0bzaxGdOv2LQZxYdHUGdpZF9YT7zMW7Djrp4xJEQNypha8mAsFlfkknHw2tONDJloA/640?wx_fmt=png&from=appmsg "")  
  
使用的新版bp接口，所以版本有要求，jdk17  
  
  
往期推荐  
  
[burpsuite SQL注入插件](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486953&idx=1&sn=ab10862e21c3541f3bf996f5396697ec&scene=21#wechat_redirect)  
  
  
[轻松编辑修改jar包工具 Recaf](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486945&idx=1&sn=d9459f4760dc0caded551f03b28d1df3&scene=21#wechat_redirect)  
  
  
[apk 变得可调试 debuggable=true](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486880&idx=1&sn=36467fed439ed3885914463567bffb32&scene=21#wechat_redirect)  
  
  
[IDA 动态调试之反反调试](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486870&idx=1&sn=b44669b43a54f84f0e3e4eaa2c7dd25d&scene=21#wechat_redirect)  
  
  
[JWT sign 未校验导致未授权用户登录](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486862&idx=1&sn=2e0bbc1f67930c8ae0dd31032e4bad4f&scene=21#wechat_redirect)  
  
  
[基于flutter的Android vpn代理工具](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486777&idx=1&sn=9c0144199ee718665d6bd790bfb1ee26&chksm=c150aad2f62723c4c2ecbcb94e2d7edbcf4064074d512b96620401dfe59e692ed136406b9dfe&scene=21#wechat_redirect)  
  
  
[Jar Obfuscator - 图形化 JAR/CLASS 字节码混淆工具](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486687&idx=1&sn=bd93740fbab2f192142c3c56ee3c3074&chksm=c150ab34f62722221c32a6cd3b9e051fe0f7383d8c7fae763d428b8a117d61eacd43bbe01428&scene=21#wechat_redirect)  
  
  
[降低js逆向分析难度的油猴脚本](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486673&idx=1&sn=d7ca2ae0861850d4807ff558468c79ba&chksm=c150ab3af627222c68566213b34cbcdbe0ca008bf01303c539364ae906259f1490d3cab3d265&scene=21#wechat_redirect)  
  
  
[简单绕过 IOS应用 frida检测](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486561&idx=1&sn=6582b889e69674b5bfc7c817ec7ce2b3&chksm=c150ab8af627229c4fa75be0bc1f27e24aef5a51059fb88b7e6de9e0bf33f93aeaa3479a0294&scene=21#wechat_redirect)  
  
  
[burp插件 | 自动丢弃不需要的http数据包](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486478&idx=1&sn=435438f1416fe0ab5345bb7f2be38354&chksm=c150abe5f62722f38e7282c061f587c6dd9be835cf25d2ebe15925a381c370efab48ffc05b24&scene=21#wechat_redirect)  
  
  
[轻松入门，frida n种过app特征检测办法之一](http://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247486441&idx=1&sn=d3ca56d7bb74111768ad6450ef567589&chksm=c150ac02f627251487e69e23f91ae5556b76ea1e28d63aebe5e62bb79ada5603e97f5453e021&scene=21#wechat_redirect)  
  
  
  
