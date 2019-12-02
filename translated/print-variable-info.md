# Print the type and file of the variable

## Examples

	#include <stdio.h>
	
	struct child {
	  char name[10];
	  enum { boy, girl } gender;
	};
	
	struct child he = { "Tom", boy };
	
	int main (void)
	{
	  static struct child she = { "Jerry", girl };
	  printf ("Hello %s %s.\n", he.gender == boy ? "boy" : "girl", he.name);
	  printf ("Hello %s %s.\n", she.gender == boy ? "boy" : "girl", she.name);
	  return 0;
	}

## Tips

In gdb, you can use the following command to view the type of the variable:

	(gdb) whatis he
	type = struct child

If you want to see detailed type information:

	(gdb) ptype he
	type = struct child {
	    char name[10];
	    enum {boy, girl} gender;
	}

If you want to see the file that defines the variable:

	(gdb) i variables he
	All variables matching regular expression "he":
	
	File variable.c:
	struct child he;
	
	Non-debugging symbols:
	0x0000000000402030  she
	0x00007ffff7dd3380  __check_rhosts_file

Oh, gdb will show all variables that contain (match) the expression. If you only want to see variables that exactly match the given name:

	(gdb) i variables ^he$
	All variables matching regular expression "^he$":
	
	File variable.c:
	struct child he;

Note: `info variables` does not display local variables, even static ones do not have much information.

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Symbols.html)

## Contributor

xmj

