#  Wireshark & Packetdrill | TCP Cork 算法续   
原创 7ACE  Echo Reply   2025-04-14 00:08  
  
**为者常成，行者常至**  
  
  
  
**实验目的**  
  
通过 packetdrill 测试 TCP Cork，继续扩展几个相关实验，本次构造模拟的是客户端场景。  
  
## 基础脚本  
  
**基础脚本为 TCP 三次握手，构造模拟的是客户端场景，相关脚本说明详见《TCP 基础之三次握手续》。**  
```
# cat tcp_fc_cork_000.pkt 
0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1
#
```  
  
****## TCP Cork  
  
TCP Cork 算法与 TCP Nagle 算法类似，主要用于优化数据传输，设计目的是为了提供比 TCP Nagle 算法更精细的控制，让应用程序能够更好地平衡网络效率和延迟。  
  
TCP_CORK 机制可以被看作是一个"瓶塞"。当它被启用时，就像给 TCP 连接塞上了一个塞子，阻止数据被立即发送出去。也就是说 TCP 不会立即发送小的数据包，而是将数据缓存在 TCP 发送缓冲区中。数据会继续累积，直到发生以下情况之一时，才会一次性发送所有累积的数据：  
- 累积的数据量达到最大分段大小（MSS）  
  
- 应用程序禁用了 TCP_CORK 选项  
  
- 设置的超时时间到达  
  
在 Linux 中可以通过 TCP_CORK 选项来设置 Socket 打开 TCP Cork 算法，TCP_CORK 选项的优先级要比 TCP_NODELAY 选项的优先级要高。  
  
## 实验测试  
  
1. 在开启 TCP Cork + 关闭 TCP Nagle 算法的场景下，写入一个 1200 字节大小的数据，大于 MSS 1000。  
```
# cat tcp_fc_cork_007.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0
+0 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 1200) = 1200

+0.01 < . 1:1(0) ack 1001 win 10000

+0 `sleep 1`
#
```  
  
执行脚本，同时通过 tcpdump 抓取数据包，现象如下。  
  
可以看到在 TCP 三次握手 100ms 后，首先发出了 1000 字节（MSS 大小）的数据包，而并没有发出 200 字节的小数据包，因为此时小数据包受限于 TCP Cork 而无法发出，尽管此时 TCP_NODELAY 选项也开启了，这也就说明了 TCP_CORK 选项的优先级要比 TCP_NODELAY 选项的优先级要高。之后在收到 ACK 确认后，再经过一个 RTO 超时后，小数据包 200 字节才能发出。  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
22:05:08.778970 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [S], seq 204770299, win 64240, options [mss 1460,sackOK,TS val 3429831360 ecr 0,nop,wscale 7], length 0
22:05:08.789063 tun0  In  IP 192.0.2.1.8080 > 192.168.6.21.38876: Flags [S.], seq 0, ack 204770300, win 10000, options [mss 1000], length 0
22:05:08.789139 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
22:05:08.889373 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [.], seq 1:1001, ack 1, win 64240, length 1000: HTTP
22:05:08.899431 tun0  In  IP 192.0.2.1.8080 > 192.168.6.21.38876: Flags [.], ack 1001, win 10000, length 0
22:05:09.114655 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [P.], seq 1001:1201, ack 1, win 64240, length 200: HTTP
22:05:09.330659 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [P.], seq 1001:1201, ack 1, win 64240, length 200: HTTP
22:05:09.774655 tun0  Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [P.], seq 1001:1201, ack 1, win 64240, length 200: HTTP
22:05:09.902242 ?     Out IP 192.168.6.21.38876 > 192.0.2.1.8080: Flags [F.], seq 1201, ack 1, win 64240, length 0
22:05:09.902316 ?     In  IP 192.0.2.1.8080 > 192.168.6.21.38876: Flags [R.], seq 1, ack 1001, win 10000, length 0
#
```  
  
  
2. 在开启 TCP Cork + 关闭 TCP Nagle 算法的场景下，写入两个 200 字节大小的数据，间隔300ms。	  
```
# cat tcp_fc_cork_008.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0
+0 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 200) = 200

+0.3 write(3, ..., 200) = 200

+0 `sleep 2`
#
```  
  
执行脚本，同时通过 tcpdump 抓取数据包，现象如下。  
  
可以看到在 TCP 三次握手 100ms + RTO 超时 212+ms 后才发出了第一个小数据包 200 字节，而在 300ms 间隔再次写入的第二个小数据包，仍然受限于 TCP Cork 而无法发出，之后由于没有 ACK 确认，第一个小数据包在不断进行超时重传。  
  
这里还会有一个现象，第二个小数据包在受限于 TCP Cork 机制下 RTO 超时后，仍然无法发出，这里的原因却是第一个小数据包超时重传，CWND 降为了 1。  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
15:29:41.967037 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [S], seq 2271455503, win 64240, options [mss 1460,sackOK,TS val 1734340504 ecr 0,nop,wscale 7], length 0
15:29:41.977191 tun0  In  IP 192.0.2.1.8080 > 192.168.245.4.46330: Flags [S.], seq 0, ack 2271455504, win 10000, options [mss 1000], length 0
15:29:41.977231 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
15:29:42.290656 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:29:42.506687 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:29:42.958661 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:29:43.822683 tun0  Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:29:44.381318 ?     Out IP 192.168.245.4.46330 > 192.0.2.1.8080: Flags [FP.], seq 201:401, ack 1, win 64240, length 200: HTTP
15:29:44.381342 ?     In  IP 192.0.2.1.8080 > 192.168.245.4.46330: Flags [R.], seq 1, ack 1, win 10000, length 0
#
```  
  
  
3. 在开启 TCP Cork + 关闭 TCP Nagle 算法的场景下，写入两个 200 字节大小的数据，间隔300ms，增加一个 ACK。  
```
# cat tcp_fc_cork_009.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0
+0 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 200) = 200

+0.3 write(3, ..., 200) = 200

+0.2 < . 1:1(0) ack 201 win 10000

+0 `sleep 2`
#
```  
  
执行脚本，同时通过 tcpdump 抓取数据包，现象如下。  
  
可以看到在上面一个实验结果的基础上，收到了 ACK 确认后，经过了一个 RTO 超时（此时已翻倍）后才发出第二个小数据包。有兴趣的同学可以看下脚本间隔时间，再对照抓包结果，想想其中的过程。  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
15:40:16.587061 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [S], seq 3595261014, win 64240, options [mss 1460,sackOK,TS val 3563759565 ecr 0,nop,wscale 7], length 0
15:40:16.597274 tun0  In  IP 192.0.2.1.8080 > 192.168.40.238.57342: Flags [S.], seq 0, ack 3595261015, win 10000, options [mss 1000], length 0
15:40:16.597310 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
15:40:16.910680 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:40:17.126698 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [P.], seq 1:201, ack 1, win 64240, length 200: HTTP
15:40:17.197446 tun0  In  IP 192.0.2.1.8080 > 192.168.40.238.57342: Flags [.], ack 201, win 10000, length 0
15:40:17.646659 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [P.], seq 201:401, ack 1, win 64240, length 200: HTTP
15:40:18.094659 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [P.], seq 201:401, ack 1, win 64240, length 200: HTTP
15:40:18.958664 tun0  Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [P.], seq 201:401, ack 1, win 64240, length 200: HTTP
15:40:19.200284 ?     Out IP 192.168.40.238.57342 > 192.0.2.1.8080: Flags [F.], seq 401, ack 1, win 64240, length 0
15:40:19.200315 ?     In  IP 192.0.2.1.8080 > 192.168.40.238.57342: Flags [R.], seq 1, ack 201, win 10000, length 0
#
```  
  
  
4.   
在开启 TCP Cork + 开启 TCP Nagle 算法的场景下，在TCP 三次握手 100ms 后连续写入两个 200 字节的小数据包，再经过 100ms，再设置 TCP_NODELAY 。  
```
# cat tcp_fc_cork_010.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 200) = 200
+0 write(3, ..., 200) = 200

+0.1 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0 `sleep 1`
#
```  
  
执行脚本，同时通过 tcpdump 抓取数据包，现象如下。  
  
可以看到在 TCP 三次握手 200ms+ 后，发出了合并 400 字节大小的数据包。实际过程如下，在 TCP 三次握手 100ms 后连续写入两个 200 字节的小数据包，因 TCP Cork 而不能发送，之后再经过 100ms 设置了 TCP_NODELAY 选项，此时 TCP_NODELAY 生效，因此合并发出了数据包。  
  
原因是虽然 TCP_NODELAY 选项的优先级比 TCP_CORK 优先级低，但是这个只对设置 TCP_NODELAY 后的应用层写入生效，**而在开始设置 TCP_NODELAY 选项的时候会尝试忽略 Cork 算法而将缓存中的数据全部发出。**  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
22:14:51.097878 tun0  Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [S], seq 3443981037, win 64240, options [mss 1460,sackOK,TS val 2991620426 ecr 0,nop,wscale 7], length 0
22:14:51.107966 tun0  In  IP 192.0.2.1.8080 > 192.168.113.109.56538: Flags [S.], seq 0, ack 3443981038, win 10000, options [mss 1000], length 0
22:14:51.107992 tun0  Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
22:14:51.308140 tun0  Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
22:14:51.521601 tun0  Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
22:14:51.957603 tun0  Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
22:14:52.310126 ?     Out IP 192.168.113.109.56538 > 192.0.2.1.8080: Flags [F.], seq 401, ack 1, win 64240, length 0
22:14:52.310159 ?     In  IP 192.0.2.1.8080 > 192.168.113.109.56538: Flags [R.], seq 1, ack 1, win 10000, length 0
#
```  
  
****  
5. 在上述脚本的基础上修改，在设置 TCP_NODELAY 选项后，尝试再次写入 200 字节的小数据包。  
```
# cat tcp_fc_cork_011.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 200) = 200
+0 write(3, ..., 200) = 200

+0.1 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0.1 write(3, ..., 200) = 200

+0 `sleep 2`
#
```  
  
执行脚本，同时通过 tcpdump 抓取数据包，现象如下。  
  
可以看到在之前实验结果之后，再次写入的数据包仍然受限于 TCP Cork 且 NODELAY 不生效（优先级低），而无法发出。  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
15:59:41.559039 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [S], seq 881791602, win 64240, options [mss 1460,sackOK,TS val 4231783469 ecr 0,nop,wscale 7], length 0
15:59:41.569198 tun0  In  IP 192.0.2.1.8080 > 192.168.157.87.41524: Flags [S.], seq 0, ack 881791603, win 10000, options [mss 1000], length 0
15:59:41.569271 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
15:59:41.769559 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
15:59:41.982665 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
15:59:42.414669 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
15:59:43.278670 tun0  Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
15:59:43.888160 ?     Out IP 192.168.157.87.41524 > 192.0.2.1.8080: Flags [FP.], seq 401:601, ack 1, win 64240, length 200: HTTP
15:59:43.888188 ?     In  IP 192.0.2.1.8080 > 192.168.157.87.41524: Flags [R.], seq 1, ack 1, win 10000, length 0
#
```  
  
  
6. 最后一个综合实验收尾，脚本如下。  
```
# cat tcp_fc_cork_012.pkt 
`ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0
+0 setsockopt(3, SOL_TCP, TCP_CORK, [1], 4) = 0

+0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)

+0 > S 0:0(0) <...>
+0.01 < S. 0:0(0) ack 1 win 10000 <mss 1000>
+0 > . 1:1(0) ack 1

+0.1 write(3, ..., 200) = 200
+0 write(3, ..., 200) = 200

+0.1 setsockopt(3, SOL_TCP, TCP_NODELAY, [1], 4) = 0

+0.01 < . 1:1(0) ack 401 win 10000

+0.1 write(3, ..., 300) = 300
+0 write(3, ..., 300) = 300

+0.2 write(3, ..., 800) = 800

+0.01 < . 1:1(0) ack 1401 win 10000

+0.25 < . 1:1(0) ack 1801 win 10000

+0 `sleep 1`
```  
  
TCP_NODELAY 后发出的 Seq 1:401 数据包被 ACK 之后，在 100ms 后连续写入两个 300 字节的小数据包并没有因 TCP_NODELAY 而立马发出，因为 CORK 算法优先，再在 200ms 后写入 800 字节数据包，满足 1 个 MSS 1000 字节大小后，立马发出 Seq 401:1401的数据包，经 ACK 确认后，再经过一个 RTO 超时后，发出 Seq 1401:1801 的数据包。  
```
# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
16:03:31.187027 tun0  Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [S], seq 1151677807, win 64240, options [mss 1460,sackOK,TS val 3566486039 ecr 0,nop,wscale 7], length 0
16:03:31.197122 tun0  In  IP 192.0.2.1.8080 > 192.168.49.20.32844: Flags [S.], seq 0, ack 1151677808, win 10000, options [mss 1000], length 0
16:03:31.197166 tun0  Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [.], ack 1, win 64240, length 0
16:03:31.397412 tun0  Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [P.], seq 1:401, ack 1, win 64240, length 400: HTTP
16:03:31.407446 tun0  In  IP 192.0.2.1.8080 > 192.168.49.20.32844: Flags [.], ack 401, win 10000, length 0
16:03:31.707615 tun0  Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [.], seq 401:1401, ack 1, win 64240, length 1000: HTTP
16:03:31.717646 tun0  In  IP 192.0.2.1.8080 > 192.168.49.20.32844: Flags [.], ack 1401, win 10000, length 0
16:03:31.930681 tun0  Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [P.], seq 1401:1801, ack 1, win 64240, length 400: HTTP
16:03:31.967647 tun0  In  IP 192.0.2.1.8080 > 192.168.49.20.32844: Flags [.], ack 1801, win 10000, length 0
16:03:32.970110 ?     Out IP 192.168.49.20.32844 > 192.0.2.1.8080: Flags [F.], seq 1801, ack 1, win 64240, length 0
16:03:32.970135 ?     In  IP 192.0.2.1.8080 > 192.168.49.20.32844: Flags [R.], seq 1, ack 1801, win 10000, length 0
#
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zQbDG065v0CQOzVwHx4IlpgpbibZVXNT5Aia82PzLspHWG0jW3uFquoA1ODg7xKIQe6ake4aNf1Shfa0yrs7NYNQ/640?wx_fmt=jpeg "")  
  
  
**往期推荐**  
  
  
[1. Wireshark 提示和技巧 | 捕获点之 TCP 三次握手](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247486731&idx=1&sn=60629500b326a2d52b19c0bbafc3c913&chksm=90bf6104a7c8e81263136212efa62c0cc7fde6a0239b562cc064d9c78d6907cec45c3539b044&scene=21#wechat_redirect)  
  
  
  
[2. Wireshark 提示和技巧 | a == ${a} 显示过滤宏](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247486344&idx=1&sn=fc6ecf75177d9ec673ab298fd5fbad3b&chksm=90bf6787a7c8ee91a8e38dc41dc075df9246a0a6a9e43eb8c4f0c564f7eec9bd03e933a1961f&scene=21#wechat_redirect)  
  
  
  
[3. Wireshark TS | 防火墙空闲会话超时问题](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247490326&idx=1&sn=35d8b825ab50625613e1b5aa56be213d&chksm=90bf7719a7c8fe0fe7f84718a9690f7785f4fafd5f3bbd5d08e621ad5c0ea0490479b7dc0952&scene=21#wechat_redirect)  
  
  
  
[4. Wireshark TS | HTTP 传输文件慢问题](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247490594&idx=1&sn=307625291ac341948215a135f5e78da7&chksm=90bf702da7c8f93b6593dc469896b15d3a0f35844b6f1abb7f9215d7a59b555aaaadd810d515&scene=21#wechat_redirect)  
  
  
  
[5. 网络设备 MTU MSS Jumboframe 全解](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247487486&idx=1&sn=955c51224fff4ad7726fb5781725eb79&chksm=90bf63f1a7c8eae744f94775d8a337f2d93751247f0967a8d177e17018928af556dc41a44dee&scene=21#wechat_redirect)  
  
  
  
  
后台回复「**TT**  
」获取   
**Wireshark 提示和技巧系列**  
   
合集  
  
后台回复「**TS**  
」获取   
**Wireshark Troubleshooting 系列**  
   
合集  
  
如需交流或加技术群，可后台直接留言，我会在第一时间回复，谢谢！  
  
![](https://mmbiz.qpic.cn/mmbiz_png/agnuXVkibSpmhZ13T6zj8IgQqQGEzj2oVFDgd2JJqtgGAnVSv9ZJcfefwuGBDOezBe61U2owxeiae0G1tOVicF1wA/640?wx_fmt=png "")  
  
  
