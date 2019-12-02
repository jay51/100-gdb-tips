#Set temporary breakpoints

##example

```
#include <stdio.h>
#include <pthread.h>

Typedef struct
{
Int a;
Int b;
Int c;
Int d;
Pthread_mutex_t mutex;
}ex_st;

Int main(void) {
Ex_st st = {1, 2, 3, 4, PTHREAD_MUTEX_INITIALIZER};
Printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
Return 0;
}
```

## Tips

When using gdb, if you want the breakpoint to take effect only once, you can use the "tbreak" command (abbreviated as: tb). Take the above program as an example:

```
(gdb) tb a.c: 15
Temporary breakpoint 1 at 0x400500: file a.c, line 15.
(gdb) i b
Num Type Disp Enb Address What
1 breakpoint del y 0x0000000000400500 in main at a.c:15
(gdb) r
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:15
15 printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
(gdb) i b
No breakpoints or watchpoints.
```

First set a temporary breakpoint on line 15 of the file. When the program is disconnected, use the "i b" ("info breakpoints" abbreviation) command to view the breakpoint and find that the breakpoint is gone. That is, after the breakpoint hits once, it is deleted.

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Set-Breaks.html) for details

##Contributors

Nanxiao

