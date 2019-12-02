# Print stack information of all threads
## Examples
	#include <stdio.h>
	#include <pthread.h>
	#include <unistd.h>
	int a = 0;

	void *thread1_func(void *p_arg)
	{
	        while (1)
	        {
	                a++;
	                sleep(10);
	        }
	}

	int main(int argc, char* argv[])
	{
	        pthread_t t1, t2;
	        pthread_create(&t1, NULL, thread1_func, NULL);
	        pthread_create(&t2, NULL, thread1_func, NULL);

	        sleep(1000);
	        return 0;
	}

## Tips
gdb can use the &quot;` thread apply all bt` &quot;command to print the stack information of all threads. Take the above program as an example:

    (gdb) thread apply all bt

    Thread 3 (Thread -1210868832 (LWP 26975)):
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6
    #1  0xb7dcc77f in sleep () from /lib/libc.so.6
    #2  0x08048575 in thread1_func ()
    #3  0xb7e871eb in start_thread () from /lib/libpthread.so.0
    #4  0xb7e007fe in clone () from /lib/libc.so.6

    Thread 2 (Thread -1219257440 (LWP 26976)):
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6
    #1  0xb7dcc77f in sleep () from /lib/libc.so.6
    #2  0x08048575 in thread1_func ()
    #3  0xb7e871eb in start_thread () from /lib/libpthread.so.0
    #4  0xb7e007fe in clone () from /lib/libc.so.6

    Thread 1 (Thread -1210866000 (LWP 26974)):
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6
    #1  0xb7dcc77f in sleep () from /lib/libc.so.6
    #2  0x08048547 in main ()
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6

It can be seen that after using the `thread apply all bt` command, the backtrace command will be implemented on all threads. `thread apply [thread-id-list] [all] args` can also execute the specified thread ID list:

    (gdb) thread apply 1-2 bt

    Thread 1 (Thread -1210866000 (LWP 26974)):
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6
    #1  0xb7dcc77f in sleep () from /lib/libc.so.6
    #2  0x08048547 in main ()

    Thread 2 (Thread -1219257440 (LWP 26976)):
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6
    #1  0xb7dcc77f in sleep () from /lib/libc.so.6
    #2  0x08048575 in thread1_func ()
    #3  0xb7e871eb in start_thread () from /lib/libpthread.so.0
    #4  0xb7e007fe in clone () from /lib/libc.so.6
    #0  0xb7dcc96c in __gxx_personality_v0 () from /lib/libc.so.6

For more usage of `thread apply` and format usage of` thread-id-list`, see [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Threads.html).

## Contributor

panzhongxian
