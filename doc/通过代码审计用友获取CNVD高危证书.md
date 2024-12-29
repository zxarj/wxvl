#  通过代码审计用友获取CNVD高危证书   
 进击安全   2024-12-29 01:14  
  
文章首发奇安信攻防社区   
https://forum.butian.net/share/3058  
## 环境搭建  
  
版本：用友NC65  
```
链接:https://pan.baidu.com/s/10V-1Foq6MJp82JDF3NHKxg 提取码:9496
```  
  
数据库：  
```
sqlserver 2016 https://cloud.tencent.com/developer/article/1644863
```  
  
  
操作系统：Windows2016  
  
用友系列很多，本次选择了用友NC65是一套很老的系统了  
### 用友源码安装  
  
下载百度云下载的压缩包，解压压缩包，运行setup.bat文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRwjtgLpicjyb3sd3gRuhRbO5xESj9ib5jMvEleHTfoWNtlMEMVhlJTG3A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR0r1ezrw9ibuY7dU2tURJiaFpS2CAJcLn2r8B1tmLC26tGm5ibEaVxP46g/640?wx_fmt=png&from=appmsg "")  
  
选择模块然后点击安装，建议选择全模块安装，这样功能多，漏洞也多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRV3alUXtmlKzH2ibYhbMrmEZ45EU8PwaELBucTh5micJjVWG26ibMTVZmw/640?wx_fmt=png&from=appmsg "")  
  
等待安装完成  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR3MRw8PIp8t9tLNyvoOZwPjh5eSUbAyDd4VEjWh9j5m1dfgqL38tgwA/640?wx_fmt=png&from=appmsg "")  
  
安装完成后目录（一般默认安装在C:\），运行startServer.bat 启动服务  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR7pXKpL8GTIoplMWoz5FNpic5O5icdQib8mF47wxWHNhCGDPlyeyJvpUAA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRsxmElSVgPia0PI6LFYoAuUBqHhl1qGkAAicJHjKxRCmibZoK6xWy2z50A/640?wx_fmt=png&from=appmsg "")  
  
这样用友NC本地环境就搭建后了，方便复现漏洞  
#### debug调试配置  
  
用友本身是有调试功能的，我们配置一下，在审计代码的断点调试  
  
配置文件路径：C:\yonyou\home\bin\sysConfig.bat  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR5Tq4trEicWfPm09ur4NA56ow40iayia2otXWUYhXvia4aq0BEjMiakrgicrg/640?wx_fmt=png&from=appmsg "")  
  
将下面的配置填入到虚拟机参数中，一般添加在最前面就可以了  
```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 
```  
  
这样在运行服务时监听5005端口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRruXjOfeGrMibv5vQ6woic20ibiaYJ4X66qxjoTzgFqtJ5Pfz7RSicHI6xMA/640?wx_fmt=png&from=appmsg "")  
  
IDEA配置  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRdrS1OSJjTGkHiaTsCibzlqYqxZUKHcj7LoqhjGaRxt3uLZoJDicUZ2LYA/640?wx_fmt=png&from=appmsg "")  
  
在jar中class文件下断点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRlJt8TnOIHJ4I19zQQAH6oUREoZBQmibMzE8HahzYGicbogxTtCABFevg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRI1yl6x66KriasBBQy6yqMfDol1jlT23FD6qmSJ4wLjYVHytibe1iblE9Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRH7EIkibc7Ne0aWXd9rtUKibvHj6YIhas1NtOYXWq2R9nyhy1CpNsiazxw/640?wx_fmt=png&from=appmsg "")  
### cfr批量反编译jar  
  
用友安装后的源码都是jar的，将jar都反编译出来，这样可以很好的审计代码  
  
工具地址：https://github.com/leibnitz27/cfr/releases/tag/0.152  
```
@echo off color 17  if "%1" == "" (    for /f "delims=" %%i in ('dir /s /b /a-d /o-s *.jar') do (        echo 正在反编译 %%~ni...        title 正在反编译 %%i...        java -jar cfr-0.152.jar "%%i" --caseinsensitivefs true  --outputdir "%%~di%%~pi%%~ni"        echo ----%%i已经翻反编译---    )    goto :end ) else (    title 正在反编译 %1...    java -jar cfr-0.152.jar %1 --caseinsensitivefs true  --outputdir "%~d1%~p1%~n1"    echo 反编译完成.    goto :end )  echo 反编译完成. @pause>nul  :end pause exit 
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRzHbictsgqf1ATZicUT2tKRsmmoKw8babiccjEhx0HYT97icEFskqdiaEjmQ/640?wx_fmt=png&from=appmsg "")  
  
将1.bat和cfr.jar放在一个目录，运行就批量反编译  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRhV4Rb6jE0ib3reL9Z8kEPqqlOicwkf3WLwBpK4ibwNTUlhk3uibsmgooDw/640?wx_fmt=png&from=appmsg "")  
  
等待反编译完成，代码太多需要时间有点长  
## 代码审计  
  
开始分析代码前，可以去用友官网查看历史漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRoAoYvXEgQKt2dBSFV94DuyY4QslmlToI8icWhFtFhZuI7iclZumichGHA/640?wx_fmt=png&from=appmsg "")  
  
通过这些历史漏洞，可以捡漏。  
- 因为一个接口存在漏洞，其他代码中也可能有漏洞  
  
- 避免重复挖掘，不然提交CNVD会重复，白费功夫  
  
主要讲我提交的两个sql注入workflowService，PaWfm2  
，这个系统sql注入还是很多的，只要用心都可以挖到漏洞  
### workflowService sql注入漏洞  
  
漏洞代码路径：C:\yonyou\home\modules\webimp\lib\pubwebimp_cpwfmLevel-1\nc\uap\wfm\action\WorkflowService.java  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRGgpzbpr00KvTUD6h1xEuT08F3qo0O6Iia89GkXbUz9bV7myRhkic0Kww/640?wx_fmt=png&from=appmsg "")  
  
在WorkflowService  
类中，将proDefPk  
参数传入getWfmXmlByPk  
方法  
  
跟进getWfmXmlByPk方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRNl3eaXzIvTxAibH8Lw8ZMFibTrAobASpecFNagAFPEzNwYaHxYNZiaiabQ/640?wx_fmt=png&from=appmsg "")  
  
看到使用到了 getProDefVOByProDefPk   
带入pk参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRUQlmmXWVvAuzEezCBa5CXYGoT2VhQOlXb1ktibzGl9tTIyVjVSMmVUg/640?wx_fmt=png&from=appmsg "")  
  
getProDefVOByProDefPk  
 是 接口类IWfmProDefQry  
定义的方法  
  
在WfmProDefQry  
类实现getProDefVOByProDefPk  
方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRrIibJibCg8HN9MIJeuXsyBuXM03JhR234gA2JpcWBQ1JgL2a93ELyC2w/640?wx_fmt=png&from=appmsg "")  
```
public WfmProdefVO getProDefVOByProDefPk(String proDefPk) throws WfmServiceException {         PtBaseDAO dao = new PtBaseDAO();         SuperVO[] superVos = null;         try {             superVos = dao.queryByCondition(WfmProdefVO.class, "pk_prodef='" + proDefPk + "'");         }         catch (DAOException e) {             WfmLogger.error((String)e.getMessage(), (Throwable)e);             throw new LfwRuntimeException(e.getMessage());         }         if (superVos == null || superVos.length == 0) {             return null;         }         return (WfmProdefVO)superVos[0]; } 
```  
  
getProDefVOByProDefPk  
该方法 直接将proDefPk   
参数 传入dao.queryByCondition   
查询  
#### PtBaseDAO类中 queryByCondition 方法下断点  
  
开启调试查看proDefP传入数据库， dao.queryByCondition  
 连接数据库查询  
  
D:\CodeQL\databases\nc\home\modules\webbd\lib\pubwebbd_pubLevel-1.jar!\nc\uap\cpb\persist\dao\PtBaseDAO.class  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR8jdwUy9TCXGeeGzpTrWvrasZeAZ3t4QjVEciaic2ibbtXS0xCDQGPC8eQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRM18XLvHZDYp3vX1LiaOiaMvn2Eb31WcRbsjHSduwfpyEEogy1ooNUibKg/640?wx_fmt=png&from=appmsg "")  
  
可以看到 sql语句 查询pk_prodef字段是使用'  
闭合了sql，导致注入漏洞 strWhere = (isnull(dr,0)=0) and pk_prodef='11';waitfor delay '0:0:4'--'  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRCjpLHMHSXPR75jiaonS4YFS0Cw7cbvribKLicFMHpQ3q7B3icCwNCCjALg/640?wx_fmt=png&from=appmsg "")  
  
注：提交sql注入给CNVD 需要跑出数据库名称等，不然会被打回。  
### PaWfm2 sql注入漏洞  
  
PaWfm2 注入的原理和 workflowService都是使用了 getProDefVOByProDefPk  
导致sql注入漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR9RiaqoApdH9snZWBBdwibibjicIom8BSutaibfRB1F849LmUsKju7wvaJSw/640?wx_fmt=png&from=appmsg "")  
  
在代码的54行中，使用了getProDefVOByProDefPk   
方法来查询，该方法实现类为WfmProdefVO  
  
WfmProdefVO proDefVo = WfmServiceFacility.getProDefQry().getProDefVOByProDefPk(proDefPk);  
  
跟踪WfmProdefVO  
类实现的getProDefVOByProDefPk  
方法  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRxHNC0xJnBwPbCnVGYEOX7vmgJnCjuPtZUAVH0mrAmnmfWFMKftgdVQ/640?wx_fmt=png&from=appmsg "")  
  
getProDefVOByProDefPk   
方法 代码  
```
    public WfmProdefVO getProDefVOByProDefPk(String proDefPk) throws WfmServiceException {         PtBaseDAO dao = new PtBaseDAO();         SuperVO[] superVos = null;         try {             superVos = dao.queryByCondition(WfmProdefVO.class, "pk_prodef='" + proDefPk + "'");         }         catch (DAOException e) {             WfmLogger.error((String)e.getMessage(), (Throwable)e);             throw new LfwRuntimeException(e.getMessage());         }         if (superVos == null || superVos.length == 0) {             return null;         }         return (WfmProdefVO)superVos[0]; } 
```  
  
getProDefVOByProDefPk  
该方法 直接将proDefPk   
参数 传入dao.queryByCondition   
查询  
#### PtBaseDAO类中 queryByCondition 方法下断点  
  
开启调试查看proDefP传入数据库， dao.queryByCondition  
 连接数据库查询 D:\CodeQL\databases\nc\home\modules\webbd\lib\pubwebbd_pubLevel-1.jar!\nc\uap\cpb\persist\dao\PtBaseDAO.class  
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgR8jdwUy9TCXGeeGzpTrWvrasZeAZ3t4QjVEciaic2ibbtXS0xCDQGPC8eQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRM18XLvHZDYp3vX1LiaOiaMvn2Eb31WcRbsjHSduwfpyEEogy1ooNUibKg/640?wx_fmt=png&from=appmsg "")  
  
可以看到 sql语句 查询pk_prodef字段是使用'  
闭合了sql，导致注入漏洞 strWhere = (isnull(dr,0)=0) and pk_prodef='11';waitfor delay '0:0:4'--'  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRV2ibOCoP81g6dubL9McHGEIuhoalxfR6GxQYYzcbZ6Gaffa0RbGQhXQ/640?wx_fmt=png&from=appmsg "")  
  
提交了三个漏洞，重复了一个，两个高危  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRUTHnU3YibqxS6lqSNZNM5WcGJsfTiax9uUhFBw9JLbdWm7Zib2jkexMSA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz5F94KbibWuOicxEpqn7XVcgRXKKDw2hfT6ibpwyLLQ51lRNnzRmMtzSTQZPyPKnsjeXr1Q8vYJsmElg/640?wx_fmt=png&from=appmsg "")  
## 总结  
- 漏洞本身没有多少技术含量，但是总归收获了用友的高危漏洞证书。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZRKuxIKRyhXhuxbCGecu4ibia3kSXD8ePQHrSvPSNtC7PmjzQwR88Hu0LpuXdQzamKBCPAXX82anLS8f0FF3LzzQ/640?wx_fmt=jpeg "")  
  
  
