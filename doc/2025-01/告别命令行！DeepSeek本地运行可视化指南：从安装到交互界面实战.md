#  告别命令行！DeepSeek本地运行可视化指南：从安装到交互界面实战   
原创 湘南第一深情  湘安无事   2025-01-31 12:13  
  
## 前言   
  
最近deepseek不是很火嘛，直接把美股干趴下，但是我去用deepseek发现注册繁忙，于是打算出个deepseek本地部署教程，但是又发现没有ui,深情哥这不费尽千辛万苦找了个ui给你们玩玩。![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPMNYZIt9x52Pl5tg5VGBibE1OwiatOGLNoDoq9wH9rAFlQTMz1aPyVFZg/640?wx_fmt=png&from=appmsg "")  
  
## ollama实现deepseek本地部署   
  
这里很简单，直接访问ollama官网   
```
https://ollama.com/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPBzsFUSCoN59p6fAuhfPIUGudmSic5OickWXyANAuqkDOKvXsTy71XP1Q/640?wx_fmt=png&from=appmsg "")  
先下载，然后酷酷给它安装好就完事了![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPiauWXMJXU2MPYBrN45JWA3Mv65gAPKNC4eIGEZN58R5GCUoI5jCOnSA/640?wx_fmt=png&from=appmsg "")  
直接点击安装就行![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPOWcoCV9wJ8ssib5WWiazsAw4JO5qeEWc263KBjoyTeg6eMibN3vYtMerQ/640?wx_fmt=png&from=appmsg "")  
然后命令行查看是否安装成功，出现下面这个情况就是成功了![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPyVkgeYBcXdDc04e2sib9Fq4ZAFw8dDPp3YG6cGgcib3vduP0kDyEv6HA/640?wx_fmt=png&from=appmsg "")  
倒回去官网搜索deepseek安装即可   
```
https://ollama.com/search?q=deepseek
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPpWd1I1JqB1lhW05vMB5aVSF58bLsicUYmfn68WbiatLUbCq3nTcYtYNA/640?wx_fmt=png&from=appmsg "")  
点进去，选择旁边的命令行下载即可![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPedicj4DsX5K7JrvILrYX1icH2rCBRh50teZsicfPFUXKQZXNXcpcmdzmA/640?wx_fmt=png&from=appmsg "")  
其实这里7b和14b代表参数规模，即70亿和140亿参数。参数越多，模型通常越大，效果可能更好。一般像深情哥的3060显卡用7b差不多了，显卡越nb就可以试试72b的。   
```
ollama run deepseek-r1:1.5b 为了示范用的1.5b 一般7b都能带动3060的显卡
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPNdFvc13IIHibXW7vRlm1yavcakIib1w9GWqvnVxWaXZXbDqiaIuEEUVqQ/640?wx_fmt=png&from=appmsg "")  
然后再次输入命令 就成功了  
```
ollama run deepseek-r1:1.5b
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPO4IOFVjXoODbCRDq3iaxOqa8llRTB5Sqq5Eq7euJHHYEX8LhOlRvyzQ/640?wx_fmt=png&from=appmsg "")  
## Gomoon实现ui交互   
  
命令行是不是看起来怪怪的，这里深情哥提供了ui界面Gomoon软件，适配所有的大模型，包括deepseek。   
```
https://gomoon.top
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPmcHO0CicumAcHVx0DwCjlXdpsxEGmhrYzBT8Xqic2OL9F5Xia4XYT1sMw/640?wx_fmt=png&from=appmsg "")  
直接下载就行，然后无脑安装，也可以联系深情哥获取![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPBwezKA4Ry9mU7HCc1aeV7ljibHyA6RicOYAy5Zwf76CiaWDbqUU4N9ibnA/640?wx_fmt=png&from=appmsg "")  
出现下面界面即可成功![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPcQicVlJzMWyDv3AiatoaBW6DcMruHNXg0Z6oAAdATpy5OnwkDge7UfwQ/640?wx_fmt=png&from=appmsg "")  
然后进行api配置，点击设置->Ollama 系列填入api地址和模型名字即可   
```
url地址：http://127.0.0.1:11434 
模型名字：deepseek-r1:1.5b
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwP5RhzEKWQd82oYhHFX7AGicHSZKcor8sLcOKDCxgbrXIXDDrwaicG4l5g/640?wx_fmt=png&from=appmsg "")  
然后使用界面问你想问的问题即可![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPjD7YIXicRsQiaicz841Pu8gFR1lMrGiaGtr5UEKMskLpnAS0ZcNXlibYIicQ/640?wx_fmt=png&from=appmsg "")  
这里也可以创建关键词助手，自己多玩玩吧![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYuEDAkPQqbS3ujMwWiaLmfwPKZoH9XnAKWG1twuscuURnc0FnAaxmKJy66U5W5icLmvD1xqkAm6gTYw/640?wx_fmt=png&from=appmsg "")  
  
## 思考和总结   
  
  
ollama这里是默认安装到c盘，所以导致模型都是下载到c盘的，这个问题我就不写了，有需要再写。有问题可以联系深情哥  
  
技术交流可以联系深情哥  
  
**END**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYvCicQ0uFJGlricBzMcQSeBRBwP7ibdL6QqtGBFpiaxB3icPcBggPgSlexibAk93icicUDPtOGOz3o3IWUE7A/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
