#  万户 ezOFFICE govdocumentmanager_judge_receivenum.jsp SQL 注入漏洞   
Superhero  Nday Poc   2025-05-25 09:42  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkYN4sZibCVo6EFo0N9b7Kib4I4N6j6Y10tynLOdgov9ibUmaNwW5yeoCbQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkhic5lbbPcpxTLtLccZ04WhwDotW7g2b3zBgZeS5uvFH4dxf0tj0Rutw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCk524CiapZejYicic1Hf8LPt8qR893A3IP38J3NMmskDZjyqNkShewpibEfA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
内容仅用于学习交流自查使用，由于传播、利用本公众号所提供的  
POC  
信息及  
POC对应脚本  
而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号Nday Poc及作者不为此承担任何责任，一旦造成后果请自行承担！  
  
  
**01**  
  
**漏洞概述**  
  
  
万户 ezOFFICE govdocumentmanager_judge_receivenum.jsp 存在SQL注入漏洞，攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码,站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。  
**02******  
  
**搜索引擎**  
  
  
FOFA:  
```
title="万户ezOFFICE协同管理平台" || title="ezOFFICE协同管理平台" || title="Wanhu ezOFFICE" || title="ezOffice for iPhone" || body="EZOFFICEUSERNAME" || body="whirRootPath" || body="/defaultroot/js/cookie.js" || header="LocLan" || (banner="/defaultroot/sp/login.jsp" && banner="Set-Cookie: JSESSIONID=") || (header="Set-Cookie: OASESSIONID=" && (title="ezOFFICE" || body="whir.util.js" || body="var ezofficeUserPortal_ = Cookie(\"ezofficeUserPortal\");"))
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDdskYv70gGg9XAOIRRN7Xqts3tGLBdibma0zDLFAib4nfh5vFE4Hh5qnPEQ/640?wx_fmt=png&from=appmsg "")  
  
  
**03******  
  
**漏洞复现**  
  
延时4秒  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDdsdwngmuB2bJpy95aZGZUC5GHDCjLLLfETxia7tUTibSaAibibjf9envpd7w/640?wx_fmt=png&from=appmsg "")  
  
sqlmap验证  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDds3H4PonNicSpqWJ5RNZTZCFKKKicaWnXMrXvEtpM5FGIA709tTOXGvibgQ/640?wx_fmt=png&from=appmsg "")  
  
  
**04**  
  
**自查工具**  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDdsnDEjMicSN6wZ2qzYXqses2xufH3ZaHKgHI7Mc42yRDzOzviabsHShI2A/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDdsbzbNQKweNgX1nNyewMBGHia9aRvEYdnKTDdz2JjmjChFfgbaaJT0obg/640?wx_fmt=png&from=appmsg "")  
  
xray  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJue4fwJLvvy34A6HWfdDdsSoaODbQo043niaiaCDp8FyxKnLMheZ0vpeNTpx7aw6h3JLRyIODWoIbA/640?wx_fmt=png&from=appmsg "")  
  
  
**05******  
  
**修复建议**  
  
  
1、关闭互联网暴露面或接口设置访问权限  
  
2、  
升级至安全版本  
  
  
**06******  
  
**内部圈子介绍**  
  
  
【Nday漏洞实战圈】🛠️   
  
专注公开1day/Nday漏洞复现  
 · 工具链适配支持  
  
 ✧━━━━━━━━━━━━━━━━✧   
  
🔍 资源内容  
  
 ▫️ 整合全网公开  
1day/Nday  
漏洞POC详情  
  
 ▫️ 适配Xray/Afrog/Nuclei检测脚本  
  
 ▫️ 支持内置与自定义POC目录混合扫描   
  
🔄 更新计划   
  
▫️ 每周新增7-10个实用POC（来源公开平台）   
  
▫️ 所有脚本经过基础测试，降低调试成本   
  
🎯 适用场景   
  
▫️ 企业漏洞自查 ▫️ 渗透测试 ▫️ 红蓝对抗   
▫️ 安全运维  
  
✧━━━━━━━━━━━━━━━━✧   
  
⚠️ 声明：仅限合法授权测试，严禁违规使用！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwI0beBCCyKGykkAazuPyvibgC0ooBGy9elQQ72f1WIB73UDYuPhx8cnCobvnOBdTcxmdwBbt2eAYIQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
