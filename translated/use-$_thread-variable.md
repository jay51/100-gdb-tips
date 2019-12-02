# Use &quot;$ _thread&quot; variable
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
	                a++;
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
gdb introduced `$ _thread` as a` convenience variable` from version 7.2, which is used to save the thread number currently being debugged. This variable is useful when writing breakpoint commands or command scripts. Take the above program as an example:
	
	(gdb) wa a
	Hardware watchpoint 2: a
	(gdb) command 2
	Type commands for breakpoint(s) 2, one per line.
	End with a line saying just "end".
	>printf "thread id=%d\n", $_thread
	>end

First set the observation point: &quot;wa a&quot; (`wa` is the abbreviation of` watch` command), that is, when the value of `a` changes, the program will pause, and then the thread number is printed in the` commands` statement.
Then proceed with the program:

	(gdb) c
	Continuing.
	[New Thread 0x7ffff782c700 (LWP 20928)]
	[Switching to Thread 0x7ffff782c700 (LWP 20928)]
	Hardware watchpoint 2: a
	
	Old value = 0
	New value = 1
	thread1_func (p_arg=0x400718) at a.c:11
	11                      sleep(10);
	thread id=2
	(gdb) c
	Continuing.
	[New Thread 0x7ffff6e2b700 (LWP 20929)]
	[Switching to Thread 0x7ffff6e2b700 (LWP 20929)]
	Hardware watchpoint 2: a
	
	Old value = 1
	New value = 2
	thread2_func (p_arg=0x400721) at a.c:20
	20                      sleep(10);
	thread id=3

You can see that when the program is paused, the thread number is printed: &quot;` thread id = 2` &quot;or&quot; `thread id = 3`&quot;.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Threads.html).

## Contributor

nanxiao
