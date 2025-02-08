#  DeepSeek+本地知识库 = 离线安全专家   
原创 Z2OSEC  Z2O安全攻防   2025-02-08 03:26  
  
   
  
# DeepSeek+本地知识库 = 离线安全专家  
  
使用ollama deepseek r1 +nomic-embed-text + anythingllm + 本地知识库 喂出一个离线网络安全专家  
## 一、下载Ollama  
  
使用Ollama可以大大降低显存需求，消费级的显卡也能运行大模型，官网下载安装即可：https://ollama.com/download  
  
安装 之后状态栏：  
  
![image-20250207173335717](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCMtpPpKh7DGFHic5nxKqQXfauntq6yRDTdN3AiaOm03qiaibobFictAOxXZg/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207173335717  
## 二、安装DeepSeek-R1模型  
  
进入Ollama官网，找到Models标签  
  
![image-20250207173406851](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCpahbWlZpF1ZOMC6nJT8qctKdfvics1nnVYkumQrnjAaUdKtjMJTS1Lw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207173406851  
  
根据自己的喜好和主机性能选择模型，这里用最近爆火的deepseek  
  
这里以 8b 为例  
  
![image-20250207174156563](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichC16PI8OLZeNWN7Qhtxm8cw1fZLMOgiafy1bS6CW7JSrO71GGfbgESQIA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207174156563  
  
复制下命令后，直接本地cmd运行即可  
  
（不挂代理下载会很慢）  
  
![image-20250207173210193](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCJC26wCUFibtuKeVhiaCbpXh4VYJY3vkwsBgmrTaIcXXsyCJeuKZmfXkA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207173210193  
  
下载完成后直接进入了cmd的对话进程  
  
![image-20250207174849012](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCIvs9h0t8burP9sKricEkmxwQSF0cMmhw4mmG1XK3EaWNry8ibQuDXOxw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207174849012  
  
下次运行，直接在cmd里面启动就好了  
  
![image-20250207175028080](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCsh9mTt9HR0jubyP8WcZvLrt1IRZW9kdQ6lvTYGAKNWBLQLfuXI3Iqg/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207175028080  
  
Ollama模型的默认存储目录：  
```
C:\Users\用户名\.ollama
```  
> C盘不够，可以更改模型存储位置：  
> 设置环境变量OLLAMA_MODELSE:\ai\ollama\models  
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCic0775yulNtMYBXERBdmtk6icu2ILPw0O9dP2gGWZB0ztPb1qpNqfU8g/640?wx_fmt=png&from=appmsg "")  
  
> image-20250208111917343  
  
  
## 三、安装AnythingLLM  
  
下载地址：  
  
https://anythingllm.com/download  
> 默认安装路径  
> C:\Users\用户\AppData\Local\Programs\AnythingLLM  
  
  
安装完成后，启动会进入自动引导界面，跟着界面一步步来：  
  
![image-20250207221049577](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCxQfWLMKIudAPIRYyxIViaAPLqy5Q8cbeUt1cCB5QEggX6Siay2DXiaftQ/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207221049577  
  
这里选择Ollama  
  
用我们刚刚下载的 DeepSeek-R1:8b 大模型  
  
![image-20250207221228331](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichC9zmicuF3TmLzpeqHlYUxxq06PDKPM2iamtw4ooicg4Zs3ZOPdEEYu6qGw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207221228331  
  
一直下一步，然后为工作区起个名字  
  
![image-20250207221354106](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCtPBhS4QuYoRRoO5xN6iaPx883UWaM8r9PPHs4K0Cwl3nfkge4F9cjQQ/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207221354106  
  
然后即可创建成功  
  
![image-20250207221927940](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCwsSnlDtSgckfsToU51lsrEZqZWicoiaJzO0drn4RPqiapzLeYSibAXniaUA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207221927940  
  
然后进行一些设置  
### LLM首选项  
  
这里之前安装的时候已经设置了  
  
![image-20250207222044131](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichC3Wrcn0RlQ3EjJQ8GKYPLuYl1mvaPwoUqodxiafuRGfYj5D7RgWibHNJA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207222044131  
### 向量数据库  
  
向量数据库不用动即可，使用自带的（ps:如果没有选择安装目录，默认在c盘，如果后续有需要可以挪走）  
  
![image-20250207222104439](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCJUa0t4ZztiaG73P4icAnzZ6zibGfEdHyef0ibxSlssrcvkvjQictMZuhHcQ/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207222104439  
### Embedder首选项  
  
嵌入模型配置，可以使用自带的  
  
![image-20250207223212974](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCh5v0kv6lSwibCtpCdQA1x2ATaKMkfdsL6XSluglu6c2UMiciaxMpKUNibA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207223212974  
  
也可以通过 Ollama 使用 nomic-embed-text 作为 Embedder （本例使用这个）  
```
ollama pull nomic-embed-text
```  
  
![image-20250207223653494](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCLiahzn4UEb0CG8tu8qZaPRjG6qGPF7ib2hVTKHFwJXCQY1PzVHiazCbcw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207223653494  
  
![image-20250207224056228](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCaOBBWfKynJp1AiaBJRQ5Ea2FY5quEdbMC78kaOH0nl2XJWxYEFAoYXA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207224056228  
  
“**Max Embedding Chunk Length**” ，定义了在将文本分割成多个块（Chunk）时，每个块的最大长度，数字越小代表文本文件会被切分的更加细致。最好改为128～512之间，这里设置为512  
> 这是DeepSeek 给出的两者的对比：  
> ![image-20250207223147682](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCE6fAy7zvCgIkurxceC3KqSfQX63ELt5URCG2icm7lDCgYlbuSfOiaj0A/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207223147682  
  
  
### 文件相似度阈值  
  
最后在当前聊天的设置中将“文档相似性阈值”：  
  
![image-20250207224540100](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCMfCuliaPZf5ACmCBN4iaicOibhyTicEKlYhnYFuKNRiaCJwiaXlCpN7icLnngA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207224540100  
  
这个可以根据实际搜索的内容与知识库的相关性灵活性设置（这里设置为高）  
## 四、投喂文档&使用  
  
首先点击上传按钮：  
  
![image-20250207225115631](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCfhR84ORia7V0JiaicTCJquSAegqDx7wJx1zSE3YicQJicsLQrFib31CTicdyA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207225115631  
  
支持多种类型的文档，直接拖进来即可（支持直接把文件夹丢过去）  
  
![image-20250207230553055](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichC2Ak7oCpf3vFQRvzIe2K85z2EBRvHxKrSictM83kicEFHd99LibFEQ3L6w/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207230553055  
> 最下方支持网址提交，当你输入网址后，点击“Fetch Website”按钮，爬虫就会对指定的网址内容进行爬取。  
  
  
拖进来之后，全部选中，接着点击“Move to Workspace”，将所有文件移入我们的WorkSpace：  
  
![image-20250207230732174](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCAKibRcqjoOIXOTkmUbrYvibE6OcqKu1v9aNmVy7UoKobmr4dvr9VS55A/640?wx_fmt=png&from=appmsg "null")  
  
image-20250207230732174  
  
最后点击“Save and Embed”按钮等待完成  
  
完成后，返回聊天框，就可以在AnythingLLM中进行基于检索增强生成（RAG）的聊天或问答了  
  
效果：  
  
![image-20250208094233555](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCL9ylOW0bn2Gxn6VAxsB3ibWNDyRSOIBm5MbD4ibBVq2LXwa4aaDricaqA/640?wx_fmt=png&from=appmsg "null")  
  
image-20250208094233555  
  
![image-20250208094254540](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichC7vOWgLeMsD5sb4AuVESd2JxOdsFFV2y4jhu3auQgic2ib18jic0eICUSw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250208094254540  
  
![image-20250208110722429](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCsDQ2A4fg54XxznMa9dhn075tXhEsDno2fYXTWv0e1zFibXpryXUaW0A/640?wx_fmt=png&from=appmsg "null")  
  
image-20250208110722429  
  
![image-20250208110706686](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCmS6yog5rBn8sgJsiakA0MUsiaK4ianVWXUk7xtMv76BFyJbT7dDnmfnzw/640?wx_fmt=png&from=appmsg "null")  
  
image-20250208110706686  
  
![image-20250208111349663](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuZibBx203xDY4AC0meIZ2ichCzpn4YkatoPgFg2dI5uxTian9P2CgYQnsAHEKTTbgfhP6sxjWqkKic6nQ/640?wx_fmt=png&from=appmsg "null")  
  
image-20250208111349663  
  
   
  
### 考证咨询  
  
  
最优惠报考  
各类安全证书(NISP/CISP/CISSP/PTE/PTS/PMP/IRE等....)，后台回复"  
好友位"咨询。  
  
### 交流群  
  
  
关注公众号回复“**加群**”，添加Z2OBot好友，自动拉你加入**Z2O安全攻防交流群(微信群)**分享更多好东西。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuYMO5aHRB3TbIy3xezlTAkbFzqIRfZNnicxSC23h1UmemDu9Jq38xrleA6NyoWBu1nAj0nmE6YXEHg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
### 关注我们  
  
  
  
**关注福利：**  
  
**回复“**  
**书籍****" 获取  网络安全书籍PDF教程**  
  
**回复“**  
**字典****" 获取 针对一些字典重新划分处理，收集了几个密码管理字典生成器用来扩展更多字典的仓库。**  
  
**回复“资料" 获取 网络安全、渗透测试相关资料文档合集**  
  
****  
点个【 在看 】，你最好看  
  
