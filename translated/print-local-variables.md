#Print the value of a function local variable

##example

```
#include <stdio.h>

Void fun_a(void) {
Int a = 0;
Printf("%d\n", a);
}

Void fun_b(void) {
Int b = 1;
Fun_a();
Printf("%d\n", b);
}

Void fun_c(void) {
Int c = 2;
Fun_b();
Printf("%d\n", c);
}

Void fun_d(void) {
Int d = 3;
Fun_c();
Printf("%d\n", d);
}

Int main(void) {
Int var = -1;
Fun_d();
Return 0;
}
```

##Tip 1

If you want to print the value of a function local variable, you can use the "bt full" command (bt is an abbreviation for backtrace). First we put a breakpoint in the function fun_a, when the program is interrupted, the call stack information is displayed:

```
(gdb) bt
#0 fun_a () at a.c:6
#1 0x000109b0 in fun_b () at a.c:12
#2 0x000109e4 in fun_c () at a.c:19
#3 0x00010a18 in fun_d () at a.c:26
#4 0x00010a4c in main () at a.c:33
```

Next, use the "bt full" command to display the local variable values ​​for each function:

```
(gdb) bt full
#0 fun_a () at a.c:6
a = 0
#1 0x000109b0 in fun_b () at a.c:12
b = 1
#2 0x000109e4 in fun_c () at a.c:19
c = 2
#3 0x00010a18 in fun_d () at a.c:26
d = 3
#4 0x00010a4c in main () at a.c:33
Var = -1
```

You can also use the following "bt full n", which means that n stacks are displayed from the inside out, and their local variables, for example:

```
(gdb) bt full 2
#0 fun_a () at a.c:6
a = 0
#1 0x000109b0 in fun_b () at a.c:12
b = 1
(More stack frames follow...)
```

And "bt full -n" means to display n stacks from the outside to the inside, and their local variables, for example:

```
(gdb) bt full -2
#3 0x00010a18 in fun_d () at a.c:26
d = 3
#4 0x00010a4c in main () at a.c:33
Var = -1
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Backtrace.html)for details 

##Tip 2

If you just want to print the value of the current function local variable, you can use the following command:

```
(gdb) info locals
a = 0
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Frame-Info.html#index-info-locals)for details 

##Contributors

Nanxiao
Xmj
