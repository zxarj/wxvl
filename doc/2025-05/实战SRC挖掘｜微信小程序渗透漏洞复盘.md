#  实战SRC挖掘｜微信小程序渗透漏洞复盘   
原创 神农Sec  神农Sec   2025-05-27 02:03  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
网络安全领域各种资源，EDUSRC证书站挖掘、红蓝攻防、渗透测试等优质文章，以及工具分享、前沿信息分享、POC、EXP分享。  
不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。  
#   
  
文章作者：  
一个想当文人的黑客  
  
文章来源：  
https://xz.aliyun.com/news/18037  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**微信小程序渗透漏洞复盘**  
##   
## 声明  
##   
  
本文章所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
  
## 0x1 前言  
##   
  
哈喽，师傅们这次又来给师傅们分享下最近的一个漏洞挖掘的一个过程，这次跟着一个师傅学习，然后自己动手去挖，也是学习到了不了东西。这次要给师傅们分享的案例是一个微信小程序的案例，这个小程序站点存在多个漏洞可以打，其中最主要是知识点就是开始的一个数据包构造，通过分析登录页面的数据包，进行队里面的数据包构造找到一个敏感信息接口，进而泄露了七千多个用户的sfz、xm、sjh等敏感信息。  
  
  
然后利用这个泄露的接口来进一步漏洞挖掘，扩大危害，其中微信小程序文件上传漏洞还是多的，小程序好多都没什么过滤的，像还有逆天的危险小程序直接没有任何的过滤的也是存在的。这里也是直接打了一个getshell。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsB92EgfGpYrpVXEQywAeEK3zCWGfA0m3iaeQHBibjSBashBOEiaZAxsZ7Q/640?wx_fmt=png&from=appmsg "")  
  
## 0x2 渗透测试  
  
### 一、浅谈  
  
这个EDU的小程序可以直接使用微信一键登录，像我们平常在挖掘微信小程序的时候，经常碰到这样的微信一键登录的功能点，像这样的初衷就是为了方便我们使用，但是越是方便其实对于安全来讲越是不安全的一个过程。  
  
  
就比如常见的一键微信、手机号登录容易造成泄露SessionKey三要素泄露，下面就分享一个我之前挖的一个小程序的微信一键登录泄露SessionKey三要素的一个漏洞。  
  
  
可以看到这个数据包直接把SessionKey、iv以及加密字段三个部分全部泄露了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QskDWLYBZeDICN2a0ng3YKh7gxLb9JA1YlO8FOcmM7QuzqXyue4S1jKA/640?wx_fmt=png&from=appmsg "")  
  
  
然后再使用Wx  
_  
SessionKey  
_  
crypt这个加解密的工具进行解密，可以看到解密出来开始一键微信登录的手机号  
  
  
工具下载链接：  
https://github.com/mrknow001/wx  
_  
sessionkey  
_  
decrypt/releases  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsVfuMCfOP10oUtZNUtfIYlQSYtjSAQfXqNb3LLgHNSlKnE2j65yyEWA/640?wx_fmt=png&from=appmsg "")  
  
  
那么我们是不是可以逆向修改手机号然后加密，再去替换，然后放包就可以登录别人的账户了呢  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QslwHgdSzV2JpSA7XhRcRECqmSJoOy10bvke6gZ3xKbB6Je0cKUWxadA/640?wx_fmt=png&from=appmsg "")  
  
### 二、burpsuit数据包分析  
  
  
首先通过微信搜索小程序，找到目标  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsGZNxyB8hcXzicoqtk8yDSZjR27A10JXnfFibIiabvFbCZsiaMCZicKsMHmQ/640?wx_fmt=png&from=appmsg "")  
  
  
这里就再继续跟大家讲下这个小程序的挖掘过程吧，然后带师傅们一起看看这个数据包  
  
  
这个数据包相信很多师傅们一眼就可以看出来这个是jeecg框架，这里给师傅们总结下判断jeecg框架特征，最简单的就是看数据包路径关键字，比如/jeecg、/sys、/system等  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsibCPlabv9KAiaq2OKdKslFibKCtRorywvcDiaVjWY04K6VxxFvynZkCwLA/640?wx_fmt=png&from=appmsg "")  
  
  
这里看到这个数据包，利用id（这里是我自己登录时候的id）可以回显出一些三要敏感的信息，比如身份证、姓名、手机号等信息  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1Qszic0jJsGytdnMOmyrpMUFE0U52QgxTSGM847S41RoqdG0iaC0J1f449A/640?wx_fmt=png&from=appmsg "")  
  
  
然后我就想，看看开始的历史数据包里面有没有泄露遍历查看id的路径，获取大量的id，然后去遍历，从而获取大量的敏感信息，然后在这个list的接口下面确实查到了很多的id  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QscUC7TqufcZ68iapIg5pvgYfwHHT1KH1uhpSBrslnuVvfZIMiaIe9yPXg/640?wx_fmt=png&from=appmsg "")  
  
  
然后我这里就替换到刚才的查询敏感信息的接口，去替换那个id值，但是发现不行，后面才知道这里对X-Access-Token值做了校验，所以这里我们没有权限去访问  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1Qs1U4C7ZGRiahCJQFRMwduWL6PMbQOAwqZicg8sIZTtGVHwiaibuXW31AeQA/640?wx_fmt=png&from=appmsg "")  
  
  
然后这里我开始想爆破这个JWT编码，看看有没有JWT密钥，然后再去构造JWT，再去使用user  
_  
id值，然后去编码，抓包放包去遍历或者尝试登录别人的账户信息。  
  
  
但是这里我使用无影这个工具没有爆破出来，于是就没有利用成功  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1Qsibd0YM502YgQx6Gv1GxmEj4Nt4z21R3tu5QH73bpERG9c7WZqK9Ut1w/640?wx_fmt=png&from=appmsg "")  
  
  
但是这里我给师傅们推荐一篇文章是写JWT伪造实战小程序漏洞案例的文章，写的蛮不错的  
  
  
[ 一次完整的Jwt伪造漏洞实战案例  https://mp.weixin.qq.com/s/ITVFuQpA8OCIRj4wW-peAA](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247485655&idx=1&sn=0598b4c4ba4ae8f0d3fa999818df5c7e&scene=21#wechat_redirect)  
  
  
### 三、峰回路转  
  
  
后来我又是回到了原始的页面那几个数据包中，对这几个数据包中的路径进行了一个分析，发现list参数好像都是进行一个数据汇总查看，那么我们上面的数据包通过修改id不成功，那么我们可不可以尝试使用修改接口参数，修改成list的，来进行一个未授权数据访问呢  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsTFgC3pHibXD8dEdrmjcTxXhqVoGZw5abSq3Jy0JdxY6D1KA2AyL3Kiaw/640?wx_fmt=png&from=appmsg "")  
  
  
开始是把id参数和后面的先删掉，然后发现不行，后面再把后面添加list参数发现还是不行  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsrOlvCd5NCLGBlPWP2u5bvXa6VjfzATtBZcaGbKcuCYmvom8h0b9icQg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsPTBIbPdLTYibCMzA0Y0Lq5PSFwjAiab8QiajvXhebTMj3vib2C5ZP1AZ1Q/640?wx_fmt=png&from=appmsg "")  
  
  
后来我就直接把前面的queryById参数删掉，再在后面添加list参数，从而就可以未授权访问敏感信息了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1Qs2YSSfWgPNlkxMy9tXsN3ntKDU894zHxkL3LfdwNCcveTAIUdqUvvGQ/640?wx_fmt=png&from=appmsg "")  
  
  
且泄露的用户数据总共有7802条  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsxjaVmjZQ3HyKjJdxPEhAnicSZk966VvStHQbUEibtwaS5jw2iaPCMVibnA/640?wx_fmt=png&from=appmsg "")  
  
  
这里再构造接口list?pageNo=1&pageSize=7802  
，就可以看到所有的敏感用户信息了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsZqNPCdKbofKicoxudhhEzJSnOt0F9fevU8ndN5DpibktBO2CKVVaCicRA/640?wx_fmt=png&from=appmsg "")  
  
### 四、再次突破  
  
  
这里碰到了idPhotoF和idPhotoZ参数，这两个参数我之前也是碰到过，在很多的招聘平台遇到过，就是需要我们认证信息，上次个人身份证正反面  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsZc3TKrzFibxQlI5K5F1uLUiaYicicYNmp9UPkskt1PlFBka9yw5lh8mT9g/640?wx_fmt=png&from=appmsg "")  
  
  
我们正常思路就是知道这个照片的路径，就直接拼接数据包的host域名，但是这里并没有成功,spring-boot的报错页面，碰到这个师傅们也可以考虑使用曾哥的spring文件泄露扫描工具扫  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsujjUgzJ4ltRAss5rRIpXicdtKrbtb5KDWic9s4QZS6ltWcHlvjtxHnxQ/640?wx_fmt=png&from=appmsg "")  
  
  
那么我们就得判断是不是路径的问题，那么我们怎么去找正确的文件存储的位置呢，下面就刚好看到了文件下载的功能点，点击尝试下载，然后看看数据包里面文件路径  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsCkblHwRg5icvjnicZZPZKoMaRaZmiaeSB9vrULdaiaQj76BFshG0kSVwPw/640?wx_fmt=png&from=appmsg "")  
  
  
可以看到这个路径确实在数据包中，那么我们就可以把路径拼接在这里尝试下，看看能不能有照片回显  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsEm4WGfibc4txqIYEpQpWQQcWC67iaJdlLTRmIiaI8bq9b8Us464KrhicWw/640?wx_fmt=png&from=appmsg "")  
  
  
这里直接拼接/download路径，直接可以回显图片成功  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsBEicom2yFyc4hGstLwKV19ibWCDCkkcEdGZxNCZGsJqVgvjyrJEvCfpg/640?wx_fmt=png&from=appmsg "")  
  
  
直接可以在浏览器拼接host访问得到身份证正面照片  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsicicWfajLwqeD7F7oXukXicOqLiaCG2KRmvlCvYnkueB42nDVf4GdVRzkA/640?wx_fmt=png&from=appmsg "")  
  
  
我们这里总共有7806张身份证正面照片的url路径，这里我们就可以写个python脚本，把他们从数据包中爬取出来，然后再自动拼接到host域名上，python脚本如下：  
  
```
import json# 假设你已经获取到了JSON数据，这里我们直接使用你提供的JSON数据json_data = '''数据包内容'''# 解析JSON数据data = json.loads(json_data)# 基础URLbase_url = "https://host/路径"# 遍历每个用户，拼接URL并打印for user in data:    id_photo_f = user.get("idPhotoF")    if id_photo_f:        full_url = base_url + id_photo_f        print(full_url)
```  
  
  
### 五、文件上传漏洞  
  
  
然后这里在测试在线申请功能点的时候，这里需要我们实名认证上传身份证照片  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsdFIicIWkhb8yupeT3nzUeeSAWCE5X8ljPqw1IeoMMnyZXNdBvQaRyiaw/640?wx_fmt=png&from=appmsg "")  
  
  
像碰到这样的文件上传功能点肯定得测试下文件上传，看看有没有什么过滤，试试打文件上传getshell，差点也可以尝试打个存储型XSS漏洞  
  
  
这里先尝试打个XSS漏洞，看看有没有过滤，发现没有，且可以成功解析弹窗XSS漏洞  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsgGia2ich7VcbvoNcp6ZA8NntRfNic6K4eaeu11HYdDzF5P0qicY5d6tDlw/640?wx_fmt=png&from=appmsg "")  
  
  
那么下面我们就可以尝试上传木马，然后进行打下getshell，传马之前，我们得先看这个站点是什么语言写的，使用插件看到是php语言写的网站  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsKI7ibFd8gPKelq82Gaa1QdEr5ibNibNBz5IKtmYN3agy98nDbVpicA1BKA/640?wx_fmt=png&from=appmsg "")  
  
  
但是这里过滤了php，但是没有过滤phtml，且可以成功解析  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsHBGEpVRTy2BrrtEr6KDCvbMmh2encibLKCHMBQpmCMJic6gX4vGSYQpQ/640?wx_fmt=png&from=appmsg "")  
  
  
这里我直接打一个phpinfo页面，证明下危害即可  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsvGv21a4V6DulfS0V04zpovY8FIrLFNyeSHohLxb2Hcq4ichibwZOzIpw/640?wx_fmt=png&from=appmsg "")  
  
### 六、越权  
  
  
这里我们使用微信一键登录的时候并没有进行实名认证，所以点击下面的功能点的时候都会弹窗，需要我们进行实名认证  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsJXQgDkWm7MIyUMYD5FNHvHTJIEDiaXkkJaiaR7Vab4q4x3MDLibygyiagQ/640?wx_fmt=png&from=appmsg "")  
  
  
那么这里我就在想，要是登录别人的账户是不是就可以使用这些功能，且可以看到别人的信息了，而且在开始登录的数据包构造路径中，我们拿到了好多用户的登录用户数据信息  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QshpCkHkp4L6MIZT2R6arz5MoicBPyic2IX0ib2BJTmxECE8qEVMrRfmEdg/640?wx_fmt=png&from=appmsg "")  
  
  
下面我们先退回登录界面，然后使用bp抓登录包，然后修改用户登录信息，用我们刚开始收集到的用户信息，进行数据包替换，然后看看能不能成功登录别人的账户  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsiaicRueGVzEmZDtPbWzlezpUrvNtAdO3zl9eHY1fiaT4oTE2ZRhVZvBvQ/640?wx_fmt=png&from=appmsg "")  
  
  
可以看到我们这里直接就可以替换成功用户数据包，从而越权到别人的账户，从而打了一个水平越权漏洞  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsmemIwvpWiclPW2iaNUibon2DkHjicRCEa5geNLormEibK4968iaGiaLibMJZibg/640?wx_fmt=png&from=appmsg "")  
  
  
既然可以水平越权，那么我们是不是可以尝试下找到admin管理员权限的用户user数据，然后进行替换越权登录呢，下面就来找下，发现确实存在admin管理员权限的用户，然后就是按照上面的越权方式就可以成功登录到管理员的用户了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsYftibHeZwzX5CjPgQt6qmFTDicgnRibwwro19iat4T3WQQ1B7JMnIkypibA/640?wx_fmt=png&from=appmsg "")  
  
## 0x3 总结  
  
  
这里给师傅们总结下我们在进行漏洞挖掘过程中需要注意的细节，比如我们在看到一个功能点多个数据包的时候，我们需要去挨个分析里面的数据包构造，进而分析数据包的走向，去了解数据包的一个业务逻辑，特别是微信小程序，因为它本来就是程序简单，所以对于防御和一些过滤来讲，并没有特别的难，甚至就比如这个小程序都可以文件上传直接getshell了。  
  
  
到这里这篇文章就结束了，上面的漏洞案例就是给师傅们分享到这里了，还希望自己写的文章队师傅们有帮助哈！祝愿师傅们多挖洞，多过漏洞！  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**内部圈子详情介绍**  
  
我们是  
神农安全  
，点赞 + 在看  
 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
```  
  
  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
  
**知识星球——**  
**神农安全**  
  
星球现价   
￥45元  
  
如果你觉得应该加入，就不要犹豫，价格只会上涨，不会下跌  
  
星球人数少于800人 45元/年  
  
星球人数少于1000人 60元/年  
  
（新人优惠卷20，扫码或者私信我即可领取）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJHePfxfpEBEibsuTPjTxtvvTaS1M05C10sGweR6sKjhnt9amVS3aPicGQ/640?wx_fmt=png&from=appmsg "")  
  
欢迎加入星球一起交流，券后价仅45元！！！ 即将满800人涨价  
  
长期  
更新，更多的0day/1day漏洞POC/EXP  
  
  
  
**内部知识库--**  
**（持续更新中）**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFu12KTxgSfI69k7BChztff43VObUMsvvLyqsCRYoQnRKg1ibD7A0U3bQ/640?wx_fmt=png&from=appmsg "")  
  
  
**知识库部分大纲目录如下：**  
  
知识库跟  
知识星球联动，基本上每天保持  
更新，满足圈友的需求  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFhXF33IuCNWh4QOXjMyjshticibyeTV3ZmhJeGias5J14egV36UGXvwGSA/640?wx_fmt=png&from=appmsg "")  
  
  
知识库和知识星球有师傅们关注的  
EDUSRC  
和  
CNVD相关内容（内部资料）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFKDNucibvibBty5UMNwpjeq1ToHpicPxpNwvRNj3JzWlz4QT1kbFqEdnaA/640?wx_fmt=png&from=appmsg "")  
  
  
还有网上流出来的各种  
SRC/CTF等课程视频  
  
量大管饱，扫描下面的知识星球二维码加入即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFxYMxoc1ViciafayxiaK0Z26g1kfbVDybCO8R88lqYQvOiaFgQ8fjOJEjxA/640?wx_fmt=png&from=appmsg "")  
  
  
  
不会挖CNVD？不会挖EDURC？不会挖企业SRC？不会打nday和通杀漏洞？  
  
直接加入我们小圈子：  
知识星球+内部圈子交流群+知识库  
  
快来吧！！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ5wUOL9GnsxoXibKezHTjL6Yvuw6y8nm5ibyL388DdDFvuAtGypahRevg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJO0FHgdr6ach2iaibDRwicrB3Ct1WWhg9PA0fPw2J1icGjQgKENYDozpVJg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
  
内部小圈子——  
圈友反馈  
（  
良心价格  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8Hviaqs0Uv6F4NTNkTKDictgOV445RLkia2rFg6s6eYTSaDunVaRF41qBibY1A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8HviaRhLXFayW3gyfu2eQDCicyctmplJfuMicVibquicNB3Bjdt0Ukhp8ib1G5aQ/640?wx_fmt=png&from=appmsg "")  
  
  
****  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWVyicxYvEv1vYVI0xMu4S1QsfqLqZALjB7VA4jWPQhoFxtFNbpjlAjz8MwH3rtbHtoEoW8qPjqjOTA/640?wx_fmt=jpeg&from=appmsg "")  
  
****  
    
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
  
