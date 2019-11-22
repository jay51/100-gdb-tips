#Set watchpoints only for specific threads

##example

```
#include <stdio.h>
#include <pthread.h>

Int a = 0;

Void *thread1_func(void *p_arg)
{
While (1)
{
a++;
Sleep(10);
}
}

Void *thread2_func(void *p_arg)
{
While (1)
{
a++;
Sleep(10);
}
}

Int main(void)
{
Pthread_t t1, t2;

Pthread_create(&t1, NULL, thread1_func, "Thread 1");
Pthread_create(&t2, NULL, thread2_func, "Thread 2");

Sleep(1000);
Return;
}
```

## Tips
Gdb can use the "`watch expr thread threadnum`" command to set the watchpoint only for specific threads, that is, only the thread numbered `threadnum` changes the value of the variable, the program will stop, and other numbered threads change the value of the variable. Will not stop the program. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x4005d4: file a.c, line 28.
Starting program: /data2/home/nanxiao/a
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".

Temporary breakpoint 1, main () at a.c:28
28 pthread_create(&t1, NULL, thread1_func, "Thread 1");
(gdb) n
[New Thread 0x7ffff782c700 (LWP 25443)]
29 pthread_create(&t2, NULL, thread2_func, "Thread 2");
(gdb)
[New Thread 0x7ffff6e2b700 (LWP 25444)]
31 sleep(1000);
(gdb) i threads
Id Target Id Frame
3 Thread 0x7ffff6e2b700 (LWP 25444) 0x00007ffff7915911 in clone () from /lib64/libc.so.6
2 Thread 0x7ffff782c700 (LWP 25443) 0x00007ffff78d9bcd in nanosleep () from /lib64/libc.so.6
* 1 Thread 0x7ffff7fe9700 (LWP 25413) main () at a.c:31
(gdb) wa a thread 2
Hardware watchpoint 2: a
(gdb) c
Continuing.
[Switching to Thread 0x7ffff782c700 (LWP 25443)]
Hardware watchpoint 2: a

Old value = 1
New value = 3
Thread1_func (p_arg=0x400718) at a.c:11
11 sleep(10);
(gdb) c
Continuing.
Hardware watchpoint 2: a

Old value = 3
New value = 5
Thread1_func (p_arg=0x400718) at a.c:11
11 sleep(10);
(gdb) c
Continuing.
Hardware watchpoint 2: a

Old value = 5
New value = 7
Thread1_func (p_arg=0x400718) at a.c:11
11 sleep(10);
```


As you can see, after using the "`wa a thread 2`" command (`wa` is the abbreviation of `watch` command), only `thread1_func` changes the value of `a` to stop the program.

It should be noted that this way of setting the watchpoint for a specific thread is only valid for the hardware watchpoint, see [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Watchpoints.html).

##Contributors

Nanxiao

