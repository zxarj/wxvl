#  EatPoc - 简单的POC捕获工具   
原创 Yangliu  橘猫学安全   2025-03-02 09:35  
  
又到每年大小考的时候了，很多非开源扫描器会集中再这段时间疯狂推送新的POC。大秀肌肉。  
  
有时候不想启用mitmproxy去精细化抓取流量，只想批量保存POC。所以做了这么一个脚本去完成需求。  
  
该工具保存经过的流量(request)，可以再用大模型修改格式，比如改成Nuclei支持的格式。  
  
  
项目地址  
```
https://github.com/yangliukk/EatPoc
```  
  
  
简介  
  
EatPoc是一个简单的模拟mitmproxy功能的HTTP请求捕获、记录和转发工具。  
  
该工具全程面向大模型开发,使用DeepSeek生成主要功能代码,通过Cursor进行优化调整。由于开发方式的特殊性,可能存在一些bug或需要改进的地方。欢迎提出建议和反馈。  
  
使用场景  
  
非开源扫描器POC更新，想进行学习或分析。但查看流量、日志等信息需要跨部门合作。该工具将接收、转发流量并保存到本地。  
  
以xpoc举例  
  
假设运行EatPoc.py的主机IP为：192.168.1.3，默认监听 8000端口  
```
# 获取所有POC
python EatPoc.py 
 
./xpoc -t http://192.168.1.3:8000
 
# 扫描器需要取信息，才能打第二步POC
# 将接收到的流量转发到存在漏洞的系统上
python EatPoc.py -p 8000 -t http://target-server.com
 
./xpoc -t http://192.168.1.3:8000
 
# 转发的目标漏洞系统是HTTPS
python3 EatPoc.py --generate-cert   //生成证书
python3 EatPoc.py -p 8000 --https -t https://target-server.com
 
./xpoc -t https://192.168.1.3:8000  //扫描器也需填https开头
```  
  
运行时的截图  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/p5qELRDe5icnNo8CCAuZSRI9FbmK3gvWXNUGllyGKPXfW8SG3uLFgUnja33cabry4NicGZP1YjYxBoYnbkhibokibg/640?wx_fmt=png&from=appmsg "")  
  
如有侵权，请联系删除  
  
**推荐阅读**  
  
[实战|记一次奇妙的文件上传getshell](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495718&idx=1&sn=e25bcb693e5a50988f4a7ccd4552c2e2&chksm=c04d7718f73afe0e282c778af8587446ff48cd88422701126b0b21fa7f5027c3cde89e0c3d6d&scene=21#wechat_redirect)  
  
  
[「 超详细 | 分享 」手把手教你如何进行内网渗透](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495694&idx=1&sn=502c812024302566881bad63e01e98cb&chksm=c04d7730f73afe267fd4ef57fb3c74416b20db0ba8e6b03f0c1fd7785348860ccafc15404f24&scene=21#wechat_redirect)  
  
  
[神兵利器 | siusiu-渗透工具管理套件](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495385&idx=1&sn=4d2d8456c27e058a30b147cb7ed51ab1&chksm=c04d69e7f73ae0f11b382cddddb4a07828524a53c0c2987d572967371470a48ad82ae96e7eb1&scene=21#wechat_redirect)  
  
  
[一款功能全面的XSS扫描器](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495361&idx=1&sn=26077792908952c6279deeb2a19ebe37&chksm=c04d69fff73ae0e9f2e03dd8e347f35d660a7fd3d51b0f5e45c8c64afc90c0ee34c4251f9c80&scene=21#wechat_redirect)  
  
  
[实战 | 一次利用哥斯拉马绕过宝塔waf](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495331&idx=1&sn=94b63a0ec82de62191f0911a39b63b7a&chksm=c04d699df73ae08b946e4cf53ceea1bc7591dad0ce18a7ccffed33aa52adccb18b4b1aa78f4c&scene=21#wechat_redirect)  
  
  
[BurpCrypto: 万能网站密码爆破测试工具](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495253&idx=1&sn=d4c46484a44892ef7235342d2763e6be&chksm=c04d696bf73ae07d0c16cff3317f6eb847df2251a9f2332bbe7de56cb92da53b206cd4100210&scene=21#wechat_redirect)  
  
  
[快速筛选真实IP并整理为C段 -- 棱眼](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495199&idx=1&sn=74c00ba76f4f6726107e2820daf7817a&chksm=c04d6921f73ae037efe92e051ac3978068d29e76b09cf5b0b501452693984f96baa9436457e4&scene=21#wechat_redirect)  
  
  
[自动探测端口顺便爆破工具t14m4t](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495141&idx=1&sn=084e8231c0495e91d1bd841e3f43b61c&chksm=c04d6adbf73ae3cdbb0a4cc754f78228772d6899b94d0ea6bb735b4b5ca03c51e7715b43d0af&scene=21#wechat_redirect)  
  
  
[渗透工具｜无状态子域名爆破工具（1秒扫160万个子域）](http://mp.weixin.qq.com/s?__biz=Mzg5OTY2NjUxMw==&mid=2247495099&idx=1&sn=385764328aff5ec49acddab380721af0&chksm=c04d6a85f73ae393ffab22021839f5baec3802d495c34fb364cbdd9b7cb0cf642851e9527ba7&scene=21#wechat_redirect)  
  
  
  
**查看更多精彩内容，还请关注**  
**橘猫学安全**  
  
  
**每日坚持学习与分享，觉得文章对你有帮助可在底部给点个“**  
**再看”**  
  
