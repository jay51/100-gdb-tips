#Enter and exit the graphical debugging interface
##example

```
#include <stdio.h>

Void fun1(void)
{
Int i = 0;

i++;
i = i * 2;
Printf("%d\n", i);
}

Void fun2(void)
{
Int j = 0;

Fun1();
j++;
j = j * 2;
Printf("%d\n", j);
}

Int main(void)
{
Fun2();
Return 0;
}
```

##Tips
Specify the "`-tui`" parameter when starting gdb (for example: `gdb -tui program`), or use the "`Crtl+X+A`" key combination in the gdb process to enter the graphical debugging interface. Take the above program as an example:

```
┌──ac────────────────────────────────────────────────────────── ────────────────────────────────────────────┐
│17 j++; │
│18 j = j * 2; │
│19 printf("%d\n", j); │
│20 } │
│21 │
│22 int main(void) │
│23 { │
B+>│24 fun2(); │
│25 return 0; │
│26 } │
│27 │
│28 │
│29 │
│30 │
│31 │
│32 │
└──────────────────────────────────────────────────────────── ──────────────────────────────────────────────────────────┘
Native process 22141 In: main Line: 24 PC: 0x40052b
Type "apropos word" to search for helps related to "word"...
Reading symbols from a...done.
(gdb) start
Temporary breakpoint 1 at 0x40052b: file a.c, line 24.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:24
(gdb)
```

As you can see, the process number of the current program, the line number of the code to be executed, and the value of the `PC` register.

Exiting the graphical debugging interface also uses the "`Crtl+X+A`" key combination.
See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/TUI.html).

##Contributors

Nanxiao
