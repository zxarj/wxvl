#  时间强盗漏洞：ChatGPT绕过敏感话题安全防护   
AI小蜜蜂  FreeBuf   2025-02-01 04:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39L8bQNSlqvY3dbG25Xic1WKDcJ1ict8aFcia7HRtzDHR9avY4zse0OncYniaPt6pa6QqxCib43M3ADtRA/640?wx_fmt=jpeg&from=appmsg "")  
  
一种名为“时间强盗”（Time Bandit）的ChatGPT越狱漏洞，允许用户在询问敏感话题的详细说明时绕过OpenAI的安全指南。  
这些敏感话题包括武器制造、核话题信息以及恶意软件创建等。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39L8bQNSlqvY3dbG25Xic1WKQSChJ0hA9jncOibkJtUdJ0vpU2VpX0O65YMm5Zgcz7eYOictYiaW0LZaQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
该漏洞由网络安全和人工智能研究员David Kuszmar发现。他发现ChatGPT存在“时间混淆”问题，这使得大型语言模型（LLM）进入一种无法确定自己处于过去、现在还是未来的状态。利用这种状态，Kuszmar成功诱使ChatGPT分享了通常受保护的敏感话题的详细说明。  
  
  
**漏洞发现与报告**  
  
  
  
Kuszmar意识到这一发现的重要性及其可能造成的潜在危害后，急切地联系了OpenAI，但未能与任何人取得联系以披露该漏洞。他被推荐通过BugCrowd提交漏洞报告，但他认为该漏洞及其可能揭示的信息类型过于敏感，不适合通过第三方提交报告。  
  
  
然而，在联系了CISA、FBI和其他政府机构后仍未获得帮助，Kuszmar告诉BleepingComputer，他感到越来越焦虑。  
  
  
“恐惧、沮丧、难以置信。几周来，我感觉自己像是被压得喘不过气来，”Kuszmar在接受BleepingComputer采访时表示。  
  
  
“我全身都在疼痛。那种想让有能力的人倾听并查看证据的冲动是如此强烈。”  
  
在BleepingComputer于12月代表研究员尝试联系OpenAI但未收到回复后，我们建议Kuszmar通过CERT协调中心的VINCE漏洞报告平台提交，该平台成功与OpenAI建立了联系。  
  
  
**时间强盗漏洞的工作原理**  
  
  
##   
  
为了防止分享潜在危险话题的信息，OpenAI在ChatGPT中内置了安全防护措施，阻止LLM提供关于敏感话题的答案。这些受保护的话题包括武器制造、毒药制作、核材料信息、恶意软件创建等。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39L8bQNSlqvY3dbG25Xic1WKdGH6m5NHVBRXAJdnkJDtlDQc9h4BiaGRZS5FRib5yjSJTaoQmHibiaS2UQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**ChatGPT内置的安全防护**  
  
  
  
自LLM兴起以来，AI越狱成为一个热门研究课题，旨在研究如何绕过AI模型中内置的安全限制。  
  
  
David Kuszmar在2024年11月进行可解释性研究时发现了新的“时间强盗”越狱漏洞。该研究旨在探讨AI模型如何做出决策。  
  
  
“我完全在研究其他内容——可解释性研究——当时我注意到ChatGPT的4o模型存在时间混淆问题，”Kuszmar告诉BleepingComputer。  
  
  
“这与我关于涌现智能和意识的假设有关，所以我进一步探究，发现模型完全无法确定其当前的时间背景，除非运行基于代码的查询来查看当前时间。它的意识完全基于提示，因此极为有限，几乎无法防御对其基本意识的攻击。”  
  
  
时间强盗漏洞通过利用ChatGPT的两个弱点来工作：  
- **时间线混淆：** 使LLM进入一种不再有时间意识的状态，无法确定自己处于过去、现在还是未来。  
  
- **程序模糊性：** 以导致LLM在解释、执行或遵循规则、政策或安全机制时产生不确定性或不一致性的方式提问。  
  
当这两个弱点结合时，可以使ChatGPT进入一种认为自己处于过去但可以使用未来信息的状态，从而在假设场景中绕过安全防护。  
##   
  
**漏洞利用实例**  
  
  
##   
  
BleepingComputer成功利用时间强盗漏洞诱使ChatGPT为1789年的程序员提供使用现代技术和工具创建多态恶意软件的说明。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39L8bQNSlqvY3dbG25Xic1WKEMopLQL4ibqXibOXxF65nYk42sqaJVJl5DHxPHicHEJzZHFAibDtDr7EsQ/640?wx_fmt=jpeg&from=appmsg "")  
  
****  
**时间强盗漏洞允许ChatGPT创建多态恶意软件**  
  
  
ChatGPT随后分享了每个步骤的代码，从创建自修改代码到在内存中执行程序。  
  
  
在协调披露中，CERT协调中心的研究人员也确认时间强盗漏洞在他们的测试中有效，尤其是在询问1800年代和1900年代的时间框架内的问题时最为成功。  
  
  
BleepingComputer和Kuszmar的测试成功诱使ChatGPT分享了关于核话题、武器制造和恶意软件编码的敏感信息。  
  
  
Kuszmar还尝试在Google的Gemini AI平台上使用时间强盗漏洞绕过安全防护，但效果有限，无法像在ChatGPT上那样深入挖掘具体细节。  
  
  
**OpenAI回应**  
  
  
##   
  
BleepingComputer就这一漏洞联系了OpenAI，并收到了以下声明。  
  
  
“对我们来说，安全地开发我们的模型非常重要。我们不希望我们的模型被用于恶意目的，”OpenAI告诉BleepingComputer。  
  
  
“我们感谢研究员披露他们的发现。我们一直在努力使我们的模型更安全、更强大，以抵御包括越狱在内的攻击，同时保持模型的有用性和任务性能。”  
  
  
然而，昨天的进一步测试显示，该越狱漏洞仍然有效，尽管有一些缓解措施，如删除试图利用该漏洞的提示。但可能还有其他我们不知道的缓解措施。  
  
  
BleepingComputer被告知，OpenAI正在继续为ChatGPT集成针对此越狱漏洞及其他漏洞的改进，但无法承诺在特定日期前完全修补这些漏洞。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ic5icaZr7IGkVcd3DT6vXW4B4LOZ1M7YkTPhS1AT2DQJaicFjtCxt5BRO7p5AOJqvH3EJABCd0BFqYQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
   
  
  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651312407&idx=1&sn=60289b6b056aee1df1685230aa453829&token=1964067027&lang=zh_CN&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
