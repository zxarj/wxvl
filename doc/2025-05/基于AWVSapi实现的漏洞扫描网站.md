#  基于AWVSapi实现的漏洞扫描网站   
Kyon-H  夜组安全   2025-05-05 12:00  
  
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
  
VulnScan，基于AWVSapi实现的漏洞扫描网站。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaTOrbBKMpJyaFoJ5tQWzxvZjdCo8WUAiaSudL7ESGVql7zwJhydH0mtCg/640?wx_fmt=png&from=appmsg "")  
## 功能介绍  
  
**登录注册功能**  
：通过Kaptcha、spring security实现验证码登录，密码加密，用户验证。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaTCiariaocxXlflgn55gDtIM5WOvc5xWDXnQZwrogDPdSXicfo0kBHia3NRg/640?wx_fmt=png&from=appmsg "")  
  
**目标扫描功能**  
：添加扫描目标地址，并设置扫描速度、扫描类型、登录设置（用户名密码登录、Cookie登录）等信息。添加扫描后利用WebSocket实时监测扫描状态，并将漏洞分布和扫描进度信息显示在前端页面。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaTYclnDZg7BsCZJJAQUicDKUpPic0GRQlLdnl32bY42DlwjptSjice07L7Q/640?wx_fmt=png&from=appmsg "")  
  
**查看漏洞功能**  
：列表显示扫描出的全部漏洞。可查看单个扫描目标的漏洞或单个扫描目标的单个漏洞严重程度的漏洞信息。点击漏洞名称可查看漏洞详情。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaTRI55qL1AuCmTTx9swDbt8JTHKkIQfice3uXn1w1FgRt8e7lhkicIdRWw/640?wx_fmt=png&from=appmsg "")  
  
**扫描报告和漏洞报告导出功能**  
：将扫描结果或漏洞信息导出为html或pdf文件。可选择导出的模板，如CWE 2011、OWASP Top 10 2017、ISO 27001等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaT2MNrfbV1VeP9cXSbQdsZYVJmHPAwTBtq7vxMHAGsRsmuK5RKptDVeg/640?wx_fmt=png&from=appmsg "")  
  
**信息统计功能**  
：对用户的扫描记录和扫描出的漏洞信息进行统计，使用Echarts插件显示图表信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WcEJkwkw9uR65Gz6uyRibaTEoejPcetL8htsibhuzW1V6T02LSM1RslGspFib3MxMkfS7qUU9ZS9ySQ/640?wx_fmt=png&from=appmsg "")  
  
**AWVS API相关功能**  
：通过RestTemplate向AWVS发送和获取数据，包括目标、扫描、漏洞、报告等相关API。  
  
**WebSocket功能**  
：1.调用异步线程获取扫描状态信息。2.调用异步线程生成报告链接等信息，结束后返回状态信息。3.回复前端的心跳检测信息。  
  
**数据校验功能**  
：对前端的数据进行JSR303数据校验，自定义枚举校验。  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
250505  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
往期推荐  
  
[外网打点、内网渗透工具箱](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494206&idx=1&sn=5d26c5707c7078490bbc5309e324eccd&chksm=c36baec6f41c27d0cb9ee923db64b65cad90bb694642a92f47220e5c4c6ccbc34f34f4fbba78&scene=21#wechat_redirect)  
  
  
[EasyTools 一个简单方便使用的渗透测试工具箱](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494198&idx=1&sn=f83063f00b50e6d578e546b16035ab13&chksm=c36baecef41c27d8ee011cbb5d1b30537a72c909659206e15e94ccbf0845aed6f42c70e626b0&scene=21#wechat_redirect)  
  
  
[Yakit插件-用于转换BurpSuite上无敌的Hae信息收集插件的配置规则为yakit使用](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494197&idx=1&sn=b0cfd1231003385f6b41eec30d1a4fba&chksm=c36baecdf41c27db354a6b943c766cde8fe0a77dafc74730f32cd01d09cf6934abcc165a4c61&scene=21#wechat_redirect)  
  
  
[微信小程序自动化辅助渗透工具e0e1-wx更新！V2.0](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494196&idx=1&sn=81fbe3c0a6e7d96e6cfac0cddcc0e0d4&chksm=c36baeccf41c27da408b162f084ea295efb26fcf9e3e6ea8f0ceca39269f38fef3b376d4bbea&scene=21#wechat_redirect)  
  
  
[自动化漏扫工具、外网打点、内网扫描 更新V1.3.0](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494187&idx=1&sn=d6ba1d8e9cf481795442b81c0c245069&chksm=c36baed3f41c27c534da37fd14d1ee22cc7de35cf13a5f1969c1e873578cfa640b7bd17cb9e2&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
