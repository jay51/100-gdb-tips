# Set read and write observation points
## Examples
	#include <stdio.h>
	#include <pthread.h>
	
	int a = 0;
	
	void *thread1_func(void *p_arg)
	{
	        while (1)
	        {
	                a++;
	                sleep(10);
	        }
	}
	
	void *thread2_func(void *p_arg)
	{
	        while (1)
	        {
	                printf("%d\n", a);;
	                sleep(10);
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
gdb can use the &quot;` awatch` &quot;command to set read and write watchpoints, that is, the program will halt when the behavior of reading variables or changing the value of variables occurs. Take the above program as an example:

	(gdb) aw a
	Hardware access (read/write) watchpoint 1: a
	(gdb) r
	Starting program: /data2/home/nanxiao/a
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib64/libthread_db.so.1".
	[New Thread 0x7ffff782c700 (LWP 16938)]
	[Switching to Thread 0x7ffff782c700 (LWP 16938)]
	Hardware access (read/write) watchpoint 1: a
	
	Value = 0
	0x00000000004005c6 in thread1_func (p_arg=0x40076c) at a.c:10
	10                      a++;
	(gdb) c
	Continuing.
	Hardware access (read/write) watchpoint 1: a
	
	Old value = 0
	New value = 1
	thread1_func (p_arg=0x40076c) at a.c:11
	11                      sleep(10);
	(gdb) c
	Continuing.
	[New Thread 0x7ffff6e2b700 (LWP 16939)]
	[Switching to Thread 0x7ffff6e2b700 (LWP 16939)]
	Hardware access (read/write) watchpoint 1: a
	
	Value = 1
	0x00000000004005f2 in thread2_func (p_arg=0x400775) at a.c:19
	19                      printf("%d\n", a);;
	(gdb) c
	Continuing.
	1
	[Switching to Thread 0x7ffff782c700 (LWP 16938)]
	Hardware access (read/write) watchpoint 1: a
	
	Value = 1
	0x00000000004005c6 in thread1_func (p_arg=0x40076c) at a.c:10
	10                      a++;

It can be seen that after using the `` aw a` ”command (` aw` is an abbreviation of the `awatch` command), each time the value of` a` is read or changed, the program will stop.
It should be noted that the `awatch` command only takes effect on hardware watchpoints, see [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Watchpoints.html).

## Contributor

nanxiao
