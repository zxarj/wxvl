#  【免杀+钓鱼】钓鱼页面搭建+免杀捆绑拿shell   
原创 赵小龙  红岸基地网络安全   2024-12-03 09:20  
  
## 简介  
  
  
今天我们将会为大家揭开钓鱼获取权限这一过程的神秘面纱。请大家务必牢记：**本次实验仅限于模拟环境中进行，目的是研究和学习相关技术**  
，任何非法使用的行为都会导致严重后果，并违背法律与道德的底线。  
  
下面，我们将展开完整的流程，同时讲解每一步的技术要点和实用方法。  
### 一、工具与技术清单  
  
我们今天要用到以下工具和技术：  
1. **公网服务器**  
：  
    - 推荐使用Linux或Windows系统。  
  
    - 本次演示使用Windows服务器，操作更直观，适合大家入门。  
  
  
1. 推荐使用Linux或Windows系统。  
  
1. 本次演示使用Windows服务器，操作更直观，适合大家入门。  
  
1. **Python开发环境**  
：  
    - 用于编写后端服务和钓鱼页面逻辑。  
  
    - 不熟悉Python的朋友，可以借助AI工具或现成代码模板进行修改。  
  
  
1. 用于编写后端服务和钓鱼页面逻辑。  
  
1. 不熟悉Python的朋友，可以借助AI工具或现成代码模板进行修改。  
  
1. **钓鱼平台**  
：  
    - 模仿目标官网（如百度、抖音、百度网盘等）的钓鱼网站，达到极高的迷惑性。  
  
    - 平台的交互设计和细节是核心，后面会详细说明。  
  
  
1. 模仿目标官网（如百度、抖音、百度网盘等）的钓鱼网站，达到极高的迷惑性。  
  
1. 平台的交互设计和细节是核心，后面会详细说明。  
  
1. **免杀木马**  
：  
    - 技术环节的重点，旨在绕过防病毒软件的检测。  
  
    - 演示中会使用我的木马工具（默认反弹到我个人服务器上）。  
  
  
1. 技术环节的重点，旨在绕过防病毒软件的检测。  
  
1. 演示中会使用我的木马工具（默认反弹到我个人服务器上）。  
  
1. **捆绑技术**  
：  
    - 将木马与受欢迎的安装包捆绑，并通过伪装技术增强信任度。  
  
  
1. 将木马与受欢迎的安装包捆绑，并通过伪装技术增强信任度。  
  
## 第一步:服务器配置  
  
#### 1. 搭建服务器环境  
  
第一步是获取一台公网服务器，选择Windows或Linux系统均可。  
本次我们选择Windows服务器：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4aaM0NlWZIoW3x4GQ47hp23yZ9iahibvO7SibricPmBCGvNFHrxfeV3JzXicg/640?wx_fmt=png&from=appmsg "")  
- 配置简单，支持多种开发环境。  
  
- 直观界面便于理解和操作。  
  
搭建服务器后，需要部署一个后端服务。常见的后端工具包括：  
- Cobalt Strike（CS）  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4a8N14C0CSKr8LHqich2s8Ksgicc63hs2ZjoPJfiaOPoBpRMaM9gsvf1JBA/640?wx_fmt=png&from=appmsg "")  
- Metasploit Framework（MSF）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4aiaNxXPtCfXB2kSeDTwOgVO5GzeKDCHCedaglBNAZ3icYjpZf5x7abfrw/640?wx_fmt=png&from=appmsg "")  
- 轻量化自定义服务，如反弹Shell监听器、文件上传模块等。我们这里采用的是自研的服务，红岸shell服务器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4aia9lGXN9fn3Ue1OXBjLJicpicR6giaYarc5ia8NCKcHatmHDkYtgPh77A1g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**第二步:网页编辑**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
#### 2. 编写伪造网页  
  
接下来，使用Python或其他工具编写一个仿真的钓鱼页面。比如：  
- 百度搜索页面：高仿官网的布局、功能和交互，增强可信度。  
  
- 抖音引流页面：伪装为福利或资源链接页面。  
  
- 百度网盘下载页面：用户点击下载后捆绑木马执行程序。  
  
**技术要点**  
：  
- 界面设计：确保页面元素的布局、配色、字体都与目标官网一致。  
  
- 动态交互：实现真实搜索功能，或模仿下载行为，增加可信度。  
  
当然，你需要拥有一定的python基础，如果没有，你可以利用ai，或者直接在龙哥的python代码中修改  
  
后续，我也会开放一些如果baidu，douyin等官网一摸一样的的伪造平台，当然这里这项技术因为存在风险，不会在这里进行展示了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4aIyRIeiaSnu9oibPrggTXX7XDNJzMvoYNia4guXJkZMFjjPpFfpzKHV3Wg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4aA1m10YpfRRJkXXUXp84Ma8FPs6lKKOgp9Cms40RCCusVibRHf7kvsgQ/640?wx_fmt=png&from=appmsg "")  
## 第三步:免杀艺术  
#### 3. 免杀木马的设计与生成  
  
木马程序是整个流程的核心技术环节，也是绕过目标防护的关键：  
- **免杀技术**  
：  
    1. 绕过常见的杀毒软件检测（如Windows Defender、火绒、360等）。  
  
    1. 采用加密与多层壳的方式混淆代码逻辑。  
  
    1. 根据目标系统的环境调整特定Payload。  
  
  
- 绕过常见的杀毒软件检测（如Windows Defender、火绒、360等）。  
  
- 采用加密与多层壳的方式混淆代码逻辑。  
  
- 根据目标系统的环境调整特定Payload。  
  
- **木马执行流程**  
：  
    1. 用户下载并执行后，触发反弹Shell或其他后门机制。  
  
    1. 与服务器建立反向连接，实现持久控制。  
  
  
- 用户下载并执行后，触发反弹Shell或其他后门机制。  
  
- 与服务器建立反向连接，实现持久控制。  
  
需要注意的是，我的木马会反弹到个人服务器上，用于实验演示，默认视为授权。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4ahnoV5ibAz9xh1cM5JNVFWPB1iaq8zhTY0pwDd4UFHvmnLsvlob64jzpg/640?wx_fmt=png&from=appmsg "")  
  
## 第四步:捆绑技术  
#### 4. 捆绑技术的应用  
  
木马程序需要通过伪装和捆绑提升分发成功率。以下是几种有效的捆绑策略：  
- **捆绑到常用软件安装包**  
：  
    1. 抖音、百度网盘、视频播放器等目标软件的安装包是理想选择。  
  
    1. 外观伪装得极度逼真，同时内部捆绑执行程序。  
  
  
- 抖音、百度网盘、视频播放器等目标软件的安装包是理想选择。  
  
- 外观伪装得极度逼真，同时内部捆绑执行程序。  
  
- **伪装下载链接或广告页面**  
：  
    1. 通过高仿页面提供虚假的软件更新或资源下载链接。  
  
    1. 配合强交互体验，让目标用户完全信任。  
  
  
- 通过高仿页面提供虚假的软件更新或资源下载链接。  
  
- 配合强交互体验，让目标用户完全信任。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4atQbba7IKW3nf8A2gSYmll2stiawGMwyUhS3Imv78ojL2SicPNibpibcS3Q/640?wx_fmt=png&from=appmsg "")  
## 第五步:权限获取  
####   
#### 5. 权限获取与后续操作  
  
目标执行木马后，后端服务会收到反弹连接，进入权限获取环节。  
- **权限控制手段**  
：  
    1. 通过CS/MSF工具提权、获取目标文件或持续控制。  
  
    1. 安装持久性后门，便于后续连接。  
  
  
- 通过CS/MSF工具提权、获取目标文件或持续控制。  
  
- 安装持久性后门，便于后续连接。  
  
- **后续利用**  
：  
    1. 数据提取与分析。  
  
    1. 模拟攻击与防御研究。  
  
  
- 数据提取与分析。  
  
- 模拟攻击与防御研究。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2upMtBvz3SoQzQXGOdUKmib4agCj47161DiaqALvCb9zxqIFsIA7Ld8jjd4ibbI0CF3QNIGRho1ic6X9og/640?wx_fmt=png&from=appmsg "")  
## 总结:完整视频分享  
  
  
视频无法查看的的话去看这里  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**免责声明**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
文章所涉及内容，仅供安全研究与教学之用，由于传播、利用本文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。  
  
  
大家对于网络安全感兴趣的话，不妨来加一下我们的老师，我们会定期在给大家分享  
**渗透****工具**  
和  
**实战****文****章**  
，还会有  
**渗透公开课**  
可以试听！  
  
**扫码添加，提升自己，可以关注我，晚上10点进行直播间展示！**  
  
**👇👇👇**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XvnzjMsl2uqSvZE6x25icBxYJVFOCI9lDasEWqq2rXaaHicvykJsBK94cBdfxibU6fOQ2iaTJ0IKoVMmiaFbIAjJz4A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
后续一些打击犯罪文章会在下方公众号发布  
  
  
  
