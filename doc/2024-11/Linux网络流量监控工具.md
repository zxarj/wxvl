#  Linux网络流量监控工具   
原创 大表哥吆  kali笔记   2024-11-20 01:02  
  
> 在Linux中，想要查看当前网络情况。常用地命令无非是iftop net­watch cacti等工具。但是这些工具一般都是命令行展示，看不到实际地流量波动效果。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaA8q3ZHY6AL7sB9YVZK9JXTx7f1KltuibFfP1icWtayzRXmJgVficibNbpEosdn4OhgHZZicLaFaiaoyibA/640?wx_fmt=png&from=appmsg "")  
  
iftop命令效果  
  
想要图形化展示实时流量效果，怎么办呢？故而，本位为大家介绍两款工具Speedometer和Bmon  
  
Speedome­ter是一款终端下的图形化显示网络速度的工具。分别执行下面命令即可安装。（本文以Kali为例）  
```
apt-get install speedometer -y
# 使用方法 (其中 eth0 是你要监听的网卡名称)
speedometer -rx eth0 -tx eth0

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaA8q3ZHY6AL7sB9YVZK9JXLAbEwXYsO1VNUeiaTSVMYmAb4nhGqCnyarpDibS5CVSiaReiancnku2qLA/640?wx_fmt=png&from=appmsg "")  
  
效果  
  
Speedomete的使用方法很简单，常用的参数有两个 -rx  和 -tx，-rx 代表显示下载速率，-tx 代表显示上传速率，后面接网络接口的名称即可。  
  
如果说上面的那款工具过于花哨，可以试试看这款 Bmon，感觉就是增强版的 iftop。它能抓取网络相关统计信息并把它们以用户友好的格式展现出来。  
  
**安装**  
```
apt-get install bmon -y
#使用
bmon

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaA8q3ZHY6AL7sB9YVZK9JXb12oTGa6Zt261UOnX3joN3fyAGafR2t1X8hgur2Eyx1ATIcG5zzpUw/640?wx_fmt=png&from=appmsg "")  
  
简洁更实用  
  
当然，如果你有更好地工具分享，欢迎下方留言哦！  
  
**更多精彩文章 欢迎关注我们**  
  
  
  
