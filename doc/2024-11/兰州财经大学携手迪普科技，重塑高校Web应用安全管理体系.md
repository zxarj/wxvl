#  兰州财经大学携手迪普科技，重塑高校Web应用安全管理体系   
 迪普科技   2024-11-22 00:52  
  
自2018年教育信息化战略深入实施以来，教育行业对网络安全建设的重视程度日益提升，以《网络安全法》为基石，全面强化教育系统的网络安全防护能力。在此背景下，各大高校积极响应，不断推进信息化进程，并致力于构建更加坚固的校园网络安全屏障。然而，随着业务的不断增加，越来越多的Web应用需要进行管理和发布，给校园的Web管理工作带来了挑战。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X7M4u244hszwshsruOG6azcMt5f0Mp0UicicG8nYALOWehVAOeypcNV7M5f6fjSfPwhvNmicWtplh9a0v4YHVP2aQ/640?wx_fmt=jpeg&from=appmsg "")  
  
针对这一现状，兰州财经大学通过**部署迪普科技Web应用发布及动态安全防护系统**  
，有效解决了在Web管理工作中遇到的诸多难题。  
  
  
**痛点一：**  
  
**Web应用发布繁琐**  
  
  
学校涉及较多部门，百余个网站需要进行管理，在使用传统的Nginx做管理的情况下，每次进行Web发布、上下线时都需要大量的配置，耗费大量人力。  
  
例如使用Nginx进行HTTPS Web发布，需要进行以下配置：  
  
  
**配置后端服务**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UDtRRRv69cRMvUVNZt9kZHiaYqX79meWRfGzLibJ9P4VCS7icNyApAe9OA/640?wx_fmt=png&from=appmsg "")  
  
  
**配置监听端口及SSL证书（密钥、协议等）**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UPKvEiamRU79D7TWD2DnFiabdpQdU5LKiaGoAcMYrQjDJ5KJDnM8trflIg/640?wx_fmt=png&from=appmsg "")  
  
  
**配置HTTP协议、回源地址等**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UlFuADtq7BgGKZ3dMhGP2U2Xf9ZMuxsFBBrjhzN14aEmeSKicG6opGrw/640?wx_fmt=png&from=appmsg "")  
  
简单的一个Web发布会涉及到大量的命令配置，如果配置内容更多，复杂程度也会增加，可以想象，如果需要进行百余个网站的改动，耗时会成倍增长。  
  
由此可见，每次进行Web发布、变动，对管理人员来说都是一份“体力活”，如果能够提升效率将会大大节省老师的时间和精力。  
  
  
**迪普科技**  
  
**Web应用发布及动态****安全**  
  
**防护系统****解决困扰**  
  
  
  
**便捷配置，一键发布**  
  
站点管理功能可以快速添加站点相关配置，在一个界面实现域名、端口、证书、协议等配置，一键实现Web发布。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UZdicPiakyGL2G49HQ96C4je8ibk8GuPIzcgOibzPX9VKnNIzsVNfiaN9GQQ/640?wx_fmt=png&from=appmsg "")  
  
后端服务、长连接、回源地址等在Nginx需要不断写命令配置的功能，也可以在界面上**简单点击、填写就可以快速配置**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UeZlWfZWyNwwjcX2J3nBWmiaQMF7ldmU8v3qwqkhYQkVXIXgkwp1wuoA/640?wx_fmt=png&from=appmsg "")  
  
  
**批量管理，快速上/下线**  
  
当存在多个网站时，可通过**自定义网站标签**并根据标签进行批量操作、一键上/下线特定网站、网站发布时间可自定义，提高网站管理效率。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UtGKxJgbicb69jwTdh1Z6UrvaQcyJruWibRL1vZ0QpHWdaQGxnV8EV9bw/640?wx_fmt=png&from=appmsg "")  
  
  
  
**痛点二：**  
  
**Web发布、管理、防护割裂**  
  
  
学校采用Nginx实现Web发布，又额外采购了负载均衡产品、Web防护产品，多个产品进行协同操作复杂，往往需要登录多个界面进行操作，一旦某个Web业务需要改动，就会引起一连串的设备策略变化，牵一发而动全身，每次的业务系统升级都让老师非常困扰。  
  
例如学校进行了HTTPS站点升级，将老旧网站的HTTP协议升级为HTTPS协议，为尽可能保证报文加密传输，可能会涉及到多个设备反复卸载、不断修改策略。  
  
**Nginx修改配置，增加密钥、协议信息**  
  
  
**Web防护设备配置SSL卸载，修改站点防护策略**  
  
  
**负载均衡设备需导入证书，添加卸载策略**  
  
**迪普科技**  
  
**多功能合一，一体化防护**  
  
  
Web应用发布及动态安全防护系统是一款新型的整合Web管理&安全防护的产品，从整体上解决多设备协同的问题，在一个设备上满足HTTPS加解密、Web发布、Web管理、安全防护的要求，使整个方案变得简单。部署迪普Web应用发布及动态安全防护系统后，便**实现了多种安全、管理功能的合一，大幅提高了管理工作的效率**。  
  
**Web发布、管理**  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UYIqLIkvOqFhnEW7M3lhRyVCd7Pibd7UBG64t9VKthVuMbcMkSZA6MNA/640?wx_fmt=png&from=appmsg "")  
  
**Web防护**  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0U3SVhApSu8AGAu2JiaVJD2AI9gxHlzm33ZBFk5xBZNQeF6GT2ThVY5CQ/640?wx_fmt=png&from=appmsg "")  
  
**加解密（证书管理）**  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UAh2b6nemmQaX5KbUS2Mc5zuNibM4mWVQ8tNJFaFO6vxsJGF1oDFP6yg/640?wx_fmt=png&from=appmsg "")  
  
  
  
**痛点三：**  
  
**爬虫等自动化攻击难防御**  
  
  
在启用防护系统前，学校门户网站不时受到爬虫工具的侵扰，导致后端服务器长时间处于高负荷运转状态。在部署迪普Web应用发布及动态防御系统后，通过多种防护方式实现有效防护。  
  
  
**迪普科技**  
  
**动静结合，防护自动工具**  
  
  
系统采用动静结合的方式进行防护，静态防护通过爬虫特征库进行快速匹配，发现爬虫。而针对爬虫或其他自动化工具，也能够通过动态防御手段，通过特殊算法进行人机识别，自动工具无法获取到访问许可，保证站点安全，**有效地减少了爬虫等自动化攻击，降低了后端服务器的负载**。  
  
**动态防护：一键开启自动化工具防扫描**  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X7M4u244hszwshsruOG6azcMt5f0Mp0UIplr6qiaqwoJsnQVVCuaDIc563nfbDmRM0rZxbRckAa6dSwCa6fLgOw/640?wx_fmt=png&from=appmsg "")  
  
  
迪普科技Web应用发布及动态防御解决方案已经广泛应用于各省高校、高职等院校，为广大客户提供了高效、便捷的Web发布、管理能力，并且成功将Web发布、管理、防护等能力结合起来，打破了传统管理、防护割裂的现状，为高校Web一体化运维提供了新思路。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X7M4u244hszwshsruOG6azcMt5f0Mp0Um9Nps4gl39RkaomibvVbIhUDK9Bic8heLkwLq3iaHADrn2XD6EiaK6benQ/640?wx_fmt=gif&from=appmsg "")  
  
高校网络安全是维护正常教学秩序、保障师生权益、促进教育数字化转型的重要基石。迪普科技将通过持续的努力与创新，积极协助构建安全、健康、高效的校园网络环境，为新时代高等教育健康发展保驾护航。  
  
  
END  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X7M4u244hszwshsruOG6azcMt5f0Mp0UwkGcxicrBiboRD0WUg5D7RoVypaTguVXtaiapN54n07l0tym8XiczOIMYg/640?wx_fmt=gif&from=appmsg "")  
  
  
