#  Burp Suite 插件 BurpGPT，可执行额外的被动扫描，以发现高度定制的漏洞，并可以运行任何类型的基于流量的分析。   
 夜组安全   2024-12-31 03:30  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**baobeiaini_ya**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
  
**01**  
  
**工具介绍**  
  
BurpGPT，可提高渗透测试的效率和质量有高级的语言处理能力，操作界面好用可发现零日漏洞、评估加密的完整性分析网络流量、评估网络应用程序  
  
  
支持自定义提示(prompts)，以满足特定的分析需求可自动生成一份安全报告根据用户的提示和Burp实时数据总结潜在的安全问题  
  
  
burpgpt利用 的功能AI来检测传统扫描仪可能遗漏的安全漏洞。它将网络流量发送到OpenAI model用户指定的设备，从而在被动扫描仪内进行复杂的分析。此扩展提供可定制的功能prompts，可实现量身定制的网络流量分析，以满足每个用户的特定需求。  
  
  
该扩展程序会生成一份自动安全报告，根据用户发出的请求prompt的实时数据总结潜在的安全问题Burp。通过利用AI和自然语言处理，该扩展程序简化了安全评估流程，并为安全专业人员提供了扫描应用程序或端点的更高层次概述。这使他们能够更轻松地识别潜在的安全问题并确定分析的优先级，同时还覆盖更大的潜在攻击面。  
  
  
**02**  
  
**工具使用**  
  
要开始使用 burpgpt，用户需要在“设置”面板中完成以下步骤，可以从 Burp Suite 菜单栏访问该面板：  
1. 输入有效的OpenAI API key。  
  
1. 选择一个model。  
  
1. 定义。此字段控制发送到 的max prompt size最大长度，以避免超过模型的（通常约为）。promptOpenAImaxTokensGPT2048GPT-3  
  
1. 根据您的要求调整或创建自定义提示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2VPGAruRh2zsDhXllK0vjZkBDmOMB3cdhERY5FdWaibyWH0ZnD6vkibCXoCjWnTrfiaeWG0goXRNUO2g/640?wx_fmt=png&from=appmsg "")  
  
一旦按照上述配置完成，就会通过Burp passive scanner所选的将每个请求发送到进行分析，并根据结果产生级别严重性发现。OpenAI modelOpenAI APIInformational  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2VPGAruRh2zsDhXllK0vjZk6gnMOJbNIJ7QrhFKqQnk957DvNv3YGp5K36eIQjdYuaibZg3a6keAdw/640?wx_fmt=png&from=appmsg "")  
###   
### 快捷配置  
### burpgpt使用户能够prompt使用系统定制流量分析placeholder。要包含相关信息，我们建议使用placeholders扩展直接处理的这些，允许将特定值动态插入到prompt：  
  
<table><thead style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><th style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">占位符</th><th style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">描述</th></tr></thead><tbody style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{REQUEST}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">已扫描的请求。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{URL}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描请求的 URL。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{METHOD}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描请求中使用的 HTTP 请求方法。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{REQUEST_HEADERS}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描的请求的标题。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{REQUEST_BODY}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描请求的主体。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{RESPONSE}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描的回应。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{RESPONSE_HEADERS}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描的响应的标题。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{RESPONSE_BODY}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">扫描的响应的主体。</td></tr><tr style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;"><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">{IS_TRUNCATED_PROMPT}</td><td style="word-break: break-all;margin-bottom: 0px;text-wrap: wrap;font-size: 15px;letter-spacing: 1px;">boolean以编程方式设置为true或的值，false用于指示是否prompt被截断为Maximum Prompt Size中定义的Settings。</td></tr></tbody></table>  
  
这些placeholders可以在自定义中使用，以动态生成特定于扫描请求的prompt请求/响应分析。prompt  
> [!NOTE] >通过使用会话处理规则或扩展（例如自定义参数处理程序）Burp Suite提供了支持任意的能力，从而允许对 进行更大程度的自定义。placeholdersprompts  
  
  
**03**  
  
**工具下载**  
  
**点击关注下方名片****进入公众号**  
  
**回复关键字【241231****】获取**  
**下载链接**  
  
  
  
**04**  
  
**往期精彩**  
  
[ APP客户端安全问题扫描工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493109&idx=1&sn=7f1a52e315b92fbcae79d5258272e2cf&chksm=c36ba10df41c281bfb29c1b311fd51794a07b273dddf77e502370ebaeb26ee1e0e818136ecaa&scene=21#wechat_redirect)  

						  
  
  
[ 网络信息系统WF2409E路由器进行了一次完整的硬件安全分析研究 | 漏洞分析 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493098&idx=1&sn=daf17eea39dbbe868a10945583414150&chksm=c36ba112f41c2804aa4b1cb0f1deca31b13077a83efc3a9cce0757ac3cf41017c970afbd3938&scene=21#wechat_redirect)  

						  
  
  
[ 一款图形化的代码审计工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247493045&idx=1&sn=f67df2ff5bb85865bece4973f1391f34&chksm=c36ba14df41c285bb5079c35b0447840e996df095342f3cc617aad1e15ebc7a028b1fffab633&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557 "")  
  
