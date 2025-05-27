#  黑客利用 0day 漏洞通过 Commvault 入侵美国云平台   
会杀毒的单反狗  军哥网络安全读报   2025-05-27 01:11  
  
**导****读**  
  
  
  
一场新的 SaaS 攻击活动已经到来 – Commvault 位居榜首。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaHjxGD6u56cVoOOcCGj6OkuHZ53OGTxzk6E0L1PjZ1pEibrfxLs0wDz6nibxVlUTYWwuMEkZ6ZtaBUQ/640?wx_fmt=webp&from=appmsg "")  
  
  
Commvault 云基础设施遭受网络攻击，导致使用 M  
  
icrosoft 365 备份通过 Metallic 未经授权访问客户数据。事件由 CISA 机构报告（https://www.securitylab.ru/news/558834.php），表明攻击者在 Microsoft Azure 云环境中开展活动。  
  
  
据该机构称，攻击者能够访问敏感数据，特别是用于连接到 Microsoft 365 备份的客户机密。这些数据存储在 Commvault 的 Azure 环境中，很可能让攻击者渗透到许多客户公司的内部 M365 环境。  
  
  
此次入侵影响了 Metallic 软件，即 Commvault 基于云的备份即服务 (SaaS) 解决方案。该机构指出，此次事件可能是针对 配置脆弱且默认访问权限过多的 云软件提供商的更大规模活动的一部分。  
  
  
最初的可疑活动通知来自微软， 时间是 2025 年 2 月。根据 Commvault 自己的报告，调查显示，一个APT黑客组织利用了 该公司网络服务器中一个此前未知的漏洞(CVE-2025-3928 )。该漏洞允许经过身份验证的远程用户在服务器上运行 Web Shell。  
  
  
Commvault 团队解释说，攻击者使用先进的技术来获取客户端用于与 M365 通信的敏感授权密钥。虽然该公司强调数据备份未受到影响，但一些凭证可能已被泄露。  
  
  
为了应对这一事件，Commvault 轮换了所有 M365 凭证并加强了对云中服务的控制。该公司继续与政府机构和工业合作伙伴合作，进一步分析情况。  
  
  
专家们提出了一系列降低风险的措施：  
- 监控 Entra审计日志， 查找与Commvault 应用程序相关的凭据的未经授权的更改或添加；  
- 分析 Microsoft 日志（Entra 审计、Entra 登录、统一审计日志）并进行内部威胁搜寻；  
- 对于单用户应用程序 - 实施条件访问策略，将 Commvault 服务组件的身份验证限制为受信任范围内的 IP 地址；  
- 检查具有提升权限的 Entra 应用程序注册和服务主体列表；  
- 仅将对 Commvault 管理接口的访问限制在受信任的网络；  
- 配置 Web 应用程序防火墙以阻止路径遍历尝试和可疑文件下载，并删除对 Commvault 应用程序的外部访问。  
这一事件凸显保护云基础设施的重要性以及及时应对威胁的必要性。  
  
https://www.securitylab.ru/news/559706.php  
  
  
新闻链接：  
  
https://www.securitylab.ru/news/559706.php  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
黑客利用 0  
d  
ay 漏洞通过 Commvault 入侵美国云平台  
  
https://www.securitylab.ru/news/559706.php  
  
  
ViciousTrap 威胁组织利用思科漏洞用  
  
5,300 台受感染设备构建全球蜜罐  
  
https://thehackernews.com/2025/05/vicioustrap-uses-cisco-flaw-to-build.html  
  
  
俄黑客组织 TAG-110 利用启用宏的 Word 文档攻击塔吉克斯坦  
  
https://www.recordedfuture.com/research/russia-aligned-tag-110-targets-tajikistan-with-macro-enabled  
  
  
俄黑客组织 Killnet 以新身份回归  
  
https://therecord.media/russian-hacker-group-killnet-returns-with-new-identity  
  
  
APT  
组织利用 Trimble Cityworks 的  
0day  
漏洞攻击美地方政府实体  
  
https://www.securityweek.com/cityworks-zero-day-exploited-by-chinese-hackers-in-us-local-government-attacks/  
  
  
APT  
组织利用 Ivanti 漏洞攻击关键部门  
  
https://www.securityweek.com/chinese-spies-exploit-ivanti-vulnerabilities-against-critical-sectors/  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
玛莎百货预计勒索软件攻击将造成 4 亿美元损失  
  
https://www.securityweek.com/marks-spencer-expects-ransomware-attack-to-cost-400-million/  
  
  
加拿大新斯科舍电力公司确认遭受勒索软件攻击  
  
https://www.securityweek.com/nova-scotia-power-confirms-ransomware-attack-280k-notified-of-data-breach/  
  
  
Commvault 漏洞（CVE-2025-3928）遭利用  
  
https://www.securityweek.com/companies-warned-of-commvault-vulnerability-exploitation/  
  
  
SilverRAT 源代码在线泄露  
  
https://hackread.com/silverrat-source-code-leaked-online-you-need-to-know/  
  
  
假冒 DigiYatra 应用程序瞄准印度用户窃取财务数据  
  
https://gbhackers.com/fake-digiyatra-apps-target-indian-users/  
  
  
黑客在暗网论坛上出售超过 500 个被盗加密数据库  
  
https://gbhackers.com/hackers-reportedly-selling-over-500-stolen-crypto-databases/  
  
  
NPM 上的数十个恶意软件包收集主机和网络数据  
  
https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/  
  
  
Katz Stealer 攻击 Chrome、Edge、Brave 和 Firefox 窃取登录信息  
  
https://cybersecuritynews.com/katz-stealer-attacking-chrome-edge-brave-firefox/  
  
  
超过 40 个恶意 Chrome 扩展程序冒充知名品牌窃取敏感数据  
  
https://gbhackers.com/over-40-malicious-chrome-extensions/  
  
  
FBI 披露 Silent Ransom 组织利用虚假 IT 支持电话攻击受害者  
  
https://gbhackers.com/fbi-issues-on-silent-ransom-group/  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
Fortinet CVE-2025-32756 的 PoC  
  
公开  
  
https://hackread.com/researchers-poc-fortinet-cve-2025-32756-quick-patch/  
  
  
硬编码 Telnet 凭证使 D-Link 路由器面临远程代码执行漏洞  
  
https://cybersecuritynews.com/hard-coded-telnet-credentials-d-link-routers/  
  
  
Meteobridge Web 界面漏洞可导致攻击者远程注入命令  
  
https://gbhackers.com/meteobridge-web-interface-vulnerability/  
  
  
三个 0Day 漏洞足以让 Versa Concerto 成为接管通信系统的工具  
  
https://www.securitylab.ru/news/559711.php  
  
  
vBulletin 论坛严重漏洞致使攻击者执行远程代码  
  
https://cybersecuritynews.com/vbulletin-forum-rce-vulnerability/  
  
  
Bitwarden PDF 文件处理程序漏洞使攻击者能够上传恶意 PDF 文件  
  
https://cybersecuritynews.com/bitwarden-pdf-file-handler-vulnerability/  
  
  
Tenable Network Monitor 漏洞可使攻击者提升权限  
  
https://cybersecuritynews.com/tenable-network-monitor-vulnerabilities/  
  
  
Apache Tomcat RCE 漏洞曝光，PoC 发布  
  
https://gbhackers.com/apache-tomcat-rce-vulnerability/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
