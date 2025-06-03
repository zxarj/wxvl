#  谷歌Chrome零日漏洞遭广泛利用，可执行任意代码   
FreeBuf  FreeBuf   2025-06-03 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibx3bJZfhehZIlWdESwTPibT7AelrWtTx3wr30jC8lQlurzf07RMRExOTmedF6nDXlmIjoK0xUYsgQ/640?wx_fmt=png&from=appmsg "")  
  
  
谷歌在确认攻击者正在广泛利用一个关键零日漏洞（zero-day vulnerability）后，紧急发布了Chrome安全更新。该漏洞编号为CVE-2025-5419，攻击者可通过Chrome V8 JavaScript引擎中的越界读写操作，在受害者系统上执行任意代码。  
  
  
**Part01**  
### 紧急安全更新发布  
  
  
谷歌已向Windows和Mac用户推送Chrome 137.0.7151.68/.69版本，Linux系统版本为137.0.7151.68，更新将在未来数日乃至数周内全球逐步推送。谷歌明确表示"利用CVE-2025-5419漏洞的代码已存在"，将此列为需要用户立即处理的高优先级安全问题。  
  
  
**Part02**  
### 漏洞技术细节  
  
  
该漏洞由谷歌威胁分析小组（Threat Analysis Group）的Clement Lecigne和Benoît Sevens于2025年5月27日发现并报告。漏洞源于Chrome的JavaScript和WebAssembly引擎V8中的内存损坏问题，该引擎负责处理网站和Web应用程序的代码。  
  
  
越界内存访问漏洞尤其危险，攻击者可借此读取敏感数据或将恶意代码写入系统内存。鉴于威胁严重性，谷歌于2025年5月28日实施紧急缓解措施，在所有Chrome平台推送配置变更，在完整补丁发布前为用户提供保护。  
  
  
**Part03**  
### 同步修复的中危漏洞  
  
  
本次安全更新还修复了第二个漏洞CVE-2025-5068，这是Chrome渲染引擎Blink中的释放后使用（use-after-free）缺陷。安全研究员Walkman于2025年4月7日报告了这个中危漏洞，谷歌为此颁发了1,000美元漏洞赏金。虽然严重性低于零日漏洞，但释放后使用漏洞仍可能导致内存损坏和潜在代码执行。  
  
  
**Part04**  
### 谷歌的安全防护机制  
  
  
谷歌坚持在大多数用户完成浏览器更新前限制详细漏洞信息的访问政策，此举可防止恶意行为者在用户仍使用易受攻击版本时，通过逆向工程补丁开发新的利用代码。谷歌将其综合安全测试基础设施归功于能够在漏洞进入稳定版前发现多数问题，开发过程中采用AddressSanitizer、MemorySanitizer、UndefinedBehaviorSanitizer、控制流完整性（Control Flow Integrity）、libFuzzer和AFL等先进工具识别潜在安全问题。  
  
  
**Part05**  
### 用户应对建议  
  
  
Chrome用户应立即通过"设置 > 关于Chrome"更新浏览器，系统将自动下载安装最新版本。鉴于CVE-2025-5419正遭活跃利用，谷歌强烈建议用户将此更新视为紧急事项。用户可检查Chrome版本是否为137.0.7151.68或更高以确保防护。企业应优先在全网部署此更新，防止攻击者通过针对该零日漏洞的恶意网站实施入侵。  
  
  
**参考来源：**  
  
Google Chrome 0-Day Vulnerability Exploited in the Wild to Execute Arbitrary Code  
  
https://cybersecuritynews.com/chrome-0-day-vulnerability-exploited-in-the-wild/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651322307&idx=1&sn=4063f0cef12989b63bd8d0d3cd998454&scene=21#wechat_redirect)  
### 电台讨论  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif "")  
  
