#  Apache Tomcat 9.8分RCE漏洞曝光，PoC 已经公开   
会杀毒的单反狗  军哥网络安全读报   2025-05-27 01:11  
  
**导****读**  
  
  
  
在广泛使用的开源 Java servlet 容器和 Web 服务器 Apache Tomcat 中发现了一个严重安全漏洞，编号为CVE-2025-24813 。  
  
  
该漏洞源于对文件路径的不当处理，特别是包含内部点（例如file.Name）的文件路径，可能允许攻击者绕过安全控制，从而导致远程代码执行（RCE）、信息泄露和恶意内容注入。  
  
  
该漏洞影响 Tomcat 版本11.0.0-M1 至 11.0.2、10.1.0 - M1 至 10.1.34以及9.0.0.M1至 9.0.98。Apache已在11.0.3、10.1.35和9.0.99版本中发布了补丁来解决此问题。  
  
  
CVE-2025-24813源于Tomcat 默认 servlet 中的路径等效问题，在某些配置下，该问题会错误处理通过 HTTP PUT 请求的文件上传。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHjxGD6u56cVoOOcCGj6Okuc9mHOTZ9IeUtIicjEsLJctpJTCF4I88RDIFy5ks1ps43ibJlMZn6CZ3A/640?wx_fmt=png&from=appmsg "")  
  
  
在以下情况下，此漏洞可被利用：  
- 默认 servlet 的readonly参数设置为false(write enabled)。  
- Content-Range允许部分 PUT 请求（使用标头）（默认启用）。  
- Tomcat 配置为基于文件的会话持久性（非默认）。  
- 该应用程序包含易受反序列化攻击的库。  
- 攻击者知道敏感文件的命名约定和位置。  
###   
### 漏洞利用步骤  
###   
  
1.  
上传恶意会话文件：  
  
攻击者发送一个 PUT 请求，其中包含精心设计的 Java 序列化有效载荷，目标为会话存储目录。  
  
  
例如：文本PUT /webapps/ROOT/WEB-INF/sessions/SESSIONID.ser HTTP/1.1 Host: vulnerable-tomcat Content-Range: bytes 0-99/100 Content-Type: application/octet-stream <malicious serialized payload>  
  
  
2.  
触发反序列化和 RCE：  
  
攻击者随后发送一个 GET 请求，其中JSESSIONID包含引用上传的会话文件的 cookie：  
  
  
文本GET / HTTP/1.1 Host: vulnerable-tomcat Cookie: JSESSIONID=SESSIONID当 Tomcat 反序列化恶意会话文件时，任意代码都会在 Tomcat 进程的权限下执行。  
  
### 风险因素及其影响  
###   
  
虽然该漏洞很严重（CVSS 9.8/10），但利用该漏洞需要非默认配置 - 具体来说，就是启用写入的默认 servlet 和基于文件的会话持久性。  
  
  
概念验证  
(Po  
C  
)  
代码已经公开，研究人员在漏洞披露后 30 小时内就观察到了攻击利用。  
  
  
潜在影响包括：  
- 远程代码执行（RCE）  
- 未经授权访问敏感文件  
- 将恶意内容注入上传的文件中  
- 服务器配置文件损坏  
- 网络内的数据泄露和横向移动  
###   
### 缓解措施和建议  
###   
  
应立即采取的缓解措施：  
- 将 Apache Tomcat  升级到11.0.3、10.1.35或9.0.99。  
- 保持默认 servlet  的readonly参数设置为true（阻止通过 PUT 进行写访问）。  
- 如果不需要，请禁用部分 PUT 请求。  
- 避免基于文件的会话持久性或将可写目录与会话存储隔离。  
- 从类路径中删除不必要的反序列化库。  
无法立即升级的组织应应用所有配置强化步骤并监控异常的 PUT 和会话活动。  
  
鉴于 Tomcat 的普遍性，研究人员建议快速修补漏洞，立即行动对于防止攻击至关重要。  
  
  
参考链接：  
  
https://cyble.com/blog/cert-nz-warns-of-cve-2025-24813-in-tomcat/  
  
  
新闻链接：  
  
https://gbhackers.com/apache-tomcat-rce-vulnerability/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
