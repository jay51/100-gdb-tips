#Print the value of the variable in the call stack frame

##example

```
#include <stdio.h>

Int func1(int a)
{
Int b = 1;
Return b * a;
}

Int func2(int a)
{
Int b = 2;
Return b * func1(a);
}

Int func3(int a)
{
Int b = 3;
Return b * func2(a);
}

Int main(void)
{
Printf("%d\n", func3(10));
Return 0;
}
```

## Tips

In gdb, if you want to see the variables in the call stack frame, you can switch to the stack frame first, then print:

```
(gdb) b func1
(gdb) r
(gdb) bt
#0 func1 (a=10) at frame.c:5
#1 0x0000000000400560 in func2 (a=10) at frame.c:12
#2 0x0000000000400582 in func3 (a=10) at frame.c:18
#3 0x0000000000400596 in main () at frame.c:23
(gdb) f 1
(gdb) p b
(gdb) f 2
(gdb) p b

You can also print directly without switching:

(gdb) p func2::b
$1 = 2
(gdb) p func3::b
$2 = 3

Similarly, for C++ function names, you need to use single quotes, such as:

(gdb) p '(anonymous namespace)::SSAA::handleStore'::n->pi->inst->dump()
```

See the [gdb manual](https://sourceware.org/gdb/current/onlinedocs/gdb/Variables.html#Variables) for details

##Contributors

Xmj


