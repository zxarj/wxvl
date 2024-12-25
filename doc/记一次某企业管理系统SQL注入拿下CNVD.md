#  记一次某企业管理系统SQL注入拿下CNVD   
原创 zkaq-小博  掌控安全EDU   2024-12-25 04:00  
  
扫码领资料  
  
获网安教程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
# 本文由掌控安全学院 -  小博 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（https://bbs.zkaq.cn）**  
## 一、资产发现  
#### 通过漏洞挖掘过程中发现该系统存在sql注入  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onlEtdG5cjcS10Z0rWaavwbPc5Bcc00tFzYQmpec88pJvr6hOxFicsN0Q/640?wx_fmt=png&from=appmsg "")  
  
img  
#### 1.二话不说先来个单引号显示 ‘011111111111111’’) )  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onnRYuEqhiasHgeYHCLMPl8HeXAE53Qybe5leE5QwIDicAJIANb0L2MVPQ/640?wx_fmt=png&from=appmsg "null")  
  
img  
#### 再来一个单号试一试可不可以把他闭合掉  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onmsMfvs7t7wwYIjhbiciaYu4HXfa8HDRe5WIX8lyibL1fKQ3NGWjncW7dg/640?wx_fmt=png&from=appmsg "null")  
  
img  
#### 换成报错注入的poc  
#### 发现右边的括号被转义掉了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4on6tcd7OZcic6VReGPcKMgCugrd2D3Gmia96EmcU7a3huwXyEaYJC4FOaA/640?wx_fmt=png&from=appmsg "null")  
img  
#### 在后面加上and试一试  
#### 成功报错回显出库名  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onc0W2d2X7Q1f9htHE8mf1sRJ9p2qGUyFficU1p88MTcWujno0SuPMKGg/640?wx_fmt=png&from=appmsg "null")  
  
img  
## 二、通用漏洞挖掘  
#### 发现技术支持的供应商公司  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onZZX0jLfhFlmpmDJ3KTAM3DaTiam1O1QvYXuzd493FNLDRjuFuv9Xf5A/640?wx_fmt=png&from=appmsg "null")  
img  
#### 1.通过公司名字查询系统名称，通过系统名称查询到图标信息，通过图标的icon信息去查询资产，通过鹰图查看到好多资产，通用漏洞拿下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onFkzsHzh6newF6ONFksOicCGLXuAuHM10zqPSialCQPtr9WibURGdU3ziaw/640?wx_fmt=png&from=appmsg "null")  
  
img  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onViaalicAXiaoibBDLMjX9DxL9WU0rXVvO4zyUZDSf0qGicrdiaPaUvicr9h0A/640?wx_fmt=png&from=appmsg "null")  
img  
## 三、通用漏洞经验总结  
#### 找到开放供应商，去站长之家查询开发的系统，系统图标信息查询存在的资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmcvGjgVJicscwWb4BFz4onicpmMEd88naGOGtgvFMN0iaq53tqLrIfzMv4FVRc1ZJG6vx03QkzfoHw/640?wx_fmt=png&from=appmsg "null")  
  
img  
```
```  
  
  
  
