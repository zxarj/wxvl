#  CABED：一款针对Chrome应用程序绑定数据的加密解密工具   
Alpha_h4ck  FreeBuf   2024-12-06 11:54  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
**关于CABED**  
  
  
## CABED是一款针对Chrome应用程序绑定数据的加密解密工具，该工具全称为Chrome App-Bound Encryption Decryption，在该工具的帮助下，广大研究人员可以使用具有路径验证和加密保护的 IElevator COM 接口来加密或解密 Chrome 127+ 中的应用程序绑定加密密钥。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38G1nYUFhMulWK7EEiadWOtSickISHUQ9NoMCQL3gFjqElaTtJibLFDBzEzudD6c8ava8lIXmKXztbtg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Chrome 版本 127 中引入的 ABE 将解密功能绑定到特定应用程序，以防止未经授权访问敏感数据（例如 Cookie）（以及将来可能出现的密码和付款信息）。而CABED可解密存储在受支持的基于 Chromium 的浏览器（包括Google Chrome、Brave 和 Microsoft Edge ）的本地状态文件中的应用绑定加密 (ABE)密钥，其功能基于COM 的IElevator服务来检索和解密这些密钥。  
##   
  
**支持的浏览器**  
  
  
> 1、Google Chrome (130.0.6723.91)  
> 2、Brave (1.71.118)  
> 3、Microsoft Edge (130.0.2849.56)  
  
##   
  
**工具要求**  
  
  
##   
> 1、操作系统：Windows  
> 2、构建工具：Microsoft Visual Studio C++ 或兼容编译器（例如 MSVCcl命令）  
> 3、需要以下库：ole32.lib、oleaut32.libs、hell32.lib、version.lib、comsuppw.lib  
  
##   
  
**工具安装**  
  
  
##   
  
广大研究人员可以直接使用下列命令将该项目源码克隆至本地：  
```
git clone https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption.git
```  
```
```  
##   
  
**工具使用**  
  
  
##   
  
使用一款C++编译器对项目代码进行编译和构建：  
```
cl /EHsc chrome_decrypt.cpp oleaut32.lib shell32.lib advapi32.lib shlwapi.lib
```  
```
```  
  
由于Chrome ABE中固有的路径验证约束，因此需要将编译后的可执行文件放置在Chrome应用程序目录中（例如，C:\Program Files\Google\Chrome\application），然后从命令行运行可执行文件：  
```
PS C:\Program Files\Google\Chrome\Application> .\chrome_decrypt.exe chrome

PS C:\Program Files\BraveSoftware\Brave-Browser\Application> .\chrome_decrypt.exe brave

PS C:\Program Files (x86)\Microsoft\Edge\Application> .\chrome_decrypt.exe edge
```  
```
```  
  
**工具运行演示**  
  
  
##   
```
PS C:\Program Files\Google\Chrome\Application> .\chrome_decrypt.exe chrome

----------------------------------------------

|  Chrome App-Bound Encryption - Decryption  |

|  Alexander Hagenah (@xaitax)               |

----------------------------------------------

 

[+] Found Chrome Version: 130.0.6723.91

[*] Starting Chrome App-Bound Encryption Decryption process.

[+] COM library initialized.

[+] IElevator instance created successfully.

[+] Proxy blanket set successfully.

[+] Retrieving AppData path.

[+] Local State path: C:\Users\ah\AppData\Local\Google\Chrome\User Data\Local State

[+] Base64 encrypted key extracted.

[+] Finished decoding.

[+] Key header is valid.

[+] Encrypted key retrieved: 01000000d08c9ddf0115d1118c7a00c04fc297eb...

[+] BSTR allocated for encrypted key.

[+] Decryption successful.

[+] DECRYPTED KEY: a5e700d6cfb16beee5e9c198789f5cd2d2b5d2debe648fe578a7504a638dc186

```  
##   
  
**项目地址**  
  
  
##   
  
**CABED**：  
  
  
https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption  
##   
  
  
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
  
> https://security.googleblog.com/2024/07/improving-security-of-chrome-cookies-on.html  
> https://drive.google.com/file/d/1xMXmA0UJifXoTHjHWtVir2rb94OsxXAI/view  
> https://x.com/snovvcrash  
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
>   
>   
>   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icEEJemUSFlfufMicpZeRJZJ7JfyOicficFrgrD4BHnIMtgCpBbsSUBsQ0N7pHC7YpU8BrZWWwMMghoQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651307029&idx=1&sn=809e704f3bd356325cf8d85ed0717a8d&chksm=bd1c2e9e8a6ba788529249c685d4979c6b11853cf8f2d798a6d8e9ce362926ec50e3639cf79f&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651308240&idx=1&sn=96d32c8e6fa90561c84164ed75f4dca0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
