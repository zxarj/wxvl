#  还在用Wireshark？这款工具直接帮你提取Web攻击+复现请求全过程！   
原创 zss  知攻善防实验室   2025-06-03 02:15  
  
### 📥 已经打包好的下载地址：  
  
GIhutb下载地址：👉   
https://github.com/CuriousLearnerDev/TrafficEye/releases  
  
夸克网盘（windows_x64+Linux_amd_64）（提取码：pyP4）：👉 链接：  
https://pan.quark.cn/s/d2db31f49d0e  
### 🛠️ 使用说明  
#### 🔧 Linux 系统用户  
> ⚠️   
**前置依赖：需安装 tshark**  
  
  
安装命令如下：  
```
```  
  
运行步骤如下：  
```
```  
#### 🖱️ Windows 系统用户  
> ✅ 已集成   
tshark  
，免安装依赖  
  
  
运行方法：  
```
```  
### 📅 最近研发进度  
  
0.0.7版后源码不在公开  
  
2025-05-25：可以看见匹配规则、风险等级、匹配位置、匹配风险位置等  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxl3Va1dnTvGibws93e2IjW7PfteHkGUKqEJtv4riawfskbrveOhZoXee8A/640?wx_fmt=png&from=appmsg "")  
  
2025-05-24：新增风险分析  
  
2025-05-10：性能优化、数据与视图分离、避免重复加载相同的图标文件、减少GUI操作、模型只在需要时提供数据  
  
2025-05-03：增加分析的IP访问URI统计  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlibUzOXJRaXQiatPWfUVMrNSJnl8WJFcwJ2aZr9M4ZJzcH9CgYzH04qVg/640?wx_fmt=png&from=appmsg "")  
  
2025-05-02：日志分析的实时交互体验（动态更新）  
  
2025-05-01：修复显示问题、优化LOG文件分析多核 CPU 并行处理能力  
  
2025-04-28：全流量大文件分析内存优化，输出超过20万行时自动写入硬盘，降低内存占用  
  
2025-04-28：性能优化，WEB日志log分析模块已经测试处理2GB文件及400万条数据  
  
2025-04-26：默认AI识别、流量包二进制文件识别、不勾选，提升整体速度  
  
2025-04-24：性能优化  
  
2025-04-23：统计分析可以点击全屏  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlwibjewOy6c0QArj0u9BAowiaZRxM6kNibabNlxBb9SuzOT1CKSOlWBia0g/640?wx_fmt=png&from=appmsg "")  
  
2025-04-20：指定请求URI、请求头、请求体AI分析，优化流量分析速度、界面修改、部分问题修复  
  
2025-04-19：完善基本AI危险识别模块  
  
2025-04-18：开始研发情报分析模块  
  
2025-04-17：开始研发AI分析模块  
  
2025-04-15：新增TLS解密功能  
  
2025-04-14：界面优化功能优化  
  
2025-04-13：新增二进制文件提取  
  
2025-04-12：开始研发二进制文件提取  
  
2025-04-11：开始界面修改  
  
2025-04-10：开始编写正则  
  
2025-04-10：开始修改核心代码  
  
2025-04-09：开始日志提取模块  
  
2025-04-08：开始日志提取正则  
  
2025-04-06：开始重放功能  
  
2025-04-05：开始设置输出数据流  
  
等等等....  
### 🧪 工具介绍  
  
该工具的主要目标是对护网蓝队、流量分析的网络流量进行详细分析，识别潜在的安全威胁，特别是针对Web应用的攻击（如SQL注入、XSS、Webshell等），它通过模块化设计让用户能够根据需要选择和定制不同的功能，适用于安全研究人员、渗透测试人员和网络管理员等专业人士  
## 🧱 工具架构  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlkiab4tlVFGPibjg2tqnDteUpRuLvQskpQ94hm1gw7E6c37TTAOn8tuCg/640?wx_fmt=png&from=appmsg "")  
## 🚀 工具现有功能  
- ✅   
pyshark   
  
- ✅ 已完成   
tshark  
 调用优化，性能大幅提升（解析速度为   
pyshark  
 的约 100 倍，原本几分钟的分析现在可在数秒内完成）  
  
- ✅自动识别文件类型进行分析  
  
- ✅可以使用sslkeys.log对HTTPS的数据解密  
  
- 🎯 全流量文件.pcapng、  
  
- ✅ 支持输出Burp Suite的http数据  
  
- ✅ 支持输出POST数据部分字节流格式  
  
- ✅ 支持输出POST数据部原始16进制数据  
  
- ✅ 支持过滤输出uri、过滤请求和响应  
  
- 📄 LOG文件分析  
  
- ✅ 支持Apache  
  
- ✅ 支持Nginx  
  
- ✅ 支持JSON  
  
- ✅ 支持F5  
  
- ✅ 支持HAProxy  
  
- ✅ 支持Tomcat  
  
- ✅ 支持IIS  
  
- 🔁 数据重放  
  
- ✅ 原封不动重放请求  
  
- ✅ 发送完整二进制请求数据  
  
- **按会话发送请求：**  
 请求会按照建立的连接会话顺序发送，例如，在哥斯拉工具中，测试 Webshell 时会自动发送三次请求，这三次请求构成一个会话，输入会话 ID 后可以重放这三次请求，完全复现会话过程  
  
- 📦 二进制文件提取支持：  
  
-  
 ✅ 支持：JAVA 序列化二进制数据  
  
-  
 ✅ 支持：C# 序列化数据  
  
-  
 ✅ 支持：C# Base64 序列化数据  
  
-  
 ✅ 支持：JAVA 字节码  
  
-  
 ✅ 支持：ZIP 文件  
  
-  
 ✅ 支持：7z 文件  
  
-  
 ✅ 支持：图片文件 (JPEG, PNG, GIF, BMP, TIFF等)  
  
-  
 ✅ 支持：音频文件 (MP3, WAV, FLAC等)  
  
-  
 ✅ 支持：视频文件 (MP4, AVI, MOV, MKV等)  
  
-  
 ✅ 支持：PDF 文件  
  
-  
 ✅ 支持：文档文件 (Word, Excel, PowerPoint, PDF等)  
  
-  
 ✅ 支持：压缩包文件 (RAR, TAR, GZ, ARJ等)  
  
-  
 ✅ 支持：邮件文件 (MBOX, PST, DBX, EML等)  
  
-  
 ✅ 支持：数据库文件 (SQLite, MySQL, MongoDB等)  
  
-  
 ✅ 支持：脚本和代码文件 (Python, JavaScript, PHP, Ruby, Java等)  
  
-  
 ✅ 支持：二进制文件签名检测（如：特定软件或硬件生成的二进制格式）  
  
- 📊 统计  
  
- ✅ 支持访问地址整理访问次数  
  
- ✅ IP地址归属地  
  
- ✅ 原始IP  
  
- ✅ 使用的方法  
  
- ✅ 访问次数  
  
- 🧰 安全检测  
  
- ✅ 信息泄露/目录遍历  
  
- ✅ 敏感文件泄露  
  
- ✅ 目录遍历  
  
- ✅ 远程文件包含  
  
- ✅ 本地文件包含  
  
- ✅ 远程代码执行  
  
- ✅ SQL注入攻击  
  
- ✅ 跨站脚本攻击（XSS）  
  
- 🧠 AI检测  
  
- ✅ 支持指定URI分析，分析优化  
  
- ✅ 支持自动化批量分析  
  
- ✅ 支持指定请求头、请求体分析  
  
### 📸 界面预览  
  
仪表盘统计界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxl5nGdBYwy8GH8Azmb401DSqMLzHQAJTrNNpnLaBYJ8Cn57XJdNqibaKw/640?wx_fmt=png&from=appmsg "")  
  
流量文件二进制数据提取  
  
![image-20250425105119351](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxljWtfE3rjMbOjsicSReib3U8vlUP6Ogdhv32FASIhU8Tzic3vlO4rKRkicg/640?wx_fmt=png&from=appmsg "")  
  
LOG web文件分析  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlVGxTyv2SGFZkoYlgqLf4dVg3aGWeo7xl23WGbQ9OXL4YRBmPjMjaicQ/640?wx_fmt=png&from=appmsg "")  
  
全流量接触可以拆分成更容易阅读的格式，方便我们分析流量  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlcGd0WicAXciaOVvreItEsbQI69iac8b1Ef6FeqO8U9gb7bTAmpPgX3PuQ/640?wx_fmt=png&from=appmsg "")  
  
流量会话重放  
- 原封不动重放请求  
  
- 发送完整二进制请求数据  
  
- **按会话发送请求：**  
 请求会按照建立的连接会话顺序发送，例如，在哥斯拉工具中，测试 Webshell 时会自动发送三次请求，这三次请求构成一个会话，输入会话 ID 后可以重放这三次请求，完全复现会话过程  
  
例如：哥斯拉会话id如下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlgR9cdVFBLr8rR1jOjmUXmkiaMsyfFzGaJ4PqTvXD3AzibPvYZhU9xgcA/640?wx_fmt=png&from=appmsg "")  
  
我们就可以输入id发送这个请求  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlV2BjuySRM9nf0xLUibt7ecp3AvMyFibF4PyXQRXm2qCdSwG4Er64GARQ/640?wx_fmt=png&from=appmsg "")  
  
统计分析  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlXffD57VKd4rde9JRKA4licgflZibGFOGsXLjpkEO8gtQa2TakKl310iag/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlDrpiaYDDz2msibC4YuhUzTnSFZib3rgmn0POdm6tkKaAO8kiadFyWaeqUQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxls0RM5Hh9pHEUmrutfFER6mOycrAFh8YNiaqwaicKqw75ibibcwl0VrFzRw/640?wx_fmt=png&from=appmsg "")  
  
正则验证  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlUzkOpT1jm95XmhWIicEANh0euMFQWNON4WndRtkpVldYv2icF136ShLA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlWxXqT9ShexO2M8tVjHsOZcy28xLYpmsw2gwLfWiaeTXXgPibXb7tkiaibg/640?wx_fmt=png&from=appmsg "")  
  
AI分析  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vr1TicS08CqibjSKFPU2DJLxlTvK8UCRYeyGTdhAqoibXHFXxmF32icotma7m2SxluwR8dZL9O9wrxziaA/640?wx_fmt=png&from=appmsg "")  
### 目前进度  
  
截止到04月14号、模块开发情况  
#### 📁 custom_extension/  
- data_processing.py  
：（研发中）自定义数据处理模块，用于处理特定格式的流量或自定义解析逻辑  
  
#### 📁 history/  
- trafficeye_data.json  
：历史流量分析数据文件，持久化存储统计信息与分析记录  
  
#### 📁 ico/  
- 用于存放程序所需的图标资源（如 GUI、输出标识等）  
  
#### 📁 lib/  
- cmdline.py  
：命令行接口模块，定义程序入口参数与CLI交互逻辑  
  
- ip2region.xdb  
：IP 地理位置数据库文件，用于 IP 归属地识别  
  
- xdbSearcher.py  
：  
ip2region  
 查询工具类，执行高效 IP 查询  
  
- bench_test.py  
 /   
iptest.py  
 /   
search_test.py  
：调试测试模块，用于测试 IP 匹配、性能基准等功能  
  
#### 📁 log_parsing/  
- log_identification.py  
：日志识别模块，用于匹配不同格式的日志并选择相应解析器  
  
#### 📁 modsec/（研发中）  
- modsec_crs.py  
：OWASP ModSecurity Core Rule Set 规则引擎接口模块。  
  
- rules/  
：存储 OWASP CRS 的规则文件与辅助数据（如 LFI/RFI/RCE/SQLi 等攻击规则）  
  
- rules_APPLICATION_ATTACK_*.py  
：用于解析和执行特定攻击规则（LFI、RFI、RCE、SQLi）的脚本  
  
#### 📄 main.py  
- 主程序入口，用于加载配置、调度模块并启动流量处理流程  
  
#### 📄  binary_extraction.py  
- 二进制文件识别、二进制文件提取模块  
  
#### 📄 core_processing.py  
- 核心处理模块，负责 HTTP 请求/响应数据的解析、转换与提取关键字段  
  
#### 📄 Godzilla.py  
- WebShell 与恶意流量检测模块，针对特殊流量行为进行识别和告警  
  
#### 📄 examine.py  
- 检查与分析工具模块，用于手动检查、特征提取或测试用途  
  
#### 📄 module.py  
- 公共模块，存放多个模块共享使用的函数、常量或基础类  
  
#### 📄 output_filtering.py  
- 过滤输出模块，根据用户定义的过滤条件筛选展示结果  
  
#### 📄 replay_request.py  
- 请求重放模块，用于重现捕获的请求流量，实现漏洞复现或攻击模拟  
  
#### 📄 rule_filtering.py  
- 规则筛选模块，结合用户配置对已加载规则进行按需启用、禁用或精细化过滤  
  
#### 📄 session_utils.py  
- 会话管理工具，用于聚合、排序和提取多个 HTTP 请求/响应构成的会话信息  
  
#### 📄 url_statistics.py  
- URL 统计模块，分析访问频率、状态码分布等维度的统计数据  
  
#### 📄 config.yaml  
### 🧠 未来计划（规划中）  
- ✅ 日志告警联动系统  
  
- ✅ 威胁情报 API 聚合（如 VT、CriminalIP、AbuseIPDB 等）  
  
- ✅ 内置规则联动 ModSecurity 模拟检测  
  
- ✅ 支持更多 WebShell 工具识别（Behinder、蚁剑等）  
  
安全考证（CISP、PTE、NISP、CISSP 等低价证书+ Admin_Ran）  
  
  
