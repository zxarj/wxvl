#  CNVD通用证书挖掘思路   
什么安全  什么安全   2025-02-06 09:23  
  
  请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责！  
  
    
先说一下我吧，我一般在CNVD提交漏洞都是为了拿到证书，毕竟是国家单位颁发的，还是有点用的。达不到证书发放条件的我一般选择在其他正规平台提交，相信大家都懂的。  
  
  那么想要获取证书，首先要知道平台对对漏洞颁发证书的条件。进入CNVD官网右上角选择工作体系-奖励计划中会有明确说明。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13VNas6BQibNNLF8RjibqrtC8Ue15Fr9Jwg7IlUKUhlVEFICludibylBLmg/640?wx_fmt=png&from=appmsg "")  
  
对于通过CNVD归档的原创漏洞，CNVD将对漏洞进行原创漏洞奖金积分评分。积分评定具体参见《CNVD原创漏洞积分评分细则》。  
  
时限要求：在漏洞归档后1个工作日内。  
  
对于中危及中危以上通用型漏洞（CVSS2.0基准评分超过4.0分），以及涉及党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件型漏洞(后续对事件型漏洞证明颁发标准将参考中央网信办颁布的关键基础设施相关定义和分类)，CNVD将给予原创漏洞证明（即CNVD漏洞证书，电子版），该证明可通过编号在CNVD官方网站进行查询跟踪。  
  
时限要求：按周对上一周归档漏洞且满足证书颁发条件的进行批量制作。  
  
总结一下就是以下几点：通用型漏洞一是所涉及的产品厂商注册资金不低于5000W，二是提供最少10个复现案例，并复现其中3个。漏洞级别为中危及以上。  
  
事件型漏洞，  
涉及党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件型漏洞(后续对事件型漏洞证明颁发标准将参考中央网信办颁布的关键基础设施相关定义和分类)，CNVD将给予原创漏洞证明。  
  
平时其实跟大家一样，都是FOFA、鹰图、零零信安等类似的资产收集平台去搜索关键字、指纹特征等去搜索。  
  
也可以多去参考其他老师的文章，多方面下手，这样会更好的掌握方法，我目前都是放弃登陆框的漏洞挖掘，个人感觉不如逻辑、跟未授权，因为开发过程中程序员不总是在绕逻辑。  
  
那么提交漏洞后就是一个比较漫长的等待，三轮审核，一审、二审、三审，时间一般在一个月左右吧，但是最近我发现这段时间的审核周期更长了，不过也不要太着急，都会给审核的，提交后也要定期关注一下，可能有材料或者佐证信息不足的退回修改的，及时修改再提交。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13atZG7JKZz3cNnia5M7LNYmgTHDpH8CSaiaEElKEQ4ebkm5sznHPeZbBA/640?wx_fmt=png&from=appmsg "")  
  
满足条件的，证书会自动发放到账户。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13COclMWEIUf0OicGtoibKP2FGmCWMJwJVNgqZWyVf5UpibS2cfZA4xF9NQ/640?wx_fmt=png&from=appmsg "")  
  
希望各位老师多多拿到证书，早日拿到证书。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13M0Syib8RfGYgNM8jZuKvicBq1sez7z35DaCWrxZCf9LdLdTRHEyx3KyQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13aNtEibwlonFc2fBWurgswEfVhu1vbEa9EwdadBNToBziaXsFBIo40Vew/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/w0DeFbFI15weS0qV0ad63uEzhBeycL13e7HTWWHcT236DMtTv74JyIjHMPwZia1abO6ssxzVJhq6EeOaeje9qgQ/640?wx_fmt=png&from=appmsg "")  
  
小  
知  
识  
  
  
  
  
**依据《刑法》第285条第3款的规定，犯提供非法侵入或者控制计算机信息罪的，处3年以下有期徒刑或者****拘役****，并处或者单处****罚金****;情节特别严重的，处3年以上7年以下有期徒刑，并处罚金。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Gn0JbCnxttRbj4Mib3fcSfwr0tP4UxXtjf47HFwaZcgwWStzGNLNMlGKQJz902fHTT8PCfOwHedLqarXh0eC9KQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
声  
明  
  
  
  
**本文提供的技术参数仅供学习或运维人员对内部系统进行测试提供参考，未经授权请勿用本文提供的技术进行破坏性测试，利用此文提供的信息造成的直接或间接损失，由使用者承担。**  
  
  
  
