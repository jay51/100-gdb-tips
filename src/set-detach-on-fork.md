#Debug both parent and child processes

##example

```
#include <stdio.h>
#include <stdlib.h>

Int main(void) {
Pid_t pid;

Pid = fork();
If (pid < 0)
{
Exit(1);
}
Else if (pid > 0)
{
Printf("Parent\n");
Exit(0);
}
Printf("Child\n");
Return 0;
}
``` 

## Tips

When debugging a multi-process program, gdb will only track the running of the parent process by default, while the child process will run independently, and gdb will not control it. Take the above program as an example:

``` 
(gdb) start
Temporary breakpoint 1 at 0x40055c: file a.c, line 7.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:7
7 pid = fork();
(gdb) n
8 if (pid < 0)
(gdb) Child

12 else if (pid > 0)
(gdb)
14 printf("Parent\n");
(gdb)
Parent
15 exit(0);
``` 

It can be seen that when stepping to the 8th line, the program prints out "Child", proving that the child process has started running independently.

If you want to debug both the parent process and the child process, you can use the "`set detach-on-fork off`" (the default `detach-on-fork` is `on`) command, so that gdb can debug both the parent and child processes and debug. When one process is in progress, another process is in a suspended state. Still take the above program as an example:

``` 
(gdb) set detach-on-fork off
(gdb) start
Temporary breakpoint 1 at 0x40055c: file a.c, line 7.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:7
7 pid = fork();
(gdb) n
[New process 1050]
8 if (pid < 0)
(gdb)
12 else if (pid > 0)
(gdb) i inferior
Num Description Executable
2 process 1050 /data2/home/nanxiao/a
* 1 process 1046 /data2/home/nanxiao/a
(gdb) n
14 printf("Parent\n");
(gdb) n
Parent
15 exit(0);
(gdb)
[Inferior 1 (process 1046) exited normally]
(gdb)
The program is not being run.
(gdb) i inferiors
Num Description Executable
2 process 1050 /data2/home/nanxiao/a
* 1 <null> /data2/home/nanxiao/a
(gdb) inferior 2
[Switching to inferior 2 [process 1050] (/data2/home/nanxiao/a)]
[Switching to thread 2 (process 1050)]
#0 0x00007ffff7af6cad in fork () from /lib64/libc.so.6
(gdb) bt
#0 0x00007ffff7af6cad in fork () from /lib64/libc.so.6
#1 0x0000000000400561 in main () at a.c:7
(gdb) n
Single stepping until exit from function fork,
Which has no line number information.
Main () at a.c:8
8 if (pid < 0)
(gdb)
12 else if (pid > 0)
(gdb)
17 printf("Child\n");
(gdb)
Child
18 return 0;
(gdb)
``` 


After using the "`set detach-on-fork off`" command, use "`i inferiors`" (`i` is the `info` command abbreviation) to view the status of the process, you can see that the parent and child processes are being debugged by gdb The front "*" is the process being debugged. When the parent process exits, use "`inferior infno`" to switch to the child process to debug.


This command is currently supported by Linux. Many other operating systems do not support it. Please pay attention when using it. See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Forks.html)


In addition, if you want the parent and child processes to run at the same time, you can use the "`set schedule-multiple on`" (the default `schedule-multiple` is `off`) command, still take the above code as an example:

```
(gdb) set detach-on-fork off
(gdb) set schedule-multiple on
(gdb) start
Temporary breakpoint 1 at 0x40059c: file a.c, line 7.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:7
7 pid = fork();
(gdb) n
[New process 26597]
Child
```

You can see that "Child" is printed, proving that the child process is also running.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/All_002dStop-Mode.html#All_002dStop-Mode)

##Contributors

Nanxiao




