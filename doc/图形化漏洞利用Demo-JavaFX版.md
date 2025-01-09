#  图形化漏洞利用Demo-JavaFX版   
yhy0  实战安全研究   2025-01-09 01:00  
  
## 这是个嘛？  
  
  
这是一个构建图形化漏洞利用的一个项目，已经写好架子，只需要往里填充exp即可，帮助安全人员快速构建一个图形化的、跨平台的漏洞利用工具。  
  
虽然有很多优秀的命令行利用工具，但我觉得还是带界面的方便、直观。  
  
使用本项目，你不需要懂太多Java语言，只需要了解基本的语法，参考自带的EXP例子，即可快速开发一款**属于你自己**  
的漏洞利用工具，建立自己的漏洞利用库。  
##   
## 编写属于你的图像化漏洞利用工具  
  
#### 项目结构  
####   
```
.
├── ExpDemo-JavaFX.iml
├── logs          运行日志文件
│   ├── debug.log
│   └── error.log
├── pom.xml
└── src
    └── main
        ├── java
        │   └── fun
        │       └── fireline
        │           ├── AppStartUp.java    应用程序启动入口
        │           ├── controller    控制JavaFX图形化界面的各种显示、事件等，核心代码 
        │           │   ├── MainController.java  主界面的controller，负责切换界面和基本信息显示
        │           │   ├── OAController.java   OA漏洞利用切换界面的相关逻辑
        │           │   ├── OthersController.java  其他漏洞界面的相关逻辑
        │           │   ├── Struts2Controller.java  Struts2漏洞利用界面的相关逻辑
        │           │   └── oa      OA漏洞利用的相关逻辑
        │           │       └── OASeeyonController.java
        │           ├── core     核心代码文件夹
        │           │   ├── Constants.java   一些常量基本信息
        │           │   ├── ExploitInterface.java   exp 编写要实现的接口
        │           │   ├── Job.java    一种漏洞全部检查的类
        │           │   └── VulInfo.java
        │           ├── exp			各种 exp 实现类
        │           │   ├── apache
        │           │   │   └── struts2
        │           │   │       ├── S2_005.java
        │           │   │       ├── S2_009.java
        │           │   │       ├── S2_016.java
        │           │   │       ├── S2_019.java
        │           │   │       ├── S2_032.java
        │           │   │       ├── S2_045.java
        │           │   │       ├── S2_046.java
        │           │   │       └── S2_DevMode.java
        │           │   ├── cms
        │           │   │   └── nc
        │           │   │       └── CNVD_2021_30167.java
        │           │   ├── oracle
        │           │   │   └── CVE_2020_14882.java
        │           │   └── others
        │           │       └── CVE_2021_22986.java
        │           └── tools  工具文件夹
        │               ├── HttpTool.java  HTTP 请求封装
        │               ├── MyCERT.java    HTTPS 请求证书设置
        │               └── Tools.java     一些处理函数
        └── resources    资源文件夹
            ├── css      界面css样式表
            │   └── main.css
            ├── fxml    界面的设计文件
            │   ├── Main.fxml
            │   ├── OA.fxml
            │   ├── Others.fxml
            │   ├── Struts2.fxml
            │   ├── Weblogic.fxml
            │   └── oa
            │       ├── OA-E-office.fxml
            │       ├── OA-Kingdee.fxml
            │       ├── OA-Landray.fxml
            │       └── OA-Seeyon.fxml
            ├── img
            │   ├── sec.png
            │   └── weixin.jpg
            └── log4j.properties   日志相关设置
```  
####   
####   
#### 编写EXP  
  
  
编写EXP时，要使用 implements  
实现ExploitInterface  
接口，实现接口中的几个方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0Jb1gh2bjWyeAZApCxVw70EW25vvBEPHxRypT5KEgbS3dvKeBVA6cficIIAiadBtnEkQUT0XJCVcUQ/640?wx_fmt=png&from=appmsg "")  
- checkVUL 使用poc 检查是否漏洞  
  
- exeCMD 使用exp执行命令  
  
- uploadFile 使用命令执行 写webshell，上传文件  
  
- getWebPath 获取网站的web目录，供上传文件使用  
  
- isVul 是否存在漏洞，检查时会根据结构自动赋值，供后续调用  
  
EXP具体编写请参考 fun/fireline/exp  
 下的各种漏洞实现  
  
当编写完EXP后，转到 fun/fireline/controller  
 下对应的**xxController.java**  
文件，比如新编写了Struts2的相关漏洞，修改**Struts2Controller.java**  
的**STRUTS2**  
变量，新加入一个漏洞名称，这里对应的是图像化界面中可供选择的漏洞列表  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0Jb1gh2bjWyeAZApCxVw70yVVsEX4Ivz14l0erEGfg4dnVywfqzWibGGxIib6hyTqEwUcaYgrYvMrw/640?wx_fmt=png&from=appmsg "")  
  
之后进入和 fun/fireline/tools/Tools.java  
 的**getExploit**  
方法中新增一个**else if**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0Jb1gh2bjWyeAZApCxVw70yJSG3vSVxTgNaobgYcEhFDpcYGKa5NfDvAUaLuGPgaZzPZA4wGAa8Q/640?wx_fmt=png&from=appmsg "")  
  
编写完后，可以直接执行fun/fireline/AppStartUp.java  
类, 查看是否正常运行。  
  
开发过程中每次修改完运行前，最好将生成的**target**  
目录删除再运行  
####   
#### 部署，发布  
  
  
当一切编写完成，bug修复完毕，在项目根目录下执行 **mvn package assembly:single**  
 即可生成 **jar**  
 文件。  
  
运行使用**target目录下最大的jar文件**  
  
对方没有Java环境怎么办？  
  
使用 **mvn jfx:native**  
 命令生产对应平台的文件，比如Mac下，执行命令**mvn jfx:native**  
命令就会在 **target/jfx/native**  
 目录下生成打包后应用(win下生成exe)，带可执行文件，带 JRE 运行环境，超大，200+M。  
  
**mvn clean**  
用于清除生成的文件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0Jb1gh2bjWyeAZApCxVw70o3k9dDyI49wpJPY6wvqtUrcPn1Kaa2U1YplV9ibD3p2vqf7TUaiaBmPg/640?wx_fmt=png&from=appmsg "")  
```
作者：yhy0
原文连接：https://github.com/yhy0/ExpDemo-JavaFX
```  
  
  
