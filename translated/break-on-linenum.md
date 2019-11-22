#Break the point on the file line number

##example

```
/* a/file.c */
#include <stdio.h>

Void print_a (void)
{
Puts ("a");
}

/* b/file.c */
#include <stdio.h>

Void print_b (void)
{
Puts ("b");
}

/* main.c */
Extern void print_a(void);
Extern void print_b(void);

Int main(void)
{
Print_a();
Print_b();
Return 0;
}
```

##Tips

This is relatively simple, if you want to break a line in the current file, you can directly `b linenum`, for example:
 
```
(gdb) b 7

You can also explicitly specify the file, `b file:linenum` for example:

(gdb) b file.c:6
Breakpoint 1 at 0x40053b: file.c:6. (2 locations)
(gdb) i breakpoints
Num Type Disp Enb Address What
1 breakpoint keep y <MULTIPLE>
1.1 y 0x000000000040053b in print_a at a/file.c:6
1.2 y 0x000000000040054b in print_b at b/file.c:6

As you can see, gdb sets breakpoints for all matching files. You can distinguish the same file name by specifying a (partial) path:

(gdb) b a/file.c:6
```

Note: One of the drawbacks of setting a breakpoint with a line number is that if you change the source program, the previously set breakpoint may not be what you want.

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Specify-Location.html#Specify-Location)

##Contributors

Xmj


