#  某云盘系统 API 端点无限制上传漏洞解析   
Massa  菜鸟学信安   2025-05-09 00:30  
  
### background  
  
在某次赚钱的时候,发现出现了这个系统的低版本 搜索了很久相关只找到了一个  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ib4IoiczUiaq8IF5qtX7EjV1Kkca1RqoChkIrafJZry2ZS7SJYF06CJgFw/640?wx_fmt=png&from=appmsg "")  
  
  
简短的一句话 但没有其他漏洞细节 于是本地搭建挖一下  
### 0x01 漏洞限制条件  
  
![image-20250306174220208.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibhhW95UROE0bIDetUIEz1kjebTt1k9A4WOUIBIVedEThjYbKdxmbsjQ/640?wx_fmt=png&from=appmsg "")  
  
首先是需要一个账号来调用后台的插件  
  
但是本套系统默认两个账号  
  
guest:guest demo:demo  
  
还有一个就是要知道web的路径 当然这个后面说  
### 0x02 漏洞分析  
  
定位到函数 发现有一个in['file']的参数  
  
![image-20250306174557708.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibNeicIlyRl9NwltlsCCIje1LvvUI0IkFuxmRAgwMbGa98GRkAiacXibU4A/640?wx_fmt=png&from=appmsg "")  
  
跟进in 在controller里面可以看到这个参数  
  
![image-20250306175026755.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibgwCOlBzBQh6C5xjfib4PUPEibOSdGAQJYNomaia8TWWFclG1acblYoO5w/640?wx_fmt=png&from=appmsg "")  
  
![image-20250306182032074.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibiaPGkjISk7c4iaxdedkw9cDmrGXIIiaFD61fmd8OsvYyxfjKVCTRCsOgA/640?wx_fmt=png&from=appmsg "")  
  
  
还是全局变量 很容易判断他可以直接传参数  
  
跟进这个可以发现有一个get_path_ext  
后缀  
  
![image-20250306182255890.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibHsc7F4H4AR0bnBHBfqAhlm2LVJXVUJf86dlAk5JSVrWSjiaOEUjQMyg/640?wx_fmt=png&from=appmsg "")  
  
可以发现只限制了数量和一些不可见字符 并没过滤php  
  
继续跟进unzip_filter_ext 可以发现他过滤了 .user.ini .htaccess  
  
![image-20250306182624887.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibAhyTsHlLYJRwY1Jwpe4R9GZeXiaZEHsTNseHM8pflOFzPSEq5WqfxPQ/640?wx_fmt=png&from=appmsg "")  
  
但是有一个checkExt检查后缀 但是逻辑有点问题  
  
在这里有一个不允许的名单  
  
还会不断的merge  
  
![image-20250306185117546.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ib5rK5pY05UlNKQla5YgsP1DofEEg3T4dP72gqZ4IibeJch726uabKn2g/640?wx_fmt=png&from=appmsg "")  
  
在这里进行判断  
  
![image-20250306185314860.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibg6HSlTKZWAaOL8rKzibRjxpSoQdOZR6yAt5RhlQbOkAnPfPGwCSscmg/640?wx_fmt=png&from=appmsg "")  
  
  
逻辑错误点在这里 我们这里的$file是php 而后面的则是.php  
  
因为stristr的意思是在前面的字符串查找后面的 而在php字符串里并不包含.php  
  
所以在这里我们可直接传入php  
  
![image-20250306190635350.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibFvKuwRCxLibtSCkzs2sZp9d53Px5mlQ8iacgibyN1SFa21v3DxjbgwqWQ/640?wx_fmt=png&from=appmsg "")  
  
打印了下 $infoData发现为NULL 那后面$linkfile就是单纯的网页地址  
  
而且他会对一个url发起请求并保存文件  
  
我们可知$cachefile 的后缀是php 其实就可以直接写文件了  
  
在目录下放一个/1.php的马  
  
![image-20250306194818702.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibclNZxRlPN4hEv4wtLjPaN67Af7pRYkMHQFjp3L2LhJY90RLzE1zdYA/640?wx_fmt=png&from=appmsg "")  
  
直接进行访问  
  
![image-20250306191647101.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibaO7Uq2jflshLLcIM0Z1N52NwQLVkibnCynjSwzKseoR3tFialt1xfSrA/640?wx_fmt=png&from=appmsg "")  
  
发现在响应头里会有php文件名 但实际上  
  
![image-20250306191716494.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibznuztpuCdG5lWDAyJCoDNW0MtNnhA2ia8CWibDe3iaicicG7G46MXa6uP8g/640?wx_fmt=png&from=appmsg "")  
  
在这里也写了完整的生成语句  
  
![image-20250306191943227.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibAouWziaywEpbicqQNRPcqVAoGPVtluTOAhQyswYhuMs2vruzBYrKA9jQ/640?wx_fmt=png&from=appmsg "")  
  
但是我们发现在生成文件的时候还是有一个目录的  
  
![image-20250306192008663.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibvVXLbhMlR5ngOTEKmYsZe5VdFIibLQ9KQicbU4eHJ7icibTGuwvxBldgDA/640?wx_fmt=png&from=appmsg "")  
  
回到刚才代码  
  
我们查看cacheFile类  
  
![image-20250306192121007.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibqyeK3XrO9ndkEUsQoZUZU2JKztDwjPgoHFVnCSj4MtyNSWWCYbjPzg/640?wx_fmt=png&from=appmsg "")  
  
在这里有一个hash_path  
的生成  
  
可以选择下断点 或者直接var_dump  
下变量  
  
发现大致目录如下  
  
![image-20250306192340806.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibooPGxiasZbgBSKVuibEX80lsPIP23BUVYjvBuQPiaNq6xHCgZL7GYtrtQ/640?wx_fmt=png&from=appmsg "")  
  
其实可以推断出来 /var/www/html/data/User/guest/home/ 为一般漏洞利用的hash_path  
  
而且你会发现虽然说他在前面设置了一个随机生成的系统密码  
  
但实在底下只是进行了md5的编码就把$path写进来了 所以  
  
![image-20250306194548339.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibibCiaibEfBcCamoqznQJV2Llbrmq2q9yiaia4Ape90xlCVQTAOcCjicH7SvQ/640?wx_fmt=png&from=appmsg "")  
  
  
![image-20250306194412913.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ib2NPcic9bMpTYWlia7ibHibY9TYY5Xh0w95QKtupp1Vc6Rr5kT8ibPV001kQ/640?wx_fmt=png&from=appmsg "")  
  
只要文件不变 md5值是不变的  
  
![image-20250306194654634.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibCd1oQlz5zicUNuODP29ehrjhYf6S6d5yMn61rFDAWAPdibCPcjIILicGA/640?wx_fmt=png&from=appmsg "")  
  
构造poc即可写木马  
### 0x03修复方案  
  
官方的修复中  
  
![image-20250306194957952.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ibDzPbVXeJK02FJuicFG0OVQicZyoOkMlib0usrZE2tLS3rRIQxQcIqtB9g/640?wx_fmt=png&from=appmsg "")  
  
在这里把文件返回头给注释掉了 但是我们上文提了自己生成也可以  
  
可以看到在path生成上完善了 拼接了$pre 没办法再进行路径的查找  
  
![image-20250306195030619.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgF6wQwLQssSvFeznUQ7cE0ib1aYTRrvRZDia8MqeaJmlfFOjmreXcJqw80HMelcNHnHWLeKce6XAia2Q/640?wx_fmt=png&from=appmsg "")  
  
**文章来源：奇安信攻防社区**  
  
**链接：https://forum.butian.net/article/673**  
  
  
