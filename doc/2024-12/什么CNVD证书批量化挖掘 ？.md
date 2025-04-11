#  什么CNVD证书批量化挖掘 ？   
原创 思极安全实验室  思极安全实验室   2024-12-01 14:20  
  
- 免责声明  
  
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
-   
**前言：**  
  
    有些朋友平时可能会借助 fofa 挖掘 CNVD 证书或者通用漏洞。通常大家使用的语法可能是(title="管理系统" || title="登录") && country="CN"，接着去寻找指纹数量大于 10 的网站。找到这些网站后，再去查找开发它们的公司，以确定资产是否大于 5000 万。然而，这样很难确定网站的归属公司。后来，增加了 body="技术支持"这个语法，有了这个语法后，就能够比较容易地确定网站的开发公司。之后，还写了脚本去遍历带有指纹的网站，虽然通用网址收集全了，但仍需要逐个打开去查看网站开发厂商，再确定厂商注册资金是否大于 5000 万。  
  
    后来发现 fofa 可以直接搜索公司名字，这样就能直接搜索出该厂商所开发的网站资产。于是，我有了一个想法，直接通过 fofa 遍历资产大于 5000 万的公司，然后配合指纹提取，这样就可以直接提取出满足条件的网站。  
  
废话少说，直接上工具：  
  
****- ## 工具使用：  
  
    需要  
fofa  
普通会员或高级用户的  
fofa_token  
值并添加到  
python  
程序开头部分如下图：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbhXia1Nan7PrUIQrgcqbVhyPiaeMUliaxhKDMUALch3JfQrdO02c6rTsWg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbwqnUX54US1M1smzXSNNEiavd0Tk7kZYOFcqYfBqYAGQsx5zmNYhr6Dw/640?wx_fmt=png&from=appmsg "")  
  
将大于  
5000W  
资产的公司放到  
gs.txt  
当中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbheibkaqm5OebG4ibhuB3hcCib3w16gHHiaW9ESQYB9PNlYibh4FuzLxDDYw/640?wx_fmt=png&from=appmsg "")  
  
运行结果会保存到ip.txt当中如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlb4noWqibYxb8LFfOZCLfX5Vib28hIGrxHeGlVPPqibdkKecsNiaEF1OnPEA/640?wx_fmt=png&from=appmsg "")  
```
这里对应情况为：
    公司名^^^指纹条数^^^标题名字^^^网站网址^^^搜索指纹
```  
  
    这里可以创建一个  
xlsx  
，将此文本文档导入进去  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbwibK8EcicAgXtnIjBiaRlaUbgibKJa8nykw3wdzf8w2zgNj51TB3LakvWg/640?wx_fmt=png&from=appmsg "")  
  
最终结果：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlb8YbArO4ZFw8sv3iawfg1N0sGTfkhYystKZpWRBVaLZib10gsDwllXLEw/640?wx_fmt=png&from=appmsg "")  
  
工具下载：20241201  
  
  
 正式运营星球：  
  
     
     星球内容包括但不限于：SRC/CNVD/攻防真实漏洞案例分享；自研工具或二开工具分享；会员拉群不定期直播；漏洞分享/资料分享等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbWPaIrbvFLXPImyBay0OILfKC14HQwNIQ5dy6syGpM8eFstRhnnz5jg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbu957uaDNWD9BRbNvXNhd5WpicYibuZLVfYicW1b0OCiauDWUwKs01ibKbQw/640?wx_fmt=png&from=appmsg "")  
  
****  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbj3x2UicW3ZKCicEFQn7p61cbBiaVvVP1X3DYnib26KZ01xbMlpaL3B4WyQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbicpc7fxib63lpoQSHbHI7L9F2qLHLAQ7bTWNiczic44JrO3zBJ2XUxia3cg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbFzlWlgH1Pic2nhrLbaH6tf4BwFumwNlZZ1b1KgjwiaPicZHs3apia89NZA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlbT559Q82UMoYBfSVyvial7xP0icl7ibSI55gOicWOhFAICVRl7VOHkq5ibFA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1znIwPOw2JJmYIXoz2kFV9hw3vMkaXlb3L5icetK3mwicJDeiaoo0B2zttBmyKrkgQWPfkKNft1LP7Wst4HRXM7ZQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/ibZ6uZjjH3v7LQZwTb4qED3KvozKicnJd9ejpVoCntCRqf53IiaK2T3myzcUn5sswkUPfpQj1KHAALFcMFNYjfriaw/640?wx_fmt=gif&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
  
