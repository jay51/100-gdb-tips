#Let catchpoint only trigger once

##example


```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

Int main(void) {
Pid_t pid;
Int i = 0;

For (i = 0; i < 2; i++)
{
Pid = fork();
If (pid < 0)
{
Exit(1);
}
Else if (pid == 0)
{
Exit(0);
}
}
Printf("hello world\n");
Return 0;
}
```

## Tips
When using the gdb debugger, you can use the ``tcatch`' command to set `catchpoint` to fire only once. Take the above program as an example:

```
(gdb) tcatch fork
Catchpoint 1 (fork)
(gdb) r
Starting program: /home/nan/a

Temporary catchpoint 1 (forked process 27377), 0x00000034e42acdbd in fork () from /lib64/libc.so.6
(gdb) c
Continuing.
Hello world
[Inferior 1 (process 27373) exited normally]
(gdb) q
```

You can see that the program pauses only when the `fork` is called for the first time.

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Set-Catchpoints.html).

##Contributors

Nanxiao

