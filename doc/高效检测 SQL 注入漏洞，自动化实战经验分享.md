#  高效检测 SQL 注入漏洞，自动化实战经验分享   
 谈思实验室   2025-02-19 10:03  
  
点击上方蓝字  
谈思实验室  
  
获取更多汽车网络安全资讯  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeMAO4Gw2MtLSZxnGIPkv87Cs9hZEhMXKxyb6m3d8icLUGIhRqHhHNhLw/640?wx_fmt=jpeg&from=appmsg "")  
  
在渗透测试项目中，经常会收集大量的接口信息，为了提高效率，通常会使用工具来完成自动化测试，针对大量接口的漏洞探测，xray 这方面做的非常不错，但对于 POST 请求，探测方式只能采用被动请求或逐个接口测试的方式。  
  
但是我在实际的工作中，需要针对大量 GET、POST 接口和参数做漏洞探测，而目前比较关注的是 SQL 注入漏洞的检测，所以基于 Xray 关于 SQL 注入检测的 payload，自己完成了一个自动检测 SQL 注入的工具。  
  
**01**  
  
**检测步骤**  
  
  
整个测试过程分为五步：  
  
1、请求 URL 接口，判断其是否存在，避免做无用功  
  
2、基础判断，添加一些特殊字符（如单引号、双引号、括号等），判断页面是否发生变化，如果发生变化，且在页面中出现报错信息，则进一步使用报错注入的语句进行判断，是否存在漏洞，用到的 payload 如下：  
```
#判断报错的漏洞类型执行 payload 计算 1 的 md5 值 c4ca4238a0b923820dcc509a6f75849
error_mysql_payloads = ["extractvalue(1,concat(char(126),md5(1)))", "1/**/and/**/extractvalue(1,concat(char(126),md5(1)))", "'and/**/extractvalue(1,concat(char(126),md5(1)))and'",")/**/AND/**/extractvalue(1,concat(char(126),md5(1)))/**/IN/**/(1", "')/**/AND/**/extractvalue(1,concat(char(126),md5(1)))/**/IN/**/('a"]
error_mssql_payloads = ["convert(int,sys.fn_sqlvarbasetostr(HashBytes('MD5','1')))", "1/**/and/**/convert(int,sys.fn_sqlvarbasetostr(HashBytes('MD5','1')))","'and/**/convert(int,sys.fn_sqlvarbasetostr(HashBytes('MD5','1')))>'0", ")/**/and/**/convert(int,sys.fn_sqlvarbasetostr(HashBytes('MD5','1')))/**/in/**/(1", "')/**/and/**/convert(int,sys.fn_sqlvarbasetostr(HashBytes('MD5','1')))/**/in/**/('a"]
```  
  
3、针对数字型参数，通过减号验证漏洞是否存在，比如 ID 为 101-1 的结果是否与 ID 为 100 的结果一致，如果一致则认为该参数存在漏洞  
  
4、针对参数进行布尔注入验证，例如常用的 and 1=1 这样的参数，主要 payload 参考：  
```
#判断是否存在 bool 型注入，计算页面相似度
bool_common_payload = [["1/**/and+3=3", "1/**/and+3=6"], ["'and'c'='c", "'and'd'='f"], ["%'and'%'='", "%'and'%'='d"]]
```  
  
5、最后检查参数是否存在延时注入，通过判断延时的请求时间来判断是否存在注入，延时 payload 参考：  
```
time_common_payload =[["'and(select*from(select+sleep(6))a/**/union/**/select+1)='", "'and(select*from(select+sleep(1))a/**/union/**/select+1)='"], ["(select*from(select+sleep(6)union/**/select+1)a)", "(select*from(select+sleep(1)union/**/select+1)a)"],["/**/and(select+1)>0waitfor/**/delay'0:0:6'/**/", "/**/and(select+1)>0waitfor/**/delay'0:0:1'/**/"], ["'and(select+1)>0waitfor/**/delay'0:0:6", "'and(select+1)>0waitfor/**/delay'0:0:1"]]
```  
  
**02**  
  
**关键点**  
  
  
在实现的过程中，最为关键的部分就是判断两次请求的页面是否一致，并且排除一些错误干扰，主要有以下几点：  
  
1、状态码判断，两次请求的状态码是否一致  
  
2、错误信息判断，根据报错的关键词进行匹配，比如：  
```
error_mysql_infolist = ["SQL syntax"]
error_mssql_infolist = ["Exception", "SQL Server", "80040e14", "引号不完整"]
error_access_infolist = ["Microsoft JET Database Engine"]
```  
  
3、页面相似度判断，计算两次请求的页面相似度，使用的是 github 上分享的相似度计算  
> https://github.com/SPuerBRead/HTMLSimilarity  
  
  
4、判断页面是否被 WAF 拦截，将 WAF 检测应用其中，针对存在 WAF 的接口，暂时跳过  
  
5、针对一些 PHP 的框架，参数中有些路径啥的无需探测，增加了黑名单参数关键词，比如：  
```
#黑名单参数名
black_parma = ["method", "mod", "s", "act", "Action", "a", "m", "c"]

```  
  
6、在参数中增加检测 payload 时，除了报错注入检测，其他检测不应该出现非正常响应，所以定义了一个黑名单响应码列表：  
```
black_code = [-1, 0, 404, 403, 500, 503, 405, 999]
```  
  
**03**  
  
**实战测试**  
  
  
1、报错注入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6Je0UdBTQ9vMpRmicwRkJ3juN88RIMQSrtKpxqC0H92jGb9ibXIBtG9chIA/640?wx_fmt=png&from=appmsg "")  
  
程序逻辑设置，只要存在报错注入，且能执行 md5 函数，则跳出检测，因为可以百分之百确定存在注入漏洞。  
  
2、数字注入  
  
案例只检测出数字注入，没有检测出布尔注入，通常这两个是同时存在的，可能是 payload 的问题：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeSI6QIQNwxqIa434Mhuo7lAjU1n8d7CdoKvD65iaIx1ibxia5ficDjbQDow/640?wx_fmt=png&from=appmsg "")  
  
使用 SQLmap 进行验证：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JelFbDL5D7ksk45HdQc4PyDKhIxI3lM2DwINOUUImsk3aib95NibQqiaia7A/640?wx_fmt=png&from=appmsg "")  
  
sqlmap 检测出了布尔注入，而脚本未检测出。  
  
3、布尔注入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeUlicG6v6PrIHvbKJoTjsDRzAq4BcVAEkPI3qPsYT24u6dkZBZ6SPkGQ/640?wx_fmt=png&from=appmsg "")  
  
使用 sqlmap 进行验证：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeaXHdTibfGJKGcKkfSWnHhJNzTyg6FhzKNE2aTnKKwbp2QwOQW6FgbsQ/640?wx_fmt=png&from=appmsg "")  
  
该案例只检测出目标存在布尔注入，跟脚本检测结果相同。  
  
4、时间盲注  
  
案例中只检测到时间盲注，为检测到其他注入方式：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6Je0bkptJCNzKicORxT2iaUiaUibfxtBX6XmVnFqyFQmeBlCK9qTha3ZiaBvrQ/640?wx_fmt=png&from=appmsg "")  
  
使用 SQLmap 进行验证：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JepmP6B5sFbZibf2c15aEbRxjzib6YP6fsibkn3fuRk5zvM3ichxB5wtddPg/640?wx_fmt=png&from=appmsg "")  
  
从结果上看，工具在验证方面还存在可以优化的部分，因为 sqlmap 检测出来了布尔注入，而该脚本未能实现。  
  
  
**end**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JePD3iaE5Sk18pHhXjxZCvFiaRl17NU5JuuY63Q0yVJu3icYItwyR1xeH2g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**精品活动推荐**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6Je89IuowXsHuccic2u3OvsyN9ZS7Ys8QpibH0CDkG0zl0WxQeNwTo9oYuw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JesbtOn5J0UFlOjHvNOHuVTBKRssAllZMla8iaxx1e66c1Owicf8HbU3icA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeMAO4Gw2MtLSZxnGIPkv87Cs9hZEhMXKxyb6m3d8icLUGIhRqHhHNhLw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JejbBOjQX1niaFYZfYQY8GMWPI5TdrD5usEL4osLy619WPJys9u4L61AQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JenlicuSmqeicSxlzBZ8M534Gbcic36hfjHpqd4icwWmNBsmuicxZuDDiajmaQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeEoZQ3LdWic1pk1B4TAicrdwskvmGbeyBP2AYWWLm778IdcfWSicia1oFHQ/640?wx_fmt=png&from=appmsg "")  
  
  
**专业社群**  
  
  
[](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)  
  
**部分入群专家来自：**  
  
  
**新势力车企：**  
  
特斯拉、合众新能源-哪吒、理想、极氪、小米、宾理汽车、极越、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......  
  
**外资传统主流车企代表:**  
  
大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......  
  
**内资传统主流车企：**  
  
吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......  
  
**全球领先一级供应商：**  
  
博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、赢彻科技、潍柴集团、地平线、紫光同芯、字节跳动、......  
  
**二级供应商(500+以上)：**  
  
Upstream、ETAS、Synopsys、NXP、TUV、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信大捷安、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、软安科技、浙江大学......  
  
**人员占比**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6Je2DDOicXUIsKjx8jiay3pF8CYR71OkpuaibDfGiaYbOib6hWkfn9xjI2cvZg/640?wx_fmt=png&from=appmsg "")  
  
  
**公司类型占比**  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibYJzia90PnKjtMKAY1pp6JeiaShADfpUQ0qJoUTO40EQR9wpHLjEGCY1F3MPbicibh26gPxkKCwic7Xgg/640?wx_fmt=png&from=appmsg "")  
  
**更多文章**  
  
# 不要错过哦，这可能是汽车网络安全产业最大的专属社区！  
  
[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)  
  
  
[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)  
  
  
[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82a9&scene=21#wechat_redirect)  
  
  
[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519068&idx=1&sn=78c66e13bd8798afd46c766b8f18abe7&chksm=e927cf87de504691c816f78b55daf93bdfb72fc1cb870d926de8b471eb3e1be61058498327b1&scene=21#wechat_redirect)  
  
  
[浅析汽车芯片信息安全之安全启动](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247512151&idx=1&sn=7fabbeeec206ce615a5a3c574bed4c43&chksm=e927f48cde507d9ab6bfd4b8389b5eafea37586707682bfe60f294feb54e1c36cb07bad4d26d&scene=21#wechat_redirect)  
  
  
[域集中式架构的汽车车载通信安全方案探究](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519952&idx=2&sn=709860de942501f20e923d15330ced9a&chksm=e927ca0bde50431df0b47ad1a2da63bf98ee637c9c00482145fbdb8755851b61421357aab4bf&scene=21#wechat_redirect)  
  
  
[系统安全架构之车辆网络安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247520446&idx=1&sn=27e10e455264cecb2a1b49d91484d036&chksm=e927d465de505d73c59a6fb4cb066c7c7d07a96ef49a841ffe598c23d28be545c5874dec7de4&scene=21#wechat_redirect)  
  
  
[车联网中的隐私保护问题](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247521010&idx=1&sn=94ef379e2b877551093a869cf9d4897e&chksm=e927d629de505f3f3cbc102682f7a21a82372108776d3484d8ce619f7db1aae0ab0a001b9b41&scene=21#wechat_redirect)  
  
  
[智能网联汽车网络安全技术研究](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247521302&idx=1&sn=01e9311cb2c84f3e64902abf5f6e7a9e&chksm=e927d0cdde5059db5fe18c5e27f830bbb6ea6df327088082e7844aa056b05f840ad4cf6e3b5a&scene=21#wechat_redirect)  
  
  
[AUTOSAR 信息安全框架和关键技术分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247521661&idx=1&sn=a72381e326e3a226059954c74698e0dd&chksm=e927d1a6de5058b0297b91ba77fcf34bd3c581476a0790c5e0cfbcbe026b5a7c27d700bfb1ca&scene=21#wechat_redirect)  
  
  
[AUTOSAR 信息安全机制有哪些？](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247522056&idx=1&sn=bbd03def212d085f533e0301f8c86f18&chksm=e927d3d3de505ac57099d5e42fb6726cf152de9aaa9590b095895874e7a4cc806abc84cc4ebf&scene=21#wechat_redirect)  
  
  
[信息安全的底层机制](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247522886&idx=1&sn=77103702d98e3788beae34b8ea3c31d0&chksm=e927de9dde50578b3dce0bba65599da38844310edd8554f43c9f1c354eaa0487b7c8b4f65c3c&scene=21#wechat_redirect)  
  
  
[汽车网络安全](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247523567&idx=1&sn=1b1d83f339de81a0dc396dd0bd6e6893&chksm=e927d834de50512246f63e47a32f7b934e64eb2b6138053ef43485b871736a122db1340bc437&scene=21#wechat_redirect)  
  
  
[Autosar硬件安全模块HSM的使用](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247527177&idx=1&sn=984bfc845ef51ec1f32cd12d37430621&chksm=e9272fd2de50a6c4013f84ed2257f634a505a04a27b4b27c30e5af4492d5fc3b0099216b1f7d&scene=21#wechat_redirect)  
  
  
[首发!小米雷军两会上就汽车数据安全问题建言：关于构建完善汽车数据安全管理体系的建议](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519331&idx=1&sn=925d48164f1c7d2d109ee433cde6805b&chksm=e927c8b8de5041aea58f73aed311cdd3bf913bbb73d8e175ac80ae643d944709e06ec418fb52&scene=21#wechat_redirect)  
  
  
