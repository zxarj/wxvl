#  本地部署DeepSeek-R1   
 哆啦安全   2025-02-18 01:04  
  
1.安装Ollama  
```
https://ollama.com/
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8T9NaQPpNHbGaruL4iaUA4l7w6UtWwUWkQw87Jf6EmnJkicAs6Vtkqib5g/640?wx_fmt=png&from=appmsg "")  
  
  
本地部署推荐使用开源工具Ollama，既提供命令行界面，又提供图形界面，能够方便地管理和使用本地的AI模型  
  
  
Ollama支持MacOS、Windows和Linux  
  
  
双击打开Ollama客户端安装包，点击Next  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU833ZjBabSoyMUKtN2KO74zTefIjzTVzyZGY3JC17LShqLWyWSjo9JFg/640?wx_fmt=png&from=appmsg "")  
  
  
点击Install安装Ollama的命令行工具（CLI）。这一步可能会让你输入系统密码  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU846ndBmyx46jicicSI7o7icQzeniaPVo9jE6b2Kkt5C64ia1LqK2wI0SJd0Q/640?wx_fmt=png&from=appmsg "")  
  
  
点击Finish，安装完成  
  
  
查看Ollama的版本号  
```
ollama --version
```  
  
2.下载DeepSeek-R1模型  
  
通过Ollama下载DeepSeek-R1模型  
了,Ollama共提供7个不同参数量的DeepSeek-R1模型  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8XcZQgAYAVXZm8sujMB9zrMLNmRIibJFJ3K5Ln91oyekNP90eQMvYzlA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8GKzOGBQQnuDL0ZMtpsGkwwh2d3qzwVf8X0D0vrdGkD6icKocWhvB0VQ/640?wx_fmt=png&from=appmsg "")  
  
  
参数量越大，代表模型推理能力越强，满血版的DeepSeek-R1参数量为671B  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU81xicicxn8gib1EiceHfQb8s4ypRLIRAzgRpibAJPMkiaucv4PfBjcIeYdJOg/640?wx_fmt=png&from=appmsg "")  
  
  
根据配置下载模型  
```
ollama pull deepseek-r1:1.5b
```  
```
ollama pull deepseek-r1:7b
```  
```
ollama pull deepseek-r1:8b
```  
```
ollama pull deepseek-r1:14b
```  
```
ollama pull deepseek-r1:32b
```  
```
ollama pull deepseek-r1:70b
```  
```
ollama pull deepseek-r1:671b
```  
  
3.在Chatbox里使用本地部署的模型  
```
https://chatboxai.app/zh
```  
  
相比Cherry Studio，Chatbox支持的客户端类型更多更全，从桌面客户端到手机app，都支持。按照上面的Chatbox官网链接下载安装即可  
  
  
把部署在本地电脑上的DeepSeek-R1集成到Chatbox里使用  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8RBTK8ibFqkpPGqraWCDu94L7HjITtn3ibVl23k4fljuCQl8PnQxaDhYA/640?wx_fmt=png&from=appmsg "")  
  
```
https://web.chatboxai.app/
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8qs5Liae2OAPYJTLfULBfqYXT2kEl4yPxwY2IFBctjYkcVKlhBofUiaicw/640?wx_fmt=png&from=appmsg "")  
  
  
打开Chatbox，点击左下角的设置，在模型提供里找到Ollama API。API连接点直接用默认的http://localhost:11434，然后选择安装好的DeepSeek-R1模型，点击保存  
  
![](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF04JWr23oMvwsJicOxDv8VU8HwAaia3L98zZaonN446pM9G8sRKJquzkJ5RVsQn0NlkI1R8icUunkCmw/640?wx_fmt=png&from=appmsg "")  
  
```
https://github.com/deepseek-ai
https://github.com/deepseek-ai/DeepSeek-V3
```  
  
推荐阅读  
  
[DeepSeek + Continue：Android 开发效率提升 10 倍的秘密！](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247497214&idx=1&sn=d3776e4e8ce79ffe90b533ae95255b10&scene=21#wechat_redirect)  
  
  
