#  SQL注入漏洞批量检查工具   
malvads  Hack分享吧   2024-12-18 00:31  
  
<table><tbody><tr><td width="557" valign="top" height="62" style="word-break: break-all;"><p style="margin-top: 8px;margin-bottom: 8px;"><span style="font-size: 14px;"><span style="color: rgb(217, 33, 66);"><strong>声明：</strong></span>该公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。</span></p></td></tr></tbody></table>  
  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
Hack分享吧  
“  
设为星标  
”，  
否则可能看不到了  
！  
  
  
**工具介绍**  
  
SQLMC（SQL注入大规模检查器）是一款用于扫描域中是否存在SQL注入漏洞的工具。它会抓取给定的URL直至指定深度，检查每个链接是否存在SQL注入漏洞，并报告其发现的结果。  
  
  
**工具特征**  
```
扫描域名中是否存在SQL注入漏洞
爬取给定的URL直到指定深度
检查每个链接的所有GET参数是否存在SQL注入漏洞
报告漏洞以及服务器信息和深度
```  
  
  
**安装使用**  
  
Kali官方软件源中已有这个工具，直接使用以下命令安装即可，如单独下载安装则需安装所需依赖项。  
```
└─# apt-get install sqlmc --fix-missing

pip3 install -r requirements.txt
```  
  
‍![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mluq8JtBbOzO3PQab0ObINmmqgJSdawgiaUTwVwdFh3ABChnqYqjhjgyg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mluq8JtBbOzO3PQab0ObINmmqgJSdawgiaUTwVwdFh3ABChnqYqjhjgyg/640?wx_fmt=png&from=appmsg "")  
  
  
sqlmc使用以下命令行参数运行：  
```
 -u, --url：需要扫描的 URL（必填）
 -d, --depth：扫描深度（必填）
 -o, --output：保存结果的输出文件
```  
  
  
使用示例：  
```
sqlmc -u http://example.com -d 2
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mlqzzVibNEticL4FRsXOH225N1unBye4c69uUNkaPSfj5ArL7d1PQ7XlNA/640?wx_fmt=png&from=appmsg "")  
  
  
**下载地址**  
  
**点击下方名片进入公众号**  
  
**回复关键字【**  
**241218****】获取**  
**下载链接**  
  
  
  
**知 识 星 球**  
  
  
  
仅前1-400名: 99¥，400-600名  
: 128¥，  
600-800名  
: 148¥，  
800-1000+名  
: 168¥  
，  
所剩不多了...！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6ufVCAtR63B7OpLKUz7Ey9zcllEBlpicVLCBBqtVE3miciahWdLUEaibyibdV7JTnkKzxqaAFbicN6sRF64w/640?wx_fmt=png&from=appmsg "")  
  
往期推荐工具  
  
[Commando VM 3.0 红队渗透工具集](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247488119&idx=1&sn=46b3e67c8df3371ed89345483a28fd81&chksm=9036f4cfa7417dd99eb192885f0027d772137ad5aa5492b11e497e07c99094dd1224202510a0&scene=21#wechat_redirect)  
  
  
[Hikvision海康威视数据库账号解密工具](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247487695&idx=1&sn=abc501bf88daa8fc338d1d9e8ddafa2d&chksm=9036f677a7417f61ee0ddae07cf2e3158223c862ac7510dd5f35c70f84b4d700d64d0e19f273&scene=21#wechat_redirect)  
  
  
[很强！Windows11 渗透测试工具包](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486427&idx=1&sn=4a229ee22d428a2c926f9250e6de6a56&chksm=9036ed63a741647536b01e6397483c6cee5eb4dd0ee551728c34e8d0b1a73cfdc64c6c69922b&scene=21#wechat_redirect)  
  
  
[N！9个OA高危漏洞利用工具v1.1.6](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486468&idx=1&sn=67e6dc1a332769490a2b3062b6c7a909&chksm=9036eabca74163aa9572b4baee14ad2bc1b16c990c64c9e865b8319a31bc23b0b021a03d4b51&scene=21#wechat_redirect)  
  
  
[v1.1！最新版Weblogic漏洞利用工具](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486498&idx=1&sn=2c0458c4a1a51518d888dd553d86beed&chksm=9036ea9aa741638c0bbd6cb8d66f197df3d929960f3aa712960c3a016fd9c36c953051b723d8&scene=21#wechat_redirect)  
  
  
[防溯源！无VPS也可用的C2小工具](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486150&idx=1&sn=f5b71fa5e38dd67b558350987198a4fd&chksm=9036ec7ea7416568728ffe8ba9cdf76c51480bd1c5da2e921cdca2e3f4d5222b504173781599&scene=21#wechat_redirect)  
  
  
[Q！两个免费的数据泄露查询平台](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486138&idx=1&sn=9ba3b3d72c6f8199be9732ea0fe24995&chksm=9036ec02a7416514c46b532af361cbf9073351710013504835751a583a1b54e350f040d1d0a0&scene=21#wechat_redirect)  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247483907&idx=1&sn=4e7cf5de0472f6685edb64a598e6aff8&chksm=9036e4bba7416dad5aa253462a84d0c47fdb4e89914c70bd5a3fbbd8b4ef05572a4e7e702faa&scene=21#wechat_redirect)  
[GodPotato！新版土豆提权利用工具](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247486017&idx=1&sn=63dec820664e5abc687ebbeb389ee3ba&chksm=9036ecf9a74165ef8a9bea29dff6ab7194d53f584cc69f6713ef10e11c0067d6d45ba36bda6d&scene=21#wechat_redirect)  
  
  
[牛B！一个国产的安卓渗透工具箱](http://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247485816&idx=1&sn=55d4450fa7dc6d8ec0ec8ed6a7d8c50d&chksm=9036efc0a74166d638ac84732d5e09caf86956561c6b2f9973f5e91429af0f8c68efcbc3b0e1&scene=21#wechat_redirect)  
  
  
