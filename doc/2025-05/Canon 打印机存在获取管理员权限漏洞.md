#  Canon 打印机存在获取管理员权限漏洞   
 网安百色   2025-05-25 11:30  
  
Canon Inc. 发布了一份重要的安全建议，警告客户注意影响其各种生产打印机、Office 多功能打印机和激光打印机的严重漏洞。  
  
这些漏洞被确定为 CVE-2025-3078 和 CVE-2025-3079，使恶意行为者能够从受感染的设备中提取敏感的身份验证信息，从而可能导致更广泛的网络渗透。  
  
该回传漏洞影响了多个产品线，包括 imageRUNNER ADVANCE 系列、imageRUNNER 系列、imagePRESS V 系列、imageCLASS 系列、i-SENSYS 系列和 Satera 系列。  
## 高危 Canon 漏洞  
  
这些漏洞的 CVSS v3.1 基本评分为 8.7，被归类为高严重性，攻击媒介指定为 CVSS：3.1。  
  
这些漏洞代表了一个重大的安全问题，因为它们影响了 Canon 的整个企业打印生态系统。  
  
CVE-2025-3078 专门针对生产打印机和办公多功能打印机，而 CVE-2025-3079 则侧重于办公/小型办公多功能打印机和激光打印机。  
  
安全研究人员指出，这些回传漏洞允许具有管理权限的攻击者将设备身份验证尝试重定向到他们控制下的恶意服务器。  
  
核心漏洞机制涉及保护不足的凭据 （CWE-522），其中 Canon 设备在没有足够保护的情况下传输外部服务的身份验证信息。  
## SMTP 和 LDAP 凭证提取方法  
  
利用这些缺陷后，攻击者可以获取在受影响产品中配置的 SMTP/LDAP 连接凭据。  
  
回传攻击利用多功能外围设备 （MFP） 和关键网络服务之间的信任关系。  
  
在典型的漏洞利用场景中，具有管理访问权限的攻击者修改设备配置中的 LDAP 服务器 IP 地址，将身份验证请求重定向到能够以明文形式捕获凭据的流氓服务器。  
  
这种技术已在渗透测试方法中得到广泛记录，攻击者重新配置设备以向侦听端口 389 的攻击者控制的系统发送 LDAP 查询。  
  
该漏洞的 EPSS（漏洞利用预测评分系统）评分为 0.03%，表明未来 30 天内被利用的可能性相对较低，尽管安全专家警告说，该技术的简单性使其对威胁行为者具有吸引力。  
  
该攻击需要高级权限 （PR：H），但可以通过网络 （AV：N） 远程执行，攻击复杂性 （AC：L） 较低。  
  
<table><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong msttexthash="7544134" msthash="74" style="box-sizing: border-box;font-weight: bold;"><span leaf="">CVE 证书</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong msttexthash="17242355" msthash="75" style="box-sizing: border-box;font-weight: bold;"><span leaf="">受影响的产品</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong msttexthash="4085822" msthash="76" style="box-sizing: border-box;font-weight: bold;"><span leaf="">冲击</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong msttexthash="17124536" msthash="77" style="box-sizing: border-box;font-weight: bold;"><span leaf="">利用先决条件</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong msttexthash="8943688" msthash="78" style="box-sizing: border-box;font-weight: bold;"><span leaf="">CVSS 3.1 分数</span></strong></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">漏洞：CVE-2025-3078</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">imageRUNNER ADVANCE 系列、imageRUNNER 系列、imagePRESS V 系列、imagePRESS 系列</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">允许具有管理权限的攻击者提取 SMTP/LDAP 凭据，从而实现横向网络移动</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">需要管理访问权限 （PR：H）</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font mstmutation="1" msttexthash="24357359" msthash="83" style="box-sizing: border-box;"><span leaf="">8.7 （高）</span></font><section><span leaf=""><br/></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">CVE-2025-3079漏洞</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">imageCLASS 系列、i-SENSYS 系列、Satera 系列、办公室/小型办公室激光打印机</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">通过对多功能打印机的回传攻击破坏身份验证数据的完整性/机密性</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">网络访问 + 管理权限</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font mstmutation="1" msttexthash="24357359" msthash="88" style="box-sizing: border-box;"><span leaf="">8.7 （高）</span></font><section><span leaf=""><br/></span></section></td></tr></tbody></table>## 缓解策略  
  
Canon 提供了全面的缓解指南，而固件补丁仍在开发中。  
  
该公司强烈建议不要将设备直接连接到公共互联网网络，而是建议在受防火墙、路由器或 Wi-Fi 路由器保护的安全网络环境中使用私有 IP 地址。  
  
关键的安全措施包括将默认密码更改为强的唯一凭据，以及实施强大的管理员和常规用户身份验证。  
  
组织应在支持的情况下启用多重身份验证 （MFA），并确保所有管理设置都使用足够复杂的密码，以抵御暴力攻击。  
  
物理安全注意事项同样重要，因为攻击者经常利用无人值守设备上的默认凭据。Canon 建议在 psirt.canon/hardening 上查阅其产品强化指南，了解全面的网络安全实践。  
  
此外，组织应实施网络分段，以隔离打印基础设施并监控设备访问日志中是否存在可疑的身份验证尝试。  
  
该公告强调，Vercel 托管的 Next.js 部署会获得自动保护，但在实施适当的缓解措施之前，自托管应用程序仍然容易受到攻击。  
  
立即对其 Canon 打印机部署进行审核，并实施建议的安全控制措施，以防止潜在的凭据盗窃和在其网络内横向移动。  
  
**免责声明**  
：  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
