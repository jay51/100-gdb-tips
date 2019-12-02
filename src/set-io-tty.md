# Specify the input and output devices of the program

## Examples

	#include <stdio.h>
	
	int main(void)
	{
	  int i;
	
	  for (i = 0; i < 100; i++)
	    {
	      printf("i = %d\n", i);
	    }
	
	  return 0;
	}

## Tips

In gdb, the program&#39;s input and output are by default using the same terminal as gdb. You can also specify a separate input and output terminal for the program.

First, open a new terminal and use the following command to get the device file name:

	$ tty
	/dev/pts/2

Then, specify the program&#39;s input and output devices through command-line options:

	$ gdb -tty /dev/pts/2 ./a.out
	(gdb) r

Or, in gdb, use the command to set it up:

	(gdb) tty /dev/pts/2

See [gdb manual] for details (https://sourceware.org/gdb/current/onlinedocs/gdb/Input_002fOutput.html#index-tty)

## Contributor

xmj

