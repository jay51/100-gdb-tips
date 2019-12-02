# Do not display thread startup and exit information
## Examples
	#include <stdio.h>
	#include <pthread.h>
	
	void *thread_func(void *p_arg)
	{
	       sleep(10);
	}
	
	int main(void)
	{
	        pthread_t t1, t2;
	
	        pthread_create(&t1, NULL, thread_func, "Thread 1");
	        pthread_create(&t2, NULL, thread_func, "Thread 2");
	
	        sleep(1000);
	        return;
	}


## Tips
By default, when gdb detects that a thread is created and exits, it will print a prompt message. Take the above program as an example:

	(gdb) r
	Starting program: /data/nan/a
	[Thread debugging using libthread_db enabled]
	[New Thread 1 (LWP 1)]
	[New LWP    2        ]
	[New LWP    3        ]
	[LWP    2         exited]
	[New Thread 2        ]
	[LWP    3         exited]
	[New Thread 3        ]


If you don&#39;t want to display this information, you can use &quot;` set print thread-events off` &quot;command, so that when a thread is created and exited, the prompt message will not be printed:

    (gdb) set print thread-events off
	(gdb) r
	Starting program: /data/nan/a
	[Thread debugging using libthread_db enabled]



You can see that the relevant information is no longer printed.

This command is not supported on some platforms, please pay attention when using it. See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Threads.html).

## Contributor

nanxiao
