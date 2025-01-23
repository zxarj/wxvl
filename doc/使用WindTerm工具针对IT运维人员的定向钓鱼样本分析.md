#  使用WindTerm工具针对IT运维人员的定向钓鱼样本分析   
戎码安全  冲鸭安全   2025-01-23 11:58  
  
近期，戎码安全运营团队捕获到一批针对IT运维人员和技术支持人员的攻击样本。通过详细分析，确认此样本攻击目标明确，无多余操作，攻击手法无繁琐堆叠，是典型的定向钓鱼攻击案例。  
  
  
鱼叉式网络钓鱼（Spear Phishing），一种高度针对性的攻击方式，攻击者会根据目标人物的特点、兴趣和工作环境来定制攻击手段和样本构造，因其精准和隐蔽而备受不法分子青睐。此次捕获到的是针对IT运维人员和技术支持人员的定向钓鱼样本，其通过对开源工具WindTerm主进程的伪造，通过远程加载PE和shellcode的方式进行窃密攻击，随后启动正常的应用程序。戎码翼龙AI原生NG-EDR 凭借其先进的威胁检测算法和实时监控能力，以及对最小异常行为的高度敏感性，成功识别并记录到了该威胁事件。  
  
  
  
**样本概述**  
  
  
WindTerm是一个开源的SSH/Telnet/Serial/Shell/Sftp 客户端连接工具，此次定向攻击对象为面向软件/互联网/运维等计算机相关技术从业者。  
  
  
####   
  
**样本文件**  
  
####   
  
下图左边为正常的应用程序，右边为攻击样本，其中目录有两个很显眼的特点非常可疑  
  
- 攻击样本(右图)中多了exe1_unpack.exe文件，并且为隐藏(这个文件是样本执行后产生的)；  
  
- 攻击样本(右图)中主程序WindTerm.exe 文件大小为20m，正常的程序仅为10m，大了一倍；  
  
  
  
**正常程序**  
  
  
**攻击样本**  
  
###### 样本文件exe1_unpack.exe 程序：  
  
exe1_unpack.exe 这个pe文件虽然是隐藏的，但是其大小与正常windterm的主程序大是相同的，对其两个pe文件简单对比就可以发现这个程序就是原本的主程序，hash是完全相同的；  
  
  
  
尝试直接执行exe1_unpack.exe，windterm主程序正常执行；  
  
##### 样本文件WindTerm.exe主程序  
  
  
时间戳被故意修改，在PE文件的解析中，编译器为Golang，而其github languages中并不包含golang的相关内容。  
  
  
综合上述内容，可初步推断WindTerm.exe 有较大可疑点。  
  
  
**静态分析**  
  
####   
  
**初始化阶段：**  
  
程序启动后，首先调用 os_Executable 来获取自身EXE的文件路径；  
  
  
调用 main_ReadEncExeData 来读取内嵌于自身EXE的文件末尾中的其他数据；  
  
**数据格式如下：**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qYNuQBhCJydkZz8RWyVnohCCZsxp24s5lHibuib4cBAGeVicibMc3EpZxiaWSGhuxUqNDRKeAnrv3hVLLhHjH7xoLHA/640?wx_fmt=png&from=appmsg "")  
  
**EncExeData 的结构如下：**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qYNuQBhCJydkZz8RWyVnohCCZsxp24s5OrW8e2MIM4Q2HRibkc2GRDpMKIw7CzZZnlUkjlhJSFsMlXzO0DmHbNA/640?wx_fmt=png&from=appmsg "")  
  
EncExeData 被读取到局部变量中，用于后续使用  
  
  
KeyData 被读取到了 result.arr[24]  
  
函数执行完毕以后返回给调用者：  
  
  
Exe2Data 被读取到了 result.arr[12]  
  
函数执行完毕以后返回给调用者：  
  
  
Exe1Data 被读取到了 result.arr[0]  
  
函数执行完毕以后返回给调用者：  
  
  
Exe2Data 被读取到了 result.arr[12]  
  
函数执行完毕以后返回给调用者：  
  
  
Exe1Data 被读取到了 result.arr[0]  
  
函数执行完毕以后返回给调用者：  
  
  
当 main_ReadEncExeData 执行结束以后，  
  
便会对 Exe1Data 和 Exe2Data 进行解密：  
  
  
  
解密完以后，调用 main_UnpackAndRunGUI 将 Exe1Data 写出一个隐藏的文件 exe1_unpack.exe 然后运行，然后调用 main_ManualMapPE 和 main_ExecutePEEntry 内存加载 Exe2Data：  
  
  
至此 WindTerm.exe 的任务算是结束了，使用创建进程启动了 Exe1Data 写出的 exe1_unpack.exe，它是原本的 WindTerm.exe，可以正常使用，让用户认为自己使用的是真正的WindTerm。而我们接下来需要关注的是被 main_ManualMapPE 执行的 Exe2Data。  
  
**攻击实施阶段：**  
  
我们将 Exe2Data 解密后的数据 Dump 到文件，命名为 exe2_unpack.exe，发现它依旧是一个Go语言编写的程序，反编译以后，我们可以看到这两个函数：  
  
- goshellcodeloader_bookmark_Bookmark_Parse  
  
- goshellcodeloader_goolepws_Goole  
  
  
  
然后我们在函数列表搜索关键字 goshellcodeloader，会发现以下函数：  
  
  
  
我们可以非常轻易的看出这是在窃取浏览器数据信息，从 goshellcodeloader_goolepws_Goole 函数中，我们可以进一步的发现它窃取的浏览器信息包括但不限于Chrome，Edge，360Chrome，360ChromeX，Brave，Opera，Vivald，CocCoc，QQBrowser，YandexBrowser，Sogou 等。  
  
  
在 goshellcodeloader_goolepws_ProcessBrowserData 函数中，我们可以看到它将浏览器的数据发送。  
  
  
在 goshellcodeloader_bookmark_SendDataToPHPScript 函数中，我们可以看到它将书签栏的数据发送。  
  
  
发送浏览器数据的同时还会发送Host信息。  
  
  
这个Shellcode会通过 CreateFileMapping 和 MapViewOfFile 映射到内存中，并且通过 TpAllocWork 和 TpPostWork 进行执行，从而绕过栈回溯检测。  
  
**动态分析**  
  
  
**在当前目录下创建一个exe1_unpack.exe文件，并设置为隐藏文件**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(211, 218, 230);border-image: initial;max-width: 100%;box-sizing: border-box !important;overflow: hidden;background-color: rgb(250, 251, 253);vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 9pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\xxxx\Desktop\WindTerm_2.6.1\exe1_unpack.exe</span></span></p></td></tr></tbody></table>  
**shellcode加载执行**  
  
**创建了一个异常的线程来执行shellcode**  
  
**检测到了shellcode自定位**  
  
  
**遍历大量浏览器路径，尝试窃取浏览器密码及敏感信息**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\BraveSoftware\Brave-Browser\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\Chromium\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\CocCoc\Browser\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\Google\Chrome\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\Microsoft\Edge\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;font-size: 11pt;color: rgb(0, 0, 0);"><span leaf="">C:\Users\administrator\AppData\Local\Tencent\QQBrowser\User Data\</span></span></p></td></tr><tr style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><td valign="top" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(0, 0, 0);max-width: 100%;box-sizing: border-box !important;overflow: hidden;vertical-align: top;"><p style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;clear: both;min-height: 1em;text-align: left;"><span data-type="text" style="-webkit-tap-highlight-color: transparent;margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span leaf="">. . . . . .</span></span></p></td></tr></tbody></table>  
**(该模拟行为中仅安装了Edge浏览器)**  
  
**在内存中加载PE文件**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qYNuQBhCJydkZz8RWyVnohCCZsxp24s5jo9LO0q7mjfBnz4WI2ACuU12gViaxlprV7IQXPbFHbLECXsISmcMDAA/640?wx_fmt=png&from=appmsg "")  
  
**访问互联网，对获取到的信息进行回传**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qYNuQBhCJydkZz8RWyVnohCCZsxp24s5o5CiboBODqicCiccgHMkfCjvTjR9G4xOVLC3sR5QFf5G9dQpzibAhloRmw/640?wx_fmt=png&from=appmsg "")  
  
**执行完上述所有行为后，启动正常的应用程序exe1_unpack.exe(被隐藏)**  
  
  
  
**进程树**  
  
  
  
**ATT&CK**  
  
  
**戎码AI攻击分析报告**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/qYNuQBhCJyeOvsaVA8eJ1CCQYY2PZm963L5CnmGpH4A4ytkMWAciaX2AJibko4icE8bIDqHZudZcamsEqtp7PvysA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1&wx_co=1 "")  
  
  
关于此次事件，戎码翼龙AI产出的攻击分析报告。  
  
  
此报告节选自戎码翼龙AI生成的攻击分析报告（全文报告共计17页）。**戎码翼龙利用先进的****生成式AI，****一键输出攻击分析报告，有效解决告警不易读、高级威胁研判慢、易漏报等关键难题。**  
其核心优势在于，整个分析过程完全自动化运行，无需任何人工介入，即可实时生成并导出详尽、结构化的威胁分析报告，对各类网络攻击行为进行深度剖析。  
  
该报告能够精准揭示攻击者深藏的战略意图与所采用的战术手段。通过全方位、多层次的上下文关联与深度溯源分析，完整重现了攻击事件的发生过程，精准勾勒出攻击活动的全貌。在此过程中，戎码翼龙AI原生NG-EDR系统发挥了关键作用，构建了一幅从动机识别直至攻击路径逆向解析的全景视图。此视图以高度可视化方式呈现，赋能用户在纷繁复杂的网络环境中精准洞悉安全态势，迅捷制定并执行有效的防护策略，为应对各类复杂攻击情形提供强有力的决策支撑！  
  
  
