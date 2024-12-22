#  FortiWLM 曝关键漏洞，攻击者可获得管理员权限   
FreeBuf  商密君   2024-12-22 01:01  
  
Fortinet 披露了 Fortinet Wireless Manager （FortiWLM） 中的一个严重漏洞，该漏洞允许远程攻击者通过特制的 Web 请求执行未经授权的代码或命令来接管设备。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR389GQon9kaib6xcIzm7t0JKib8U98Q3eop7c9gpx74rlU2PRa4FIjLicqbmkeh1HKO0JGTudpsHxyy3g/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
FortiWLM 是一种集中式管理工具，用于监控、管理和优化无线网络，被政府机构、医疗保健组织、教育机构和大型企业使用。  
  
  
该漏洞被跟踪为 CVE-2023-34990，是一个相对路径遍历缺陷，评分高达 9.6。Horizon3 研究员 Zach Hanley 于 2023 年 5 月发现并披露了该漏洞。但在数月后仍未修复。于是 Hanley 决定于 2024 年 3 月 14 日在一篇关于他发现的其他 Fortinet 漏洞的技术文章中披露相关信息和 POC。尽管研究人员公开警告，但缺少 CVE编号以及安全公告意味着大多数用户没有充分意识到风险。  
  
  
该漏洞会影响 FortiWLM 8.6.0 到 8.6.5 和 8.5.0 到 8.5.4 版本 。当 'op_type' 设置为 'upgradelogs' 时，通过在 'imagename' 参数中使用目录遍历技术，攻击者可以从系统中读取敏感的日志文件。这些日志通常包含管理员会话 ID，可用于劫持管理员会话并获得特权访问权限，从而允许威胁行为者接管设备。  
  
  
根据12月18日发布的安全公告，漏洞已在 2023 年 9 月底发布的 FortiWLM 版本 8.6.6 和 8.5.5 中修复。但Fortinet直到最近才正式发布该漏洞的安全通告。  
  
  
换言之，该漏洞作为零日漏洞持续了大约四个月的时间，鉴于 FortiWLM 部署在关键环境中，可能成为攻击者的目标，通过远程入侵导致整个网络中断和敏感数据泄露。因此，强烈建议 FortiWLM 管理员在可用更新可用时应用所有可用更新。  
  
  
编辑：陈十九  
  
审核：商密君  
  
**征文启事**  
  
大家好，为了更好地促进同业间学术交流，商密君现开启征文活动，只要你对商用密码、网络安全、数据加密等有自己的独到见解和想法，都可以积极向商密君投稿，商密君一定将您的声音传递给更多的人。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXNcXmbiaiaCljdXpwzOEQ9QTBXMibM6rZTOnbTSwTmCXncQLria2vuLGxn8QPtznzBc0as8vBxWIjrWxQ/640?wx_fmt=jpeg "")  
  
来源：FreeBuf  
  
注：内容均来源于互联网，版权归作者所有，如有侵权，请联系告知，我们将尽快处理。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1HyKzSU2XXOdeQx0thlyozF2swQTEN9iaaBNDG0jTKfAgqgdesve8x5IEWNvYxjF6sAWjO1TPCZVsWd0oiaDn3uw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMyyClGk1cttkSBbJicAn5drpXEbFIeChG9IkrslYEylRF4Z6KNaxNafDwr5ibcYaZXdnveQCNIr5kw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaMcJkA69QYZ9T4jmc3fdN6EA7Qq9A8E3RWcTKhxVEU1QjqOgrJMu2Qg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点分享  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaiaRXdw4BFsc7MxzkVZaKGgtjWA5GKtUfm3hlgzsBtjJ0mnh9QibeFOGQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点点赞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1HyKzSU2XXMZPiaDBD8yxbIHiciauWK4tuiaeiaNlRO9954g4VS87icD7KQdxzokTGDIjmCJA563IwfStoFzPUaliauXg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
点在看  
  
