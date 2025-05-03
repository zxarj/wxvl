#  未修复的Windows快捷方式漏洞可导致远程代码执行，PoC已公布   
 FreeBuf   2025-05-03 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icbm1QXk9w6O9EM8c0VvZicm1LNgOR2haSDl5SbUYribmiaUxekWrmibyphSqqiahu9L1DMZ32v1xOxyTw/640?wx_fmt=png&from=appmsg "")  
  
  
  
安全研究员Nafiez近日公开披露了一个此前未知的Windows LNK文件（快捷方式）漏洞，攻击者可能利用该漏洞在无需用户交互的情况下远程执行代码。尽管研究人员已发布可用的概念验证（PoC），微软仍拒绝修复该漏洞，称其"未达到安全修复标准"。  
  
  
**01**  
  
  
  
**漏洞利用机制分析**  
  
  
该漏洞利用Windows快捷方式文件结构中的特定元素构建复杂攻击链。通过精心构造包含恶意EnvironmentVariableDataBlock和UNC路径的LNK文件，攻击者可在用户仅打开包含恶意快捷方式的文件夹时，触发静默网络连接。  
  
  
"当用户访问包含LNK文件的文件夹时，资源管理器会解析该文件夹中的所有文件...这正是文件初始化准备被调用/执行的阶段，"Nafiez在技术分析中解释道。  
  
  
该漏洞的特别危险之处在于，攻击实施甚至不需要用户点击快捷方式——仅浏览包含恶意LNK文件的目录就足以触发攻击。  
  
  
**02**  
  
  
  
**概念验证技术细节**  
  
  
漏洞利用通过操控LNK文件结构中的多个关键元素实现：  
- 设置HasArguments标志和EnvironmentVariableDataBlock以控制执行流程  
  
- 嵌入UNC路径（如\192.168.44.128\c）作为目标  
  
- 设置特定BlockSize和签名值来控制LNK文件行为  
  
Windows资源管理器通过包括IInitializeNetworkFolder和IShellFolder2在内的COM接口链处理这些特制文件，这些接口负责处理网络资源。当用户访问文件夹时，该处理过程会自动启动，为静默执行创造了条件。  
  
  
**03**  
  
  
  
**微软的安全立场与业界担忧**  
  
  
微软以"网络标记"（Mark of the Web，MOTW）安全功能已提供足够保护为由，决定不修复此漏洞。MOTW是对可能恶意的下载文件添加的数字标签，会在执行前触发安全警告。  
  
  
这种处理方式延续了微软对以往LNK漏洞的一贯态度。根据其安全服务标准，微软仅修复那些"违反安全边界或安全功能设计意图"且达到严重性阈值的问题。  
  
  
研究员Nafiez指出，编译代码后运行可执行文件生成LNK文件，并确保运行Responder工具捕获NTLM哈希。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icbm1QXk9w6O9EM8c0VvZicm5QFiabpQuWBXN1hP6GO62W5F3F45RSqz3nUlGdFQgcZiaYKaX4CtLiakw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
安全专家担忧仅依赖MOTW可能不足，因已存在已知绕过技术。Elastic安全实验室最近发现的"LNK stomping"技术已被威胁分子使用至少六年，可成功绕过MOTW控制。  
  
  
**04**  
  
  
  
**LNK文件攻击历史与现状**  
  
  
这并非LNK文件首次被利用。微软此前曾修复过LNK文件中的关键漏洞，包括2017年的远程代码执行漏洞和2010年遭主动利用的另一个漏洞。  
  
  
LNK文件正日益成为威胁分子的热门攻击媒介。正如Intezer安全研究人员所言："LNK文件（即Windows快捷方式）看似简单，但威胁分子可用其执行其他二进制文件并造成严重危害"。  
  
  
随着概念验证代码的公开，业界担忧该漏洞可能很快被威胁分子武器化用于实际攻击。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR39ibFdyjP3Qp8CEJxFWljbW1y91mvSZuxibf3Q3g2rJ32FNzoYfx4yaBmWbfwcRaNicuMo3AxIck2bCw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319699&idx=1&sn=127e9ca1a8d55931beae293a68e3b706&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319086&idx=1&sn=e2ff862babd7662c4fa06b0e069c03f2&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651319257&idx=1&sn=a603c646a53e3a242a2e79faf4f06239&scene=21#wechat_redirect)  
  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39ibFdyjP3Qp8CEJxFWljbW1uEIoRxNoqa17tBBrodHPbOERbZXdjFvNZC5uz0HtCfKbKx3o3XarGQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5KDnCKUfVLVQGsc9BiaQTUsrwzfcianumzeLVcmibOmm2FzUqef2V6WPQQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38mFMbqsUOVbBDicib7jSu7FfibBxO3LTiafGpMPic7a01jnxbnwOtajXvq5j2piaII2Knau7Av5Kxvp2wA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
