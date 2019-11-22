#Exit the function being debugged

##example

```
#include <stdio.h>

Int func(void) {
Int i = 0;

i += 2;
i *= 10;

Return i;
}

Int main(void) {
Int a = 0;

a = func();
Printf("%d\n", a);
Return 0;
}
```

##Tips

When you step through a function, if you don't want to continue tracking, you can exit in two ways.

The first uses the "`finish`" command, so the function continues execution and prints the return value, then waits for the next command. Take the above code as an example:

```
(gdb) n
17 a = func();
(gdb) s
Func () at a.c:5
5 int i = 0;
(gdb) n
7 i += 2;
(gdb) fin
Find finish
(gdb) finish
Run till exit from #0 func () at a.c:7
0x08050978 in main () at a.c:17
17 a = func();
Value returned is $1 = 20
```

You can see that when you don't want to continue to track the `func` function, after executing the "`finish`" command, gdb will print the result: "`20`" and then stop there.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Continuing-and-Stepping.html)for details 

The second use the "`return`" command, so the function will not continue to execute the following statement, but return directly. You can also specify the return value of a function with the "`return expression`" command. Still take the above code as an example:

```
(gdb) n
17 a = func();
(gdb) s
Func () at a.c:5
5 int i = 0;
(gdb) n
7 i += 2;
(gdb) n
8 i *= 10;
(gdb) re
Record remove-inferiors return reverse-next reverse-step
Refresh remove-symbol-file reverse-continue reverse-nexti reverse-stepi
Remote restore reverse-finish reverse-search
(gdb) return 40
Make func return now? (y or n) y
#0 0x08050978 in main () at a.c:17
17 a = func();
(gdb) n
18 printf("%d\n", a);
(gdb)
40
19 return 0;
```

You can see that the "`return`" command exited the function and modified the return value of the function.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Returning.html#Returning)for details 

##Contributors

Nanxiao

