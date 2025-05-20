#  ChatGPT漏洞允许攻击者在共享对话中嵌入恶意SVG与图像文件   
 FreeBuf   2025-05-20 11:48  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibibIiawN2rxHETiabficydCkPHDar57bWKibCDeYA9sjweQuIksJjZjiaQNT6hJ9qs5ChxrDDIthYc6dMQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
### Part01  
### 漏洞详情  
  
  
研究人员发现ChatGPT存在一个严重安全漏洞（编号CVE-2025-43714），攻击者可利用该漏洞将恶意SVG（可缩放矢量图形）和图像文件直接嵌入共享对话中，可能导致用户遭受复杂的钓鱼攻击或接触到有害内容。该漏洞影响截至2025年3月30日的所有ChatGPT系统版本。  
  
  
安全专家发现，当用户重新打开或通过公开链接共享对话时，ChatGPT会错误地执行SVG代码，而非将其作为代码块中的文本显示。这种行为实际上在该AI平台中创建了一个存储型跨站脚本（XSS）漏洞。  
  
  
**Part02**  
### 攻击原理  
  
  
与JPG或PNG等常规图像格式不同，SVG文件是基于XML的矢量图像，可以包含HTML脚本标签——这是该格式的合法功能，但如果处理不当则十分危险。当这些SVG文件以内联方式而非代码形式呈现时，嵌入的标记会在用户浏览器中执行。  
  
  
研究人员zer0dac指出："ChatGPT系统在2025年3月30日之前版本会内联渲染SVG文档，而非将其作为代码块中的文本显示，这使得攻击者能在大多数现代图形网页浏览器中实施HTML注入。"  
  
  
![payloads.webp](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibibIiawN2rxHETiabficydCkPHYIcBm5dImbH0avcRJBk6yvNupgXp5DEAYUH9rknlnSHGPMGibcPnNpA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part03**  
### 潜在危害  
  
  
攻击者可精心设计看似合法的SVG代码嵌入欺骗性信息。更令人担忧的是，恶意行为者可能创建包含诱发癫痫的闪烁效果的SVG文件，对光敏性个体造成伤害。  
  
  
其他平台的类似漏洞报告指出："SVG文件可包含嵌入式JavaScript代码，当图像在浏览器中渲染时就会执行。这会产生XSS漏洞，使恶意代码能在其他用户会话上下文中执行。"  
  
  
**Part04**  
### 应对措施  
  
  
据报道，OpenAI在收到漏洞报告后已采取初步缓解措施，暂时禁用链接共享功能，但彻底修复底层问题的方案仍在开发中。安全专家建议用户谨慎查看来自未知来源的共享ChatGPT对话。  
  
  
该漏洞尤其令人担忧，因为大多数用户对ChatGPT内容存在天然信任，不会预期平台会出现视觉操控或钓鱼尝试。安全研究人员强调："即使没有JavaScript执行能力，视觉和心理操控仍构成滥用行为，特别是当可能影响他人健康或欺骗非技术用户时。"  
  
  
这一发现凸显出，随着AI聊天界面日益融入日常工作流程和通信渠道，防范传统网络漏洞的重要性正与日俱增。  
  
  
**参考来源：**  
  
**ChatGPT Vulnerability Lets Attackers Embed Malicious SVGs & Images in Shared Chats**  
  
https://cybersecuritynews.com/chatgpt-vulnerability-malicious-images/  
  
  
###   
###   
###   
### 推荐阅读  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651320917&idx=3&sn=7dc05cb9d3ab151bf6da222ec282fb34&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
###   
  
