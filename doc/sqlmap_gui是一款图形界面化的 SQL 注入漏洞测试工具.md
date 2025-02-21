#  sqlmap_gui是一款图形界面化的 SQL 注入漏洞测试工具   
 黑白之道   2025-02-21 01:59  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
## 工具简介  
  
SQLMap 是一款自动化的 SQL 注入漏洞测试工具，它能帮助安全研究人员、渗透测试员和网络安全专家识别、利用和修复SQL注入漏洞。为了更方便用户操作和理解其工作流程，我们推出了 SQLMap 可视化工具，使得SQLMap的操作更加简单直观，尤其适合没有命令行经验的用户。该工具将 SQLMap 命令行工具进行图形化，提供更加直观、易于操作的界面，让用户可以轻松进行 SQL 注入测试。  
## 主要特点  
- 🎯 **图形化界面**：告别繁琐的命令行输入，通过可视化的界面进行操作。  
  
- 🚀 **快速扫描**：简单设置，轻松启动扫描，节省您的时间。  
  
- 🛠️ **高级功能**：支持 SQLMap 的所有高级功能，如自定义 payload、数据库信息泄露、Web 应用程序防护绕过等。  
  
## 环境要求  
- 🖥️ **操作系统**：Windows  
  
- ⚙️ **Java 版本**：1.8+ 版本  
  
- 🧑‍💻 **SQLMap**：确保本地已经安装并配置好 SQLMap 工具  
  
## 工具截图  
  
双击jar包打开程序如图所示，会在当前文件夹生成一个config.txt文件  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcqickEnpHn3x5iaIiayjHjLTlPFfPAUfACnbZzw1fjYLg3RFc7wETHzn1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
config.txt文件里面记录的是sqlmap路径和代理信息，可在工具中导入，也可手动填写  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcT2WQEXDZvyT5xKc4jpY2LeqCUwG2N90R8ibxhGDIMl89gX2lAX1XEBg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
文件->导入sqlmap，选择sqlmap文件夹就可以了(不用选择具体文件)  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcArRym3zK7M3icV0CgnwWR7xl2CklmLv8ouyjDAjPgwicofuqlRr7PibYQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
设置->代理，可以挂代理，工具自带测试代理是否可用功能  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMca9oHtSs5NDGHMtgxN2Q5hvicP5TzWkeSI58VicibDOraDsckoS4oThSPg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
脚本文件会自动获取sqlmap文件中tamper文件夹，也可以手动添加脚本到里面  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcBapibv5R3DMGk3K0KL1BZdqN0WoUp9HiblRPL3YU7o2yx5eATfp6Aib2A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
自定义参数在GET请求下就是sqlmap的 -p id ，POST请求就是sqlmap的 -data id=1，GET/POST请求可在url那一行最左边选
测试级别、风险级别、线程数、库、表、列都可以自定义，还有一些可自选的功能项
选择完后点击预览按钮，则会生成sqlmap语句在预览框中显示，可以自定义调整，修改、删除、添加
然后点击start就是开始运行**注：必须先点预览，预览框中出现了命令才能点start运行**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcltKuwiaMsuGibzoFEjicWZSZC9tyZB6FXfTNVcWTcVd0OfibvLcf0lGuXA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
关于抓包跑，可直接在burp抓包，复制请求包粘贴到文本框中，在需要测试的地方加上 * 点击start即可
其他地方不需要改，可以选择需要的脚本和一些功能项等等**注：当预览框和抓包跑文本框都有信息时，优先会运行预览框命令**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xrl71kBL8Pxw3tKhoYRRMcYXuT7f8icFlVo8vIoiaJIS6ialGj1uwwXNHXMd4sOgjypfdsvJdst53IA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
## 工具获取  
  
  
  
https://github.com/suqianjue/sqlmap_gui/tree/main  
  
> **文章来源：夜组安全**  
  
  
  
黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！  
  
如侵权请私聊我们删文  
  
  
**END**  
  
  
