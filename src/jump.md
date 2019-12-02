# Jump to the specified location for execution

## Examples

	#include <stdio.h>
	
	void fun (int x)
	{
	  if (x < 0)
	    puts ("error");
	}
	
	int main (void)
	{
	  int i = 1;
	
	  fun (i--);
	  fun (i--);
	  fun (i--);
	
	  return 0;
	}

## Tips

When debugging a program, you may accidentally walk over the wrong place:

	(gdb) n
	13	  fun (i--);
	(gdb) 
	14	  fun (i--);
	(gdb) 
	15	  fun (i--);
	(gdb) 
	error
	17	  return 0;

It looks like it&#39;s on line 15, and something went wrong when calling fun. A common approach is to set a breakpoint on line 15 and then run it from scratch.

Even better if your environment supports reverse execution.

If it is not supported, you can also `jump` to line 15 and execute it again:

	(gdb) b 15
	Breakpoint 2 at 0x40056a: file jump.c, line 15.
	(gdb) j 15
	Continuing at 0x40056a.
	
	Breakpoint 2, main () at jump.c:15
	15	  fun (i--);
	(gdb) s
	fun (x=-2) at jump.c:5
	5	  if (x < 0)
	(gdb) n
	6	    puts ("error");

have to be aware of is:

1. The `jump` command only changes the value of the pc, so changing the program execution may have different results, such as the value of the variable i
2. With the cooperation of (temporary) breakpoints, you can make your program jump to a specified position and stop

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Jumping.html#Jumping)

## Contributor

xmj

