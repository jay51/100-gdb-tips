# Use &quot;$ _siginfo&quot; variable
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
On some platforms (such as Linux), use gdb to debug the program. When a signal occurs, gdb can read some additional information about the current signal through the `$ _siginfo` variable before throwing the signal to the program. The information is `kernel` is passed to the signal handler. Take the above program as an example:

	Program received signal SIGHUP, Hangup.
	0x00000034e42accc0 in __nanosleep_nocancel () from /lib64/libc.so.6
	Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.132.el6.x86_64
	(gdb) ptype $_siginfo
	type = struct {
	    int si_signo;
	    int si_errno;
	    int si_code;
	    union {
	        int _pad[28];
	        struct {...} _kill;
	        struct {...} _timer;
	        struct {...} _rt;
	        struct {...} _sigchld;
	        struct {...} _sigfault;
	        struct {...} _sigpoll;
	    } _sifields;
	}
	(gdb) ptype $_siginfo._sifields._sigfault
	type = struct {
	    void *si_addr;
	}
	(gdb) p $_siginfo._sifields._sigfault.si_addr
	$1 = (void *) 0x850e

We can understand the type of each member in the `$ _siginfo` variable, and we can read the value of the member.


See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Signaling.html#Signaling).

## Contributor

nanxiao
