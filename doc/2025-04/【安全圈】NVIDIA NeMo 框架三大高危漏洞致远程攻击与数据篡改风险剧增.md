#  【安全圈】NVIDIA NeMo 框架三大高危漏洞致远程攻击与数据篡改风险剧增   
 安全圈   2025-04-25 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
安全漏洞  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaK50E4nv3xvMMJaGjmwKyzyY0hBrIogY0tds8A6978sug75Cqd0iaALUh46D4zxB2F1D44jX20U2w/640?wx_fmt=png&from=appmsg "")  
  
NVIDIA NeMo 框架存在三个高危漏洞，攻击者可利用这些漏洞执行远程代码，这有可能危及人工智能（AI）系统的安全，并导致数据被篡改。  
  
这些安全漏洞分别被认定为 CVE-2025-23249、CVE-2025-23250 和 CVE-2025-23251，每个漏洞的通用漏洞评分系统（CVSS）基础得分均为 7.6 分，这表明对于这个广受欢迎的生成式人工智能框架的用户来说，存在着重大风险。  
  
NVIDIA 于 2025 年 4 月 22 日发布了安全补丁，敦促用户立即进行更新，以防范在 Windows、Linux 和 macOS 平台上可能出现的漏洞被利用的情况。  
  
**NVIDIA****NeMo 框架中的高危漏洞**  
  
第一个漏洞（CVE-2025-23249）涉及对不可信数据的不安全反序列化，这可能使攻击者能够远程执行任意代码。  
  
这个被归类为 CWE-502 的漏洞，使得攻击者能够在数据处理周期中操纵序列化对象并注入恶意代码。  
  
官方安全公告指出：“NVIDIA NeMo 框架存在一个漏洞，用户可能会因远程代码执行而导致对不可信数据进行反序列化。成功利用这个漏洞可能会导致代码执行和数据篡改。”  
  
第二个漏洞（CVE-2025-23250）源于不正确的路径验证（CWE-22），攻击者有可能通过利用路径遍历技术来执行任意文件写入操作。  
  
安全研究人员指出，这一弱点可能会让攻击者覆盖敏感文件或引入恶意配置，从而有可能劫持训练流程或在人工智能工作流程中污染数据集。  
  
第三个漏洞（CVE-2025-23251）与对代码生成的控制不当（CWE-94）有关，攻击者可利用该漏洞进行远程代码执行。  
  
对于一个为生成式人工智能应用设计的框架来说，这一点尤其令人担忧，因为它直接影响到可信和不可信代码执行环境之间的界限。  
  
NVIDIA 对来自上海大学的安全研究员 Peng Zhou 表示感谢，因为他报告了 4 月份发现的这三个漏洞。  
<table><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><span leaf="">CVEs</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><span leaf="">Affected Products</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><span leaf="">Impact</span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><span leaf="">Exploit Prerequisites</span></strong><strong style="box-sizing: border-box;font-weight: bold;"></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><span leaf="">CVSS 3.1 Score</span></strong></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">CVE-2025-23249 CVE-2025-23250</span><span leaf=""><br/></span><span leaf="">CVE-2025-23251</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">NVIDIA NeMo Framework (Windows, Linux, macOS; all versions prior to 25.02)</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">Code execution, data tampering</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">Remote attacker, user interaction required</span></section></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><section><span leaf="">7.6 (High)</span></section></td></tr></tbody></table>  
这三个漏洞具有相同的攻击向量规格  
  
（AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:H/A:L），这表明它们可以在攻击复杂度较低且无需特权的情况下被远程利用，不过需要用户进行交互操作。  
  
NeMo 框架是一个可扩展的云原生生成式人工智能平台，被从事大型语言模型（LLM）、多模态模型以及包括语音识别和计算机视觉等各种人工智能应用研究的研究人员和开发人员广泛使用。  
  
该公司已发布 25.02 版本以修复这些问题，并强烈建议所有受影响的系统立即进行更新。  
  
安全专家建议使用 NeMo Framework 的机构采取以下措施：  
  
1.立即更新到 25.02 版本。  
  
2.检查任何可能已受到损害的人工智能系统。  
  
3.在人工智能开发流程周围实施额外的安全控制措施。  
  
4.监控系统，留意可能表明存在漏洞被利用情况的异常活动。  
  
这些漏洞凸显了在人工智能开发框架中安全的重要性日益增加，因为它们在全球的商业运营和研究计划中变得越来越关键。  
  
  
  END    
  
  
阅读推荐  
  
  
[【安全圈】警惕！新型恶意软件通过多层混淆技术劫持Docker镜像](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652069259&idx=1&sn=326c3497b6e6e654a9628f4e662d3909&scene=21#wechat_redirect)  
  
  
  
[【安全圈】重大供应链攻击预警：XRP官方NPM包遭劫持植入私钥窃取程序](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652069259&idx=2&sn=afe3ad55e70f079c97b674d104dfe7a4&scene=21#wechat_redirect)  
  
  
  
[【安全圈】加州蓝盾医保470万患者数据遭泄露，误配谷歌分析工具酿近年最大医疗隐私事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652069259&idx=3&sn=a34002c3f2e5b52241931f98f5e52646&scene=21#wechat_redirect)  
  
  
  
[【安全圈】新型钓鱼攻击预警：黑客滥用Google表单绕过邮件安检窃取凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652069259&idx=4&sn=37779dd9ac19192b61a98b1d6d0e8b44&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
