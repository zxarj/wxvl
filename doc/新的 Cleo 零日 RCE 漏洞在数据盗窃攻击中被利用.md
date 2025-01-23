#  新的 Cleo 零日 RCE 漏洞在数据盗窃攻击中被利用   
胡金鱼  嘶吼专业版   2025-01-23 06:00  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif "")  
  
黑客正在积极利用 Cleo 托管文件传输软件中的零日漏洞来破坏企业网络并进行数据盗窃攻击。该漏洞存在于该公司的安全文件传输产品 Cleo LexiCom、VLTrader 和 Harmony 中，允许不受限制的文件上传和下载，从而导致远程代码执行。  
  
Cleo MFT 漏洞影响版本 5.8.0.21 及更早版本，是对先前修复的漏洞 CVE-2024-50623 的绕过，Cleo 于 2024 年 10 月解决了该漏洞。但是，该修复并不无懈可击，它还允许威胁者绕过它并继续攻击在攻击中利用。  
  
Cleo 表示，其软件被全球 4000 家公司使用，包括 Target、沃尔玛、Lowes、CVS、Home Depot、FedEx、Kroger、Wayfair、Dollar General、Victrola 和 Duraflame。  
  
这些攻击让人想起之前利用托管文件传输产品中的零日漏洞进行的 Clop 数据盗窃攻击，包括 2023 年大规模利用 MOVEit Transfer、使用 GoAnywhere MFT 零日漏洞的攻击以及 2020 年 12 月针对 MOVEit Transfer 的零日漏洞攻击。  
  
然而，网络安全专家认为，这些 Cleo 数据盗窃攻击与新的 Termite 勒索软件团伙有关，该团伙最近入侵了全球许多公司使用的供应链软件提供商 Blue Yonder。  
# 野外攻击  
  
Huntress 安全研究人员首先发现了对 Cleo MFT 软件的主动利用，他们还在一篇新文章中发布了概念验证 (PoC) 漏洞，提醒用户应采取紧急行动。  
  
Huntress 解释说：“这个漏洞正在被广泛利用，运行 5.8.0.21 的完全修补的系统仍然可以被利用。我们强烈建议您将任何暴露于互联网的 Cleo 系统移至防火墙后面，直到发布新补丁为止。”  
  
CVE-2024-50623 的活跃利用证据始于 2024 年 12 月 3 日，12 月 8 日观察到的攻击量显著上升。尽管归属尚不清楚，但这些攻击与以下 IP 地址相关：加拿大、荷兰、立陶宛和摩尔多瓦。  
  
**·**176.123.5.126 - AS 200019 (AlexHost SRL) - 摩尔多瓦  
  
**·**5.149.249.226 - AS 59711 (HZ Hosting Ltd) - 荷兰  
  
**·**185.181.230.103 - AS 60602 (Inovare-Prim SRL) - 摩尔多瓦  
  
**·**209.127.12.38 - AS 55286 (SERVER-MANIA / B2 Net Solutions Inc) - 加拿大  
  
**·**181.214.147.164 - AS 15440 (UAB Baltnetos komunikacijos) - 立陶宛  
  
**·**192.119.99.42 - AS 54290 (HOSTWINDS LLC) - 美国  
  
这些攻击利用 Cleo 漏洞将名为“healthchecktemplate.txt”或“healthcheck.txt”的文件写入目标端点的“autorun”目录，这些文件由 Cleo 软件自动处理。  
  
发生这种情况时，这些文件会调用内置导入功能来加载其他有效负载，例如包含 XML 配置（“main.xml”）的 ZIP 文件，其中包含将执行的 PowerShell 命令。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Fnjymj66ZNKZclsSzRznjJnR1JIiapibCdknTtFEaWOWicqicuN5uIz7ibicTTTTntJI37HhworypJbZA/640?wx_fmt=png&from=appmsg "")  
  
利用在易受攻击的设备上执行 PowerShell 命令  
  
PowerShell 命令与远程 IP 地址建立回调连接、下载额外的 JAR 有效负载并擦除恶意文件以阻碍取证调查。Huntress 表示，在后利用阶段，攻击者使用“nltest.exe”枚举 Active Directory 域，部署 Webshell 以在受感染的系统上进行持久远程访问，并使用 TCP 通道最终窃取数据。  
  
完成对系统的攻击后，威胁者会执行 PowerShell 命令来删除攻击中的文件，例如“C:\LexiCom\cleo.1142”。Huntress 的遥测数据表明，这些攻击已经影响了至少 10 个使用 Cleo 软件产品的企业，其中一些企业从事消费品、食品行业、卡车运输和航运业务。  
  
Huntress 指出，还有更多潜在受害者超出了其可见范围，Shodan 互联网扫描返回了 390 个 Cleo 软件产品结果，绝大多数（298 个）易受攻击的服务器位于美国。  
  
Macnica 的威胁研究员表示，他的扫描结果为 Harmony 返回 379 个结果，为 VLTrader 返回 124 个结果，为 LexiCom 返回 240 个结果。  
# 需要采取行动  
  
鉴于 CVE-2024-50623 的活跃利用以及当前补丁（版本 5.8.0.21）的无效性，用户必须立即采取措施来降低妥协风险。Huntress 建议将暴露于互联网的系统移至防火墙后面并限制对 Cleo 系统的外部访问。  
  
公司可以通过在目录“C:\LexiCom”、“C:\VLTrader”和“C:\Harmony”中查找可疑的 TXT 和 XML 文件来检查其 Cleo 服务器是否受到损害，并检查 PowerShell 命令执行的日志。  
  
恶意 XML 文件将在“hosts”文件夹中找到，并包含 bash（在 Linux 上）或 PowerShell（在 Windows 上）命令。Cleo 发布了适用于 Linux 和 Windows 的脚本，可以帮助查找这些恶意 XML 文件。  
  
最后，Huntress 建议删除 Harmony/VLTrader/Lexicom 下的所有“Cleo####.jar”文件（例如 cleo.5264.jar 或 cleo.6597.jar），因为它们可能是在利用漏洞期间上传的。另外，建议按照以下步骤关闭自动运行功能：  
  
1.打开 Cleo 应用程序（LexiCom、VLTrader 或 Harmony）  
  
2.导航至：配置>选项>其他窗格  
  
3.清除标记为“自动运行目录”的字段  
  
4.保存更改  
  
Huntress 表示，Cleo 预计针对此漏洞的新安全更新将晚些时候发布。此外，有媒体向 Cleo 询问了有关该漏洞的其他问题，并被告知安全更新“正在开发中”。   
  
参考及来源：https://www.bleepingcomputer.com/news/security/new-cleo-zero-day-rce-flaw-exploited-in-data-theft-attacks/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Fnjymj66ZNKZclsSzRznjCwE2ubK28PB1Jms8KESeI4AXQ1rrSTve4IkR5gcbCueB7gRSFiauJAg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Fnjymj66ZNKZclsSzRznjAUdHWagibeNdF9e3f9CQmffp9QjHHOqR4v0AJMDfa3nicvCW2wtEc7Lw/640?wx_fmt=png&from=appmsg "")  
  
  
