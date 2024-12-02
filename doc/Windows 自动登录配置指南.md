#  Windows 自动登录配置指南   
原创 ralap  网络个人修炼   2024-12-02 02:01  
  
对于频繁使用的测试环境来说，每次启动虚拟机都手动输入账号密码比较麻烦。为了简化这一过程，可以通过配置自动登录来节省时间和提高效率。然而，出于安全性的考虑，并不推荐在生产环境中使用此功能。以下是几种实现自动登录的方法：  
## 1.使用注册表编辑器启用自动登录  
  
通过修改Windows注册表中的相关条目，可以实现系统的自动登录。具体步骤如下：  
  
1.按下   
Win + R 组合键打开“运行”对话框，  
输入   
regedit  
 并按回车键打开注册表编辑器。  
  
2.导航至路径  
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon。
```  
  
3.在右侧窗格中，创建或修改以下三个字符串值：  
1.   
1.   
1.   
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc0XMjqSc1ibOzS9t7WdibUBLP559vhrxJpZehfLElKcLM63hY8XXRZct1g/640?wx_fmt=png&from=appmsg "")  
#### 2.通过用户账户设置启用自动登录  
  
1.按下   
Win + R 组合键，输入   
netplwiz 并按回车键打开“用户账户”窗口。  
  
2.选择希望自动登录的账户，取消选中“要使用本计算机，用户必须输入用户名和密码”选项。  
  
3.点击“应用”按钮，在弹出的对话框中输入账户的密码，再次点击“确定”完成设置。  
  
如果设置过程中没有弹出要求输入密码的对话框，可以尝试先勾选再取消该选项来触发它。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc0ibetHic7KokricZ513Z7sBRHXClLJJwdMaSC8JptWAicnUics0AOIEbrK1w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc0qIZQTw3jH2hbQEx1IqF8tYp3puA7LKUDHMhnm0mHIjLCfHrlxBVSHg/640?wx_fmt=png&from=appmsg "")  
## 3.使用 Sysinternals 工具 Autologon   
  
Microsoft 提供了一个名为 Autologon 的小工具，可以方便地配置自动登录。操作步骤如下：  
  
1.访问https://learn.microsoft.com/zh-cn/sysinternals/downloads/autologon，点击下载Autologon  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc0ZlCnoev06Fa1SS30vDHIbp1ku7acwZXI7aBvsLmFmBehGqrvrkqguA/640?wx_fmt=png&from=appmsg "")  
  
2.解压后运行Autologon.exe,点击Agree,填写对话框，然后点击“启用”就可以了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc0kaqEicZJOZAumExGJszJlemMeCYejGUsfbfuQxhrVjOibEOuw5cl2HpA/640?wx_fmt=png&from=appmsg "")  
  
**4.空密码**  
  
以上三种只支持开机自动登录，注销或锁屏后需要输入密码，如果需要全程不输入密码，可以设置空密码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKKsIOXBrjAVUkbjibv2fibc00KrRWHQwiahRoFIpxN5N7pEfU6do3sib6xg4V3Jd2aXo5rFMIPMqXtxA/640?wx_fmt=png&from=appmsg "")  
  
win+R,输入  
compmgmt.msc，选择计算机管理-系统工具-本地用户和组-用户，选择对应用户设置空密码即可  
  
安全提示：自动登录和空密码登录都会降低系统的安全性。在使用这些功能时，务必确保计算机处于受控环境中，避免敏感信息泄露。  
  
**参考链接：**  
  
https://learn.microsoft.com/zh-cn/troubleshoot/windows-server/user-profiles-and-logon/turn-on-automatic-logon  
  
https://learn.microsoft.com/zh-cn/sysinternals/downloads/autologon  
  
  
  
