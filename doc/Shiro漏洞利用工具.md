#  Shiro漏洞利用工具   
Y5neKO  李白你好   2024-11-27 00:04  
  
**免责声明：**由于传播、利用本公众号李白你好所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号李白你好及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
****  
  
**1**►  
  
**工具介绍**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9cS8WwxeIkv3pnqhdMZKmicFZSAiafd4OyjPq4TPNXX2bUDvqfCs25DJQ/640?wx_fmt=png&from=appmsg "")  
  
**2**►  
  
**工具使用**  
```
C:\Tools\Red_Tools\ShiroEXP>java -jar ShiroEXP.jar -h

   _____    __      _                    ______   _  __    ____
  / ___/   / /_    (_)   _____  ____    / ____/  | |/ /   / __ \
  \__ \   / __ \  / /   / ___/ / __ \  / __/     |   /   / /_/ /
 ___/ /  / / / / / /   / /    / /_/ / / /___    /   |   / ____/
/____/  /_/ /_/ /_/   /_/     \____/ /_____/   /_/|_|  /_/
                                        

 -be,--brute-echo              爆破回显链
 -bk,--brute-key               爆破key
 -c,--cmd <arg>                执行命令
    --cookie <arg>             携带Cookie
    --gadget <arg>             指定利用链
    --gadget-echo <arg>        指定回显链
 -h,--help                     打印帮助
 -k,--key <arg>                指定key
    --mem-pass <arg>           内存马密码
    --mem-path <arg>           内存马路径
    --mem-type <arg>           打入内存马类型(输入ls查看可用类型)
 -rf,--rememberme-flag <arg>   自定义rememberMe字段名
 -s,--scan                     扫描漏洞
    --shell                    进入Shell模式
 -u,--url <arg>                目标地址
```  
  
爆破key及加密方式  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9icPMCObBES9eRgblxK8bia4APn63gKsbKqWsZkDyzFR4P3nwDQicjjhNA/640?wx_fmt=png&from=appmsg "")  
  
漏洞验证  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9h5KehjRvfpxFy9icCqK8ub8ZmvbWDqTXhJOBP2Ry0pBGl7HBvF3U99g/640?wx_fmt=png&from=appmsg "")  
  
爆破回显链  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9LygDY97c6aeGPIx3WbgBbJic4dANWf0k7r89WXBjlaxiaEpia0wNoH2icw/640?wx_fmt=png&from=appmsg "")  
  
命令执行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9HW1LetHSmwCn0fOtCpwiapENVrJc4mI9HsbtkayTARw83HicNPYjVkcQ/640?wx_fmt=png&from=appmsg "")  
  
Shell模式  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9TcAaytwYBBuu1HZstZEJv7FCsL7SC5gicJAVUicCRF1ZpLKefLYia7Qtw/640?wx_fmt=png&from=appmsg "")  
  
注入内存马  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9gdNA2MW8dEIlbuWiaddCWGEr7CzMRw55SqXLxd2TkQodKeHdPD1ElVg/640?wx_fmt=png&from=appmsg "")  
  
  
**3**►  
  
**PS**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUA9zPJzZ4Ycxvr3D0RAw0ia9V8xKyp8hubMAdesib4zTx3Mk6G8t9dO8icIugI5R17dyvXtl4r3VsRTw/640?wx_fmt=png&from=appmsg "")  
  
  
**4**►  
  
**工具获取**  
  
**点击关注下方名片****进入公众号**  
  
**回复关键字【241127****】获取****下载链接**  
  
  
**5**►  
  
**往期精彩**  
  
[ 记两次内网入侵溯源的真实案例 ](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247509463&idx=1&sn=1da434a56d7b6640d14fc9ee1c2d69f7&chksm=c09ad687f7ed5f910955a44a40ba64b911e4b53634ef920086723f6f2d43f0847028c29071e9&scene=21#wechat_redirect)  

						  
  
  
[ 攻防演习之三天拿下官网站群 ](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247509413&idx=1&sn=628bece22e6a7c11896dd8c5cf6d6f1a&chksm=c09ad6f5f7ed5fe3ddb69d63b3793a068672f3cff1005a0ecf711821081dbddf18dba04656c5&scene=21#wechat_redirect)  

						  
  
  
[ Palo Alto 防火墙0day漏洞 CVE-2024-0012 和 CVE-2024-9474 检测POC&EXP ](http://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247509402&idx=1&sn=fd513ef1bfe094d6bfc52a0238d8efe2&chksm=c09ad6caf7ed5fdc26ffebc69bd8cf7f0cd7f3364238fc4d86312cb1b687f90bc433f9f25a43&scene=21#wechat_redirect)  

						  
  
  
  
