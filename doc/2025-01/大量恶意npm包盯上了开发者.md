#  大量恶意npm包盯上了开发者   
老布  FreeBuf   2025-01-12 02:01  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39RhLAfzTwzY96hucZP2Hjgk8w1jSGoEsXQtczSluwuQvd2HAF5Q9Wrgx8yDNcW0qd1InxNgIhnYA/640?wx_fmt=jpeg&from=appmsg "")  
  
近日，研究人员发现，有大量的恶意npm软件包，它们冒充以太坊开发者使用的Hardhat开发环境，正在窃取私钥和其他敏感数据。  
研究人员称，这些恶意软件包总共被下载了一千多次。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39RhLAfzTwzY96hucZP2Hjgt24KF3McCcopwLllqgJicj0H0sT9MlRsI4G4aiahWw2Zw9icodsPOtk5Q/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
**针对性攻击活动**  
  
  
  
Hardhat是由Nomic Foundation维护的、广泛用于以太坊开发的工具，它可用于在以太坊区块链上开发、测试和部署智能合约以及去中心化应用程序（dApps）。通常，区块链软件开发者、金融科技公司、初创企业和教育机构会使用它。  
  
  
这些用户往往会通过npm（Node Package Manager，JavaScript生态系统里广泛使用的工具，用于管理依赖项、库和模块）获取项目组件。  
  
  
在npm平台上，三个恶意账户上传了20个信息窃取包。这些包采用“拼写错误伪装”（typosquatting）手段冒充合法包，引诱用户安装。Socket列出了16个恶意包的名称，包括：  
  
- nomicsfoundations- @nomisfoundation/hardhat - configure- installedpackagepublish- @nomisfoundation/hardhat - config- @monicfoundation/hardhat - config- @nomicsfoundation/sdk - test- @nomicsfoundation/hardhat - config- @nomicsfoundation/web3 - sdk- @nomicsfoundation/sdk - test1- @nomicfoundations/hardhat - config- crypto - nodes - validator- solana - validator- node - validators- hardhat - deploy - others- hardhat - gas - optimizer- solidity - comments - extractors  
  
  
一旦安装这些包，其中的代码就会尝试收集Hardhat的私钥、配置文件以及助记词，然后用硬编码的AES密钥进行加密，再传输给攻击者。  
  
  
Socket解释说：“这些包借助Hardhat运行时环境，通过 `hreInit()` 和 `hreConfig()` 等函数收集私钥、助记词和配置文件等敏感信息，然后利用硬编码的密钥和以太坊地址将这些数据高效地泄露出去。”  
  
  
**安全风险与缓解措施**  
  
  
  
私钥和助记词用于访问以太坊钱包，所以此次攻击首先可能导致的后果是发起未经授权的交易从而使资金遭受损失。  
而且，由于许多受感染的系统属于开发者，攻击者可能会未经授权访问生产系统，破坏智能合约或者部署现有dApp的恶意克隆，为大规模攻击做准备。  
  
  
Hardhat配置文件可能包含第三方服务的API密钥以及开发网络和端点的信息，这些信息可能被用于开展钓鱼攻击。  
  
  
软件开发者要谨慎行事，在安装前验证软件包的真实性，警惕拼写错误伪装并查看源代码。一般来说，私钥不应进行硬编码，而应存储在安全的保险库之中。  
  
  
为降低此类风险，建议使用锁定文件（lock files），为依赖项指定特定版本并且尽量减少依赖项的使用。  
  
  
【  
FreeBuf粉丝交流群招新啦！  
  
在这里，拓宽网安边界  
  
甲方安全建设干货；  
  
乙方最新技术理念；  
  
全球最新的网络安全资讯；  
  
群内不定期开启各种抽奖活动；  
  
FreeBuf盲盒、大象公仔......  
  
扫码添加小蜜蜂微信回复「加群」，申请加入群聊】  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ich6ibqlfxbwaJlDyErKpzvETedBHPS9tGHfSKMCEZcuGq1U1mylY7pCEvJD9w60pWp7NzDjmM2BlQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2&tp=webp "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ic5icaZr7IGkVcd3DT6vXW4B4LOZ1M7YkTPhS1AT2DQJaicFjtCxt5BRO7p5AOJqvH3EJABCd0BFqYQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651253272&idx=1&sn=82468d927062b7427e3ca8a912cb2dc7&scene=21#wechat_redirect)  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
