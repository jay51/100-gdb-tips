# Set catchpoint for exec calls
## Examples
	#include <unistd.h>
	
	int main(void) {
	    execl("/bin/ls", "ls", NULL);
	    return 0;
	}



## Tips
When using gdb to debug a program, you can use the `catch exec` command to set a catchpoint for the exec series of system calls. Take the above program as an example:

	(gdb) catch exec
	Catchpoint 1 (exec)
	(gdb) r
	Starting program: /home/nan/a
	process 32927 is executing new program: /bin/ls
	
	Catchpoint 1 (exec'd /bin/ls), 0x00000034e3a00b00 in _start () from /lib64/ld-linux-x86-64.so.2
	(gdb) bt
	#0  0x00000034e3a00b00 in _start () from /lib64/ld-linux-x86-64.so.2
	#1  0x0000000000000001 in ?? ()
	#2  0x00007fffffffe73d in ?? ()
	#3  0x0000000000000000 in ?? ()


You can see that when the `execl` call occurs, gdb will suspend the running of the program.
Note: Currently only HP-UX and GNU / Linux support this feature.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Catchpoints.html).

## Contributor

nanxiao
