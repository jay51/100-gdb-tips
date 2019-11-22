#Set catchpoint for fork call
##example

```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

Int main(void) {
Pid_t pid;

Pid = fork();
If (pid < 0)
{
Exit(1);
}
Else if (pid > 0)
{
Exit(0);
}
Printf("hello world\n");
Return 0;
}

```

## Tips
When using the gdb debugger, you can use the ``catch fork`' command to set `catchpoint` for the `fork` call, using the above program as an example:

```
(gdb) catch fork
Catchpoint 1 (fork)
(gdb) r
Starting program: /home/nan/a

Catchpoint 1 (forked process 33499), 0x00000034e42acdbd in fork () from /lib64/libc.so.6
(gdb) bt
#0 0x00000034e42acdbd in fork () from /lib64/libc.so.6
#1 0x0000000000400561 in main () at a.c:9
```

It can be seen that gdb will suspend the running of the program when the `fork` call occurs.
Note: This feature is currently only supported on HP-UX and GNU/Linux.
See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Catchpoints.html).

##Contributors

Nanxiao

