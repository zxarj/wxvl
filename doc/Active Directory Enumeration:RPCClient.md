#  Active Directory Enumeration:RPCClient   
Raj Chandel  七芒星实验室   2024-12-01 23:01  
  
#### 文章前言  
  
本篇文章中我们将重点介绍如何通过SMB协议和RPC协议来枚举域内信息，下文中使用的工具为rpcclient  
#### 信息枚举  
##### Server Information  
```
rpcclient -U Administrator%Ignite@123 192.168.1.172
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzfxKKIiaFsUJib6iaoX7z6LhM2Bciaaf5gfp0NNZnYasDXltzB5Pu9EvbGQ/640?wx_fmt=png "")  
##### Domain Information  
```
querydominfo
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzQGBh2TAiakIRia2rgTBxzcOiajCDTPapP4R9n9OzxQK9DQmPvW5Rln3nQ/640?wx_fmt=png "")  
##### Enumerating Domain Users  
```
enumdomusers
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzQ5InUl26EKibwgsAJxy4PhsmHa4oW23iboMRAIpQXs2ficicWZETepfcicA/640?wx_fmt=png "")  
##### Enumerating Domain Groups  
```
enumdomgroups
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqz8ichs2spiaItTdXibHJKNbhumzwV3OeZn2HTibxcE6UxUQQx76pHicgnZbQ/640?wx_fmt=png "")  
##### Group Information Queries  
```
querygroup 0x200
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzIY9ibk9emElsL0hy3sp0WqDEZR93v4hFQB6r4icugtl6cEqPicTacqsyA/640?wx_fmt=png "")  
##### User Information Queries  
```
queryuser yashika
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzrhxZKvl78b1gdMueeUEmvd1vRYsRfLE9ribOvn4C89bYNYsmujhO4wQ/640?wx_fmt=png "")  
##### Enumerating Privileges  
```
enumprivs
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzLPmpAWPuGiaBicbo0vcfgGKPQAudXRUr3o6KFONjpcR6npK6wrSkaNiaA/640?wx_fmt=png "")  
##### Domain Password Information  
```
getdompwinfo
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzdRGv1w1BCGictQgWLl7t4O4qGvJekua8WNZueXd6NTfSqJCO7X5VWlQ/640?wx_fmt=png "")  
##### User Password Information  
```
getusrdompwinfo 0x1f4
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzKxlfXSh40wRfAjCiaDFGxyC4Abhtza5c0pgcsibsMiauxTQxQF6DEhYrw/640?wx_fmt=png "")  
##### Enumerating SID from LSA  
```
lsaenumsid
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzpx4zP5yr5LDucNLicJtjwhPlYxPZ9yCF0tJTF631RhEia1qqo0ibS4FUQ/640?wx_fmt=png "")  
##### Creating Domain User  
```
createdomuser hacker
setuserinfo2 hacker 24 Password@1
enumdomusers
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzErRrt8jnjrYymdQxYDicTibdEp7K07mr9bo3avFunXic2dvJxge9hWH9w/640?wx_fmt=png "")  
##### Lookup User Names  
```
lookupnames hacker
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzKdCEEswJ6whGrDQlDerrLcsUs7ARCK2J2m3DM0W4HerQRZIZeEv3Ow/640?wx_fmt=png "")  
##### Enumerating Alias Groups  
```
enumalsgroups builtin
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzs1IBHXICOeLaVoVwcD0WQahBAFDKcDtfNxlpLgjE8AlYibDMOfBOpCw/640?wx_fmt=png "")  
##### Delete Domain User  
```
deletedomuser hacker
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzfWBNhQQqCaW8Wrv60dU35UbRsHlgbf6Gqh51y1BOtrE3aaruarMic1w/640?wx_fmt=png "")  
##### Net Share Enumeration  
```
netshareenum
netshareenumall
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzdA4iaW2RYsQyOr2zxQ2VRFiciazZzUBWOcjzfVcnLDoyDlEgDEEWH8zmw/640?wx_fmt=png "")  
##### Net Share Get Information  
```
netsharegetinfo Confidential
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzBnTzUJiaH151wtDRtGNps0b4Zia8cCmVUmADO3DD8eu7Vb7aFEdCESVA/640?wx_fmt=png "")  
##### Enumerating Domains  
```
enumdomains
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzdM9K1EVr6mORj6ujfWMMniaN1ibn9Oj3icnqHYgKvx5Tib6SEuJaEYzTLg/640?wx_fmt=png "")  
##### Enumerating Domain Groups  
```
enumdomgroups
enumdomusers
queryusersgroups 0x44f
querygroupmem 0x201
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzibJwCLANWFgichSj50rKHDt854Gv093ibv5u1C3fcKHIZLbBpFY2ly2rg/640?wx_fmt=png "")  
##### Change Password of User  
```
chgpasswd raj Password@1 Password@987
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzJoDa5HE7ayJ03SkW1Z6vPNOqcntaAoTvYjnohVJicZyibs5ibBfZISxXg/640?wx_fmt=png "")  
##### Create Domain Group  
```
createdomgroup newgroup
enumdomgroups
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzpBqNSQUvyFq4YJcgW7SYicur8th7zXZzfAmgK0OEkM9K0ibV9VuNib5Lw/640?wx_fmt=png "")  
##### Delete Domain Group  
```
deletedomgroup newgroup
enumdomgroup
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzHib8ZVBveC2FQnGdjdqyDYRt9JFOI5Qhx6ILBp7eGpx1jpPjwibzJfbg/640?wx_fmt=png "")  
##### Domain Lookup  
```
lookupdomain ignite
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzDAkS3Ux18so43Rd0fMmhDpQnm0mpXibXAqtZ7FBa7sHcccJJ5c0zqdw/640?wx_fmt=png "")  
##### SAM Lookup  
```
samlookupnames domain raj
samlookuprids domain 0x44f
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzUxLpDTq7maBFtS7yygec0sUWbj1y15kdLOyaM5gBgLicVtBNkFqe3uA/640?wx_fmt=png "")  
##### SID Lookup  
```
lsaenumsid
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzmafGNteX1OCtoAFlhicVuOkhmFAMEGT1GyYZSKJuW3zzbgWhD8OTmIw/640?wx_fmt=png "")  
##### LSA Query  
```
lsaquery
dsroledominfo
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqznPUZpP7jPyWibNgB8eCzOgEia5FiavpoaMVRiafmEKJiblrjLoSjYO7h7qw/640?wx_fmt=png "")  
##### LSA Create Account  
```
lookupnames raj
lsacreateaccount S-1-5-21-3232368669-2512470540-2741904768-1103
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzsqQKUzibtX7eVPgLe5FNiam7jJjLdY4ibqpyGSznnsy5yq1icINjY8YgBQ/640?wx_fmt=png "")  
##### LSA Group Privileges  
```
lsaenumsid
lookupsids S-1-1-0
lsaenumacctrights S-1-1-0
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzMAq5JB7setuoasJPuG4jkz8QcOTYYBjZJ6j4un4DQ9Jdj0vHWbXb0A/640?wx_fmt=png "")  
```
lsaaddpriv S-1-1-0 SeCreateTokenPrivilege
lsaenumprivsaccount S-1-1-0
lsadelpriv S-1-1-0 SeCreateTokenPrivilege
lsaenumprivsaccount S-1-1-0
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzj1255fNReUbJswFH2FwtME8jBYkA3amN8RtVqYicxF9Xdbqy2ag0yEw/640?wx_fmt=png "")  
##### LSA Account Privileges  
```
lookupnames raj
lsaaddacctrights S-1-5-21-3232368669-2512470540-2741904768-1103 SeCreateTokenPrivilege
lsaenumprivsaccount S-1-5-21-3232368669-2512470540-2741904768-1103
lsaremoveacctrights S-1-5-21-3232368669-2512470540-2741904768-1103 SeCreateTokenPrivilege
lsaenumprivsaccount S-1-5-21-3232368669-2512470540-2741904768-1103
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzkmctQEVA8NUWAiardwwaxDHPOVlrt2DYekQn79rAmM03FY1VRftTqfg/640?wx_fmt=png "")  
```
lsalookupprivvalue SeCreateTokenPrivielge
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzJSDoeMUGG71mh1pepwQW0GPffUTKQASGicsgy926xMgicTXa3VODblKA/640?wx_fmt=png "")  
##### LSA Security Objects  
```
lsaquerysecobj
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmDhaBaVUQpbiclDTK9UnFqzDrhE28xhqvXuOWs8Bl0zt7JfsCXFUfhP737uEHrPC19MS7OGHsEUWw/640?wx_fmt=png "")  
#### 文末小结  
  
在本文中，我们能够使用rpcclient工具通过域内的SMB和RPC枚举大量信息，本文可以作为红队攻击和列举域的参考，但也有助于蓝队了解和测试在域上应用的保护及其用户的措施~  
  
  
**推 荐 阅 读**  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHmiazrVsk32mFQGSWeuiayXUyzzibVnQv61JSSelD87SuCK0b4WEK9SicNg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHuymSGgjibhhPTabupfXRQ63icNSVu5ILUZMhaicD6icF02SQUGazFfxAsQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHwv5DglsmjjelBqrLtokic0InowAFBH2tGMBALBj5HqWdw9naXIsnQSQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHIaBgzXLZTzKELSmO0826xOlmn3q7U2t188XgsNw6TQKg4Qnqakb4DA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
横向移动之RDP&Desktop Session Hija  
  
  
