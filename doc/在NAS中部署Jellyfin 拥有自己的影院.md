#  在NAS中部署Jellyfin 拥有自己的影院   
原创 大表哥吆  kali笔记   2024-12-24 00:00  
  
> 拥有NAS,那就必须有自己的影视平台。哪如何搭建自己的影视平台呢？  
  
  
在前面的文章中，我们讲到了搭建emby。可以移步文章《[利用emby搭建家庭影院](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247497732&idx=1&sn=ac71775f8445b24cce7d79eb7964b268&scene=21#wechat_redirect)  
》。但由于收费，开心版也没什么意思。因此本文为大家推荐Jellyfin的部署吧！  
  
**拉取镜像**  
```
docker pull jellyfin/jellyfin:latest

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8VsotibmkvAVQvnn2yDdhN67M1e8s3THvMZIQ98SkBLQnicwfYt2QTicdA/640?wx_fmt=png&from=appmsg "")  
  
**启动容器**  
  
在启动容器之前，我们先配置容器的相关目录（可自行设置，注意自己的文件路径）  
```
#创建目录
mkdir -p /nas/jellyfin/{config,cache}
#启动容器
docker run -d -v /nas/tool/jellyfin/config:/config -v /nas/tool/jellyfin/cache:/cache -v /nas/我的电影:/media --net=host jellyfin/jellyfin:latest

```  
  
注意：/nas/我的电影:/media是将你的电影目录挂载到了media目录，在后面添加目录时，选择media就行了。  
# 配置  
  
启动容器后，访问ip:8096  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8zchde8F2jFNhDaCMp1BeDJ5icgXwwxomOyVyWq9Ub9jgKI3haMwV82Q/640?wx_fmt=png&from=appmsg "")  
  
设置语言  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8uXibiaibEaVG9D7HtINyTmy9uM3ToL6Z1zNc5klxknuNm4ruWn5xtTpeQ/640?wx_fmt=png&from=appmsg "")  
  
设置账号信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8JEyPqcqpux417nRQYnK2QlibcxHdj51HSO07lohSoUZc2KJiaCef93Iw/640?wx_fmt=png&from=appmsg "")  
  
设置媒体库  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT88oAglMvtSdH1JZtbP4la0Sp5W7OHCWE7Usybl65bQPqKZY7Wch7TfA/640?wx_fmt=png&from=appmsg "")  
配置完成后，我们接着登录。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT82GeejNNn98qzKEN7WoCwLHpSbJxKrqicUG0AAKmGOFzicHpDhQus5pQA/640?wx_fmt=png&from=appmsg "")  
# 配置刮削  
  
在控制台-插件菜单下找到存储库并添加存储库。存储库URL：https://mirror.ghproxy.com/https://github.com/cxfksword/jellyfin-plugin-metashark/releases/download/manifest/manifest_cn.json  
  
在插件的目录下找到刚刚添加的MetaShark插件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8AzYh8ZXRHicia9SCic4RFXH7SJyNBP13Z29RQSLfkceSbDcic0d5rcnGOA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8QEc6CiaN0Y2XVOVFyfdptweicmC06fO41doLgte81pqqTuQsS9mysYyw/640?wx_fmt=png&from=appmsg "")  
  
安装  
  
接下来，配置插件。首先登录豆瓣，登录后打开控制台。在名称中找到verify_users的请求，并复制cookie  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8Hocq9ncL4ZQ9MO1Ahz131NGA6aQ2ibNA8Lj1KEA5BfAACEh8vmEPupw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8Uicf0P1WzfCLhgbMib14D13LB1cw0RIehhAfSqr1GxRiaPKbKxRKONic2g/640?wx_fmt=png&from=appmsg "")  
  
复制后显示已生效则配置正确  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8LTcvmaFumABlaWcJKCHbucAmumuEy1ruVklA1KMu54ve5bpd4ZibJJA/640?wx_fmt=png&from=appmsg "")  
  
启用  
  
其它刮削器均可选择关闭，也可以启用作为MetaShark失效时的备用选择。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatiaTbbp9AjcnwqjyLjXTasT8xCOg0ov8HlBWz29UGfwND9Vkqic77y0hQpNV2U9le16j9mm0cxdrorw/640?wx_fmt=png&from=appmsg "")  
  
效果  
  
更多精彩文章 欢迎关注我们  
  
  
