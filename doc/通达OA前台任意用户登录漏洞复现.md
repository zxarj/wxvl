#  通达OA前台任意用户登录漏洞复现   
Sword  网络安全学习爱好者   2024-11-18 01:28  
  
## 漏洞描述  
  
通达OA是一套使用比较广泛的办公系统。该漏洞因为使用uid作为身份标识，攻击者在远程且未经授权的情况下，通过利用此漏洞，可以直接绕过登录验证逻辑，伪装为系统管理员身份登录OA系统。通达OA官方于2020年4月17日发布安全更新。  
## 漏洞影响版本  
  
通达OA < 11.5  
  
通达OA 2017版本  
##   
## 漏洞原理  
  
本次复现为2017版本，则重点分析该版本，但原理都是基本相同的，只不过文件路径不同而已。根据POC的代码分析如下，该漏洞涉及的文件包含以下四个：  
  
```
/ispirit/login_code.php
/general/login_code_scan.php
/ispirit/login_code_check.php
/general/index.php
```  
  
  
通达OA源码使用zend5加密 ，分析源码需要先进行解密  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWxoZ0NnvIiayo2V6xbh9jPJwbszsiaAqicUUU6ILxS6lv3uYtup1ibgbSfA/640?wx_fmt=png&from=appmsg "")  
  
使用的解密工具是:SeayDzend，工具使用很简单  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsW0toxEJs04icPzEgsnAGibibYA3VgNBf0r2d0Q9EJVRsoIROdrWAdJictpw/640?wx_fmt=png&from=appmsg "")  
### /ispirit/login_code.php：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsW8ibrOj8qiciaMsL9mDDTxibibaQcarNq2MMiauc5GLSknttPPbJJEZ0xMPog/640?wx_fmt=png&from=appmsg "")  
  
该文件用来获取codeuid参数，如果不存在，则会自动生成一个codeuid，并且将其写入CODE_LOGIN_PC缓存中（通达OA使用了缓存系统Redis，同时也提供了对缓存的使用方法），但是在18行位置将这个参数显示出来，导致用户可以获取这个参数的值，从而可以绕过后面的验证。  
### /general/login_code_scan.php：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWVVYA6mYmQTjlbRm00D413Uwn5g8GMthMQcjhzUiak7ZlSA156JuRdZg/640?wx_fmt=png&from=appmsg "")  
  
在这一文件中，用户可以控制输入的关键参数uid，在存在漏洞的通达OA版本中，后台数据库里uid对应的用户是admin管理员账户。并且将该数据存储在CODE_INFO_PC缓存中，因为我们在第一个文件中获取的codeuid存储在CODE_LOGIN_PC中，所以这里在复现时需要指明source变量为pc，这里的username则为admin，而type变量需要指明为confirm，原因在后面会进行解释。  
### /ispirit/login_code_check.php：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWOJLicMAccL8EvvEo9RgJRDU66el0fAbVtem1fWzWnp9Uc9sCHZya3Lw/640?wx_fmt=png&from=appmsg "")  
  
这里使用之前存储的两个缓存中的内容，一个用来获取codeuid，一个用来获取通过post传入的uid等关键信息，这里红框就是为什么前一步需要将type设置为confirm。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWyS4LvABQF2r9VbmEwv2tXHmvXpe2qobKfeXmlkeOdD19PPjpCpvTyQ/640?wx_fmt=png&from=appmsg "")  
  
这里是最为关键的位置，代码获取用户可控的参数uid，并依次作为依据直接带入数据库进行查询  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWNicgRvNjBzbBsk6t9mNeMX4KhzDLhm4a3ia5viapXBa3icSVhuKIX9OMFA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWATlZMicgSGaoGA14Jick40XABrFnSAibhaEJUlwA0Bxoel4eUwYicDlgOA/640?wx_fmt=png&from=appmsg "")  
  
随后将查询的信息直接写入session中，通过这一步，session中包含的就是管理员的身份信息。  
  
以上就是该漏洞的原理，V11版本原理类似，可用对照POC中的步骤进行分析复现。  
## 漏洞复现  
###   
### 环境搭建  
  
通达OA-TDOA11.4_2 建议在虚拟机环境下安装  
```
下载地址：https://cdndown.tongda2000.com/oa/2019/TDOA11.4.exe
```  
  
下载下来一路默认下一步就行！  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWuhdmpffP1c1jTfJ0ibRqgQicRIbC7wT4DPXy5nMfAHbSCBQA2Xh2j9icg/640?wx_fmt=png&from=appmsg "")  
  
安装完成最后需要检测端口  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWUicreZnL0VUczstOfz1h7sNG5vQRtVpUNNlE6ZupJ8u35TQmlicuiaIBQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWVYzWB0W6629LF3swbxRRTBibR2YHQsT1b83ELvCkDMiaJTpyb3uqZ3cA/640?wx_fmt=png&from=appmsg "")  
  
最后点击确定就行  
###   
###   
  
最后点击确定就行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWIM6kZcnnn1icHGT3vfqz7Cz0Osw8IfA9VkuRytcjmHnlzyF9LibYVI1A/640?wx_fmt=png&from=appmsg "")  
  
### 漏洞利用  
#### code1：手工利用  
  
按照poc中的步骤，首先抓首页的包进行更改，  
  
访问/ispirit/login_code.php  
  
通过返回包获取codeuid  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsW9Lm6KEoty9ZNV8FtiaAm3lB6065iaWw9YTQdScLHbsibQJRDgsQVCicYYw/640?wx_fmt=png&from=appmsg "")  
  
而后使用POST方式访问/general/login_code_scan.php提交payload，其中codeuid需要改为上一步中返回的值。  
```
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWfS0nMC3Q0ickwqxzECQlStuHRjsQTPYAjXCEOA63fKmVY0HquVibr1VQ/640?wx_fmt=png&from=appmsg "")  
  
第三步使用GET方式访问/ispirit/login_code_check.php，带上参数codeuid，让后台进行代入查询，并返回携带管理员身份信息的凭证。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWy5AibVODPibOcCmWibSpJqBdpzpwKg0ZjXfWs9zIuKibFlYwia54ic7jCicLQ/640?wx_fmt=png&from=appmsg "")  
  
经过这步后客户端已经拥有了管理员的身份信息，直接访问OA主页/general/index.php，放行该数据包，成功以管理员身份登录OA系统。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWZ90C9QVmEg2ticRsT9cfYTyT0YjhniapnZp7TtpCrERHiavOeComARxqg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWKAmRW3qTlA6zJUy83AHNnAlCtRhxt6o1go8X3RlfzE7CfsfbZycmTA/640?wx_fmt=png&from=appmsg "")  
#### code2：POC利用  
```
python3 .\POC.py -v 2017 -url http://192.168.142.129/
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWEfAcarphu5vo4KkBGOt3Y59iah8rNSesX3zNSzFYsnyyszKqXCpR5Jg/640?wx_fmt=png&from=appmsg "")  
  
访问主页  
http://192.168.142.129/general/index.php  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWg0LcSLBkaIDmszQRmJxQj1qLrBicQHGTebNlVbGKGqXBkqOWMgPwRicA/640?wx_fmt=png&from=appmsg "")  
  
修改cookie中PHPSESSID的值并刷新页面就会发现登录成功了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWxiaiaQLiafhZ8nKWibV2LoyWDbQXawYiaYUiczkvVhZAjKagNS165aetvoPA/640?wx_fmt=png&from=appmsg "")  
  
最后修改cookie也可以在bp里面修改  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWdiaY8qvGrVBsIGj9yG0E3afqKj4pRkw6uz67iaH9L6FzC2Eiac5LukBHw/640?wx_fmt=png&from=appmsg "")  
## 修复建议  
  
更新最新版本  
## 复现环境所需安装包以及工具在公众号回复通达OA11.4获取  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZAPxzic90CGBb636ckQ1MC08nniczShXsWeVS7woVPhY6icYib7q60xQWZZE2mqGygaFSiaSUkFTJVzHfYWsa7ZG7Qw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
