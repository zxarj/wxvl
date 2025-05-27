#  Zer0 Sec团队-某SRC任意文件读取漏洞挖掘案例   
原创 Syst1m  Zer0 sec   2025-05-27 02:00  
  
**Zer0 Sec**  
  
**某SRC任意文件读取漏洞**  
  
  
**案例详情**  
  
宇宙无敌免责  
  
本推文提供的信息、技术和方法仅用于教育目的。文中讨论的所有案例和技术均旨在帮助读者更好地理解相关安全问题，并采取适当的防护措施来保护自身系统免受攻击。  
  
严禁将本文中的任何信息用于非法目的或对任何未经许可的系统进行测试。未经授权尝试访问计算机系统或数据是违法行为，可能会导致法律后果。  
  
作者不对因阅读本文后采取的任何行动所造成的任何形式的损害负责，包括但不限于直接、间接、特殊、附带或后果性的损害。用户应自行承担使用这些信息的风险。  
  
我们鼓励所有读者遵守法律法规，负责任地使用技术知识，共同维护网络空间的安全与和谐。  
  
本文由Zer0 Sec团队的Juneha师傅（讲师）供稿  
  
0x1 发现漏洞  
  
- 一开始是在浏览器控制台网络请求处发现了个/getfile接口,通过查看url接口大致能看出是用于请求Json文件的  
  
  
  
![88974-loxm4zw8bh.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYO18zJyuFkiaI7TUmGG1odo21ZSCS6mR6DmQm3QTF5CHuylE1M2VP16Ww/640?wx_fmt=png&from=appmsg "")  
  
- 正常请求打开看一下URL响应内容,确实是用于加载json文件的  
  
  
  
![42221-fb2qilwdod.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOPSJBWeWrjViaQMpebd3JvN6MbALXAwCWuiaJ189YkEJOyg4QUNO40bpQ/640?wx_fmt=png&from=appmsg "")  
  
- 尝试在原有URL上添加一个内容发现会爆出真实路径在/var/pvc/category/下  
  
  
  
![67834-052m10jah76t.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOUFkr31lr8PV8ey7zuB7aewHia9xBLOCX5639unckk8uXHdYLS8OvhVw/640?wx_fmt=png&from=appmsg "")  
  
- 这里我是打算说试试看填个/etc/paasswd发现提示信息有误  
  
  
  
![41959-yn8jqursd2f.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOEswmibr6drczCc1cfyRBUDnu29c2IIegAK2ibNu2eK3BbudlXsEwVSWQ/640?wx_fmt=png&from=appmsg "")  
  
- 经过测试发现是要满足 abc.abc这种带点的文件名格式  
  
  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYO8NxO0RITib39jysOoAExCwTjnM1Nvy7icXhwsSZcicbQ6sKgXxXotug8Q/640?wx_fmt=png&from=appmsg "")  
  
- 一开始想的是读取系统里面自带的符合条件的文件,然后我提取了系统里面自带的文件作为字典，这里成功读取到了证书文件啥的，但是读取这些文件也没有危害。  
  
  
```
```  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOfb9ibffpAe4PaZtmQHRG2mgUHGVE8QfibiabQ64ldLzALcWib6HGZia5ib3Q/640?wx_fmt=png&from=appmsg "")  
  
  
0x02任意文件读取  
  
- 后面在本地环境里面测试一下,发现要满足这个条件并不难，找一个存在的且满足条件的文件夹然后利用../../去读取即可，例如我这里创建了个test.dir来测试发现刚好能满足当前场景，接下来只需要找到系统自带的满足条件的文件夹即可。  
  
  
```
```  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOF4ib4JDthbbt1lxJQxiaKjiaGw17bFCsR94etnV344680jxUORQ2m1XIw/640?wx_fmt=png&from=appmsg "")  
  
- 接下来在centos系统中通过find来筛选出满足条件的自带文件夹作为字典  
  
  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYODiav4oHzyAJvrazy7ic8wR7p8WQiajShiaQQZoXTcbdl1YSRt9b4DIuZHg/640?wx_fmt=png&from=appmsg "")  
  
- 随后使用Burp去fuzz一下，成功读取到了/etc/passwd文件  
  
  
```
```  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOQptrmqn5RgvFlzib1LfqEg9EyBygqCjRyCvL8XZ0ZDmOWbTXIcwwJAw/640?wx_fmt=png&from=appmsg "")  
  
- 尝试了一下读取 /etc/shadow发现可以读取，但是没有密码信息，那推测这个环境可能是个容器环境  
  
  
```
```  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOP69gjSicx1hIgmvuOl8BLZMDvuUPpBTBz3UzZGEhaxSySGpqD6zib0GA/640?wx_fmt=png&from=appmsg "")  
  
- 通过读取环境变量，成功获取数据库跟使用的外部api服务的key等信息  
  
  
  
![12851-6l4aml3dvtg.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOo02et1miaZI9LrdibZfJ7qqyRcWK6JbEx7TKKuttyHBn3gZyEOWHQQ4w/640?wx_fmt=png&from=appmsg "")  
  
  
**团队课程简介**  
  
详细介绍请访问以下链接：  
  
https://www.yuque.com/syst1m-/blog/lc3k6elv0zqhdal3?singleDoc#  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOEUapzzC1Kzaib0MJRSlKbTEgZftswEoHLKxySvib2MHXgFO9udvCzia3g/640?wx_fmt=png&from=appmsg "")  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOzUxumQZMt3BCGgE9IfVl2oYUmRZEcl1yc5am4m9qJ5Q88ic1c4xPiaXA/640?wx_fmt=png&from=appmsg "")  
  
🎉优惠详情  
  
课程原价 1199 元，本次五一优惠力度空前，多重福利可叠加！  
  
- 学生专属：如果你是大学生，凭借学生证，立减 100 元！知识提升，经济无负担，让你在校园就能为未来的职业发展储备力量。  
  
- 两人成团：快拉上你的小伙伴一起学习！两人成团，每人再减 100 元。学习路上有伴，互相交流、共同进步，还能享受超值优惠，何乐而不为？  
  
- B 站&&公众号粉丝福利：关注我们 B 站和公众号的粉丝们有福啦！凭 B 站和公众号关注截图（两个都要），立减 50元。感谢一路以来的支持，这份专属福利请收好！  
  
  
  
**报名方式**  
  
  
- 扫描以下二维码加绿泡泡，备注“报名课程”  
  
  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOOk3rIuvmG5j4fJHpJrCjYOL0UMx9wnEE5qgQWHYxMEv20Y7Z8EGgupC1vUy65yGJR9tg8LANhlIg/640?wx_fmt=png&from=appmsg "")  
  
  
- 外部交流群（欢迎进群互相交流），由于群人数超过了200，只能邀请拉群，可以关注公众号，后台回复“加群”，获取助手绿泡泡，联系小助手邀请进群  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/lSfs7HwzmOPQ0wFex2MNKbDRZ2sAzNCAMvALMuUhBbiazlVRN2P3ib3wPCuoMWibCUJvJNdAhBXKC6KHNBUWTr1vg/640?wx_fmt=png&from=appmsg "")  
  
  
  
