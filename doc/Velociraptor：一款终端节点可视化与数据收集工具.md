#  Velociraptor：一款终端节点可视化与数据收集工具   
Alpha_h4ck  FreeBuf   2024-11-16 02:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/oQ6bDiaGhdyoFWEgZIHic7sqnootFEuOic7RlQNGhKY6d2ZESG3WpiaTMRlD0z4xO6mQrTZjkWHCkMpO2QtCfUJH6g/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**关于Velociraptor**  
  
  
## Velociraptor是一款终端节点可视化与数据收集工具，该工具使用了Velociraptor 查询语言 (VQL) ，可以帮助广大研究人员查询收集基于主机的状态信息。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38kicxmSKeQw5hH5XX7P9Sn5gHUcRCfDxzZDLibicibpsosbSSwAV3kXSDUwztKSfiadHMIKqvmGUlXEibA/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
**功能介绍**  
  
  
  
Velociraptor 是一个独特、先进的开源端点监控、数字取证和网络响应平台。当前版本的Velociraptor具备以下功能特点：  
> 1、能够有效应对数据泄露；  
> 2、通过数字取证分析重建威胁行为者的活动；  
> 3、寻找威胁行为者的活动证据；  
> 4、调查恶意软件爆发和其他可疑网络活动；  
> 5、持续监控可疑的用户活动，例如将文件复制到 USB 设备；  
> 6、网络外机密信息泄露；  
> 7、随着时间的推移收集端点数据，以用于威胁搜寻和未来调查；  
  
##   
  
**工具特点**  
  
  
##   
> 1、有用 ——每个工件和用例都必须向用户返回有价值的信息  
> 2、简单 ——设计和界面必须易于浏览和使用  
> 3、指导性 ——用户不需要是 DFIR 专家，因为所有元素都应提供信息描述和指导  
> 4、功能强大 ——用户无需做太多额外工作即可实现其目标  
> 5、快速 ——性能应快速且对资源的影响较小，同时允许在需要时管理性能  
> 6、可靠 ——每个功能和工件都应按预期工作，并且相对没有错误和问题  
  
##   
  
**工具要求**  
  
  
##   
> Go v1.23.2+  
> make  
> gcc  
> Node.js LTS（v18.14.2+）  
  
##   
  
**工具安装**  
  
  
##   
  
由于该工具基于Go开发，因此我们首先需要在本地设备上安装并配置好Go v1.23.2+环境。  
  
  
广大研究人员可以直接使用下列命令将该项目源码克隆至本地：  
```
git clone git clone https://github.com/Velocidex/velociraptor.git
```  
```
```  
  
  
然后切换到项目目录中，使用下列命令构建源码：  
```
$ cd velociraptor

$ cd gui/velociraptor/

$ npm install

$ make build

$ cd ../..

$ make

$ make linux

$ make windows
```  
  
为了在 Linux 上构建 Windows 二进制文件，您需要 mingw 工具。  
在 Ubuntu 上，这很简单：  
```
$ sudo apt-get install mingw-w64-x86-64-dev gcc-mingw-w64-x86-64 gcc-mingw-w64
```  
```
```  
  
**工具使用**  
  
  
##   
### 快速启动  
  
****```
$ velociraptor gui
```  
  
这将启动 GUI、前端和本地客户端。  
您可以像往常一样从客户端（仅在您自己的机器上运行）收集工件。  
###   
### 本地运行 Velociraptor  
  
  
Velociraptor 也可用作本地分类工具。您可以使用 GUI 创建一个独立的本地收集器：  
> 1、按上述方法启动 GUI ( velociraptor gui)。  
> 2、选择Server Artifacts侧边栏菜单，然后Build Collector。  
> 3、选择并配置您想要收集的工件，然后选择选项Uploaded Files并下载您的自定义收集器。  
  
##   
  
**许可证协议**  
  
  
##   
  
本项目的开发与发布遵循  
GNU AFFERO GPL v3  
开源许可协议。  
##   
  
**项目地址**  
  
  
##   
  
**Velociraptor**：  
  
https://github.com/Velocidex/velociraptor  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊  
】  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ61icYlLmBLDpdYEZ7nIzpGovpHjtxITB6ibiaC3R5hoibVkQsVLQfdK57w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
> https://docs.velociraptor.app/  
  
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651302087&idx=1&sn=29d91904d6471c4b09f4e574ba18a9b2&chksm=bd1c3a4c8a6bb35aa4ddffc0f3e2e6dad475257be18f96f5150c4e948b492f32b1911a6ea435&token=21436342&lang=zh_CN&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651302006&idx=1&sn=18f06c456804659378cf23a5c474e775&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
