#  不容忽视的威胁：探索与JWT相关漏洞（另类的越权）   
AegisGuard  AegisGuard   2025-05-29 05:57  
  
免责声明  
  
合法使用原则：文中提及的技术、工具或案例，仅用于授权范围内的安全测试、防御研究或合规技术分享，未经授权的网络攻击、数据窃取等行为均属违法，需承担法律责任。  
  
风险自担与责任豁免：文章内容基于公开信息整理，不保证技术的准确性、完整性或适用性。读者需自行评估技术应用风险，若因不当使用导致任何法律后果或损失，均由使用者自行承担，与本公众号及作者无关。  
  
法律管辖与提示：本公众号坚决拥护相关法律法规，反对任何危害网络安全的行为，读者需严格遵守法律法规。  
# 一、JWT介绍  
- JWT，全称是JSON Web Token，用于在网络应用环境间以JSON对象安全地将信息作为令牌进行传输，这种令牌被广泛应用于用户认证和信息交换的场景中。  
  
- 与传统会话令牌不同，服务器所需的所有数据都存储在客户端的JWT本身中。这使得JWT成为高度分布式网站的热门选择，因为用户需要与多个后端服务器无缝交互。  
  
- 实际上JWT也是一种鉴权字段（cookie字段变为JWT）  
  
## JWT的结构  
- JWT通常由三部分组成：Header（头部）、Payload（载荷）和Signature（签名），这三部分通过点号.  
连接在一起形成一个完整的JWT字符串。  
  
- Header：包含了令牌的类型（即JWT）和所使用的签名算法（如HMAC SHA256或RSA等）。例如：  
  
```
{
  "alg": "HS256",
  "typ": "JWT"
}
```  
- Payload：包含声明（claims）。Claims是关于实体（通常是用户）和其他数据的声明。JWT定义了三种类型的claim：registered、public和private。  
  
- Registered claims：这些是一组预定义的claims，不是强制的，但推荐使用，包括iss（issuer）、exp（expiration time）、sub（subject）、aud（audience）等。  
  
- Public claims：可以随意定义，为了避免冲突应该在IANA JSON Web Token Registry中定义或者使用一个抗冲突的命名空间。  
  
- Private claims：用于在同意使用它们的各方之间共享信息，并且既不是Registered也不是Public claims。  
  
- Signature：要创建签名部分，就必须采取编码后的header、编码后的payload、一个秘钥，以及头部指定的算法。比如使用HMAC SHA256算法，签名按照下面方式创建：  
  
```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01ocEsK3hR8Kl2FCfFUm1UC1dUNfZo1yWPM8A9X7AutPkhUKCnxibMJoEw/640?wx_fmt=png&from=appmsg "")  
## JWT的工作原理  
- 当用户使用其凭据成功登录时，服务器会生成一个JWT并返回给客户端。  
  
- 之后，客户端应在每个请求中附带这个令牌（通常通过HTTP头部Authorization字段携带）。  
  
- 服务器接收到请求后，首先验证JWT的有效性，如果有效，则处理请求。  
  
# 二、Burp插件推荐-JWT Editor  
- 便于修改JWT  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oA2Yglaia9gPJHdWKFotliackXo28ujewcjdGM4Wf4mWbrEwXOw8KEk8g/640?wx_fmt=png&from=appmsg "")  
# 三、通过未验证的签名绕过JWT身份验证  
- 方法：签名随便写即可绕过  
  
- 靶场地址：  
https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature  
  
- 场景：通过登录已给的普通用户账号密码登录后，访问管理员的管理面板，删除另一个用户（本质其实就是越权）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oZibcpZhhiaXVfXPjxeC77aKYfd3RutsWYuDzqUdgjqNGeD9xBh5UlyFA/640?wx_fmt=png&from=appmsg "")  
- 先通过已给的账户进行登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01onGGgNiaUE48BTSQjHOSqicU1icbOhBWEjPeibUQCGQJdjO1LkuZoS6ZhDw/640?wx_fmt=png&from=appmsg "")  
- 登录成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oSFOGKxrrNZ1uhJ04Qiaq7L7ZysXVFME4zCAdsPat9UYwnERc35C35oQ/640?wx_fmt=png&from=appmsg "")  
- 访问/admin  
这个页面，发现不是管理员账户，无法访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01orMDdaEQTQUtFckepjhD3Mh8Su9JQWbsAric10ddWbiacibRLhJZLcfvsg/640?wx_fmt=png&from=appmsg "")  
- 再次访问，使用Burp抓包，发送到Repeater，发现通过JWT鉴权  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oqLZN1KMH3ZxknOfonE0KI5uFDG2ibniaGUJNwAteuQYxibHTyVDBcgpNg/640?wx_fmt=png&from=appmsg "")  
- 点击JSON Web Token，可以清晰看到解码后的JWT各个字段的值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o78gCfVdD12b0LbXp3b4gstfJyjWXg0IlGF8MVMWYrRcgRHMtAico0EQ/640?wx_fmt=png&from=appmsg "")  
- 能够看到现在登录的账户是wiener  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o2vVcn8shAXfHubXiadQRh258hXTbAtWQvLck4lhSFQZKCyAeuYMJWXw/640?wx_fmt=png&from=appmsg "")  
- 此时将wiener改为administrator，然后发包，发现访问成功  
  
- 原因是此处没有验证JWT的签名字段  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oNSDXQGDiaicrhR097TuOqAg46kgTgxtGPn05jZ2eJopgvTR1TxicZjJQQ/640?wx_fmt=png&from=appmsg "")  
- 由于没有验证JWT的签名字段，所以在攻击过程中就可以随意更改这个签名，然后发包，发现依然能够成功访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oGN5r7kVq21fLj7e4fpDj9eR8iawpp6EKZXC3EMEMp44uQQDmMLia3ElA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oDTYHicUfSjlFHqWADsaTvYOEwtRfBjcOL9sLBE3py8wNBzLVG86bTeg/640?wx_fmt=png&from=appmsg "")  
- 此时就可以将这个能够访问成功的JWT复制下来  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o32iccO2VFQzuxRzicMFFjMiam6USzCU3C4SrThsEIytejEhyehM9Hm2qA/640?wx_fmt=png&from=appmsg "")  
- 然后重新访问/admin  
，用Burp抓包，将此时的JWT换成刚能够成功访问的JWT，然后放包，并且将每一步的JWT都替换一下，直到所有数据包替换完成  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o0BLuqAu5p15OOYEhkTicFeZznicmm9bgC51eQicBLxPyic98bcibhsjudOw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oQaEj6ViamMB7PAtUC1PGE1K941Sg5SiadMm43d9oSxiba16UuX6ibAicxFw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oWjmbiaSTFpDmkicSibv4iajPyBVOOAnveq6VlRuR19KictoK14Nf5vcmG7A/640?wx_fmt=png&from=appmsg "")  
- 此处的不用改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o0ibKrdnYlQelh2v8IckUhusUuFwSOpCNdpognCgARwLn3EyqEnPUo0g/640?wx_fmt=png&from=appmsg "")  
- 最后回到浏览器，发现成功越权访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oSKIxH9ibHA3ibnP3a1pZyYayQblcyd4jdRzbbOVU9Y7a0l4j8x6icBPOA/640?wx_fmt=png&from=appmsg "")  
- 此时点击删除carlos用户，依旧将JWT进行修改，最后即可删除成功  
  
# 四、不签名攻击（none攻击）  
- 原理：  
  
- JWT标头包含一个alg  
参数。这会告诉服务器使用哪种算法对令牌进行签名，从而告诉服务器在验证签名时需要使用哪种算法。JWT可以使用一系列不同的算法进行签名，但也可以保持不签名状态。  
  
- 在这种情况下，alg  
参数设置为none  
，这表示所谓的“不安全的 JWT”。由于这样做的明显危险，服务器通常会拒绝没有签名的令牌。  
  
- JWT允许设置其头部中的alg  
字段为"none"，表示这是一个不签名的JWT，这意味着任何实体都可以修改令牌内容而不被发现。  
  
- 靶场地址：  
https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification  
  
- 场景：通过登录已给的普通用户账号密码登录后，访问管理员的管理面板，删除另一个用户  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oypITGeUmmk3ZfvOQBJ8ormE4zYyR91TG2O58rGhoW60YKljtAiaAmFA/640?wx_fmt=png&from=appmsg "")  
- 先通过已给的账户进行登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oo7RVFHZdYYDP3EZ64LLS63r8LnEMKR1YTmzHFAY2GHcsqojLQlBWAA/640?wx_fmt=png&from=appmsg "")  
- 登录成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oy7Tjd1Jd18SzhPo1hMQDCRFnniadeibno4L5oic5MvWZ0gmyI4HzLhROQ/640?wx_fmt=png&from=appmsg "")  
- 访问/admin  
这个页面，发现不是管理员账户，无法访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01of7AUYWaBBV1ZSm6Z5xcvhj7CDp7qOLiaibQEg7mzYF1mhAWNBdwlib41A/640?wx_fmt=png&from=appmsg "")  
- 再次访问，使用Burp抓包，发送到Repeater，发现通过JWT鉴权  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oCGEZZqe5RianibG0bODCen1YYguiazlzLdIzT6HvgnLjeGkPpI9CYy4bw/640?wx_fmt=png&from=appmsg "")  
- 点击JSON Web Token，将wiener用户改为administrator，然后发包，发现依旧没有访问成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oSia6xVbHqia4jX4PDGHLszEPLwZhuzpuriahcvkyicFTGoAIqXweB3xRYQ/640?wx_fmt=png&from=appmsg "")  
- 此时在左下角，将alg改为none，发包后发现访问成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oVkhX5nLPiambpQ9T03zzfuMWpLd0x5AicjoRDDibYFibuQOnMvCjjtJDiaA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01ocAStibq2oaCmbWPt4JCCAgD1hjcUs9Rc280Z4VicVFg9XbFFe640EwKQ/640?wx_fmt=png&from=appmsg "")  
# 五、通过弱签名密钥绕过JWT身份验证  
- 靶场地址：  
https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key  
  
- 先通过已给的账户进行登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oG4cPButU3deQYcSfsweRUwRnA19xLpCZ9IxYoGoiau4VbUBOzd6uQSQ/640?wx_fmt=png&from=appmsg "")  
- 登录成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oL44TI9QCu0FAx91GSias8wVJ72VDdsaY0h30FxKyQnlVvQlPplWNVvQ/640?wx_fmt=png&from=appmsg "")  
- 访问/admin  
这个页面，发现不是管理员账户，无法访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oic2KrH7ReumLVP7rYbl9mRuHAsIUsHEIicAQTVr9hP3eL2wngkU9yxPQ/640?wx_fmt=png&from=appmsg "")  
- 再次访问，使用Burp抓包，发送到Repeater，发现通过JWT鉴权  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oaGIWp5MtKGUJAGKNQtNwcia9gFOnlI80PKruicv3Rmxef2reF4PwicPoQ/640?wx_fmt=png&from=appmsg "")  
- 点击JSON Web Token，可以看到加密算法为HS256  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oQ6n8tWsxa0sczOvSib2mcv3Z6FZD691bPB23H8rosjmvRg4qg37wicQw/640?wx_fmt=png&from=appmsg "")  
- 此时可以将整个JWT复制到无影工具中，对密钥进行破解  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01otiaZNU7tVIXwo5r5O7ypeGkVB65z2Q5OFXKt0cCHPaPW5PRftibeQia5Q/640?wx_fmt=png&from=appmsg "")  
- 然后将JWT和破解出来的密钥复制到以下网站，然后将wiener用户改为administrator  
  
- https://jwt.io/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01oawHSvTBsJNj2EV0WhVmcBNUVNTthexvVJvFgqfMO0cGaCEzaVXic9ibw/640?wx_fmt=png&from=appmsg "")  
- 将重新编码后的JWT复制到Burp，然后发包，发现访问成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYDBFLXQBkuibL7k4ZbCyn01o50FjLicMDibCxqKLBao4F3oKn1n0AXUNq4J9hZib6lOL8kaRdkNVeH94A/640?wx_fmt=png&from=appmsg "")  
  
  
