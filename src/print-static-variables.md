# Print the value of a static variable

## Examples

	/* main.c */
	extern void print_var_1(void);
	extern void print_var_2(void);
	
	int main(void)
	{
	  print_var_1();
	  print_var_2();
	  return 0;
	}
	
	/* static-1.c */
	#include <stdio.h>
	
	static int var = 1;
	
	void print_var_1(void)
	{ 
	  printf("var = %d\n", var);
	} 
	
	/* static-2.c */
	#include <stdio.h>
	
	static int var = 2;
	
	void print_var_2(void)
	{ 
	  printf("var = %d\n", var);
	} 

## Tips

In gdb, if you print static variables directly, the result is not necessarily what you want:

	$ gcc -g main.c static-1.c static-2.c
	$ gdb -q ./a.out
	(gdb) start
	(gdb) p var
	$1 = 2

	$ gcc -g main.c static-2.c static-1.c
	$ gdb -q ./a.out
	(gdb) start
	(gdb) p var
	$1 = 1

You can specify the file name (context) explicitly:

	(gdb) p 'static-1.c'::var
	$1 = 1
	(gdb) p 'static-2.c'::var
	$2 = 2

See [gdb manual] for details (https://sourceware.org/gdb/current/onlinedocs/gdb/Variables.html#Variables)

## Contributor

xmj

