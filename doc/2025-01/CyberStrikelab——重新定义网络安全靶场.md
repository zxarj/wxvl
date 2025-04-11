#  CyberStrikelab——重新定义网络安全靶场   
cslab  红蓝公鸡队   2025-01-14 10:16  
  
**CyberStrikeLab**  
 是一个专注于网络安全的在线仿真实战平台。  
  
网络安全的学习不应该只停留在表面的、理论的、枯燥的图文或视频中，实践才是检验的唯一标准。  
  
我们深知实战对于网络安全学习的重要性、稀缺性，为此我们做了一款这样的产品，他，**更实战**  
，**更系统**  
，**更方便**  
。  
  
平台地址：www.cyberstrikelab.com  
## 更实战  
  
实战是我们非常看重的点，靶场如果单纯只是靶场，距离实际渗透环境远，那将没有任何意义。  
  
**渗透不是一whoami都是system权限，免杀不是放一个马在虚拟机里面去点。**  
  
**传统的**  
、**脱离实际的**  
靶场不是我们的目标，**CyberStrikeLab**  
的靶机是由红队人员根据多年工作经验，拿出部分实战案例搭建，我们采用INTEL-VT、KVM等虚拟化技术完全模拟实战环境，包括了AV/EDR，这才是真正的实战。  
  
为了让大家直观感受，下面我们介绍**TengSnake**  
综合场景。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVcLmDPVgdAWMVLajz5h9LpmshtM4GlU3aN3A9aE7L051c399ibEZ2CWw/640?wx_fmt=png&from=appmsg "")  
  
该靶机一共4个网段，N台主机，其中所需要的知识点至少包含了：  
- 信息收集  
  
- getshell  
  
- 权限提升  
  
- Evasion  
  
- 横向移动  
  
- 多层代理  
  
- 权限维持  
  
- 域渗透  
  
- 。。。。。  
  
各种极限环境、知名AV/EDR。。。（不能剧透太多了）  
  
内测小伙伴直呼过瘾：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVqZyBX9RwEPWJWqZaU288icPLHOZ0PImDXtrneLDBkuD4miaaxA0Oy6LA/640?wx_fmt=png&from=appmsg "")  
## 更系统  
  
平台靶机建设参考了MITRE ATT&CK  
威胁框架，希望能够更加系统的拆解复杂场景下所需要的单点知识。  
  
目前已建设的模块有：  
- 权限提升  
  
- Evasion  
  
- 信息收集  
  
- 权限维持  
  
- 综合场景  
  
《PRIV》系列靶机涵盖了windows和linux的所有类型提权方式，并在一定程度上摒弃了传统傻瓜式提权方式，更贴合实战环境。在这里，“土豆“，”uac“，”脏牛“等提权技术均可以使用，学习权限提升更系统。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVCbYPqbmfZDLJjlx4aYboM4WEs7TzHic0GiaHTh7Yia8apt2VqMsjJice9Q/640?wx_fmt=png&from=appmsg "")  
  
《EVA》系列靶机涵盖了多种知名AV/EDR在真实环境下的防护，我们结合了实际渗透场景，经验丰富的红队人员都知道：在实际渗透过程中的免杀难度和本地搭建的免杀难度往往相差甚远。要想在《EVA》系列“过关”，你需要至少学会在静态和动态下的双重免杀，这很有难度，所以EVA系列的靶机难度至少为“困难”，初学者朋友切勿轻易挑战。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVdje4G5XnLyqGS2v6D9V2R1A1WG0jicZc4207rZDwh82NAOC9iaQ7ibibwA/640?wx_fmt=png&from=appmsg "")  
  
《PT》系列靶机是综合型靶机，包含了多个知识点，有适合新手朋友的相对简单的靶机，也有适合提升的相对困难的靶机，在这里你能真实的遇到实战中所遇到的问题，一些典型的极限环境，都能在这个版块进行体验。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVuWwfwWlqzpVickLzt8M0z5ZPMRFAyVeYj4C2f4uF0ejQ160ISV6jcEg/640?wx_fmt=png&from=appmsg "")  
  
《综合场景》是实战仿真的内网环境，准确的说不仅仅是内网环境，因为每打开一个环境，更像是一次红队行动，从信息收集，到getshell，再到权限维持、多层代理、横向移动，以及一路上的Evasion。。。  
  
未来我们会持续推出多层网络，更庞大，更贴近实战的内网靶机，希望你能玩的酣畅淋漓。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVHxjSrrkVSwvCP0tuovXoY7PpuUFWW1xmrrbxqB7Od6DhcPAAVfvrZg/640?wx_fmt=png&from=appmsg "")  
## 更方便  
  
体验靶机只需要一台电脑，以及准备好你的渗透工具即可。  
  
如果你要访问CVE板块，只需点击开启靶机，选择你要开启的时间即可，开启时间基本在数秒内即可体验  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVH42WalUOqIYS5Ox5icuBaEd3JP9z0Czud5fwyeM0hxtuB3a7vOBEorw/640?wx_fmt=png&from=appmsg "")  
  
如果你要访问仿真靶标，则需要准备openvpn软件，点击开启靶机，会自动加载靶机资源，平台为了尽可能仿真实战环境，资源要求较多，请耐心等待，开启完成后下载相关配置并连接，平台验证连接成功后即可访问目标。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVC7uQWoRcPNunrb1lZEic2OqX3WvCvIdoK3VKEpj1zzQtvVZadOGmmPg/640?wx_fmt=png&from=appmsg "")  
  
如果你要访问综合场景下的仿真内网资源，同样需要准备openvpn软件，等待开启后，连接专属于你的vpn服务器，即可开始畅游内网之旅。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ybSkegBMogPw0n8d2iavicnzKR5tLNXhCVQoibZbNibFChEVQkia5waP7h1w5IWRHmTic1fAfnvmluCicf5rEjw4MAgMA/640?wx_fmt=png&from=appmsg "")  
  
  
欢迎前来体验：  
  
  
www.cyberstrikelab.com  
  
  
