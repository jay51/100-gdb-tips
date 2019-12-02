# Print tail call stack frame information
## Examples
	#include<stdio.h>
	void a(void)
	{
	        printf("Tail call frame\n");
	}
	
	void b(void)
	{
	        a();
	}
	
	void c(void)
	{
	        b();
	}
	
	int main(void)
	{
	        c();
	        return 0;
	}

## Tips
When the last instruction of a function is to call another function, the compiler that turns on the optimization option often uses the return value of the last called function as the return value of the caller, which is called &quot;Tail call&quot;. Take the above program as an example, compile the program (using &#39;-O&#39;):

    gcc -g -O -o test test.c
View the `main` function assembly code:

	(gdb) disassemble main
    Dump of assembler code for function main:
    0x0000000000400565 <+0>:     sub    $0x8,%rsp
    0x0000000000400569 <+4>:     callq  0x400536 <a>
    0x000000000040056e <+9>:     mov    $0x0,%eax
    0x0000000000400573 <+14>:    add    $0x8,%rsp
    0x0000000000400577 <+18>:    retq
You can see that the `main` function directly calls the function` a`, and the shadow of the function `b` and the function` c` cannot be seen at all.
  
Put a breakpoint at the entrance of the function `a`. After the program stops, print the stack frame information:

	(gdb) i frame
	Stack level 0, frame at 0x7fffffffe590:
	 rip = 0x400536 in a (test.c:4); saved rip = 0x40056e
	 called by frame at 0x7fffffffe5a0
	 source language c.
	 Arglist at 0x7fffffffe580, args:
	 Locals at 0x7fffffffe580, Previous frame's sp is 0x7fffffffe590
	 Saved registers:
	  rip at 0x7fffffffe588
I don&#39;t see information about the tail call.

You can set the `debug entry-values` option to a non-zero value, so that in addition to outputting normal function stack frame information, you can also output information about the tail call:

	(gdb) set debug entry-values 1
	(gdb) b test.c:4
	Breakpoint 1 at 0x400536: file test.c, line 4.
	(gdb) r
	Starting program: /home/nanxiao/test
	
	Breakpoint 1, a () at test.c:4
	4       {
	(gdb) i frame
	tailcall: initial:
	Stack level 0, frame at 0x7fffffffe590:
	 rip = 0x400536 in a (test.c:4); saved rip = 0x40056e
	 called by frame at 0x7fffffffe5a0
	 source language c.
	 Arglist at 0x7fffffffe580, args:
	 Locals at 0x7fffffffe580, Previous frame's sp is 0x7fffffffe590
	 Saved registers:
	  rip at 0x7fffffffe588

You can see that &quot;` tailcall: initial: `&quot; is output.

See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Tail-Call-Frames.html).

## Contributor

nanxiao
