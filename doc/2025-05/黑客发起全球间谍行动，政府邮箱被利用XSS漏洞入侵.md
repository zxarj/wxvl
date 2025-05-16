#  黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵   
 安全客   2025-05-16 06:40  
  
近日，安全研究人员披露，一个名为**“RoundPress”**  
的全球网络间谍活动正在持续展开，攻击者通过 Webmail 服务中的数个XSS漏洞，对全球多国政府和关键机构发起邮件窃密攻击。该行动被认为与黑客组织 APT28（又称“Fancy Bear”或“Sednit”）有关。  
  
  
**01**  
  
**行动时间跨度长，涉及目标广泛**  
  
  
这项网络间谍活动始于 2023 年，并在 2024 年持续扩展攻击范围。被攻击的 Webmail 系统包括 Roundcube、Horde、MDaemon 及 Zimbra。  
  
  
根据披露，遭到攻击的目标涵盖：  
  
  
希腊、乌克兰、塞尔维亚、喀麦隆等**国家政府部门**  
；  
  
乌克兰和厄瓜多尔的**军方单位**  
；  
  
乌克兰、保加利亚、罗马尼亚的**国防企业**  
；  
  
乌克兰和保加利亚的**关键基础设施单位**  
。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6xickNTmMtBic7UVU4fsjkCV2kAfC2UxribYeiayeoFHbk49NI5Ft6dFWlIB7plR3BMxosBkl8kS0ibVg/640?wx_fmt=jpeg&from=appmsg "")  
  
攻击目标分布（来源：ESET）  
  
  
**02**  
  
**打开邮件即中招，攻击过程零交互**  
  
  
攻击从一封带有当前新闻或政治内容的钓鱼邮件开始，攻击者常引用**真实新闻片段**  
提升可信度。  
  
  
邮件正文中嵌入恶意 JavaScript 脚本，借助 Webmail 前端页面的 XSS 漏洞实现执行。受害者**仅需打开邮件即可触发攻击，****无需点击链接、输入信息或其他操作**  
。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6xickNTmMtBic7UVU4fsjkCV6sn8ibSh3HI11voB7064QVbwib4rWRvCS4QAcJnpfHMibfFrJBdXiaDibSQ/640?wx_fmt=jpeg&from=appmsg "")  
  
攻击链概述（来源：ESET）  
  
  
攻击脚本不具备持久化能力，但足以在一次执行中完成以下行为：  
  
  
创建隐藏输入字段，引导浏览器或密码管理器**自动填充邮箱凭据**  
；  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6xickNTmMtBic7UVU4fsjkCV7jhuuRLSdUXe024kxj7ljZr8gaGMeQtQEt1wwVKjR2rYPm9pKNUcFw/640?wx_fmt=jpeg&from=appmsg "")  
  
凭据窃取函数（来源：ESET）  
  
读取页面 DOM 或发送 HTTP 请求，获取邮件内容、联系人、Webmail 配置、登录记录、2FA 设置及密码等信息；  
  
将采集数据通过 HTTP POST 请求发送至攻击者控制的远程服务器。  
  
  
根据目标 Webmail 产品的不同，攻击脚本具备略有差异的功能模块，表现出**高度定制化**  
。  
  
  
**03**  
  
**涉及多个严重 XSS 漏洞**  
  
  
“RoundPress” 行动利用了多个 Webmail 产品中的 XSS 漏洞，进行恶意 JavaScript 注入。具体漏洞包括：  
  
  
**Roundcube – CVE-2020-35730**  
  
2023 年被用于攻击的存储型 XSS 漏洞，攻击者将脚本嵌入邮件正文，用户在浏览器中**打开即被执行**  
，导致凭据和数据泄露。  
  
  
**Roundcube – CVE-2023-43770**  
  
2024 年初被利用的漏洞，Roundcube 在处理超链接文字时存在过滤不当问题，攻击者可插入 **<script>**  
标签实施攻击。  
  
  
**MDaemon – CVE-2024-11182**  
  
2024 年底被用作零日攻击的 HTML 解析器漏洞，攻击者构造畸形 title 属性及 noembed 标签，通过隐藏的**<img onerror>**  
实现 JavaScript 执行，获取凭据并**绕过双因素认证**  
。  
  
  
**Horde – 未确认 XSS 漏洞**  
  
黑客曾尝试在 **<img onerror>**  
 中注入脚本攻击 Horde，但疑因新版系统具备过滤机制未能成功，具体漏洞未被证实，疑似已被修复。  
  
  
**Zimbra – CVE-2024-27443**  
  
该漏洞出现在 Zimbra 的日历邀请处理功能，攻击者利用 X-Zimbra-Calendar-Intended-For 头部未过滤输入，实现 JavaScript 注入，在用户查看日历邀请时执行。  
  
  
虽然尚未发现 2025 年有明确的 RoundPress 攻击活动迹象，但研究人员指出，鉴于主流 Webmail 产品中仍持续曝出 XSS 漏洞，黑客组织所使用的攻击技术具备**高度可复用性**  
，仍对全球政府机构及关键行业构成潜在威胁。  
  
  
消息来源：  
  
https://www.bleepingcomputer.com/news/security/government-webmail-hacked-via-xss-bugs-in-global-spy-campaign/  
  
  
推荐阅读  
  
  
  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-shadow: rgb(0, 0, 0) 0px 0px 0px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">01</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649788563&amp;idx=1&amp;sn=b342ee39e53f84204ba881a7b078f5ed&amp;scene=21#wechat_redirect" textvalue="欧洲漏洞数据库（EUVD）上线" data-itemshowtype="0" target="_blank" linktype="text" data-linktype="2">欧洲漏洞数据库（EUVD）上线</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">02</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;color: rgb(87, 107, 149);text-decoration: none;-webkit-user-drag: none;cursor: default;max-width: 100%;font-family: &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 12px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: 1px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649788555&amp;idx=1&amp;sn=85759a0ebd4a25a7607e07d309ef2450&amp;scene=21#wechat_redirect" textvalue="德州14亿美元隐私诉讼和解再创记录" data-itemshowtype="0" target="_blank" linktype="text" data-linktype="2">德州14亿美元隐私诉讼和解再创纪录</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">03</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;color: rgb(87, 107, 149);text-decoration: none;-webkit-user-drag: none;cursor: default;max-width: 100%;font-family: &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 12px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: 1px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649788548&amp;idx=1&amp;sn=f494f2b0019b53b104727c1645c848af&amp;scene=21#wechat_redirect" textvalue="勒索风暴席卷金融行业" data-itemshowtype="0" target="_blank" linktype="text" data-linktype="2">勒索风暴席卷金融行业</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr></tbody></table>  
  
  
**安全KER**  
  
  
安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6xickNTmMtBic7UVU4fsjkCVHsrt9L5tCPM1IIcqJRC93zMhZJLeHib0Zzs7WdK5NQEMibFdX5b2mt1Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6xickNTmMtBic7UVU4fsjkCV3ct2Olt2rZnBCPh5H2TX9mFIEvOI9O8dAyBe9HFwJMbR20qUVyfLvA/640?wx_fmt=png&from=appmsg "")  
  
**注册安全KER社区**  
  
**链接最新“圈子”动态**  
  
