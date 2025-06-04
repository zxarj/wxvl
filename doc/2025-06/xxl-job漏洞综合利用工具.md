#  xxl-job漏洞综合利用工具   
pureqh  李白你好   2025-06-04 00:00  
  
**免责声明：**  
由于传播、利用本公众号李白你好所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号李白你好及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
## 工具介绍  
  
xxl-job漏洞综合利用工具  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCCJg3pR9eIphgknhe0o6z2Wic5rbE2eYS0ElutoFHD5W4ZAapmrYviacpFzR4ib7bKzyTdVg73HNicvQ/640?wx_fmt=png&from=appmsg "")  
## 检测漏洞  
  
1、默认口令  
  
2、api接口未授权Hessian反序列化（只检测是否存在接口，是否存在漏洞需要打内存马验证）  
  
3、Executor未授权命令执行  
  
4、默认accessToken身份绕过  
## 关于内存马  
  
1、内存马使用了xslt，为了提高可用性提供了冰蝎Filter和Vagent两种内存马  
  
2、如需自定义可替换resources下的ser文件，其中filter.ser为冰蝎filter内存马、agent.ser为冰蝎agent内存马、xslt.ser会落地为/tmp/2.xslt,  
  
3、内容为使用exec执行/tmp/agent.jar、exp.ser则是加载/tmp/2.xslt  
  
4、vagent内存马连接配置:冰蝎:http://ip:port/xxl-job-admin/api, 其他类型内存马类似， 将api改为luckydayc、luckydayjs等即可  
  
5、Behinder内存马连接配置:   
  
密码: Sgjmccrzo  
  
请求路径: /api  
  
请求头: Referer: Lepxcnzd  
  
脚本类型: JSP  
  
6、由于agent发送文件较大，所以可能导致包发不过去，建议多试几次或者将超时时间延长  
  
7、由于Hessian反序列化基本上都是直接发二进制包，所以理论上讲其他的Hessian反序列化漏洞也可以打  
## 工具下载  
  
点击关注下方名片  
进入公众号  
  
回复【  
xxl-job漏洞  
】获取  
下载链接  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCCJg3pR9eIphgknhe0o6z2FeCjDlQcA34SLibIbW2UDKHeQzibUTLzT9pjibavsUJY3SiaeRGyeePWNA/640?wx_fmt=png&from=appmsg "")  
```
https://github.com/pureqh/xxl-job-attack
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCCJg3pR9eIphgknhe0o6z26ick5axUxxZHc11fthhibYVZYXMWlDVWMbGSfj67ibCIaA6u52ibO99iaqQ/640?wx_fmt=png&from=appmsg "")  
## 往期精彩  
  
  
[华硕路由器遭僵尸网络攻击，9000余台设备被植入持久性后门2025-05-30](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247512516&idx=1&sn=f410447ffc00847f97d626c5a1df7b73&chksm=c09ac294f7ed4b8220f840ce12c729ec13148e96e43a7a62379e7cc7618a2f4c7776e7d4f20e&scene=21#wechat_redirect)  
[高阶渗透 | 绕过阿里云WAF进行MySQL手注实录2025-05-29](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247512507&idx=1&sn=5551ebc85ca037c3094ffa0741aaab54&chksm=c09ac2ebf7ed4bfdb6b8c4ed91f289496c66582d3b55bdc30fe91fec92c38ba9c13326aa1364&scene=21#wechat_redirect)  
[你不会还在用“社工裤”玩开盒呢？2025-05-28](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247512501&idx=1&sn=2087ed50e2388e0efc6a33b672e3fd80&chksm=c09ac2e5f7ed4bf3e75a1c76d4c7b28ffa975668c52f2281199d1c18b9a84222126e2ea4780c&scene=21#wechat_redirect)  
  
  
  
