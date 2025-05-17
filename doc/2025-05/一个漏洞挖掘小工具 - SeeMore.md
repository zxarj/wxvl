#  一个漏洞挖掘小工具 - SeeMore   
 马哥网络安全   2025-05-17 09:00  
  
介绍  
  
1、在某系统发现在导入文件时，文件内容没有进行过滤导致存储型xss注入，可以发送任何人或提交模板（管理员会审查）危害挺大的，然后提交漏洞后他进行了修复。  
  
2、但是  
程序员只是将导入功能的元素添加"display: none;"隐藏起来了， 但是这个功能还是存在，所以可以通过将"display: none;"删除达到显示导入功能（二次绕过）。  
  
3、这里再提供一思路，在第2次修复后，程序员可能只是将页面对应的代码段删除，但是后端的api仍然存在，可以利用之前的数据包（可能需要修改Cookie） 进行重放攻击。  
  
但是如果每次都要去手动修改不可见元素为可见就太麻烦了，还可能错过一些可利用的功能点，所以就做了这个插件可以显示隐藏的可点击（重点）元素，不会将一些无用的文本弹窗等显示出来造成页面的不美观，下面讲讲这个插件的应用场景以及安装方法。  
  
如果大家在使用过程中遇到了bug或一些没有成功显示的元素，可以提交到issues中，作者会尽快完善匹配规则，感谢大家支持。  
  
使用  
  
  
1、这里以Webgoat靶场为例  
  
![PixPin_2025-03-01_19-58-08](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqibn8yGQjgIPkSjr1oGTMIyhOdY5XRNhbxb6LwDmbB0bPrlsGEicWHm9g/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic "")  
  
2、点击 Show Hidden 即可，显示出隐藏的按钮。点击 recover 即可恢复之前的页面。  
  
![PixPin_2025-03-01_20-00-28](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqBaibq3BDGbmEyxiajVJhlIde9b4pBvxqHdmVTYCXqpibm0ed4WHzOI5Sg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
3、安装教程，Google 打开 chrome://extensions/ 链接，开启开发者模式，点击"加载以解压的扩展程序"，选择下载解压后的文件夹导入即可。  
  
![PixPin_2025-03-01_20-02-55](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqtSbZ4MwNrb7AzR1BE2Bicc6fia4KvfH1Lch3micgY7M7QmvZ9iaVFibSELA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
![PixPin_2025-03-01_20-03-24](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqZKeLbtczXQvDb11Ms0eqp7ic8F6TjK6vBIjOqjLhFAH72Je4d24BZEg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
#### V1.0.1更新  
  
  
1、添加显示通过 <!-- 注释隐藏起来的可点击内容，这个页面存在隐藏的功能框  
  
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqeVPsxUtmicBDzGVNAdaVg2cbibfHaAsBvgyzEIoe9ic67cCVb1ffNmAqA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
2、点击 Show Hidden 显示功能  
  
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aqzDuQ2ecx2uic9zlLV7ejicjg3FpSydNYhmo2l53bljgZiakCK34ARu8FA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
#### v1.0.2更新  
#### 修复部分bug（注释功能）  
#### 案例补充  
  
  
发现上传功能，可以上传任意后缀但是对于大多数文件不解析，但可以解析html文件  
  
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgFSE34z9hic3a9MXRI1HI2aq1wtkxIP8sbh57zk0QjaYo0Hiadg3r3P3qyK6srAoEF3osMwUTd4NUZQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
项目地址  
  
**https://github.com/Bbdolt/SeeMore**  
  
  
  
想学硬核网安技术？一定不要错过这次训练营！  
  
get 攻防实战能力！  
  
✅教你搭建 vmware 与 kali 虚拟机  
  
✅掌握 metasploit 生成木马技巧  
  
✅深度解析木马原理与防御  
  
✅带你从工具搭建到实现远程控制  
  
🔥5.21-22晚8点，网安大佬亲自指导，  
  
轻松 get 攻防实战能力，扫码立刻报名！  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkwcjtOtVXODCkPibWO4Py9F7ff0EOvVVMIUmrCUMRGAG5Q07ZjpSjiaIk5DB5LK8ePbsESVR1s3LBA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
