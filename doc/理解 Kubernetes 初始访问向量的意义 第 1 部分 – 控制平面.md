#  理解 Kubernetes 初始访问向量的意义 第 1 部分 – 控制平面   
Shay Berkovich  securitainment   2024-11-23 02:30  
  
> Making Sense of Kubernetes Initial Access Vectors Part 1 – Control Plane  
  
  
## 动机  
  
Kubernetes (K8s) 是一个复杂的分布式系统，旨在以可扩展和可管理的方式运行容器化工作负载。它现在是云原生环境中部署工作负载的默认方法。由于其灵活性和可扩展性，Kubernetes 在处理各种工作负载（例如，批处理、高性能计算、基于 GPU 的工作负载）方面表现出色，这促进了其广泛的采用。  
  
Kubernetes 安全性一直在努力跟上生态系统的快速演变。Kubernetes 的常见威胁类型包括  
加密挖矿、资源劫持、数据盗窃、云转移、  
IP 盗窃等。然而，所有这些攻击都依赖于一件事：成功的初始访问。  
  
另一个不太明显的动机因素是：我们的  
2023 Kubernetes 安全   
报告显示，一旦攻击者获得初始访问权限，就有充足的机会在集群内进行横向移动和  
权限升级。这使得保护初始访问变得更加关键。  
  
了解集群的潜在访问向量以及如何检测初始攻击至关重要。感兴趣吗？继续阅读。  
## 分类  
  
在 Kubernetes 初始访问的系统化实践中存在差距。像 MITRE 容器  
矩阵和 Microsoft Kubernetes 威胁矩阵这样的框架列出了一些初始访问的技术，但没有深入分析或风险优先级。在本博客系列中，我们介绍了初始访问向量的分类。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOQQj77jbKsYC4AII7ia8WH5K8UXiadhdg3gcbfPSIlKSRMG5rd57hMjiaQ/640?wx_fmt=png&from=appmsg "")  
  
主要支柱代表四个主要访问领域：控制平面、数据平面、云访问和 CI/CD。云访问和 CI/CD 不在本文的讨论范围内；在这里，我们将专注于 Kubernetes 本身。这些领域进一步分为更小的向量，每个向量都以与之相关的最显著风险为顶点。例如，错误配置是暴露 Kubelet API 访问的主要风险。下面，我们将专注于控制平面访问，分解初始访问向量、相关风险以及建议的保护和检测技术。在下一篇文章中，我们将深入探讨数据平面访问。  
## Kubernetes API 访问  
  
K8s API 服务器不仅是控制平面组件之间的通信枢纽；它也是集群外部用户交互的前端。这使得它成为访问和管理 K8s 集群的主要方法。  
## 未认证访问  
  
K8s API 的访问是通过基于角色的访问控制 (RBAC) 管理的。这里的关键概念是用户角色。默认情况下，K8s 将每个未认证用户映射到 system:anonymous 角色，该角色属于 system:unauthenticated 组。当此功能被禁用时（如在 AKS 中），未认证用户在尝试访问 API 端点时会收到 401 错误。当启用时（如在 EKS 和 GKE 中），未认证用户被授予匿名角色的基本权限，例如检索版本和健康信息：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOUaOlxic2BlibEHFnqfAEd32X00VibEOmJh4Dk71THnoH08NTf7ppeXtMg/640?wx_fmt=png&from=appmsg "")  
  
然而，这为潜在的 RBAC 错误配置打开了大门。例如，一个懒惰的集群管理员可能会暂时为 system:unauthenticated 组分配过多的权限，因为开发团队需要访问但没有适当的凭据。未认证访问已导致多次  
事件。  
## Kubeconfig  
  
Kubeconfig 文件定义了 kubectl 如何对 API 服务器进行身份验证。它有三个主要部分：集群（集群 IP 和证书颁发机构）、用户（身份验证数据）和上下文（集群/用户对）。**我们建议将 Kubeconfig 文件视为包含机密的文件**，尤其是 **用户** 部分，因为它包含身份验证数据。  
```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tL...
  server: IP
  name: cluster1
- cluster:
...
contexts:
- context:
    cluster: cluster1
    user: user1
  name: context1
- context:
...
kind: Config
preferences: {}
users:
- name: user1
  user:
- name: user2
  user:
- name: user3

```  
  
在 EKS 和 GKE 中，这些是运行本地 kubectl exec 插件（aws cli, aws-iam-authenticator, gke-gcloud-auth-plugin.exe）的指令，这些插件将获取必要的云凭证，从而不将凭证存储在 kubeconfig 文件中。这有两个优点：（1）减少文件暴露的风险，（2）将身份验证/授权移至身份域，这更易于审计、检测威胁等。然而，在 AKS 中，身份验证材料取决于集群的身份验证/授权方法。当创建新的 AKS 集群时，用户必须选择方法，默认选项是“使用 Kubernetes RBAC 的本地账户”：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOeXzddr2z81ELJdcqa7ibEhegmMHbibZGCq5Ml75wibRYX5JkzUIzONnng/640?wx_fmt=png&from=appmsg "")  
  
默认情况下，AKS 中的 Kubeconfig 文件包含可用于成功身份验证的用户令牌和客户端证书数据。如果证书未旋转，恶意行为者可能会对集群拥有**长期访问**，因为证书有效期为两年。  
  
**注意**：当然，泄露的云凭证本身对 K8s 环境构成非常严重的风险，无论云类型如何。然而，这超出了本文的范围，并在上面的矩阵中一般标记为“云访问”。  
  
这种风险也适用于自托管集群，这些集群提供更广泛的身份验证选项（例如，作为令牌文件、SSH 凭证、特殊命令等）。无论设置如何，都应将 Kubeconfig 文件视为敏感文档。**绝不要**将其检入公共存储库，这仍然是凭证泄露的最常见方式之一。简单的 GitHub 搜索可以揭示明文访问凭证：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOdibibiauYJ55XyBC8rEgd5eYuQ1zDFhQIfqREcjPc2VoAD0tk3V2AtEMw/640?wx_fmt=png&from=appmsg "")  
## Kubectl 代理  
  
Kubectl   
代理 是一种较少人知的访问 K8s API 服务器的方法，通常用于临时诊断或调试。运行 kubectl proxy –port=8080 会在本地主机和 K8s API 服务器之间创建一个临时代理服务器。对 localhost:8080 的任何 API 调用都将作为由运行命令的用户授权的 HTTP 请求执行。如果攻击者拥有本地或网络访问权限（甚至 SSRF 也可以），他们可以利用这种未认证的连接到达源站——开发者笔记本或跳板虚拟机：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOzKyicLMSFaKSEjiaH63dGLRLxm4rZg8TZiaGjia3P2xxanbF7uUuDn15xg/640?wx_fmt=png&from=appmsg "")  
  
幸运的是，这不是一种常见的错误配置。Shodan 报告少于 100 个端点返回状态 200，并带有相关的 Kubernetes 标头：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOWgTQeo7zpvWibj8gZib8r2FcphJkmMYPsaXpibNEdcibl8F5NpPIbus1lQ/640?wx_fmt=png&from=appmsg "")  
## Kubelet API 访问  
  
Kubelet 是运行在每个工作节点上的集群控制平面代理，默认情况下，它仅对同一节点上的内部组件可访问。然而，可以将 Kubelet API 外部暴露以进行调试。此设置通过存储 kubelet 配置的 .conf 文件中的 --anonymous-auth 和 --authorization-mode 参数进行控制。最糟糕的错误配置之一是在节点上设置 –-anonymous-auth=True / --authorization-mode=AlwaysAllow 组合，使 Kubelet API 对匿名访问开放。通过 Kubelet API 的初始访问不会在 K8s 审计日志中可见，需要传感器或 VPC 流日志来检测此类活动。这是   
TeamTNT 针对的错误配置之一，但现在在生产系统中很少见，通常与蜜罐集群相关。  
## 管理接口  
  
像 K8s Dashboard、Kubeflow、Argo Workflows 等管理接口提供了额外的集群访问。典型的错误配置是将仪表板未认证并暴露于公共互联网。这里的风险取决于仪表板的功能和权限。  
  
这些错误配置在几年前更为常见，当时默认设置并不安全（最臭名昭著的妥协例子仍然是 2017 年的 Tesla 仪表板  
暴露）。如今，仪表板必须明确安装，默认启用身份验证。例如，Shodan 报告大约 4,000 个暴露的 Kubernetes 仪表板。然而，默认安装  
模式需要身份验证，因此期望轻松获胜的攻击者将面临登录屏幕：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOnUX2ZZg29E9ovvSkMuBOOwibjfM2Cd58jwVWibB9XBib0sg7KicU1RuYmMyHDob9KtgiafrwhgD5icAibw/640?wx_fmt=png&from=appmsg "")  
## 总结：通过控制平面访问 Kubernetes  
  
Kubernetes 是一个复杂的分布式系统，具有多个访问向量。每一个，如果不加以保护，都可能导致整个集群的妥协。在这篇文章中，我们分享了控制平面 Kubernetes 初始访问向量的分类，旨在帮助操作员和安全专业人员更好地保护他们的集群。我们还概述了每个向量的检测和预防策略。  
  
我们试图在深度和广度之间取得平衡。在下一篇文章中，我们将在数据平面访问向量上做同样的事情。  
  
