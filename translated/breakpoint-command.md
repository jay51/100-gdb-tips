#Use the breakpoint command to change the execution of the program

##example

```
#include <stdio.h>
#include <stdlib.h>

Void drawing (int n) {
If (n != 0)
Puts ("Try again?\nAll you need is a dollar, and a dream.");
Else
Puts ("You win $3000!");
}

Int main (void) {
Int n;

Srand (time (0));
n = rand () % 10;
Printf ("Your number is %d\n", n);
Drawing (n);

Return 0;
}
```

##Tips

This example program may not be very good, just to demonstrate the use of breakpoint commands:

```
(gdb) b drawing
Breakpoint 1 at 0x40064d: file win.c, line 6.
(gdb) command 1
Type commands for breakpoint(s) 1, one per line.
End with a line saying just "end".
>silent
>set variable n = 0
>continue
>end
(gdb) r
Starting program: /home/xmj/tmp/a.out
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Your number is 6
You win $3000!
[Inferior 1 (process 4134) exited normally]
```

It can be seen that when the program runs to the breakpoint, the value of the variable n is automatically changed to 0 and then continues.

If you are debugging a large program, it will take a long time to recompile it, such as debugging the compiler bug, then you can try this in the gdb first experimental modification without modifying the source code. Compile.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Break-Commands.html#Break-Commands)for details 

##Contributors

Xmj
