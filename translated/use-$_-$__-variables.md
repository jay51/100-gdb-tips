# Use &quot;$ \ _&quot; and &quot;$ __&quot; variables
## Examples
	#include <stdio.h>

	int main(void)
	{
	        int i = 0;
	        char a[100];
	
	        for (i = 0; i < sizeof(a); i++)
	        {
	                a[i] = i;
	        }
	
	        return 0;
	}

## Tips
The &quot;` x` &quot;command will store the last checked memory address value in the&quot; convenience variable &quot;&quot; `$ _`&quot;, and will place the contents of this address in the &quot;convenience variable&quot; &quot;` $ __ `&quot; Take the above program as an example:
	
	(gdb) b a.c:13
	Breakpoint 1 at 0x4004a0: file a.c, line 13.
	(gdb) r
	Starting program: /data2/home/nanxiao/a
	
	Breakpoint 1, main () at a.c:13
	13              return 0;
	(gdb) x/16xb a
	0x7fffffffe4a0: 0x00    0x01    0x02    0x03    0x04    0x05    0x06    0x07
	0x7fffffffe4a8: 0x08    0x09    0x0a    0x0b    0x0c    0x0d    0x0e    0x0f
	(gdb) p $_
	$1 = (int8_t *) 0x7fffffffe4af
	(gdb) p $__
	$2 = 15


You can see that the value of &quot;` $ _` &quot;is` 0x7fffffffe4af`, which is exactly the last memory address checked by the &quot;` x` &quot;command. The &quot;` $ __ `&quot; value is `15`.
Also note that some commands (like &quot;` info line` &quot;and&quot; `info breakpoint`&quot; will provide a default address for &quot;` x` &quot;commands to check, and these commands will also set the value of&quot; `$ _`&quot; To that default address value:

	(gdb) p $_
	$5 = (int8_t *) 0x7fffffffe4af
	(gdb) info breakpoint
	Num     Type           Disp Enb Address            What
	1       breakpoint     keep y   0x00000000004004a0 in main at a.c:13
	        breakpoint already hit 1 time
	(gdb) p $_
	$6 = (void *) 0x4004a0 <main+44>


It can be seen that after using the &quot;` info breakpoint` &quot;command, the value of&quot; `$ _`&quot; becomes `0x4004a0`.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Convenience-Vars.html).

## Contributor

nanxiao
