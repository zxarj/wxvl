#  EmbedPayloadInPng：一款图片文件Payload嵌入工具   
Alpha_h4ck  FreeBuf   2024-11-25 11:03  
  
##   
  
  
**关于EmbedPayloadInPng**  
  
  
  
EmbedPayloadInPng是一款功能强大的Payload嵌入工具，该工具能够将Payload拆分为多个IDAT部分，并将Payload数据嵌入到PNG图片文件中。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVTOT1MicSJQ5ics3wfIUWPMqtqPRLponJjacg2b8dwqDKpFx1G6tRaVAg/640?wx_fmt=png&from=appmsg "")  
  
  
值得一提的是，EmbedPayloadInPng拆分的IDAT的每一段数据都会使用自己的 16 字节密钥和 RC4 加密算法单独加密。  
##   
  
**工具组成**  
  
  
  
当前版本的EmbedPayloadInPng由两个组件组成：  
> EmbedPayloadInPng.py- Python脚本负责将输入的Payload嵌入到指定的 PNG 文件中。  
> FetchPayloadFromPngEmbedPayloadInPng.py- 负责从输出的 PNG 文件中提取Payload，并使用ExtractDecryptedPayload函数对其进行解密。  
  
  
**嵌入式PNG文件结构**  
  
  
  
如前所述，EmbedPayloadInPng.py负责将Payload嵌入 PNG 文件。下面是嵌入Payload的 PNG 文件的结构：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVeja75aHDm0zlyBicppB6HPoHvUMHs0qT6ia3ebJ04ey9HAkIm8LPo6TA/640?wx_fmt=png&from=appmsg "")  
  
由于一个IDAT部分的最大大小为 8192 字节，因此我们的Payload被分成多个IDAT部分。每个部分的大小相当于(8192 - 16 [RC4 密钥长度])。此外，最后一个IDAT部分将包含Payload的剩余字节。  
  
  
下面给出的是EmbedPayloadInPng.py的输出并将其与创建的 PNG 文件的结构进行了比较。  
输出 PNG 文件部分  
：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVG7iatyNGibmr4nR0SJ47ttCgpmuibf4R11zUs6fookX3Rd9nqXloicIWLg/640?wx_fmt=png&from=appmsg "")  
  
随机 IDAT 部分，用于标记Payload的开始位置。此部分的 CRC 哈希值在该项目的 C 代码中用于标识PNG 文件中Payload的开始位置：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVxEuh9PicDW8FYwRsEjuAocQkBR9lFicL6k5aHzHzEx7s9HMxa8erMvtQ/640?wx_fmt=png&from=appmsg "")  
  
第一个Payload的IDAT部分，紧随随机部分之后（蓝色部分）。此图还展示了 CRC 哈希的位置以及之前随机化 IDAT 部分的大小（黄色部分）：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVTE6necwfyujjXxMF055sDl5xB1Iqbn3YYKsSREicqicNAyfr5dc8MCtQ/640?wx_fmt=png&from=appmsg "")  
  
第一个Payload的IDAT 部分的 CRC 哈希值，位于Payload加密的第一个块后面的部分末尾：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVWzfn3ggIKUXHgqIQ6lHnNqic82DNUNRd4Zlpauz07YZ4oyDeaj4wPxQ/640?wx_fmt=png&from=appmsg "")  
  
第二个Payload的IDAT 部分的起始位置：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVG3dRPxgVznFaHvBfh2nC5nQHHX9hNFrN2mlUxw1EUxMuxuQdwnoKkw/640?wx_fmt=png&from=appmsg "")  
  
**工具安装**  
  
  
  
由于该工具基于Python 3开发，因此我们首先需要在本地设备上安装并配置好最新版本的Python 3环境。  
  
  
接下来，广大研究人员可以直接使用下列命令将该项目源码克隆至本地：  
```
```  
  
**工具使用**  
  
  
  
  
  
使用EmbedPayloadInPng.py创建嵌入Payload的PNG文件：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdPz7zXnRq2Vrwy5aC3nPVicMEYgPCoXaDoRBP7hHKm9ib1vjf2ZGlWibee97yBz4EzhPRnQoBCGPQw/640?wx_fmt=png&from=appmsg "")  
  
  
  
嵌入Payload的PNG文件名为Output.png跟源文件对比是相同的。  
  
  
**许可证协议**  
  
  
  
  
本项目的开发与发布遵循  
MIT  
开源许可协议。  
  
  
**项目地址**  
  
  
EmbedPayloadInPng  
：【  
GitHub传送门  
】  
  
  
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
> https://maldevacademy.com/?ref=gh  
>   
>   
>   
>   
>   
>   
>   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](http://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307635&idx=1&sn=63635c9ba9b91d7fb1b4c07ca89098c0&chksm=bd1c2cf88a6ba5ee8bbced7c67456ee2a77e68082585d9e4e2977b2c6c8d8eb7d1d9d6f6d209&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
