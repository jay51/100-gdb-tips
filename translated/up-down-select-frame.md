# Switch function stack frame up or down
## Examples
	#include <stdio.h>

	int func1(int a)
	{
	        return 2 * a;
	}
	
	int func2(int a)
	{
	        int c = 0;
	        c = 2 * func1(a);
	        return c;
	}
	
	int func3(int a)
	{
	        int c = 0;
	        c = 2 * func2(a);
	        return c;
	}
	
	int main(void)
	{
	        printf("%d\n", func3(10));
	        return 0;
	}

## Tips
When debugging a program with gdb, when the program is paused, you can use the &quot;` up n` &quot;or&quot; `down n`&quot; command to select the function stack frame up or down, where `n` is the number of layers. Take the above program as an example:

    (gdb) b test.c:5
	Breakpoint 1 at 0x40053d: file test.c, line 5.
	(gdb) r
	Starting program: /home/nanxiao/test
	
	Breakpoint 1, func1 (a=10) at test.c:5
	5               return 2 * a;
	(gdb) bt
	#0  func1 (a=10) at test.c:5
	#1  0x0000000000400560 in func2 (a=10) at test.c:11
	#2  0x0000000000400586 in func3 (a=10) at test.c:18
	#3  0x000000000040059e in main () at test.c:24
	(gdb) frame 2
	#2  0x0000000000400586 in func3 (a=10) at test.c:18
	18              c = 2 * func2(a);
	(gdb) up 1
	#3  0x000000000040059e in main () at test.c:24
	24              printf("%d\n", func3(10));
	(gdb) down 2
	#1  0x0000000000400560 in func2 (a=10) at test.c:11
	11              c = 2 * func1(a);


You can see that after the program is interrupted, first execute the &quot;` frame 2` &quot;command and switch to the` fun3` function. Then execute the &quot;` up 1` &quot;command, and then switch to the` main` function, that is, move one layer to the outer stack frame. Conversely, when the &quot;down 2&quot; command is executed, it will move to the inner stack frame by two layers. If `n` is not specified,` n` defaults to `1`.

There are also two commands `up-silently n` and` down-silently n`. They differ from the commands `up n` and` down n` in that they do not print after switching stack frames. Information, still using the above program as an example:

    (gdb) up
	#2  0x0000000000400586 in func3 (a=10) at test.c:18
	18              c = 2 * func2(a);
	(gdb) bt
	#0  func1 (a=10) at test.c:5
	#1  0x0000000000400560 in func2 (a=10) at test.c:11
	#2  0x0000000000400586 in func3 (a=10) at test.c:18
	#3  0x000000000040059e in main () at test.c:24
	(gdb) up-silently
	(gdb) i frame
	Stack level 3, frame at 0x7fffffffe5a0:
	 rip = 0x40059e in main (test.c:24); saved rip = 0x7ffff7a35ec5
	 caller of frame at 0x7fffffffe590
	 source language c.
	 Arglist at 0x7fffffffe590, args:
	 Locals at 0x7fffffffe590, Previous frame's sp is 0x7fffffffe5a0
	 Saved registers:
	  rbp at 0x7fffffffe590, rip at 0x7fffffffe598

It can be seen that when switching from `func3` to` main` function stack frame, no relevant information is printed.

See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Selection.html#Selection).

## Contributor

nanxiao
