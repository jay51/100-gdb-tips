# View signal processing information
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
	        signal(SIGINT, handler);
	        signal(SIGALRM, handler);
	        
	        while (1)
	        {
	                sleep(1);
	        }
	        return 0;
	}

## Tips
When debugging a program with gdb, you can use the &quot;` i signals` &quot;command (or&quot; `i handle`&quot; command, where `i` is the abbreviation of the` info` command) to see how gdb handles signals received by the process:

	(gdb) i signals 
	Signal        Stop      Print   Pass to program Description
	
	SIGHUP        Yes       Yes     Yes             Hangup
	SIGINT        Yes       Yes     No              Interrupt
	SIGQUIT       Yes       Yes     Yes             Quit
	......
	SIGALRM       No        No      Yes             Alarm clock
	......

The first item (`Signal`): Mark each signal.
The second item (`Stop`): indicates whether gdb will suspend the program when the signal being debugged has a corresponding signal.
The third item (`Print`): indicates whether gdb will print related information when the debugged program has a corresponding signal.
The fourth item (`Pass to program`): Whether gdb will send this signal to the program being debugged.
The fifth item (`Description`): description information of the signal.

From the output above, you can see that when the `SIGINT` signal occurs, gdb will suspend the program being debugged and print relevant information, but it will not send this signal to the program being debugged. When the `SIGALRM` signal occurs, gdb will not suspend the program being debugged, nor print related information, but will send this signal to the program being debugged.

Start gdb to debug the above program, and start another terminal at the same time, and send `SIGINT` and` SIGALRM` signals to the process being debugged. The output is as follows:

	Program received signal SIGINT, Interrupt.
	0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
	(gdb) c
	Continuing.
	Receive signal: 14

It can be seen that when the `SIGINT` is received, the program is suspended and the signal information is also output, but the` SIGINT` signal is not passed to the process for processing (the program does not output). When receiving the `SIGALRM` signal, the program did not pause and did not output signal information, but the` SIGALRM` signal was passed to the process for processing (the program printed the output).


See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Signals.html).

## Contributor

nanxiao
