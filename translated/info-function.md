# List function names

## Examples

	#include <stdio.h>
	#include <pthread.h>
	void *thread_func(void *p_arg)
	{
	        while (1)
	        {
	                sleep(10);
	        }
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

When debugging with gdb, use the &quot;` info functions` &quot;command to list all the function names of the executable. Take the above code as an example:

	(gdb) info functions
	All defined functions:
	
	File a.c:
	int main(void);
	void *thread_func(void *);
	
	Non-debugging symbols:
	0x0805079c  _PROCEDURE_LINKAGE_TABLE_
	0x080507ac  _cleanup@plt
	0x080507bc  atexit
	0x080507bc  atexit@plt
	0x080507cc  __fpstart
	0x080507cc  __fpstart@plt
	0x080507dc  exit@plt
	0x080507ec  __deregister_frame_info_bases@plt
	0x080507fc  __register_frame_info_bases@plt
	0x0805080c  _Jv_RegisterClasses@plt
	0x0805081c  sleep
	0x0805081c  sleep@plt
	0x0805082c  pthread_create@plt
	0x0805083c  _start
	0x080508b4  _mcount
	0x080508b8  __do_global_dtors_aux
	0x08050914  frame_dummy
	0x080509f4  __do_global_ctors_aux
	0x08050a24  _init
	0x08050a31  _fini

	
You can see that the function prototype is listed as well as the function without debugging information.

In addition, this command also supports regular expressions: &quot;` info functions regex` &quot;, which will only list the function names that match the regular expression, for example:

	(gdb) info functions thre*
	All functions matching regular expression "thre*":
	
	File a.c:
	void *thread_func(void *);
	
	Non-debugging symbols:
	0x0805082c  pthread_create@plt




You can see that gdb will only list functions whose name contains &quot;thre`&quot;.

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Symbols.html)

## Contributor

nanxiao



