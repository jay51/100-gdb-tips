# Support preprocessor macro information

## Examples

	#include <stdio.h>
	
	#define NAME "Joe"
	
	int main()
	{
	  printf ("Hello %s\n", NAME);
	  return 0;
	}

## Tips

The program compiled with `gcc -g` does not contain preprocessor macro information:

	(gdb) p NAME
	No symbol "NAME" in current context.

If you want to view the macro information in gdb, you can use `gcc -g3` to compile:

	(gdb) p NAME
	$1 = "Joe"

For preprocessor macro commands, see [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Macros.html#Macros)

## Contributor

xmj

