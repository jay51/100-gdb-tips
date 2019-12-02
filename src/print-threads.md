#View thread information

##example

```
#include <stdio.h>
#include <pthread.h>
void *thread_func(void *p_arg)
{
        while (1) {
                printf("%s\n", (char*)p_arg);
                sleep(10);
        }
}
int main(void) {
        pthread_t t1, t2;

        pthread_create(&t1, NULL, thread_func, "Thread 1");
        pthread_create(&t2, NULL, thread_func, "Thread 2");

        sleep(1000);
        return;
}
```

##Tips

To debug multithreaded programs with gdb, you can use the "i threads" command (i is the info command abbreviation) to view the information of all threads. Take the above program as an example (running platform is Linux, CPU is X86_64):

```
(gdb) i threads
Id   Target Id         Frame
3    Thread 0x7ffff6e2b700 (LWP 31773) 0x00007ffff7915911 in clone () from /lib64/libc.so.6
2    Thread 0x7ffff782c700 (LWP 31744) 0x00007ffff78d9bcd in nanosleep () from /lib64/libc.so.6
* 1    Thread 0x7ffff7fe9700 (LWP 31738) main () at a.c:18
```


The first item (Id): gdb indicates the unique ID of each thread: 1, 2, and so on.

The second item (Target Id): is the ID of the specific system platform used to indicate each thread. Different platform information may be different. Like the current Linux platform shows: Thread 0x7ffff6e2b700 (LWP 31773).

The third item (Frame): shows which function the thread executes to.

The front with "*" means "current thread", which can be understood as a "default thread" selected when gdb debugs a multithreaded program.

Taking the Solaris platform (CPU is X86_64) as an example, you can see that the display information is slightly different:

```
(gdb) i threads
[New Thread 2 (LWP 2)]
[New Thread 3 (LWP 3)]
  Id   Target Id         Frame
  6    Thread 3 (LWP 3)  0xfeec870d in _thr_setup () from /usr/lib/libc.so.1
  5    Thread 2 (LWP 2)  0xfefc9661 in elf_find_sym () from /usr/lib/ld.so.1
  4    LWP    3          0xfeec870d in _thr_setup () from /usr/lib/libc.so.1
  3    LWP    2          0xfefc9661 in elf_find_sym () from /usr/lib/ld.so.1
* 2    Thread 1 (LWP 1)  main () at a.c:18
  1    LWP    1          main () at a.c:18

```

You can also use "i threads [Id...]" to specify information for printing certain threads, for example:

```
(gdb) i threads 1 2
Id   Target Id         Frame
2    Thread 0x7ffff782c700 (LWP 12248) 0x00007ffff78d9bcd in nanosleep () from /lib64/libc.so.6
* 1    Thread 0x7ffff7fe9700 (LWP 12244) main () at a.c:18
```

Use "thread thread-id" to switch between different threads and view the stack information of the specified thread.

```
(gdb) thread 2
[Switching to thread 2 (Thread 0x7ffff782c700 (LWP 12248))]...
```

Use "thread apply [thread-id-list] [all] args" to execute commands on multiple threads, for example: `thread apply all bt` to see the stack information for all threads.

```
(gdb) thread apply all bt
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Threads.html).

## Contributors

nanxiao, shanbaoyin
