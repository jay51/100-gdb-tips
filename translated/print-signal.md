# Whether to print signal information when a signal occurs
## Examples
	#include <stdio.h>
	#include <signal.h>
	
	void handler(int sig);
	
	void handler(int sig)
	{
	        signal(sig, handler);
	        printf("Receive signal: %d\n", sig);
	}
	
	int main(void) {
	        signal(SIGHUP, handler);
	        
	        while (1)
	        {
	                sleep(1);
	        }
	        return 0;
	}

## Tips
When debugging a program with gdb, you can use the &quot;` handle signal print / noprint` &quot;command to set whether to print signal information when a signal occurs. Take the above program as an example:

	(gdb) i signals 
	Signal        Stop      Print   Pass to program Description
	
	SIGHUP        Yes       Yes     Yes             Hangup
	......

	(gdb) r
	Starting program: /data1/nan/test 
	[Thread debugging using libthread_db enabled]
	[New Thread 1 (LWP 1)]
	
	Program received signal SIGHUP, Hangup.
	[Switching to Thread 1 (LWP 1)]
	0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
	(gdb) c
	Continuing.
	Receive signal: 1

You can see that by default, when the `SIGHUP` signal occurs, gdb will suspend the execution of the program and print the information of the received signal. You need to execute the `continue` command to continue the execution of the program.

Next, use the `` handle SIGHUP noprint` command to set that when the `SIGHUP` signal occurs, gdb does not print the signal information. The execution is as follows:

	(gdb) handle SIGHUP noprint 
	Signal        Stop      Print   Pass to program Description
	SIGHUP        No        No      Yes             Hangup
	(gdb) r
	Starting program: /data1/nan/test 
	[Thread debugging using libthread_db enabled]
	Receive signal: 1

It should be noted that when setting `noprint`,` nostop` is also set by default. It can be seen that when the program receives the `SIGHUP` signal, it does not pause and does not print signal information. Instead, it continues.

If you want to restore the previous behavior, you can use the `` handle SIGHUP print` command.

See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Signals.html).

## Contributor

nanxiao
