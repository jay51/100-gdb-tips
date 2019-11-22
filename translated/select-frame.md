#Select function stack frame

## example

```
#include <stdio.h>

Int func1(int a) {
Return 2 * a;
}

Int func2(int a) {
Int c = 0;
c = 2 * func1(a);
Return c;
}

Int func3(int a) {
Int c = 0;
c = 2 * func2(a);
Return c;
}

Int main(void) {
Printf("%d\n", func3(10));
Return 0;
}
```

##Tips

When debugging a program with gdb, when the program is paused, you can use the "`frame n`" command to select the function stack frame, where `n` is the number of layers. Take the above program as an example:

```
(gdb) b test.c: 5
Breakpoint 1 at 0x40053d: file test.c, line 5.
(gdb) r
Starting program: /home/nanxiao/test

Breakpoint 1, func1 (a=10) at test.c:5
5 return 2 * a;
(gdb) bt
#0 func1 (a=10) at test.c:5
#1 0x0000000000400560 in func2 (a=10) at test.c:11
#2 0x0000000000400586 in func3 (a=10) at test.c:18
#3 0x000000000040059e in main () at test.c:24
(gdb) frame 2
#2 0x0000000000400586 in func3 (a=10) at test.c:18
18 c = 2 * func2(a);
```

It can be seen that after the program is disconnected, the innermost function frame is the #0` frame. After executing the `frame 2` command, the current stack frame becomes the function frame of `fun3`.

You can also select a function stack frame with the "`frame addr`" command, where `addr` is the stack address. Still take the above program as an example:

```
(gdb) frame 2
#2 0x0000000000400586 in func3 (a=10) at test.c:18
18 c = 2 * func2(a);
(gdb) i frame
Stack level 2, frame at 0x7fffffffe590:
Rip = 0x400586 in func3 (test.c:18); saved rip = 0x40059e
Called by frame at 0x7fffffffe5a0, caller of frame at 0x7fffffffe568
Source language c.
Arglist at 0x7fffffffe580, args: a=10
Locals at 0x7fffffffe580, Previous frame's sp is 0x7fffffffe590
Saved registers:
Rbp at 0x7fffffffe580, rip at 0x7fffffffe588
(gdb) frame 0x7fffffffe568
#1 0x0000000000400560 in func2 (a=10) at test.c:11
11 c = 2 * func1(a);
Use the "`i frame`" command to know that `0x7fffffffe568` is the function stack frame address of `func2`, and use "`frame 0x7fffffffe568`" to switch to the function stack frame of `func2`.
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Selection.html#Selection).

##Contributors

Nanxiao

