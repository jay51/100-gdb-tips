#Debug the already running process

##example

```
#include <stdio.h>
#include <pthread.h>
Void *thread_func(void *p_arg)
{
While (1)
{
Printf("%s\n", (char*)p_arg);
Sleep(10);
}
}
Int main(void)
{
Pthread_t t1, t2;

Pthread_create(&t1, NULL, thread_func, "Thread 1");
Pthread_create(&t2, NULL, thread_func, "Thread 2");

Sleep(1000);
Return;
}
```

##Tips

There are two ways to debug a running process: one is the ID of the specified process when gdb starts: gdb program processID (you can also specify the process ID with -p or --pid, for example: gdb program -p=10210). Taking the above code as an example, the process ID has been obtained with the "ps" command: 10210:

``` 
Bash-3.2# gdb -q a 10210
Reading symbols from /data/nan/a...done.
Attaching to program `/data/nan/a', process 10210
[New process 10210]
Retry #1:
Retry #2:
Retry #3:
Retry #4:
Reading symbols from /usr/lib/libc.so.1...(no debugging symbols found)...done.
[Thread debugging using libthread_db enabled]
[New LWP 3 ]
[New LWP 2 ]
[New Thread 1 (LWP 1)]
[New Thread 2 (LWP 2)]
[New Thread 3 (LWP 3)]
Loaded symbols for /usr/lib/libc.so.1
Reading symbols from /lib/ld.so.1...(no debugging symbols found)...done.
Loaded symbols for /lib/ld.so.1
[Switching to Thread 1 (LWP 1)]
0xfeeeae55 in ___nanosleep () from /usr/lib/libc.so.1
(gdb) bt
#0 0xfeeeae55 in ___nanosleep () from /usr/lib/libc.so.1
#1 0xfeedcae4 in sleep () from /usr/lib/libc.so.1
#2 0x080509ef in main () at a.c:17
```  

If it is too troublesome to check the process number every time, please try the following script

```shell
# Save as xgdb.sh (add executable permissions)
#使用xgdb.sh a
Prog_bin=$1
Running_name=$(basename $prog_bin)
Pid=$(/sbin/pidof $running_name)
Gdb attach $pid
```

The other is to start gdb first, then "attach" the process with the "attach" command:

```  
Bash-3.2# gdb -q a
Reading symbols from /data/nan/a...done.
(gdb) attach 10210
Attaching to program `/data/nan/a', process 10210
[New process 10210]
Retry #1:
Retry #2:
Retry #3:
Retry #4:
Reading symbols from /usr/lib/libc.so.1...(no debugging symbols found)...done.
[Thread debugging using libthread_db enabled]
[New LWP 3 ]
[New LWP 2 ]
[New Thread 1 (LWP 1)]
[New Thread 2 (LWP 2)]
[New Thread 3 (LWP 3)]
Loaded symbols for /usr/lib/libc.so.1
Reading symbols from /lib/ld.so.1...(no debugging symbols found)...done.
Loaded symbols for /lib/ld.so.1
[Switching to Thread 1 (LWP 1)]
0xfeeeae55 in ___nanosleep () from /usr/lib/libc.so.1
(gdb) bt
#0 0xfeeeae55 in ___nanosleep () from /usr/lib/libc.so.1
#1 0xfeedcae4 in sleep () from /usr/lib/libc.so.1
#2 0x080509ef in main () at a.c:17
```  

If you don't want to continue debugging, you can use the "detach" command to "leave" the process:

```
(gdb) detach
Detaching from program: /data/nan/a, process 10210
(gdb) bt
No stack.
```
See the [gdb manual] (https://sourceware.org/gdb/current/onlinedocs/gdb/Attach.html#index-attach)for details 

##Contributors

Nanxiao

