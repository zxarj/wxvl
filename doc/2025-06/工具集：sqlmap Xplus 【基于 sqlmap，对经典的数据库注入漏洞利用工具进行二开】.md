#  工具集：sqlmap Xplus 【基于 sqlmap，对经典的数据库注入漏洞利用工具进行二开】   
 风铃Sec   2025-06-06 03:33  
  
##### 声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！【文末获取工具】  
  
**0x01 工具介绍**  
  
  
在众多的地区性攻防演练中，SQL Server数据库堆叠注入仍有较高的爆洞频率，但因为一些常见的演练场景限制，如不出网、低权限、站库分离、终端防护、上线困难、权限维持繁琐等，仅一个--os-shell已经难满足我们的需求。  
  
sqlmapxplus 基于sqlmap，对经典的数据库漏洞利用工具进行二开，参考各种解决方法，增加MSSQL数据库注入的利用方式。  
##### 目前已经完成的功能如下  
  
①OLE文件上传  
> OLE  
 自动化过程允许你通过 SQL Server 调用 COM 对象，从而可以控制系统中的某些功能，比如文件操作、网络请求  
  
  
②xpcmdshell文件上传  
> xp_cmdshell  
 是 MSSQL 提供的一个扩展存储过程，它允许你在数据库中执行系统命令，这就相当于“拿到了系统的命令执行能力”。  
  
  
③CLR安装功能  
> CLR是MSSQL 支持托管的   
.NET  
 代码执行，通过   
**CLR**  
程序集。攻击者可以上传一个自定义的 .NET 程序集，并注册为 SQL 函数或存储过程。此时攻击者就可以可以执行任意 .NET 代码，包括：下载文件、执行 Shellcode、创建用户、打开 RDP 等系统服务  
  
  
此外，sqlmap Xplus还支持内存马上传、能够实现mssql注入场景下的自动化注入内存马、自动化提权、自动化添加后门用户、自动化远程文件下载、自动化shellcode加载功能。  
  
**0x02 工具使用**  
  
新增功能汇总：  
```
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0Hluiaiaou6yTGE4H9ibGFv2ToCOV6obRXN3UGtJoh6nt2sAribHrytXmWtSUYyAzOwiauCdTibccWPBRaOA/640?wx_fmt=png&from=appmsg "")  
  
**文件操作功能**  
:  
```
```  
  
**CLR相关的功能**  
```
```  
  
更多利用场景请查看coolcat佬文章：  
[https://mp.weixin.qq.com/s/6RpxXitEPt8rA1DFb56Oxw](https://mp.weixin.qq.com/s?__biz=Mzk0NjYyNDI0Ng==&mid=2247483871&idx=1&sn=4c1a0b6b8094f49e60892b9b4d4ddd77&scene=21#wechat_redirect)  
  
 写的非常细致  
  
**0x03 工具下载**  
  
夸克网盘  
「Sqlmap Xplus」  
链接：  
https://pan.quark.cn/s/a003d811a758  
  
**0x04 资源分享【自收集综合漏洞检测工具集合-持续更新】**  
  
  
夸克网盘「综合漏洞自检测工具」链接：  
https://pan.quark.cn/s/302256a9ecf6  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmlZzSKVkFwWmDaHOzamDNvVyq7gvdiasmTmsRp0xPTsCQmNVkp3vmLPz5YnSld5v4jrWX3CsKg0Zw/640?wx_fmt=png&from=appmsg&watermark=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qGTEdaLg0Hluiaiaou6yTGE4H9ibGFv2ToCeFftRyImzFHz3EeeQUXjnh76oiaNcGLBG9wk5Evb6f7MECbv3UgnlibQ/640?wx_fmt=jpeg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmlZzSKVkFwWmDaHOzamDNvOUES8ttWjotPnZKA8hfXdpk52MBbrl82V0rtyonyfQnPMs4DR4xzRQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
#####   
  
