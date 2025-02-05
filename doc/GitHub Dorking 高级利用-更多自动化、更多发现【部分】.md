#  GitHub Dorking 高级利用-更多自动化、更多发现【部分】   
骨哥说事  骨哥说事   2025-02-05 02:41  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
# 防丢失：https://gugesay.com/  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
目录  
  
- 高级API以及Token发现  
  
- 更深一级的配置和凭证泄露  
  
- 通过GitHub寻找错误配置的Web服务  
  
- 高级自动化技术  
  
- 利用Github API运行Dork  
  
- 从已删除的提交中搜索信息  
  
- 一次搜索多个目标  
  
- 利用Github Dorking扩展进行大规模搜索  
  
-           
  
- 搜索包含“API_KEY”的公共存储库  
  
- 从GitHub Relases 历史中搜索‘秘密’  
  
****  
本文将分享更多Dorking技巧以及自动化技术，你将会学习到：  
- 高级Dorking技巧，用于发现.env_  
文件  
  
- 更多自动化脚本，用于大规模搜索  
  
- 利用新工具分析历史提交、删除文件以及整个组织的敏感信息  
  
- 领先一步的快速可扩展的‘侦查’技巧  
  
# 高级API以及Token 发现  
  
  
**加入星球，随时交流：**  
  
**********（会员统一定价）：128元/年（0.35元/天）******  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jnMJtHJnShkTnh3vR3fmaqicPicANic6OEsobrpRjx5vG6mMTib1icuPmuG74h2bxC4eP6nMMzbs5QaSlw/640?wx_fmt=jpeg&from=appmsg "")  
  
**感谢阅读，如果觉得还不错的话，欢迎分享给更多喜爱的朋友～****====正文结束====**  
  
  
