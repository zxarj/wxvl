#  Mitre_Att&ck框架T1622（调试器规避）技术的简单实现   
原创 彭瑞  新蜂网络安全实验室   2024-12-13 01:00  
  
一、技术描述  
  
在Mitre Att&ck框架中，T1036.006(调试器规避）技术位于“防御规避（Defense Evasion）”战术中，官方对该技术的描述如下：  
  
攻击者可能采用各种手段来检测和规避调试器。调试器通常被防御者用来追踪或分析潜在恶意软件的有效负载执行。  
  
调试器规避可能包括根据检测调试环境特征的结果来改变行为。类似于虚拟化/沙箱规避，如果攻击者检测到调试器，他们可能会改变其恶意软件的行为，以脱离受害者或隐藏植入物的核心功能。他们也可能在投放二级或附加的有效负载之前搜索调试器的特征。  
  
具体的检查会根据目标和/或攻击者而有所不同，但可能涉及如IsDebuggerPresent()和NtQueryInformationProcess()等原生API函数调用，或手动检查进程环境块(PEB)的BeingDebugged标志。对调试工件的其他检查还可能试图枚举硬件断点、中断汇编操作码、时间检查或测量当前进程中的异常（假设存在的调试器会“吞噬”或处理潜在的错误）。  
  
攻击者可能利用从这些调试器检查中学到的信息，在自动化发现过程中塑造后续行为。通过循环调用如OutputDebugStringW()等原生API函数产生的消息，攻击者还可以通过分离进程或将无意义的数据淹没调试日志来规避调试器。  
  
  
二、技术实现  
  
下面的操作在Linux系统中完成。  
  
1、检查/proc/self/status  
  
原理：  
  
恶意软件可以读取/proc/self/status文件中的TracerPid字段。如果该值不是0，则表示当前进程正在被另一个进程跟踪（即被调试）。  
  
  
演示：  
  
编写测试脚本：  
  
vi check_debug.sh  //编辑脚本文件，加入下面的内容  
  
#!/bin/bash  
  
  
# 检查是否被调试  
  
check_debugger() {  
  
    # 读取 /proc/self/status 文件中的 TracerPid 字段  
  
    tracer_pid=$(grep -o "TracerPid:[[:space:]]*[0-9]*" /proc/self/status | awk '{print $2}')  
  
  
    # 如果 TracerPid 不是 0，表示有调试器存在  
  
    if [ "$tracer_pid" -ne 0 ]; then  
  
        echo "Debugger detected"  
  
        exit 1  
  
    fi  
  
}  
  
# 调用函数进行检查  
  
check_debugger  
  
# 如果没有被调试，则进入循环持续输出“running”  
  
while true; do  
  
    echo "running"  
  
    sleep 1  # 添加短暂的延迟以避免过快输出  
  
done  
  
保存退出。  
  
脚本启动时查看/proc/self/status文件中TracerPid的值，如果该值非0则认为调试器在运行并退出，否则持续输出“running”。  
  
  
//赋予执行权限  
  
chmod +x check_debug.sh  
  
  
//未处于调试模式  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0IpibYrSbrfcicMeOAhXtwUiaCYWK7B0rZBQ2r0gxSXMAmDhcOVCxiaShN4XHw/640?wx_fmt=png&from=appmsg "")  
  
  
//使用strace对脚本进行跟踪调试  
  
strace -f ./check_debug.sh  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0Ipibd0oejL6OQLsG0JxcOqLP5VibMxP1JbafsXY24GTrkiaSBRuKibZQzIfyA/640?wx_fmt=png&from=appmsg "")  
  
脚本输出“Debugger detected”并退出。  
  
  
2、利用ptrace系统调用  
  
原理：  
  
恶意软件可以通过尝试附加到自己上进行调试（例如通过PTRACE_TRACEME），如果成功，则说明没有其他调试器存在；如果失败，则可能已经有调试器附着。  
  
  
演示：  
  
编写测试程序  
  
vi ptrace_check_1.c  //加入下面的内容  
  
#include <stdio.h>  
  
#include <stdlib.h>  
  
#include <sys/ptrace.h>  
  
#include <unistd.h>  
  
#include <errno.h>  
  
  
int main() {  
  
    // 尝试使用 PTRACE_TRACEME 附加到自身。如果调试器已存在，则会失败。  
  
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {  
  
        if (errno == EPERM) {  
  
            fprintf(stderr, "Debugger detected\n");  
  
            return 1; // 表示检测到调试器  
  
        } else {  
  
            perror("ptrace"); // 处理其他 ptrace 错误  
  
            return 1;  
  
        }  
  
    }  
  
  
    // 如果 ptrace 成功，则表示未检测到调试器  
  
    while (1) {  
  
        printf("running\n");  
  
        usleep(1000000); // 暂停 1 秒，避免过度输出  
  
    }  
  
  
    r  
eturn 0;  
  
}  
  
保存退出。  
  
程序启动时尝试将PTRACE_TRACEME附加到自身，若失败认为存在调试器并退出，若成功则持续输出“running”。  
  
  
//编译生成可执行文件  
  
gcc -o ptrace_check ptrace_check.c  
  
  
//未处于调试模式  
  
./ptrace_check_1  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0IpibS6Se2E0QhLAZgjj8xhUNOmlyrBI1iaicoQiar8IfvtgzNcATS4VmNj5qg/640?wx_fmt=png&from=appmsg "")  
  
  
//处于调试模式  
  
strace ./ptrace_check_1  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0Ipib3zVdTec6m2yhw1eLRZeMLpXRF6BIHRiaY0iaiac6g85JBmvl2dSTwZEmA/640?wx_fmt=png&from=appmsg "")  
  
输出“Debugger detected”并退出。  
  
  
3、检查父进程  
  
原理：  
  
恶意软件可以检查自己的父进程ID，并验证其名称是否属于已知的调试工具（例如gdb、strace等），或者检查其他与调试相关的属性。  
  
  
演示：  
  
vi check_dad.c  //加入下面的内容  
  
#include <stdio.h>  
  
#includ  
e <stdlib.h>  
  
#include <string.h>  
  
#include <unistd.h>  
  
  
// 检测父进程名称  
  
int is_being_debugged() {  
  
    char parent_cmd[256];  
  
    char parent_cmd_path[256];  
  
    sprintf(parent_cmd_path, "/proc/%d/cmdline", getppid());  
  
  
    FILE *file = fopen(parent_cmd_path, "r");  
  
    if (file == NULL) {  
  
        perror("fopen");  
  
        return 0;  
  
    }  
  
  
    if (fgets(parent_cmd, sizeof(parent_cmd), file) != NULL) {  
  
        // 去除换行符  
  
        size_t len = strlen(parent_cmd);  
  
        if (len > 0 && parent_cmd[len - 1] == '\n') {  
  
            parent_cmd[len - 1] = '\0';  
  
        }  
  
    }  
  
  
    fclose(file);  
  
  
    // 检测父进程名称是否为 gdb 或 strace  
  
    if (strcmp(parent_cmd, "gdb") == 0 || strcmp(parent_cmd, "strace") == 0) {  
  
        return 1;  
  
    }  
  
  
    return 0;  
  
}  
  
  
int main() {  
  
    if (is_being_debugged()) {  
  
        printf("Debugger detected\n");  
  
        exit(1);  
  
    } else {  
  
        while (1) {  
  
            printf("running\n");  
  
            sleep(1);  
  
        }  
  
  
    }  
  
    re  
turn 0;  
  
}  
  
保存退出。  
  
该程序启动时查看父进程名称，如果是gdb或者strace，则认为有调试器在运行并退出，否则持续输出“running”。  
  
  
//编译生成可执行文件  
  
gcc -o check_dad check_dad.c  
  
  
//未处于调试模式  
  
./check_dad  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0IpibicuQzzFniaLVk8VB2VA8u0lbb0A8fDEQNsnnrnYM481KRE8kLyTyhibFg/640?wx_fmt=png&from=appmsg "")  
  
  
//处于调试模式  
  
strace ./check_dad  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kyPvT2WYYLGJia88jZ3ATDPd2rzAV0IpibQJ6l8ldGzICmU6yYNAvVWkUgYh0xuI20UJGm0RRfp2V37aibKJLIJnQ/640?wx_fmt=png&from=appmsg "")  
  
输出  
“Debugger detected”并退出。  
  
