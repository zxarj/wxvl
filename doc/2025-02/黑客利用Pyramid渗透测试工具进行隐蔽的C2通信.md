#  黑客利用Pyramid渗透测试工具进行隐蔽的C2通信   
AI小蜜蜂  FreeBuf   2025-02-14 11:58  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
黑客们最近利用开源的Pyramid渗透测试工具，建立隐蔽的命令与控制（C2）通信。  
Pyramid于2023年首次在GitHub上发布，是一个基于Python的后渗透框架，旨在绕过终端检测与响应（EDR）工具。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibS68M2J8HH4TbtJCJa8icwgsyth4DyUxFdpBiaq0ws2QC6OMnRS5FFJTMYYopefeZFOVWXdhPiaB7Ug/640?wx_fmt=jpeg&from=appmsg "")  
  
## Pyramid工具的技术特性  
  
****  
Pyramid的轻量级HTTP/S服务器功能使其成为恶意攻击者减少检测风险的首选工具。它利用Python在许多环境中的合法存在，通过基于Python的HTTP/S服务器传递文件，并作为攻击操作的C2服务器。  
  
  
该框架还包括直接加载知名工具（如BloodHound、secretsdump和LaZagne）到内存中的模块。Hunt.io的安全分析师指出，这种内存执行方式允许操作者在已签名的Python解释器上下文内行动，可能绕过传统的终端安全措施。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibS68M2J8HH4TbtJCJa8icwg3iayjUCDA8ic8Ylzv3TmT8mibj0J3n172dDTqXE9v7OCxDNUYjDqUGvCg/640?wx_fmt=jpeg&from=appmsg "")  
  
Pyramid README截图 (来源 – Hunt.io)  
##   
## 检测Pyramid服务器的机会  
  
****  
识别Pyramid服务器涉及分析特定的网络特征。当与疑似Pyramid服务器交互时，响应头会显示出以下独特特征：  
```
`Server: BaseHTTP/0.6 Python/3.10.4 Date: WWW-Authenticate: Basic realm="Demo Realm" Content-Type: application/json`
```  
```
```  
  
服务器还会返回一个JSON响应体：  
```
`{ "success": false, "error": "No auth header received" }`
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibS68M2J8HH4TbtJCJa8icwgciaHr4keshQPHrgEvRIWAtO6pXMK3sjiaxFHIgLxMy8XGA3w5vklPD5Q/640?wx_fmt=jpeg&from=appmsg "")  
  
Pyramid C2 HTTP 401响应 (来源 – Hunt.io)  
  
  
最近的扫描已识别出多个与Pyramid服务器相关的IP地址，包括104.238.61[.]144、92.118.112[.]208和45.82.85[.]50。这些服务器与一家名为DevaGroup的网络营销服务的域名相关联，尽管目前尚未发现恶意样本。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibS68M2J8HH4TbtJCJa8icwg8uEjpibR1y21JvWUwnjDGmoDqwiaf3knYqadSAgBicUjKCxWfPkLXmjrw/640?wx_fmt=jpeg&from=appmsg "")  
  
Pyramid C2服务器追踪 (来源 – Hunt.io)  
##   
## 检测技术细节  
  
****- **HTTP状态码:**   
  
401 Unauthorized  
  
- **响应体哈希值 (SHA-256):**  
  
54477efe7ddfa471efdcc83f2e1ffb5687ac9dca2bc8a2b86b2 53cdbb5cb9c84  
  
- **服务器头:**   
  
BaseHTTP/0.* Python/3.*  
  
- **认证和内容头:**   
  
WWW-Authenticate: Basic realm=”Demo Realm” 和 Content-Type: application/json  
  
这些参数可用于构建结构化查询，以识别与Pyramid相关的基础设施，从而增强网络安全防御。通过关注认证挑战、响应头和特定的错误信息，防御者可以提高检测的准确性，并减少误报。  
  
随着开源攻击性安全工具的不断发展，追踪类似的实现将为新基础设施提供早期预警，并完善检测方法。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ic5icaZr7IGkVcd3DT6vXW4B4LOZ1M7YkTPhS1AT2DQJaicFjtCxt5BRO7p5AOJqvH3EJABCd0BFqYQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651312407&idx=1&sn=60289b6b056aee1df1685230aa453829&token=1964067027&lang=zh_CN&scene=21#wechat_redirect)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
