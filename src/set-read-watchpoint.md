#Set read point

##example

```
#include <stdio.h>
#include <pthread.h>

Int a = 0;

Void *thread1_func(void *p_arg)
{
While (1)
{
Printf("%d\n", a);
Sleep(10);
}
}

Int main(void)
{
Pthread_t t1;

Pthread_create(&t1, NULL, thread1_func, "Thread 1");

Sleep(1000);
Return;
}
```

## Tips
Gdb can use the "`rwatch`" command to set the read watchpoint, that is, when the read variable behavior occurs, the program will pause. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x4005f3: file a.c, line 19.
Starting program: /data2/home/nanxiao/a
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".

Temporary breakpoint 1, main () at a.c:19
19 pthread_create(&t1, NULL, thread1_func, "Thread 1");
(gdb) rw a
Hardware read watchpoint 2: a
(gdb) c
Continuing.
[New Thread 0x7ffff782c700 (LWP 5540)]
[Switching to Thread 0x7ffff782c700 (LWP 5540)]
Hardware read watchpoint 2: a

Value = 0
0x00000000004005c6 in thread1_func (p_arg=0x40071c) at a.c:10
10 printf("%d\n", a);
(gdb) c
Continuing.
0
Hardware read watchpoint 2: a

Value = 0
0x00000000004005c6 in thread1_func (p_arg=0x40071c) at a.c:10
10 printf("%d\n", a);
(gdb) c
Continuing.
0
Hardware read watchpoint 2: a

Value = 0
0x00000000004005c6 in thread1_func (p_arg=0x40071c) at a.c:10
10 printf("%d\n", a);

```
As you can see, after using the "`rw a`" command (`rw` is an abbreviation for `rwatch` command), each time you access the value of `a`, the program will stop.

Note that the `rwatch` command only works for hardware watchpoints, 
see the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Watchpoints.html).

##Contributors

Nanxiao

