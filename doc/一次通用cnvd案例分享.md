#  一次通用cnvd案例分享   
 sec0nd安全   2025-01-19 12:12  
  
通用资产  
  
整体思路  
:  
  
1.提取相关系统指纹,例如路由器,监控等系统，例如 规则列表等  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icLbY1XjRBsdfiaDXFKFbA61a8MDJECuP8CkYjicQyVqtrzGbegDImTBkw/640?wx_fmt=png "")  
  
2.访问测试 寻找功能点 例如弱口令进后台进一步利用，或者未授权等等  
  
3.此案例为弱口令加JDBC漏洞利用  
  
本案例fofa资产:  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2ic381ZBvO5WoicvbdKotVvVnU4yk1lYeiaJpuwBuyPYPmKDrP9XSBd4PVA/640?wx_fmt=png "")  
  
  
复现案例  
  
点击fofa任意搜索资产:  
  
来到页面 弱口令登入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icVUovntcofJJic7UK0LJgPLMlJd5922Sgwib1vUtibia2DZZE22cjakjOTQ/640?wx_fmt=png "")  
  
查看功能点，发现存在数据库配置  
  
直接利用JDBC的漏洞伪造mysql环境，利用工具  
  
https://github.com/fnmsd/MySQL_Fake_Server  
  
以MySQL_Fake_Server为例：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icdZYo9vdsqzPM9yj9Fibx2tAQ1iaIYrnbtjS1qH0TiaqsazXhCHicdU1Utg/640?wx_fmt=png "")  
  
Config.json配置文件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icuTK6YXzUXVbfmPP3V0ZYoCkgBCELiaj7WgbkHw55lniaHnJkYYSVNGiaA/640?wx_fmt=png "")  
  
配置了默认的几个系统文件，可以指定jdbc连接时读取对应文件  
  
VPS启动伪造的Mysql服务  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icZs2TOCtrABq4iauXS7p9OGdsDiay38YEib4mBMgfECmDyQZxlBERkBmng/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icIRhicdHWXDxdymdPhE2FcqAnnXGLnpJh6kUddWFqDRibunk0LW3wOktA/640?wx_fmt=png "")  
  
填写好VPS的地址,然后点击连接测试,Burp抓包放到重发器去  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icDUJlywJogyNH6jtgZKNS6QRrVebNpp70x0x0D1USL1VZIRBegdUIIw/640?wx_fmt=png "")  
  
此时可以成功读取到windows的hosts文件内容  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ASf2g4J3S7aa8TeAWpPiacuVFg1ccLr2icZmxLicQPibUyvuoderzjja4p36I86notvHPVcibh7JdVLAcNeYPJdDsUQ/640?wx_fmt=png "")  
  
需复现三个，剩下贴网站即可，其他案例同理  
  
漏洞利用参考链接:  
  
https://mp.weixin.qq.com/s/2C_4N5QbkOLqRyR8dNlFxA  
  
