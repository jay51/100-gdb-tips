#Set the value of the variable

##example

```
#include <stdio.h>

Int func(void)
{
Int i = 2;

Return i;
}

Int main(void)
{
Int a = 0;

a = func();
Printf("%d\n", a);
Return 0;
}
```

##Tips

In gdb, you can use the "`set var variable=expr`" command to set the value of the variable, taking the above code as an example:


```
Breakpoint 2, func () at a.c:5
5 int i = 2;
(gdb) n
7 return i;
(gdb) set var i = 8
(gdb) p i
$4 = 8
```

You can see that the value of `i` is changed to `8` with the `set` command in the `func` function.

You can also use the "`set {type}address=expr`" method, meaning to assign a value to a variable with a storage address of `address` and a variable type of `type`. Still use the above code as an example:

```
Breakpoint 2, func () at a.c:5
5 int i = 2;
(gdb) n
7 return i;
(gdb) p &i
$5 = (int *) 0x8047a54
(gdb) set {int}0x8047a54 = 8
(gdb) p i
$6 = 8
```

You can see that the value of `i` has been modified to `8`.

In addition, the register can also be used as a variable, so you can also modify the value of the register:

```
Breakpoint 2, func () at a.c:5
5 int i = 2;
(gdb)
(gdb) n
7 return i;
(gdb)
8               }
(gdb) set var $eax = 8
(gdb) n
Main () at a.c:15
15 printf("%d\n", a);
(gdb)
8
16 return 0;
```

It can be seen that since the eax register stores the return value of the function, when the value of the eax register is changed to `8`, the return value of the function also becomes `8`.

See the [gdb manual](https://sourceware.org/gdb/current/onlinedocs/gdb/Assignment.html#Assignment) for details

## Contributors

Nanxiao
