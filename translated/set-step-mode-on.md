# Enter function without debugging information

## Examples

	#include <stdio.h>
	#include <pthread.h>
	
	typedef struct
	{
	        int a;
	        int b;
	        int c;
	        int d;
	        pthread_mutex_t mutex;
	}ex_st;
	
	int main(void) {
	        ex_st st = {1, 2, 3, 4, PTHREAD_MUTEX_INITIALIZER};
	        printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
	        return 0;
	}



## Tips

By default, gdb will not enter functions without debugging information. Take the above code as an example:

	(gdb) n
	15              printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
	(gdb) s
	1,2,3,4
	16              return 0;

	
It can be seen that because the printf function does not carry debugging information, the &quot;s&quot; command (s is the abbreviation of &quot;step&quot;) cannot enter the printf function.

You can execute the &quot;set step-mode on&quot; command so that gdb does not skip functions without debugging information:

	(gdb) set step-mode on
	(gdb) n
	15              printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
	(gdb) s
	0x00007ffff7a993b0 in printf () from /lib64/libc.so.6
	(gdb) s
	0x00007ffff7a993b7 in printf () from /lib64/libc.so.6


You can see that gdb has entered the printf function. Next, you can use the method of debugging the assembler to debug the function.

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Continuing-and-Stepping.html)

## Contributor

nanxiao



