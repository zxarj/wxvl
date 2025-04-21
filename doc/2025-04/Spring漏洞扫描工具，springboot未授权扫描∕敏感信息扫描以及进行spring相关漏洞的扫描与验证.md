#  Spring漏洞扫描工具，springboot未授权扫描/敏感信息扫描以及进行spring相关漏洞的扫描与验证   
WuliRuler  无影安全实验室   2025-04-21 13:18  
  
免责声明：  
本篇文章仅用于技术交流，  
请勿利用文章内的相关技术从事非法测试  
，  
由于传播、利用本公众号无影安全  
实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！  
如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**  
"设为星标，这样更新文章也能第一时间推送！  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
安全工具  
  
  
  
## 0x01 工具介绍  
  
**SBSCAN是一款专注于spring框架的渗透测试工具，可以对指定站点进行springboot未授权扫描/敏感信息扫描以及进行spring相关漏洞的扫描与验证。**  
- **最全的敏感路径字典**  
：最全的springboot站点敏感路径字典，帮你全面检测站点是否存在敏感信息泄漏  
  
- **支持指纹检测**  
：  
  
- 支持spring站点指纹匹配：支持启用指纹识别，只有存在spring指纹的站点才进行下一步扫描，节约资源与时间 (无特征的站点会漏报，客官自行决策是否启用)  
  
- 支持敏感路径页面关键词指纹匹配：通过维护敏感路径包含的关键词特征，对检出的页面进行指纹匹配，大大提升了工具检出的准确率，减少了人工去确认敏感页面真实性投入的时间  
  
- **支持指定模块发起检测：**  
 不想跑漏洞，只想检测敏感路径？ 或者只想检测漏洞？ 都可以，通过 -m  
 参数指定即可  
  
- **最全的spring漏洞检测POC：**  
 spring相关cve漏洞的检测poc全部给你集成到这款工具里，同类型最全  
  
- **无回显漏洞解决：**  
 无回显漏洞检测扫描器光看响应状态码不太靠谱？支持--dnslog参数指定dnslog域名，看到dnslog记录才是真的成功验证漏洞存在  
  
- **降噪输出结果：**  
 可通过指定-q  
参数只显示成功的检测结果  
  
- **友好的可扩展性：**  
 项目设计初期就考虑了用户的自定义扩展需求，整个项目尽量采用高内聚低耦合模块化的编程方式， 你可轻松的加上自己的poc、日常积累的敏感路径、绕过语句，轻松优化检测逻辑，具体见下文的“自定义扩展”  
  
- **其他一些常规支持**  
：单个url扫描/ url文件扫描 / 扫描模块选择 / 支持指定代理 / 支持多线程 / 扫描报告生成  
  
## 0x02 工具使用  
  
  
**MacOS && linux**  
```
$ git clone https://github.com/sule01u/SBSCAN.git
$ cd SBSCAN
$ python3 -m venv sbscan         # 创建虚拟环境
$ source sbscan/bin/activate     # 激活虚拟环境
$ pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple   # -i 指定pip源安装依赖,可选；
$ python3 sbscan.py --help
```  
  
**Windows**  
```
$ git clone https://github.com/sule01u/SBSCAN.git
$ cd SBSCAN
$ python3 -m venv sbscan         # 创建虚拟环境
$ .\sbscan\Scripts\activate        # 激活虚拟环境
$ pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple   # -i 指定pip源安装依赖,可选；
$ python3 sbscan.py --help
```  
  
**检测效果图, 使用彩色表格打印更直观显示检测结果，检测报告保存位置将会在扫描结束后控制台显示**  
  
****  
**检测时可使用 tail -f logs/sbscan.log 实时查看详细的检测情况**  
  
****```
## 🧾 已支持检测CVE列表- CVE-2018-1273- CVE-2019-3799- CVE-2020-5410- CVE-2022-22947- CVE-2022-22963- CVE-2022-22965- JeeSpringCloud_2023_uploadfile
```  
## 0x03 工具下载  
  
**点****击关注**  
**下方名片****进入公众号**  
  
**回复关键字【250421****】获取**  
**下载链接**  
  
  
最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，**  
  
**价格将上涨20元，越早进越优惠！！！**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFERvgmiaRWOkaOT8aCVKhAf4Yab5X63k4NpTL9CzAmhw61VKGWrkCzd8LZIdEgUrlfhU8ib65tVG6EiaQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
