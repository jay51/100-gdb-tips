#Set the catchpoint crack anti-debugging program by calling ptrace

##example

```
#include <sys/ptrace.h>
#include <stdio.h>

Int main()
{
If (ptrace(PTRACE_TRACEME, 0, 0, 0) < 0 ) {
Printf("Gdb is debugging me, exit.\n");
Return 1;
}
Printf("No debugger, continuous\n");
Return 0;
}
```



## Tips

Some programs don't want to be debugged by gdb, they will call the "`ptrace`" function in the program. Once the return fails, it proves that the program is being tracked by a similar program such as gdb, so it exits directly. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x400508: file a.c, line 6.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:6
6 if (ptrace(PTRACE_TRACEME, 0, 0, 0) < 0 ) {
(gdb) n
7 printf("Gdb is debugging me, exit.\n");
(gdb)
Gdb is debugging me, exit.
8 return 1;
```


The way to crack such a program is to set `catchpoint` for the `ptrace` call, and modify the return value of `ptrace` to achieve the purpose. Still take the above program as an example:

```
(gdb) catch syscall ptrace
Catchpoint 2 (syscall 'ptrace' [101])
(gdb) r
Starting program: /data2/home/nanxiao/a

Catchpoint 2 (call to syscall ptrace), 0x00007ffff7b2be9c in ptrace () from /lib64/libc.so.6
(gdb) c
Continuing.

Catchpoint 2 (returned from syscall ptrace), 0x00007ffff7b2be9c in ptrace () from /lib64/libc.so.6
(gdb) set $rax = 0
(gdb) c
Continuing.
No debugger, continuing
[Inferior 1 (process 11491) exited normally]
```

It can be seen that by modifying the value of the `rax` register, the purpose of modifying the return value is achieved, so that gdb can continue to debug the program (print "`No debugger, continuing`").

For detailed procedures, see this article [Avoiding PTRACE_TRACME Anti-Tracking Tips] (http://blog.linux.org.tw/~jserv/archives/2011_08.html).

##Contributors

Nanxiao

