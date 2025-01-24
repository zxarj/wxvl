#  某系统webpack接口泄露引发的一系列漏洞   
原创 zkaq - 腾风起  掌控安全EDU   2025-01-24 04:00  
  
扫码领资料  
  
获网安教程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
# 本文由掌控安全学院 - 腾风起 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**  
## 信息搜集  
  
这里找到从小穿一条裤子长大的兄弟，要挟他交出来他的统一账号，否则把小时候的照片挂网上，开始某大学的资产搜集，直接hunter搜索此大学域名![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHFJuxgRytQ1DTUvXXSQTUvEEX6Spe4Gz87XficTsOo5boDDWJZZ0Apug/640?wx_fmt=png&from=appmsg "")  
看有价值的站点，ok找到下面的站点  
## 未授权+敏感信息泄露+越权+任意用户密码重置  
#### 1.越权访问  
  
站点是webpack打包 app.js 还有路由的js没有登录就有大量js接口还有path路径泄露![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHFg4OPk66ClwwSMNuHRl2rhJhibssbdO8ZgUCw7LWASQL016pCw3l4HA/640?wx_fmt=png&from=appmsg "")  
以普通用户身份登录，所有的还活着的接口都能访问，很多管理员才能访问接口也能访问，并且进行增删改查等操作，这里提供几个页面：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHpdaDDWu81CEstcmHyXkgXEyEWu2nDnCbPzJuvcqdDQBMPwc3GdEcRQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHfYV4TZLMicbISyffF8IvDarl8lQ6iaeEsy9Eiaql4WKdS7wwttMhasXvQ/640?wx_fmt=png&from=appmsg "")  
#### 2.大量敏感信息  
  
根据上面翻js，找到下面这个页面，接口回显所有用过这个系统的同学和老师的信息，包括身份id，电话，照片，邮箱，学号工号等等，数据量巨大，后面任意用户密码重置会继续利用这些信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibH9fsLwedad5eOfGRZFnUD8KLEJWIm1OJPNq24Axr8tgUIhSiaSicVP9fQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHWVXpYl85L5lzGjTy0IJXicff6tsmpEuIUthOStwlzvF8oxVXJLqUubA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHPQ63RWBCh5cqO7pbWFWK7rKawWlg0TlIrMRLxdibeTq7Oql7uyJSwKg/640?wx_fmt=png&from=appmsg "")  
#### 越权  
  
有些页面做了鉴权，没有访问权限，但是通过前面的未授权获得的信息 我们知道各类用户的id和usertype  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHiahUPCFJfI6s9jiavo9mfByvjccV8JJLicyL9thq1r7hdE5Y4MhQNThJA/640?wx_fmt=png&from=appmsg "")  
比如有一个教师列表接口普通学生无法访问，但是在返回包中，把学生的id和usertype修改为管理员对应的参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHpFSKKC06xMaNxu6OIpm1e5uDd56zZsa6GzLCHIsVP5HwicG9MabETXg/640?wx_fmt=png&from=appmsg "")  
成功访问，拿到所有老师的敏感信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibH8ardsojiaC9UVJFnEZAsq7k6BiaTtqq4J17OiclWHoNcumUiakjsmfKpxg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHuibYeiaDUzWRlWgp19qA6icib3E4Q6V0VAKjXW6sttUKHbLiafk79qJBrEA/640?wx_fmt=png&from=appmsg "")  
#### 任意用户密码重置  
  
在修改密码界面抓取提交的报文，修改成我们前面拿到的各种信息，对应起来id，userNum，cardNum可以实现所有用户的密码修改和信息修改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHBkBteGJOibciaeKqRXlGj0j6uNjHtoRRwXXaPK59LlQPVIggKEpW9NNQ/640?wx_fmt=png&from=appmsg "")  
  
对应不起来会报错  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHNiaEJrlCsnkFiblCFvtrwcxpquz1GtRznXqqg85hPKe1ORs007ibicjjEw/640?wx_fmt=png&from=appmsg "")  
重置其他用户密码并且登录成功![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcptONorLcSQIdv6NV1e6aibHbZQ9O1Sz0r8Q0Habh7ibOu6oAVJSK6eyAJQhI7mpV0pvsf8be55h5Sw/640?wx_fmt=png&from=appmsg "")  
  
  
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，  
  
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**没看够~？欢迎关注！**  
  
  
  
**分享本文到朋友圈，可以凭截图找老师领取**  
  
上千**教程+工具+交流群+靶场账号**哦  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
******分享后扫码加我！**  
  
  
**回顾往期内容**  
  
[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)  
[记一次利用堡垒机内部邮件钓鱼突破外网](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247546579&idx=1&sn=7b98384283af5b40e65bffd578e10edd&token=633082196&lang=zh_CN&scene=21#wechat_redirect)  
[](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)  
  
  
[攻防演练 | 一次近源渗透](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247540190&idx=1&sn=0c370f60c2246dadc9e74f2fcebde915&token=633082196&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[某通用引发供应链的思考](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247539466&idx=1&sn=40e97feb1555bbdd382826e5410d20ac&token=633082196&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[某医院小程序存在支付漏洞和越权](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247533798&idx=1&sn=c469a42556cdef54d3b62f0623484640&token=633082196&lang=zh_CN&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
点赞+在看支持一下吧~感谢看官老爷~   
  
你的点赞是我更新的动力  
  
  
