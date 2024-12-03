#  Burpsuite存储桶配置不当漏洞检测插件   
黑熊安全  黑熊安全   2024-12-03 03:30  
  
亲爱的读者，我们诚挚地提醒您，黑熊安全公众号的技术文章仅供个人研究学习参考。任何因传播或利用本实验室提供的信息而造成的直接或间接后果及损失，均由使用者自行承担责任。黑熊安全团队及作者对此概不负责。如有侵权，请立即告知，我们将立即删除并致歉。感谢您的理解与支持！  
  
## 用法  
  
存储桶相关配置检测自动化，访问目标网站将会自动检测，如：访问的网站引用存储桶上的静态资源，就会触发检测逻辑,将指纹识别方式修改了下，通过server头及域名中的一个方式进行判断，另外由于敏感信息误报较多，已经取消了。  
  
## 导入burpsuite  
  
检测结果，目前支持阿里云，华为云，腾讯三个厂商的检测，存储桶文件遍历，acl读写，Policy读写及未授权上传![](https://mmbiz.qpic.cn/mmbiz_png/kmmKLfv0wVicrUvHjj7IOiczQ9GjIUic1uOpTCVAGn8hc7Nf0pwO8IEGzBWoThqvIKSEv29EOIuQKx9PNAcJHcImg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kmmKLfv0wVicrUvHjj7IOiczQ9GjIUic1uOUI2PszQPfWf61n0LUMhNJLR6iaZMyAn0FP8icGkfM93TDegxqEK4BjlA/640?wx_fmt=png&from=appmsg "")  
  
**使用的新版bp接口，所以版本有要求，jdk17**  
## 打包  
  
**mvn package 或者直接用打包好的，放到下载链接里了**  
  
**下载链接：https://pan.quark.cn/s/f273b9d53b4f**  
  
  
已发布文章所有下载工具连接：https://pan.quark.cn/s/0c1cbe67aec4  
  
承接SRC众测、网站众测、红蓝攻防、代码审计、培训、公众号广告等业务。微信：xxbearyyds  
  
  
