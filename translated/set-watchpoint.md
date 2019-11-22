#Set the observation point

##example

```
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
Int a = 0;

Void *thread1_func(void *p_arg) {
While (1) {
    a++;
    Sleep(10);
    }
}

Int main(int argc, char* argv[]) {
Pthread_t t1;
Pthread_create(&t1, NULL, thread1_func, NULL);

Sleep(1000);
Return 0;
}
```

##Tips
Gdb can use the "`watch`" command to set the watchpoint, that is, when a variable value changes, the program will stop. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x4005a8: file a.c, line 19.
Starting program: /data2/home/nanxiao/a
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".

Temporary breakpoint 1, main () at a.c:19
19 pthread_create(&t1, NULL, thread1_func, "Thread 1");
(gdb) watch a
Hardware watchpoint 2: a
(gdb) r
Starting program: /data2/home/nanxiao/a
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
[New Thread 0x7ffff782c700 (LWP 8813)]
[Switching to Thread 0x7ffff782c700 (LWP 8813)]
Hardware watchpoint 2: a

Old value = 0
New value = 1
Thread1_func (p_arg=0x4006d8) at a.c:11
11 sleep(10);
(gdb) c
Continuing.
Hardware watchpoint 2: a

Old value = 1
New value = 2
Thread1_func (p_arg=0x4006d8) at a.c:11
11 sleep(10);
``` 

As you can see, after using the "`watch a`" command, when the value of `a` changes: from `0` to `1`, from `1` to `2`, the program will stop.
You can also use the command "`watch *(data type*)address`", still use the above program as an example:

```
(gdb) p &a
$1 = (int *) 0x6009c8 <a>
(gdb) watch *(int*)0x6009c8
Hardware watchpoint 2: *(int*)0x6009c8
(gdb) r
Starting program: /data2/home/nanxiao/a
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
[New Thread 0x7ffff782c700 (LWP 15431)]
[Switching to Thread 0x7ffff782c700 (LWP 15431)]
Hardware watchpoint 2: *(int*)0x6009c8

Old value = 0
New value = 1
Thread1_func (p_arg=0x4006d8) at a.c:11
11 sleep(10);
(gdb) c
Continuing.
Hardware watchpoint 2: *(int*)0x6009c8

Old value = 1
New value = 2
Thread1_func (p_arg=0x4006d8) at a.c:11
11 sleep(10);
```

First get the address of `a`: `0x6009c8`, then set the observation point with "`watch *(int*)0x6009c8`", you can see the same effect as the "`watch a`" command.

The observation point can be implemented by software or hardware, depending on the specific system. However, the observation point of the software implementation will cause the program to run very slowly, so be careful when using it. See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Watchpoints.html).

If the system supports hardware observation, when setting the observation point, the following information will be printed:

Hardware watchpoint num: expr

If you do not want to use hardware to observe points, you can set them as follows:
Set can-use-hw-watchpoints

##View breakpoints
List all the observation points currently set:
```
Info watchpoints
```

The breakpoint set by watch can also be controlled with commands that control breakpoints. Such as disable, enable, delete, etc.

##Contributors

Nanxiao

