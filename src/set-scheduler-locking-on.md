# Allow only one thread to run
## Examples
	#include <stdio.h>
	#include <pthread.h>
	int a = 0;
	int b = 0;
	void *thread1_func(void *p_arg)
	{
	        while (1)
	        {
	                a++;
	                sleep(1);
	        }
	}
	
	void *thread2_func(void *p_arg)
	{
	        while (1)
	        {
	                b++;
	                sleep(1);
	        }
	}
	
	int main(void)
	{
	        pthread_t t1, t2;
	
	        pthread_create(&t1, NULL, thread1_func, "Thread 1");
	        pthread_create(&t2, NULL, thread2_func, "Thread 2");
	
	        sleep(1000);
	        return;
	}


## Tips
When debugging multithreaded programs with gdb, once the program is interrupted, all threads are suspended. At this point, when you debug one of the threads (such as the &quot;` step` &quot;,&quot; `next`&quot; command), all threads will be executed simultaneously. Take the above program as an example:

	(gdb) b a.c:9
	Breakpoint 1 at 0x400580: file a.c, line 9.
	(gdb) r
	Starting program: /data2/home/nanxiao/a
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib64/libthread_db.so.1".
	[New Thread 0x7ffff782c700 (LWP 17368)]
	[Switching to Thread 0x7ffff782c700 (LWP 17368)]
	
	Breakpoint 1, thread1_func (p_arg=0x400718) at a.c:9
	9                       a++;
	(gdb) p b
	$1 = 0
	(gdb) s
	10                      sleep(1);
	(gdb) s
	[New Thread 0x7ffff6e2b700 (LWP 17369)]
	11              }
	(gdb)
	
	Breakpoint 1, thread1_func (p_arg=0x400718) at a.c:9
	9                       a++;
	(gdb)
	10                      sleep(1);
	(gdb) p b
	$2 = 3

`thread1_func` updates the value of the global variable` a`, and `thread2_func` updates the value of the global variable` b`. I put a breakpoint on the `a ++` statement in `thread1_func`. When the breakpoint hits for the first time, the value of` b` is printed as `0`. After stepping through` thread1_func` several times, the value of `b` It becomes `3`, which proves that` thread2_func` is also executed when stepping through `thread1_func`.
If you want to suspend execution of other threads while debugging one thread, you can use the &quot;` set scheduler-locking on` &quot;command:

    (gdb) b a.c:9
	Breakpoint 1 at 0x400580: file a.c, line 9.
	(gdb) r
	Starting program: /data2/home/nanxiao/a
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib64/libthread_db.so.1".
	[New Thread 0x7ffff782c700 (LWP 19783)]
	[Switching to Thread 0x7ffff782c700 (LWP 19783)]
	
	Breakpoint 1, thread1_func (p_arg=0x400718) at a.c:9
	9                       a++;
	(gdb) set scheduler-locking on
	(gdb) p b
	$1 = 0
	(gdb) s
	10                      sleep(1);
	(gdb)
	11              }
	(gdb)
	
	Breakpoint 1, thread1_func (p_arg=0x400718) at a.c:9
	9                       a++;
	(gdb)
	10                      sleep(1);
	(gdb)
	11              }
	(gdb) p b
	$2 = 0

It can be seen that after stepping through `thread1_func` several times, the value of` b` is still `0`, which proves that` thread2_func` was not executed when stepping through `thread1_func`.

In addition, the `set scheduler-locking` command supports a` step` mode in addition to the `off` and` on` modes (the default is `off`). Meaning: When you use the &quot;` step` &quot;command to debug a thread, other threads will not execute, but when you use other commands (such as&quot; `next`&quot;) to debug the thread, other threads may execute.

This command depends on the scheduling strategy of the specific operating system, and you need to pay attention when using it. See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/All_002dStop-Mode.html#All_002dStop-Mode).

## Contributor

nanxiao
