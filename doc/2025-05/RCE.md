#  RCE   
 迪哥讲事   2025-05-20 09:30  
  
春日午后，我沿着杨柳大道悠闲溜达。暖融融的阳光穿过新抽嫩芽的柳枝，在柏油路上折射出细碎的金斑。道旁绿化带里，嫩绿的草叶间零星点缀着淡紫色野花，春风拂过，柳絮如雪般轻盈飘落。不经意间，一抹黑色闯入视野 —— 绿化带边缘的枯叶堆里，半支黑色 U 盘闪着金属冷光，在阳光下折射出奇异的反光，像是在无声地召唤。我弯腰拨开杂草捡起它，发现 U 盘外壳上斑驳的标签写着 “RCE 备份”，边缘还残留着些许泥土，谁能想到这个被遗落在春意里的小小物件，竟藏着两年前的远程命令执行漏洞代码。  
  
风掀起桌上的 A4 纸，我望着窗外随风摇曳的柳枝，忽然觉得这场景像极了此刻攥在掌心的 U 盘 —— 有些秘密，总藏在最意想不到的角落，等着被阳光照亮的瞬间，抖落满身尘埃。  
  
唰～，我从梦里醒来，看着 手机上亮眼的 9.05，我知道，那是我快迟到了。   
  
看着年年都一样的资产，甚至难堪，漏洞越挖越少，安全等级越来越高，但还是要进行季度测试  
  
打开资产表，随机选中一个，映入眼前的，则是普通的登录页面，只是颜色过于单调  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEjdDekyp7qJAaic2F7VMEneQjRmBOjRiaTcQxcueia1MNI2CCz4adSedFg/640?wx_fmt=png&from=appmsg "")  
  
  
首先脑海里浮现很多知识，突然有人开口说先测弱口令，另一个则说 测个毛线弱口令，我天天看他挖漏洞，一个弱口令都没挖到。  
  
. . . . . .  
  
stop，你俩安静点，思路都被你们扰乱了。  
  
随后，按照登陆框测试思路，我先打开谷歌插件，查看 js 路径，就这么几条，还挖个屁  
  
但是看到路径，有似曾相识的赶紧，原来是 thinkphp 老前辈  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEqzZHvCB62slkwMfYF7WpkzXGR8GGia7dL213D4gljycL0Bheeu5k0zw/640?wx_fmt=png&from=appmsg "")  
  
  
为了验证结果，我在域名后面输入 aaaaa，然后报错信息中确定了 thinkphp，并且版本是 5.0.9  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYE9egwK4fOg3FYz0RbOreJ98TQlXxcKSpLnnQ4bKXq0I1HVK2muFnicjw/640?wx_fmt=png&from=appmsg "")  
  
  
于是掏出祖传扫描工具，开始进行探测  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYE4FjXz4zJYoXHtwOaqUurVwib9axz94QjPVicSbaiabVmMPz7WmO65gLvw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEsxiaCDDuj046zuKorNa92mEu7D6C7GIH5EiaZlBL2KacmmkiahoS10vhA/640?wx_fmt=png&from=appmsg "")  
  
  
为什么要这么对我，我到底哪里做错了，为什么一个 poc 都没成功，哦  不 ！！！！  
  
忽然我看到了一抹曙光，那是注册按钮  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYE5IkzzaHM3jU7v0gAVnq1ORziaX1TL7OPrzj2ylAUFBcD58GS5px2jUA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYE3RVicJ10qmJKBCI6jOKicU4yd62HUBo0znSOgfnpz3EtQYw74eQv2wtg/640?wx_fmt=png&from=appmsg "")  
  
  
发送成功，但是手机却没收到验证码，又一次伤了我的心  
  
于是针对特定版本搜索 poc  
```
```  
  
五一例外，全是 error  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEeaI3eLD7Nj8Qia0DpuCujckzl51XskpKRaRibNicic2yDngdHsyrnx8wQQ/640?wx_fmt=png&from=appmsg "")  
  
## 信息泄露  
  
就在我百思不得其解时，我灵光一闪，index 模块不存在，要么删除了要么改名字了  
  
结合刚刚手机号注册的接口，api 会不会就是 index？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEcrpjq2kJZx7D5iczAg8h46cjicPDXbrpPC9UQFHczic79QRRJticwvVBSw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYE0NuXgUj6icCfKHdCibo5ibCp9MQGGJ1al3jNNPLw0zp3MfO7aAoLwib7ibA/640?wx_fmt=png&from=appmsg "")  
  
果然，成功了，怪不得扫不出来，工具里的 poc 都是 index 开头  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEibibKfyVdtcbJ0IuBPddGVSic2Ipia8fy0wVgCZyC7MfqoXKgKGXV0WjIA/640?wx_fmt=png&from=appmsg "")  
  
既然显示出数据库的信息了，那岂不是可以连接了  
  
当你开了一扇门，肯定会有一扇窗被关闭  
  
内网的数据库地址，这让我很难办啊  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEDRicNb40brX2AIib6GsPB8F5uTa0WEvQgczbCpjJwJKLwGYvD1hib5icfA/640?wx_fmt=png&from=appmsg "")  
  
## RCE  
  
然后又试了其他 poc，果不其然，还是存在漏洞滴  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEeibvkced5RiaGbiaKsqkn8fMQk0yIOULUJd57lP8RYeKO1qzH1oYtRaHg/640?wx_fmt=png&from=appmsg "")  
  
  
我猜想，或许是接口名称的悄然变更，让它在两年时光里与无数目光擦肩而过，始终未被察觉。直至今日，终于为第一次测试时遗留的空缺画上了句号。  
## SQL  
  
下一处亦然是一个登录页面，但此时的框架变成了 jeecg-boot  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYExB5pcbftJrhWPbNflhogFj1qoW13TLeE0SYsOuMy69ntTGhSnxBic3w/640?wx_fmt=png&from=appmsg "")  
  
根据数据包中存在   
/sys/login  
 路径这一特征，结合我此前对 CMS 系统架构的审计经验，初步判断该目标系统可能存在特定风险。  
  
从技术细节来看，多数基于   
**Jeecg-Boot**  
 开发的系统会内嵌   
**JMReport（积木报表）**  
。在过往审计中发现，该组件通常存在多个潜在漏洞接口。经本轮测试验证，发现其中  
**仅一个接口未进行权限认证**  
，且通过该接口成功触发了  
**SQL 注入漏洞**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYESgukcfTXsyhWv1dfMQoaATAPIYKXNoC0uAHB9BzAloWHdBSpKJuLIw/640?wx_fmt=png&from=appmsg "")  
  
  
剩下就是普通漏洞了  
## 越权+存储 XSS+反射 XSS  
  
越权访问，注册商家账号，通过接口里泄露用户功能访问列表  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEbQIwGBftBBuibibWL2foV0CmuYCQiaWqpPI1SUKNPeme1pFETJcvy63Fg/640?wx_fmt=png&from=appmsg "")  
  
  
然后就越权到个人中心了，修改昵称为 xss 语句，然后有个变更日志，打开就触发 xss 了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEsWVqWHLoVkSylIxkwLr1iaY7DGRjowILfnXkde7q1kEY1kfN5IIDWBQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYESkWQTLAyWFIic9h7E3DXRTQiap5x25iaZlVnsmVFpuL1DxTt1csB9qZzQ/640?wx_fmt=png&from=appmsg "")  
  
  
反射 xss 就是 ueditor 编辑器，你们懂的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQbLkACGcEqzY7p9yib1tBEYEWcIeI5Cda1rOPgaiapZErZfKJT1z1BZ11FsUEt9rH3SjY1Y777cdqeQ/640?wx_fmt=png&from=appmsg "")  
  
如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款  
  
![https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
注:星球老会员一律半折  
  
  
往期回顾  
# 如何绕过签名校验  
#   
  
[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)  
  
  
[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)  
  
  
[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)  
  
  
[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)  
  
  
[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)  
  
  
[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)  
  
  
[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
  
  
  
