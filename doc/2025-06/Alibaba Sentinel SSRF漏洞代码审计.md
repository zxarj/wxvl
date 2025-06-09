#  Alibaba Sentinel SSRF漏洞代码审计  
小瑟斯  实战安全研究   2025-06-09 02:00  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibh6AMR1JynTibCiaricvcGrwpgTycUdfvW0TyibzoleLeJvZpmKFMtZsmBQ/640?wx_fmt=jpeg&from=appmsg "")  
  
## 一、Sentinel介绍  
  
  
引用自官方介绍  
  
  
随着微服务的流行，服务和服务之间的稳定性变得越来越重要，Sentinel 是面向分布式、多语言异构化服务架构的流量治理组件，主要以流量为切入点，从流量路由、流量控制、流量整形、熔断降级、系统自适应过载保护、热点流量防护等多个维度来帮助开发者保障微服务的稳定性。  
  
  
## 二、漏洞分析  
  
  
Sentinel组件曾经有发现过SSRF漏洞（CVE-2021-44139），关于此漏洞，已有很多师傅进行过分析复现，本文在此不赘述，本文着重于分析的SSRF漏洞是另外一处，获取集群状态功能相关的SSRF漏洞。  
  
  
## 三、Sentinel版本  
  
  
我这里分析的版本是v1.8.8，在2025-05获取时处于最新Releases版。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibibea2093TiacdzwuEZTHOLBC583EDlXlIng4tnXukRTgM2Tzkd8uHodQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibt3Pjsq058K8s6bLB6nMiab2DIAR1AXujGHOqiaSW6JavzOpDn9aLsPzg/640?wx_fmt=jpeg&from=appmsg "")  
  
## 四、漏洞代码  
  
  
(1)漏洞点主要位于com/alibaba/csp/sentinel/dashboard/controller/cluster/ClusterConfigController.java的第119行---146行，该区域代码功能主要是获取集群或者目标机器状态功能相关，让我们来分析下代码  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibgZenEph5AB7tq9Pf1aibib0fqf8t1gSuk8YUt1mvYWgLThUSwW6OL6uA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
(2)通过第120行判断出首先它接收三个参数：app（应用名称）、ip（IP地址）和port（端口号），然后在第123行---130行，判断三个参数是否为空，为空则抛出对应的异常，然后第132行和133行，调用 checkIfSupported 方法检查当前版本是否支持该 app、ip 和 port 的组合。如果不支持，则调用 unsupportedVersion 方法返回不支持的响应。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibsceI7KjlX9ia7icLXTjUoicLIARa4icyEPW1ylwEUZE0xs9vt1GecFic2fg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(3)接下来第136行---144行，使用 clusterConfigService.getClusterUniversalState 方法异步获取集群状态，之后使用 thenApply 将结果转换为成功的结果对象，然后使用 get 方法阻塞等待结果，期间如果发生 ExecutionException，记录错误日志并返回错误响应，如果发生其他异常，记录错误日志并返回失败的结果，错误码为 -1，错误信息为异常消息。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibTqlicKAUDqEdn3PZunoY05tic74nNKjKT5ITToXCU3hNcE8QiaeM34GBw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(4)跟进clusterConfigService.getClusterUniversalState 方法，来到com/alibaba/csp/sentinel/dashboard/service/ClusterConfigService.java，第148行---166行，定义了一个名为 getClusterUniversalState 的方法，该方法返回一个 CompletableFuture<ClusterUniversalStateVO> 对象。这个方法的主要目的是从 Sentinel API 客户端获取集群的通用状态信息，并根据这些信息进一步获取客户端和服务器的相关信息。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibqaTXBZ0jCj2CNlRN4MQyoqGNfNelmX3cic2icODJEicyeeFwtKkibJYhkg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(5)第149行sentinelApiClient.fetchClusterMode(ip, port)则是调用 sentinelApiClient 的 fetchClusterMode 方法，获取集群模式信息，这个方法返回一个 CompletableFuture 对象，之后的第150行.thenApply(e -> new ClusterUniversalStateVO().setStateInfo(e))则是当 fetchClusterMode 方法完成时，将结果 e 传递给 thenApply 方法，thenApply 方法创建一个新的 ClusterUniversalStateVO 对象，并设置其 stateInfo 属性为 e。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibZFicEaicL0FlvDHxoOyzB7w5icE6RPic93pc6ZJpLiaJoeC3wKAZ9JribwJw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(6)跟进sentinelApiClient.fetchClusterMode 方法，来到com/alibaba/csp/sentinel/dashboard/client/SentinelApiClient.java，第626行---637行，这段主要功能是通过给定的 IP 地址和端口号来获取集群模式，并将其解析为 ClusterStateSimpleEntity 对象，然后使用 executeCommand 方法发送请求到指定的 IP 和端口，路径为 FETCH_CLUSTER_MODE_PATH。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibHDTDt6QaTvgya7W4icAOYS7WAfl9t9AZ9Gse8HroXrER99LtU4pt6YA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(7)跟进第631行的executeCommand执行方法，看看执行了什么，来到第253行，没有发现相关的SSRF代码，再继续跟进第254行的executeCommand执行方法，跳转到了266行，也没有发现相关的SSRF代码，再继续跟进第267行的executeCommand执行方法，来到了第280行。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibrSZ7hPOe5Mb2UWqDc8mXs21YZ5Gd8ZPJdEXa3yCUj7KibSMceBReibfg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibfbnAuibdIy1LI8At9k4J2J6SpYuLh59ibtVYe2qibBafjYtXics64ssUkQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
(8)第280行---第315行，前面传入的各个参数，都集中在这里进行进一步校验和检查处理，进行参数检查与合法性验证，之后构建基础的URL字符串，包括协议（http://）、IP地址、端口号以及API路径，最后构造HTTP请求（GET或POST），然后异步执行该请求。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibyfMUak9Ngnqib8Q7JH64Hiba5dZb4kIqFjK6HyhIJ1TNCicEMjY8Dc68A/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
(9)第310行最后使用HttpGet方法发起http请求时，没有对IP地址合法性进行完整校验，进而导致了SSRF漏洞的产生。  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibcXiay4lEN1udZrrDIZZlsaweZnJicsHI8VdsKZEjLibDwO7eOVgr5dIwQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
## 五、漏洞复现  
  
  
通过前面的ClusterConfigController.java代码，我们得知了漏洞接口是/state_single，然后第57行定义了起始路径/cluster，然后再传入3个参数，分别是app、ip、port，最后得出的漏洞地址是【http://localhost:8080/cluster/state_single】，该接口需要登录后才能访问。  
  
  
构造访问的漏洞地址：  
  
  
【http://localhost:8080/cluster/state_single?app=SSRF-TEST&ip=127.0.0.1&port=80】  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibpV3iajPNbkNQQWwCHkXMDLJiabYicgu3sK2iaoL0ITGV8Q0s6cZ33icxrtQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibstcARNPl28wuPkmg2VGJR4ibplicYPhXe06rRxu1dS9JebzFLFOibSdkg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0ibP6TJkRhjdmxz62labakIQTMagAq8sGtSUtGYHiax42dzKRE6560baVQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2nanSbDREKQzeAzvK5Ta0iblzjHOy9yn61JvjwB1oSq22bWic1H1WqQgbalMvHrU5iaoibQqBGHGbDtA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
## 六、总结  
  
  
本文主要分析了Sentinel组件获取集群状态功能点建立http连接时，没有对IP地址合法性进行完整校验，进而导致SSRF漏洞，总体来说并不难，新人第一次投稿分析此类文章，如有描述错误，还请各位师傅多多指教。  
  
  
  
参考链接：  
  
  
https://github.com/alibaba/Sentinel/issues/2451  
  
  
https://sentinelguard.io/zh-cn/docs/introduction.html  
  
  
https://www.cnblogs.com/charonlight/p/17552045.html  
  
```
作者：小瑟斯
原文链接：https://xz.aliyun.com/news/18017
```  
  
  
