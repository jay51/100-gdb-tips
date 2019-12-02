# Debug child process

## Examples

	#include <stdio.h>
	#include <sys/types.h>
	#include <unistd.h>
	
	int main(void) {
		pid_t pid;
	
		pid = fork();
		if (pid < 0)
		{
			exit(1);
		}
		else if (pid > 0)
		{
			exit(0);
		}
		printf("hello world\n");
		return 0;
	}


## Tips

When debugging multi-process programs, gdb tracks the parent process by default. E.g:

	(gdb) start
	Temporary breakpoint 1 at 0x40055c: file a.c, line 8.
	Starting program: /data2/home/nanxiao/a
	
	Temporary breakpoint 1, main () at a.c:8
	8               pid = fork();
	(gdb) n
	9               if (pid < 0)
	(gdb) hello world
	
	13              else if (pid > 0)
	(gdb)
	15                      exit(0);
	(gdb)
	[Inferior 1 (process 12786) exited normally]


	


You can see that the program executes to line 15: the parent process exits.

To debug a child process, use the following command: &quot;set follow-fork-mode child&quot;, for example:

	(gdb) set follow-fork-mode child
	(gdb) start
	Temporary breakpoint 1 at 0x40055c: file a.c, line 8.
	Starting program: /data2/home/nanxiao/a
	
	Temporary breakpoint 1, main () at a.c:8
	8               pid = fork();
	(gdb) n
	[New process 12241]
	[Switching to process 12241]
	9               if (pid < 0)
	(gdb)
	13              else if (pid > 0)
	(gdb)
	17              printf("hello world\n");
	(gdb)
	hello world
	18              return 0;


You can see that the program executes to line 17: the child process prints &quot;hello world&quot;.

This command is currently supported by Linux and not supported by many other operating systems. Please pay attention when using it. See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Forks.html)

## Contributor

nanxiao



