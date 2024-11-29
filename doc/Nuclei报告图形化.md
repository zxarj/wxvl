#  Nuclei报告图形化   
原创 【白】  白安全组   2024-11-29 07:28  
  
Nuclei可以与ProjectDiscovery云平台集成，以简化Nuclei结果的可视化并且快速生成报告。  
  
1、访问  
https://cloud.projectdiscovery.io/sign-in  
获取api  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUbHzcftBqU0ISUoZrHSJiaWMP1zJ0DcibEvBKmsTCYwJoKYYagjbn0nuEztxn70KjezOAiaZabr8R6xA/640?wx_fmt=png&from=appmsg "")  
  
cca93f45-bc41-4cca-a642-c757797aca78  
  
2、使用命令配置nuclei  
  
使用命令：  
  
nuclei -auth  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUbHzcftBqU0ISUoZrHSJiaWMcb4h98vmVnlrltv0gxKTEeyibX9dTMuWh9YjN1GEvoaA9njiaTGqzHJg/640?wx_fmt=png&from=appmsg "")  
  
然后我们这里直接粘贴，这里记得是看不到的，粘贴之后直接回车就可以乐  
  
3、之后，如果我们需要执行扫描，并且将结果上传云端，就在运行的时候加上-cloud-upload  
  
nuclei -u http://www.xxxx.com -t cves/ xxx.yaml -cloud-upload -ms  
  
扫描完成之后，会显示一个url，访问之后，可以在平台上查看结果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUbHzcftBqU0ISUoZrHSJiaWMAH6wox3SVCo6Vxpyibw7yKMeuzz4u5cKOJ9opj2s7b2dHDEyDggu6Tw/640?wx_fmt=png&from=appmsg "")  
  
最后会有这个地址，我们访问登录就会进入到可视化界面中访问了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUbHzcftBqU0ISUoZrHSJiaWMKcJbqR57YpdPjBg8pm5zbULzJmW9DWvcLicAFHEkpNWhibXNmF6WuLfw/640?wx_fmt=png&from=appmsg "")  
  
