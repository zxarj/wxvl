#  oss存储桶遍历漏洞利用工具   
d1sbb  夜组安全   2024-11-22 00:00  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**baobeiaini_ya**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2Xvvlzc5lra8XdgLYGCfX5ooaMiaUJy4vKvStTngQp4122jauXltltcCuYib5WBBdaXu5dh91dGvibyQ/640?wx_fmt=png&from=appmsg "")  
  
  
**01**  
  
**工具介绍**  
  
存储桶遍历漏洞利用脚本批量提取未授权的存储桶OSS的文件路径、大小、后缀名称提取的结果会自动生成到csv和xlsx文件中  
  
安装：  
```
pip3 install pandas
```  
  
使用：  
```
python3 ossFileList.py -u https://xxx.oss-cn-xxx.aliyuncs.com/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvStttMyUEPibXC3ibcqWiaX5Q3ic8ic9Ozav6Yw7NMublkY6TLXC4aDXRfh0xnw/640?wx_fmt=png&from=appmsg "")  
  
优化：1.自动生成的csv文件后，通过filetype拆分成不同的工作表，易读。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvSttxjBibESCXhUaA69Ppf1BEiaaBRABSgo6TorMnaIOp3iaQeQHO65jtagLQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvSttXoMHjYP7I8DTB1p82HPuV5PTDACD78KQYibXOq3B0vbmhCG9SPiblMnw/640?wx_fmt=png&from=appmsg "")  
  
2.修复XML解析有误，无法遍历的bug  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvSttypVo9cBDSdGTk4NcUnibfBlC0eLokQfcQAxp4RjVpmvpPae0U4M162A/640?wx_fmt=png&from=appmsg "")  
  
TODO:下个版本增加url批量   
```
python3 ossFileList.py -f filename
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvSttywfj6RUMz2X0JApUiav6OEqO1FtH2RqUVbPLHrKTFRVYSsHiajw6icmNA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WpBpmYhRkicghKQSynkvStticw69B0Ox5dl7Rnx4iaU2Xqc0HRORhdp6XpFRT0Yl8HXRarsfHrxY0ibw/640?wx_fmt=png&from=appmsg "")  
  
   
```
原作者：https://github.com/source-xu/ossx
```  
  
  
**02**  
  
**工具下载**  
  
**点击关注下方名片****进入公众号**  
  
**回复关键字【241122****】获取**  
**下载链接**  
  
  
**03**  
  
**往期精彩**  
  
[ 漏洞利用、shell反弹  | 一键利用工具 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492775&idx=1&sn=93a3a6836cb68f8168e9655508828d18&chksm=c36ba05ff41c29491a88ff7e29c2c8d8c421adb2a70475a6c9277b9782ea264d8cbd037b8032&scene=21#wechat_redirect)  

						  
  
  
[ Jeecg-boot密码离线爆破 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492776&idx=1&sn=bedc90ea00564ef67b2ea85427c80c24&chksm=c36ba050f41c29460082bb27c40ac623605ce36a23c5faf61c1701503d160b05c9bb2333d990&scene=21#wechat_redirect)  

						  
  
  
[ apk文件加固特征检查工具，汇总收集已知特征和手动收集大家提交的app加固特征，目前总计约170条特征，支持40个厂商的加固检测 ](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247492739&idx=1&sn=8ccd6d896f7a32bb85d0d49e2aee6f64&chksm=c36ba07bf41c296d9110d2d0c5959e9b0f8d9e8fe105bfe00ef75d7e13b0ba0e0d8f802f9b1d&scene=21#wechat_redirect)  

						  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557 "")  
  
