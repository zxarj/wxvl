#  SQL注入漏洞批量检查工具   
 黑白之道   2024-12-20 02:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
  
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
  
‍![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mluq8JtBbOzO3PQab0ObINmmqgJSdawgiaUTwVwdFh3ABChnqYqjhjgyg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mluq8JtBbOzO3PQab0ObINmmqgJSdawgiaUTwVwdFh3ABChnqYqjhjgyg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/79gZQNibQ6uc1aU9wroWmyCbWBYOWl1mlqzzVibNEticL4FRsXOH225N1unBye4c69uUNkaPSfj5ArL7d1PQ7XlNA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**下载地址**  
  
**https://github.com/malvads/sqlmc**  
  
> **文章来源：Hack分享吧**  
  
  
  
黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！  
  
如侵权请私聊我们删文  
  
  
**END**  
  
  
