#  IaC 和 PaC 工具中的网络安全缺陷使云平台面临新的攻击   
 信息安全大事件   2024-11-25 11:46  
  
网络安全研究人员披露了两种针对基础设施即代码   
（IaC） 和策略即代码 （PaC） 工具的新攻击技术，例如 HashiCorp 的 Terraform 和 Open Policy Agent （OPA），它们利用专用的域特定语言 （DSL） 来破坏云平台并泄露数据。  
  
“由于这些是功能有限的强化语言，因此它们应该比标准编程语言更安全——事实上，它们确实如此，”Tenable 高级安全研究员 Shelly Raban 在上周发布的一份技术报告中表示。“然而，更安全并不意味着无懈可击。”  
  
OPA 是一种流行的开源策略引擎，允许组织跨云原生环境（例如微服务、CI/CD 管道和 Kubernetes）实施策略。策略是使用名为 Rego 的本机查询语言定义的，然后由 OPA 进行评估以返回决策。  
  
Tenable 设计的攻击方法以供应链为目标，攻击者通过泄露的访问密钥获得未经授权的访问权限，将恶意 Rego 策略插入 OPA 服务器，随后在策略决策阶段使用该策略来允许使用称为“http.send”的内置函数进行凭据泄露等恶意操作。  
  
即使在   
OPA 部署限制使用 http.send 的情况下，这家网络安全公司发现，也可以利用另一个名为“net.lookup_ip_addr”的功能，通过一种称为 DNS 隧道的技术使用 DNS 查找来走私数据。  
  
“因此，net.lookup_ip_addr功能是您可以考虑限制或至少在策略中注意的另一个功能，因为它还会带来从 OPA 部署中泄露数据的风险，”Raban 说。  
  
Terraform 与 OPA 类似，旨在通过基于代码的定义简化设置、部署和管理云资源的过程。可以使用另一种称为 HashiCorp 配置语言 （HCL） 的声明性 DSL 来设置这些配置。  
  
攻击者可以通过利用其“terraform plan”命令（通常作为 GitHub“pull_request”工作流的一部分触发）来以开源 IaC 平台为目标，以执行包含恶意数据源的未经审查的更改  
在  
   
CI/CD 过程中。  
  
“这会带来风险，因为公共存储库中的外部攻击者或私有存储库中的恶意内部人员（或有立足点的外部攻击者）可能会利用拉取请求来实现其恶意目标，”Tenable 指出。“数据源在'terraform 计划'期间运行，这大大降低了攻击者的切入点。”  
  
反过来，这些数据源可能是流氓外部数据源、Terraform 模块或 DNS 数据源，因此只需要使用来自受信任来源的第三方组件。减轻此类风险的其他一些建议包括：  
- 实施精细的基于角色的访问控制   
（RBAC） 并遵循最小权限原则  
  
- 设置应用程序级和云级日志记录以进行监控和分析  
  
- 限制应用程序和底层计算机的网络和数据访问  
  
- 防止在   
CI/CD 管道中自动执行未经审核和潜在恶意的代码  
  
<table><tbody style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><tr class="ue-table-interlace-color-single js_darkmode__0" data-style="-webkit-tap-highlight-color: transparent; outline: 0px; background-color: rgb(28, 28, 28); visibility: visible; color: rgb(205, 205, 205) !important;" style="-webkit-tap-highlight-color: transparent;outline: 0px;background-color: rgb(28, 28, 28);visibility: visible;color: rgb(205, 205, 205) !important;"><td width="557" valign="top" data-style="-webkit-tap-highlight-color: transparent; outline: 0px; word-break: break-all; hyphens: auto; border-color: rgb(76, 76, 76); background-color: rgb(255, 218, 169); visibility: visible; color: rgb(25, 25, 25) !important;" class="js_darkmode__1" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;border-color: rgb(76, 76, 76);background-color: rgb(255, 218, 169);visibility: visible;color: rgb(25, 25, 25) !important;"><section style="-webkit-tap-highlight-color: transparent;outline: 0px;line-height: normal;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;outline: 0px;font-size: 12px;visibility: visible;color: rgb(0, 0, 0);">尊敬的读者：<br style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"/>感谢您花时间阅读我们提供的这篇文章。我们非常重视您的时间和精力，并深知信息对您的重要性。<br style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"/>我们希望了解您对这篇文章的看法和感受。我们真诚地想知道您是否认为这篇文章为您带来了有价值的资讯和启示，是否有助于您的个人或职业发展。<br style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"/>如果您认为这篇文章对您非常有价值，并且希望获得更多的相关资讯和服务，我们愿意为您提供进一步的定制化服务。请通过填写我们提供的在线表单，与我们联系并提供您的邮箱地址或其他联系方式。我们将定期向您发送相关资讯和更新，以帮助您更好地了解我们的服务和文章内容。</span></section><section style="-webkit-tap-highlight-color: transparent;outline: 0px;line-height: normal;visibility: visible;"><br style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"/></section><section style="-webkit-tap-highlight-color: transparent;outline: 0px;line-height: normal;text-indent: 0em;visibility: visible;"><span style="-webkit-tap-highlight-color: transparent;outline: 0px;color: rgb(0, 0, 0);">                   </span><img class="rich_pages wxw-img" data-backh="106" data-backw="106" data-cropselx1="0" data-cropselx2="119" data-cropsely1="0" data-cropsely2="119" data-galleryid="" data-imgfileid="100006365" data-ratio="1" data-s="300,640" data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/JqliagemfTA5N8G6ZVujodYTTD7NSaxFG5suXlkibicfoGRzCk6vHhCUBx7ST8b4AxdsFVNNAH4ltePBWX4AxKY0A/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp" data-type="png" data-w="1000" style="-webkit-tap-highlight-color: transparent;outline: 0px;font-family: 宋体;font-size: 14px;letter-spacing: 0.578px;text-align: center;visibility: visible !important;width: 119px !important;"/></section><section style="-webkit-tap-highlight-color: transparent;outline: 0px;line-height: normal;text-indent: 0em;"><span style="-webkit-tap-highlight-color: transparent;outline: 0px;font-family: 宋体;font-size: 12px;letter-spacing: 0.578px;text-align: center;color: rgb(0, 0, 0);">                               扫描二维码，参与调查</span></section><section style="-webkit-tap-highlight-color: transparent;outline: 0px;line-height: normal;"><br style="-webkit-tap-highlight-color: transparent;outline: 0px;letter-spacing: 0.544px;"/></section></td></tr></tbody></table>  
  
  
**END**  
  
  
  
点击下方，关注公众号  
  
获取免费咨询和安全服务  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JqliagemfTA5OxIlGh6IbpxrTJHkcY5DZ4O80nevX4Ev7IHvjZfPZDDMxibSVWk4IdYfaYpuhBgz2iaWS5tzXZLJw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
安全咨询/安全集成/安全运营  
  
专业可信的信息安全应用服务商！  
  
http://www.jsgjxx.com  
  
  
