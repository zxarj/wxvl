#  直播课时更新-系统0day安全（第7期）   
看雪课程  看雪学苑   2025-04-07 18:00  
  
直播课更新：  
  
  
直播课8：httpd通用中间件框架逆向分析思路及漏洞案例分析-2  
  
https://www.kanxue.com/book-140-5320.htm  
  
  
  
近些年来不论是HVV行动还是各种红蓝对抗中，边界设备或者企业级网络设备被当作是进入内网的最快目标，因此对于这些类型的设备安全问题开始越来越被广泛关注，掌握此类设备的漏洞挖掘方法和渗透思路能够能提升你的实战技能并让你你在实战对抗中更加游刃有余。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibicvVumEAtfUlgP9LlbuWO6trfpetV4lzTOM81XibzznNaa4Caah83iaDg/640?wx_fmt=jpeg&from=appmsg "")  
  
限时优惠：¥21000  
  
深入探索IoT/网络设备漏洞挖掘的奥秘  
  
  
**·**  
  
  
**课程简介**  
  
  
本课程专注于IoT和企业级网络设备固件漏洞分析与挖掘。由  
资深安全专家H4lo讲师授课，课程结合丰富的实战经验和深入的技术分析，旨在全面提升学员在设备固件漏洞挖掘方面的能力。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibW3jLHicZLesaWahTIe1TQ4Pc9VKWNsVu4uPBJ8rFCvjZtK4qwl9WLCA/640?wx_fmt=png&from=appmsg "")  
  
  
课程内容涵盖了**固件安全基础、固件/镜像获取与处理、固件加密/解密、固件仿真与调试、漏洞挖掘与分析**等多个方面。  
全方面多纬度介绍关于各类嵌入式设备、网络设备、边界安全设备等漏洞挖掘基础、方法、技巧和思路，课程帮助学员掌握企业级网络设备的逆向分析方法，提升个人竞争力。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4LpfCkoXn5ugG5deKNeNPTYRpfIWJBnh0wmBccVNke95oicVbk4ibRibrQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
**·**  
  
  
**讲师介绍：H4lo（ID）**  
  
  
专注IoT/网络设备漏洞方向挖掘，发现多个知名厂商的严重设备固件安全漏洞，涵盖   Cisco、Fortinet、Netgear、Draytek、Sonicwall 等品牌，在天网杯、强网拟态、补天杯等漏洞破解赛中取得优异成绩，Geekpwn   2020/2021名人堂。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4qXpGPwd4xvuKQs4k8c2B6MIrOMlQ9dnQwKaaocPJdo4UWQICz7nSfw/640?wx_fmt=png&from=appmsg "")  
  
  
  
**·**  
  
  
**课程目录（上下滑动查看）**  
  
  
**第一章 固件安全基础**  
  
本章节介绍固件安全的基础概念以及针对固件漏洞挖掘需准备的一些基本环境的安装和使用。  
  
  
1.1固件安全概述  
  
介绍固件安全的内容以及固件安全研究的范畴  
  
  
1.2固件/镜像定义和介绍  
  
固件和镜像的基本概念介绍，以及运行的环境、原理等做一个综述。如针对固件中，linux内核操作系统的固件和RTOS操作系统的固件分别做一些简单的介绍（从内核、操作系统、逆向分析角度）  
  
针对镜像中，分别对ISO格式、ova/ovf格式的镜像做一下简单的介绍。  
  
  
1.3软件环境准备  
  
本机准备的一些软件环境，以及外部硬件设备、软硬件工具等准备。  
  
1.3.1软件环境安装  
  
binwalk、gdb、交叉编译buildroot等软件环境的安装。  
  
1.3.2交叉编译介绍和编译  
  
交叉编译中uclibc、uclibc-ng等的介绍  
  
  
1.4硬件环境准备  
  
1.4.1基本硬件工具使用  
  
电烙铁、热风枪、编程器等工具的准备和使用。  
  
1.4.2硬件调试口使用  
  
UART、JTAG、SWD调试口的判断和使用  
  
  
**第二章 固件/镜像获取与处理**  
  
本章节介绍漏洞研究环境或者固件/镜像的获取以及处理方法。  
  
  
2.1固件/镜像环境获取  
  
介绍如何获取漏洞挖掘环境，以及一些技巧  
  
包括官网下载、第三方市场购买、云市场下载、抓取升级包、硬件提取等方法  
  
2.1.1固件/镜像获取的几种方法  
  
介绍常规的思路获取环境的几种方法  
  
案例：官网下载、第三方市场购买、云市场下载、抓取升级包  
  
2.1.2硬件方式提取固件  
  
介绍如何从硬件中提取固件和镜像  
  
案例1：sop8、tsop8芯片的固件提取  
  
案例2：emmc、sop48芯片的固件提取  
  
案例3：UART调试口获取固件  
  
  
2.2固件/镜像的解压  
  
介绍如何使用binwalk进行固件解压以及从镜像中如何提取出待分析的二进制、脚本文件  
  
2.2.1常规方式固件提取  
  
介绍binwalk -e一把梭固件提取的方法  
  
案例1：常规的squashfs文件系统固件  
  
2.2.2镜像磁盘挂载文件提取  
  
案例2：ext3/ext4镜像挂载磁盘提取固件  
  
2.2.3其他案例  
  
案例3：vxwork固件程序提取  
  
  
2.3固件/镜像分析  
  
介绍拿到解压处理的环境之后，如何进行分析以及一些相关技巧  
  
2.3.1镜像常见架构分析  
  
如底层用的是什么操作系统（freebsd/centos等）、Bios、内核启动方式，主程序服务启动的方式等  
  
2.3.2固件信息分析  
  
介绍分析二进制和脚本代码的整体分析思路和分析步骤  
  
全局代码分析、敏感功能点审计  
  
2.3.3固件修改和重打包  
  
介绍如何通过修改固件的方式，获得固件的底层shell权限等。包括不同类型的固件、镜像如何重打包  
  
案例1：乔安摄像头固件后门植入  
  
案例2：fortigate固件后门植入  
  
  
**第三章 固件加密/解密与通信加解密**  
  
3.1常见固件加密方式  
  
介绍常见的几种固件加密手段和方法  
  
3.1.1简单混淆加密  
  
对固件头、固件签名等进行魔改  
  
3.1.2版本迭代加密  
  
Dlink设备的版本迭代加密方式，即由非加密转变到加密过程的步骤解密。  
  
3.1.3密钥加密  
  
对称加密和非对称加密的固件加密方式  
  
案例1：天融信topacm oem方式的aes加密  
  
  
3.2固件解密思路  
  
根据上述介绍常见固件的解密思路提供具体的实战案例  
  
ruijie固件解密  
  
topsec固件解密  
  
nsfoucs固件解密  
  
  
**第四章 固件仿真与调试**  
  
4.1 固件仿真常见方法  
  
qemu在固件模拟中的使用方法  
  
  
4.2 Qemu工具调试方法  
  
使用qemu进行固件模拟或者程序模拟的调试方法以及相关的调试技巧  
  
  
4.3 环境调试  
  
介绍环境调试的相关方法  
  
4.3.1 软件镜像环境调试  
  
案例1：模拟initrd镜像解密，luks密钥解密  
  
案例2：通过gdb调试vmware虚拟机内核拿shell  
  
4.3.2 硬件环境调试  
  
案例1：硬件设备调试进uboot获取shell  
  
案例2：通过硬件故障注入步骤进uboot  
  
  
**第五章 固件漏洞挖掘与分析**  
  
5.1认证绕过漏洞  
  
描述认证绕过漏洞的概念和基本原理  
  
5.1.1认证机制介绍  
  
网络设备中常见的几种认证方式  
  
passwd认证  
  
数据库认证  
  
token  
  
saml认证  
  
5.1.2认证绕过案例和复现思路  
  
认证绕过的常见案例和复现思路  
  
  
5.2命令注入漏洞  
  
描述命令注入漏洞的概念和基本原理  
  
5.2.1命令注入相关概念  
  
介绍命令注入原理和发生的位置  
  
5.2.2命令注入案例和复现思路  
  
命令注入的常见案例和复现思路  
  
案例1：url直接命令注入  
  
案例2：命令执行后门  
  
案例3：物联网设备wifi密码配对命令注入  
  
  
5.3内存相关漏洞  
  
描述内存漏洞的概念和基本原理  
  
5.3.1栈溢出相关概念  
  
介绍栈溢出的原理、x86和arm/mips架构栈溢出的区别  
  
5.3.2栈溢出案例和复现思路  
  
描述栈溢出漏洞的概念和基本原理和复现思路  
  
案例1：栈溢出造成的认证绕过  
  
案例2：栈溢出覆盖返回地址的利用  
  
5.3.3堆溢出案例和复现思路  
  
描述堆溢出漏洞的概念和基本原理和复现思路  
  
  
**第六章 物联网安全之NAS设备漏洞分析**  
  
6.1 Qnap Multimedia Console漏洞分析(CVE-2023-23364)  
  
qnap中Multimedia Console组件的未授权栈溢出漏洞  
  
https://www.qnap.com/en/security-advisory/qsa-23-29  
  
6.1.1漏洞分析  
  
二进制逆向分析  
  
6.1.2漏洞利用  
  
rop  
  
6.1.3修复建议  
  
对输入的长度进行限制  
  
  
**第七章 网络安全设备漏洞分析（VPN/防火墙等）**  
  
本章选取几个经典的VPN/防火墙设备的历史CVE漏洞进行分析，覆盖镜像解压、固件解析、程序分析和漏洞挖掘等步骤。  
  
  
7.1Fortigate防火墙漏洞分析(CVE-2022-42475)  
  
2022年堆溢出漏洞,https://www.fortiguard.com/psirt/FG-IR-22-398  
  
7.1.1环境预处理及环境架构分析  
  
固件后门植入获取调试shell  
  
7.1.2漏洞分析  
  
IDA逆向代码分析  
  
7.1.3漏洞利用  
  
漏洞利用方法和rop  
  
7.1.4漏洞修复建议  
  
修复建议  
  
  
7.2Paloalto防火墙漏洞分析(CVE-2022-3064)  
  
2022年强网杯PANOS，请求走私漏洞+后端栈溢出漏洞+SUID提权漏洞  
  
7.2.1环境预处理及环境架构分析  
  
历史漏洞获取shell或者vmware镜像的gdb调试  
  
7.2.2漏洞分析  
  
请求走私调试、栈溢出分析  
  
7.2.3漏洞利用  
  
请求走私利用、栈溢出ROP、SUID提权程序分析  
  
7.2.4漏洞修复建议  
  
规范http协议处理、限制字符串长度等  
  
  
7.3sophos防火墙漏洞分析（CVE-2022-1040）  
  
json解析差异导致的认证绕过、perl代码中的命令注入  
  
7.3.1环境预处理及环境架构分析  
  
cli之后获取shell  
  
环境架构分析  
  
7.3.2漏洞分析  
  
java代码分析、perl代码分析  
  
7.3.3漏洞利用  
  
json编码、命令注入  
  
7.3.4漏洞修复建议  
  
规范json处理，过滤敏感字符  
  
  
7.4Sonciwall防火墙漏洞分析（CVE-2021-20038）  
  
前台栈溢出漏洞，https://github.com/jbaines-r7/badblood  
  
7.4.1环境预处理及环境架构分析  
  
gdb调试获取shell、架构分析  
  
7.4.2漏洞分析  
  
cgi的逆向分析思路  
  
7.4.3漏洞利用  
  
栈喷射  
  
7.4.4漏洞修复建议  
  
对字符串长度进行限制  
  
  
**第八章 企业级路由设备漏洞分析**  
  
8.1 Cisco Rv110w漏洞分析(CVE-2020-3331)  
  
https://bbs.kanxue.com/thread-271900.htm  
  
8.1.1漏洞分析  
  
栈溢出位置代码分析  
  
8.1.2漏洞利用  
  
漏洞rop利用  
  
8.1.3修复建议  
  
对字符串长度进行限制  
  
  
8.2 Cisco Rv340漏洞分析(CVE-2024-20470)  
  
8.2.1漏洞分析  
  
栈溢出位置代码分析  
  
8.2.2漏洞利用  
  
漏洞rop利用  
  
8.2.3修复建议  
  
对字符串长度进行限制  
  
  
**第九章 邮件网关漏洞分析**  
  
针对历史的一些邮件网关进行漏洞分析  
  
9.1 CoreMail邮件服务器 25端口栈溢出漏洞  
  
2023年强网杯线下漏洞案例，证书patch和栈溢出漏洞复现  
  
9.1.1证书patch  
  
9.1.2漏洞分析  
  
二进制逆向分析  
  
9.1.3漏洞利用  
  
rop  
  
9.1.4修复建议  
  
对输入的长度进行限制  
  
  
**第十章 网络设备上的漏洞挖掘高级技术**  
  
10.1 fuzzing模糊测试  
  
基于web server等协议的模糊测试等  
  
  
10.2 污点追踪  
  
污点追踪原理和使用  
  
  
10.3 基于LLM漏洞挖掘  
  
介绍使用大模型来辅助漏洞挖掘和大模型在污点追踪上的优势  
  
  
**第十一章 物联网设备rootkit相关知识**  
  
对于rootkit持久化技术在设备中的使用以及相关的防御的手段等  
  
11.1基于固件植入的方法  
  
  
11.2基于分区修改的方法  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GDKxUicIYay3UHVJ49UvwUEvSPiahTYwFEywvmxUhDqxic44h39tSicEYkicEZ88y41NIXU2q6RGQfiarQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
**·**  
  
  
**立即学习**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibSsg2PIdUXY07dcmAGke1BP17Pm5CwdRXU1sudYia0186ibs0wfl6Kpicw/640?wx_fmt=png&from=appmsg "")  
  
**限时优惠：¥21000**  
  
提升设备固件漏洞挖掘思路和方法  
  
掌握各类企业级网络设备逆向分析方法  
  
提升个人竞争力，扩宽职业道路  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibPRnSicDWUI8IFy5CAlMBvGudf05w8sYvlCIulGicbicrplAazHEZXqLBQ/640?wx_fmt=gif&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibAGMYaTFey7kLE8s8J8RibcfYSx3ZMF82KOCzKxWkqE9SBX5ibmicLUT3g/640?wx_fmt=png&from=appmsg "")  
  
**·课程咨询·**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HTh5DkjV7aH3DiaicwXmsjN4CGJxk8P11iaZZrGmGZS67HFNdxFYfljwmcaicMFJxaTXRJ36K6RQTAIg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibPRnSicDWUI8IFy5CAlMBvGudf05w8sYvlCIulGicbicrplAazHEZXqLBQ/640?wx_fmt=gif&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibMb2gCbcN9djJKuniaVu1M6UKUzibiaqnmOy6R6V0eCjpodVk0CFEMqibpw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIib2GU6n99d7fH02oh0rmf28GtZkstpK3ZNRCIFibTUb1FAkx5tSYX6iaow/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIib2GU6n99d7fH02oh0rmf28GtZkstpK3ZNRCIFibTUb1FAkx5tSYX6iaow/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIib2GU6n99d7fH02oh0rmf28GtZkstpK3ZNRCIFibTUb1FAkx5tSYX6iaow/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FewYl2MAlQHldGibTNbZaIibJC0Acx3icpySFJQMzciaTzBt9z2eMibYCXJ4LaxZkQuJMMyBA403KFp7A/640?wx_fmt=gif&from=appmsg "")  
  
点击阅读原文查看更多  
  
