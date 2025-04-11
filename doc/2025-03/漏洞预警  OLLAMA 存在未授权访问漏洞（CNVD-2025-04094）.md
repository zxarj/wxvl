#  漏洞预警 | OLLAMA 存在未授权访问漏洞（CNVD-2025-04094）   
原创 烽火台实验室  Beacon Tower Lab   2025-03-04 16:12  
  
**1**  
  
  
  
  
**一、漏洞概述**  
  
<table><tbody><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>漏洞类型</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">未授权访问</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>漏洞等级</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">高危</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>漏洞编号</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">CNVD-2025-04094</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>漏洞评分</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">无</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>利用复杂度</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">低</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>影响版本</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><section><p style="text-align: center;">Ollama所有版本</p><p style="text-align: center;">（未设置访问认证的情况下）</p></section></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>利用方式</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">远程</p></td></tr><tr><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="30.0000%"><p style="text-align: center;"><strong>POC/EXP</strong></p></td><td colspan="1" rowspan="1" style="border-color: rgb(62, 62, 62);padding: 0px;" width="70.0000%"><p style="text-align: center;">已公开</p></td></tr></tbody></table>  
  
  
  
近日，国家信息安全漏洞共享平台（CNVD）披露Ollama未授权访问漏洞（CNVD-2025-04094）。为避免您的业务受影响，建议您及时开展安全风险自查。  
  
  
Ollama是一个github开源大语言模型运行框架，用于本地部署运行大模型语言，如DeepSeek-R1、Llama 3.3、Phi-4、Mistral等等。Ollama 提供对模型量化的支持，可以显著降低显存要求，使得在普通家用计算机上运行大型模型成为可能。Ollama 支持多种操作系统，包括 macOS、Windows、Linux 以及通过 Docker 容器运行。  
  
  
据描述，由于Ollama默认部署配置未强制启用身份认证机制，如果部署公网，其端口（11434）将能直接被访问，未经授权的攻击者可在远程条件下调用Ollama服务高危接口，从而控制Ollama 执行任意Prompt指令，篡改系统配置，拉取删除私有模型文件等操作。如果Ollama以Docker部署，攻击者可能通过特殊指令通过容器逃逸，控制整个服务器。  
  
  
漏洞影响的产品和版本：Ollama所有版本（暴露于公网且未设置访问认证的情况下）。  
  
  
**2**  
  
  
  
  
**二、漏洞复现**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAOvd5WuOaL6ibrJ4icXiacuPp3kZc0yfhpUsNvr8SNhJyhyt4zoaZD3fbriaaUmB7dyT8icNRtyia5AqwKQ/640?wx_fmt=png&from=appmsg "")  
  
  
**3**  
  
  
  
  
**三、资产测绘**  
  
  
据daydaymap数据显示互联网存在306,173个资产，国内风险资产分布情况如下，主要分布在国内。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAOvd5WuOaL6ibrJ4icXiacuPp3L40bFvsgjRggQnGOnR5Tc5qGdjahiaiaadibQT5QQmA3ujgIzhl6iaXYuA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAOvd5WuOaL6ibrJ4icXiacuPp3hNfPjgVlYIBbve9zo5AOJrhmriaxgZHPia3jcA9B7p9Ban76DFhdYwGA/640?wx_fmt=png&from=appmsg "")  
  
  
**4**  
  
  
  
  
**四、解决方案**  
  
  
1、若无必要建议将Ollama服务端口从公网禁止访问，仅内网或vpn访问。  
  
2、配置ip白名单，限制指定来源IP访问Ollama服务  
  
3、建议配置反向代理接入身份认证授权机制（如使用OAuth2.0）  
  
4、建议修复前先进行文件备份。  
  
5、检查服务日志（~/.ollama/logs/server.log）中出现异常请求如：“POST /api/pull”、"POST /api/delete"、 "POST /api/generate"。  
  
  
**5**  
  
  
  
  
**五、参考链接**  
```
https://www.cnvd.org.cn/webinfo/show/10976
https://www.ddpoc.com/DVB-2025-8898.html
```  
  
  
  
  
  
  
