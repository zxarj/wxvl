#  （吃瓜）刘农TV之渗透中遇到的神人运维   
原创 黄豆安全实验室  黄豆安全实验室   2025-01-30 06:04  
  
> 本文记录了从nacos弱口令到接管全部资产、泄露全部用户数据的过程  
  
  
拿到域名，第一时间itdog看一眼有没有cdn：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaasClMbcm3sjdiaVFgxp4uWw9Q2wZPWJPDZJZviaicr1oyOxRYrPpWsNAg/640?wx_fmt=png&from=appmsg "")  
  
  
很显然没有，那么先把ip放到fofa看一下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaibpsym9FJwYUcv9uSW7NBib3SAGPqibj7QKFTfZyDvPWEaSiaibyyMQ0I7w/640?wx_fmt=png&from=appmsg "")  
  
看到nacos直接nacos:nacos测一下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJahdCJvSl9B10yGw9nNhDf5z9uiajA5pQuFESbniaSDOXiakpBG1kibWfHRw/640?wx_fmt=png&from=appmsg "")  
  
也是登录成功了，运维可谓是个神人，nacos放公网还弱口令  
  
翻了翻他的配置文件，发现其中一个有大量的敏感信息，包括但不限于微信appid、secret，阿里ak&sk、数据库账号密码  
  
先使用云鉴看看ak&sk  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJa6zncmEB7VrcMbhuCRUprOsWxucociaKBBibfBBSicWfhxw5bF7vLPQoNw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaeIgjPzY3bBqL8WDdDnQFpyjFtmlPGbCag2Zxo6NxwmdESXazfFYOzQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaVSoDQTIQ5ialYtZepgM9sqOiakYhgIxI4bQficM2jvw0rQUupTOsFfoIw/640?wx_fmt=png&from=appmsg "")  
  
然后云资产管理工具看一下能不能连上服务器  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaQ5Fq8AYFSsRcYTdSwnqxEe7abkeFFlIaCFAmMQre9HGWvXwlLebicTQ/640?wx_fmt=png&from=appmsg "")  
  
完全可以，但是：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaiaia54s3pbc1rWQIv1cLenURFPiczrYzuHCADYxjGQwzzLNebZfk8ym9Q/640?wx_fmt=png&from=appmsg "")  
  
而oss可以正常登录  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJa63Nohqz6vDtS92ia3By4lGI6zRpGmfX6xym06kic7BCRldagjoMMwUQg/640?wx_fmt=png&from=appmsg "")  
  
之后翻文件的时候看到这么两串数据：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJauJMDtd7B17P4qloZpCAVMqeBpThibe4DOa27QL0dGwNPdUSHaTCoppQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaAAozjBp6XK8B1BtB6veXa4jHT8ibzbMgCzAILfd8lY9c0PLYnEOjd7g/640?wx_fmt=png&from=appmsg "")  
  
rabbitmq就不看了，因为官网的连接工具要钱  
  
这个druid也是个神人配置的，设置的惊人的弱口令，看他资产的时候恰好看到个swaggerUI的未授权，扫一下目录：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJanfXKK6bQaMZXPwvD15SzmrTw8STLgbEq33rZo1vDs5fSpwkJP5xMTA/640?wx_fmt=png&from=appmsg "")  
  
这里没看到druid，但是有一堆信息泄露，测了测那个swagger，也是没有任何鉴权输入数据就能用，到这里能忍住不喷这个运维的也是神人  
  
看完druid就该数据库了，这里依然是把数据库的账号密码地址都放到了一起，生怕别人打进来不知道怎么往下继续打  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJahBNt48ssW4hxvPxnIQx9M40eMtooHP2Fgyew7Ab2zM8tw5lOPDDAAQ/640?wx_fmt=png&from=appmsg "")  
  
连上去之后收获了一堆毫无加密的用户数据，包括手机号姓名  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJajicrTMTstlUyLaOSOLib6LyH7bV2SISaKdjrZvcLHEkFxQnISpylfSGg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJazjNbDY8434ZDhLs4UOsg6uoEFpWrvicmnFDTIpdViaI1iaicGjj5nv6uaw/640?wx_fmt=png&from=appmsg "")  
  
这里测出来是他的子域admin.xxx.com的表，但是cmd5解不出来，气死我了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaJDe7ALmoGc2IFHZCBPKrVB1dYRibRJCWiah8KBTlOPziaTj94oJvibicT1A/640?wx_fmt=png&from=appmsg "")  
  
继续翻数据看到了上面这条，同时数据库也有这个表：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaf1bw0ibE6cpuyzOcSPv0ypc6WUzyZybZ5LicCB4PNN24TpLib0ibwMgfmw/640?wx_fmt=png&from=appmsg "")  
  
  
最后cmd5解出来是admin:123456  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJauh6Asqp5xFvUacNiaYEoLbR1MVNgEI2t7ib2cssbJssThiaFdyOO03x4A/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaD98JTBibUQvabzH9h0clWMkyRo5wI1kcriaZNw2OWK7ia2eywnKFCMvBQ/640?wx_fmt=png&from=appmsg "")  
  
可谓是意料之外，情理之中  
  
最后就来看他泄露的微信的这几个数据吧（mchkey&id，appid&secret以及miniapp的configs）  
  
拿到appid&secret第一件事肯定是获取token：  
  
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=&secret=  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJabkMId9Tzfnr4dybpYqHwaNlbfG9F8PCSDRVjicEHKq4ZqibWvH2JqIZw/640?wx_fmt=png&from=appmsg "")  
  
有了这些数据就去https://developers.weixin.qq.com/测试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfbNT9mE8mva6GtlWZJUiaxJaA8aAaOqWqfZghVLS0LI2KibKZESReQS3DuSHuXXyvk6ibK9ZIjic6MbVQ/640?wx_fmt=png&from=appmsg "")  
  
点到为止，我们就结束测试  
  
综上，由于该单位运维是一个惊人的神人，导致该单位存在nacos弱口令、微信全部id&key泄露、服务器大量数据泄露、接管oss、接管数据库，看完文章还不喷这个运维的是这个👍  
  
