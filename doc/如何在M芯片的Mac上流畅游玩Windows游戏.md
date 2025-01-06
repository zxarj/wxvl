#  如何在M芯片的Mac上流畅游玩Windows游戏   
原创 骨哥说事  骨哥说事   2025-01-06 16:02  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
# 文章原文：https://gugesay.com/archives/3788  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
# 背景介绍  
  
最近几天骨哥浅尝了一下在某音的游戏直播，一直使用的是家里的PC台式机，不得不说，Windows系统的直播效果是真心不错，但是呢，有一些很不错的单机游戏，能否在Mac上玩耍呢，于是乎就有了这篇文章。  
  
目前一般主流的选择是，使用 Parallel Desktop（以下简称PD） 或者 CrossOver 的方案来实现在 MacOS on Apple Silicon 平台上运行Windows的各类游戏。  
  
骨哥一直以来都不爱使用PD，因此最终选择了性能更好的 CrossOver。  
  
前段时间，骨哥看了一个讲解Steam掌机为何能流畅的运行Windows游戏的视频，在目前日益成熟的 wine 技术（wine 的实现原理是将程序对 Windows 的系统调用转换成宿主系统的系统调用，从而执行其中的 Windows 可执行程序）上，MacOS 底层提供的 Rosetta 2 可以将 x86 程序的指令集转译为 ARM 指令集以便在 Apple Silicon 平台上运行 x86 程序，因此为 MacOS ARM 平台运行 Windows x86 平台的 游戏的扫除了“障碍”。  
  
因此CrossOver自然成为了我的不二选择，OK，那么就让我们开始吧。  
# 步骤  
## 拥有一台Mac Book  
  
这里无论你是Mac Book Air 还是Mac Book Pro，基本内存在16G以上足够（当然，内存越大越好哈）。  
## 安装CrossOver  
  
很简单，直接官网下载安装，官方提供了14天免费的试用期，当然，你可以采用一些“特殊手段”来延长试用期甚至永久免费（咳咳，本文就不对该部分进行说明了）。  
## 安装Steam  
  
然后打开CrossOver，在搜索框中搜索“Steam”，选择Steam进行安装：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOktCPeYW5vb7FCvma5CqHwEBgK6xlPkUFbFKDG2ppoL2F0GQtQ7Xzk2A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkkVY8v8PMF14ibyWW9tDVN2ic8XkzZEmkE7ySsFEZLHAx6Tgv06oaXnHA/640?wx_fmt=png&from=appmsg "")  
## 配置容器  
  
安装Steam后，在右侧需要设置一下容器的高级设置，把DXVK和高分辨率模式开启：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkCmNYw1AEgLyAUv3icwfT7pD3TuSJAHCWhIbtef8N6NicYQcWP7dzfUlA/640?wx_fmt=png&from=appmsg "")  
## 配置游戏安装【可选】  
  
由于Mac的硬盘和内存比较昂贵，不想占用Mac本身硬盘的童鞋们，可以将游戏装在外置的移动硬盘上，方法也很简单，插上你的移动硬盘，然后点击右侧Wine 配置，在驱动器中添加你的外置硬盘即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOknIib457pTXGZs6U8U8Dtw4m6aUaKgTbTGB3vzkAktrKqscUa066ogfw/640?wx_fmt=png&from=appmsg "")  
## 代理设置  
  
由于“众所周知”的原因，你直接访问Steam可能会失败，因此需要在网络设置中，设置代理，才能流畅无阻的访问Steam，点击右侧的“Internet 设置”，然后在“连接”选项中，勾选“使用代理服务器”，填入你的代理服务器地址和端口即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkLicnoAAbD7CxeOFer8HocLgiaXp4vIj38miaDOmI2BLH0ZFY1RpcGmictg/640?wx_fmt=png&from=appmsg "")  
# 启动Steam  
  
双击Steam图标即可启动Steam了，如果你很久登不进去的话，或者登进去提示离线模式的话，可以在Steam的图标上点击右键，选择“带选项运行”，然后使用 -tcp 参数来启动Steam即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOk0Uf0bWbjTrLeTdv9o8t8g6VB3xmYnSlxFhqvI0E7wXxSzmUEHJg7Pg/640?wx_fmt=png&from=appmsg "")  
  
如果我们设置了外接移动硬盘来保存游戏安装目录，还需要到Steam的设置>存储空间>添加驱动器中设置：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkoJ9TFZ77ZSs4yYtu72DBwtoKXOG0UcqaAUicbPJCuAR7MibrZOlZtNiaA/640?wx_fmt=png&from=appmsg "")  
# 启动游戏  
  
然后就是通过Steam来下载和安装游戏了，顺利安装后，就可以双击游戏来启动游戏了：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkZ3K5um9pKZicNGj26icyq87Fzg3KkafUnyHpZ9ZNObEI8byX3tOPAWYg/640?wx_fmt=jpeg&from=appmsg "")  
  
更有网友尝试了在Mac上玩耍黑神话和GTA 5，基本都非常流畅：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOk5b4ctR3RgYot2wEljYM5N4ozORnKNZibFXGCEMP2PMXKrcRWGQzPleg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnE73gBhOZmIoKcCvQLdVOkXibVtSNIJ082tbPh1L55eWyciaWfnSTCDPrYDjSMchznbwdhcHA10uIA/640?wx_fmt=png&from=appmsg "")  
  
Nice，愉快的玩耍吧～  
  
  
**加入星球，随时交流：**  
  
****  
**（前50位成员）：99元/年************（后续会员统一定价）：128元/年******  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jnMJtHJnShkTnh3vR3fmaqicPicANic6OEsobrpRjx5vG6mMTib1icuPmuG74h2bxC4eP6nMMzbs5QaSlw/640?wx_fmt=jpeg&from=appmsg "")  
  
**感谢阅读，如果觉得还不错的话，欢迎分享给更多喜爱的朋友～****====正文结束====**  
  
  
