#Display assembly code window

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
When using gdb to graphically debug the interface, you can use the "`layout asm`" command to display the assembly code window. Take the above program as an example:

```
┌──────────────────────────────────────────────────────────── ──────────────────────────────────────────────────────────┐
>│0x40052b <main+4> callq 0x4004f3 <fun2> │
│0x400530 <main+9> mov $0x0,%eax │
│0x400535 <main+14> leaveq │
│0x400536 <main+15> retq │
│0x400537 nop │
│0x400538 nop │
│0x400539 nop │
│0x40053a nop │
│0x40053b nop │
│0x40053c nop │
│0x40053d nop │
│0x40053e nop │
│0x40053f nop │
│0x400540 <__libc_csu_fini> repz retq │
│0x400542 data16 data16 data16 data16 nopw %cs:0x0(%rax,%rax,1) │
│0x400550 <__libc_csu_init> mov %rbp, -0x28(%rsp) │
└──────────────────────────────────────────────────────────── ──────────────────────────────────────────────────────────┘
Native process 44658 In: main Line: 24 PC: 0x40052b

(gdb) start
Temporary breakpoint 1 at 0x40052b: file a.c, line 24.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:24
(gdb)
```

As you can see, the assembly code for the current program is displayed.
If you want to display both the source code and the assembly code, you can use the "`layout split`" command:

```
┌──ac────────────────────────────────────────────────────────── ────────────────────────────────────────────┐
>│24 fun2(); │
│25 return 0; │
│26 } │
│27 │
│28 │
│29 │
│30 │
└──────────────────────────────────────────────────────────── ──────────────────────────────────────────────────────────┘
>│0x40052b <main+4> callq 0x4004f3 <fun2> │
│0x400530 <main+9> mov $0x0,%eax │
│0x400535 <main+14> leaveq │
│0x400536 <main+15> retq │
│0x400537 nop │
│0x400538 nop │
│0x400539 nop │
│0x40053a nop │
└──────────────────────────────────────────────────────────── ──────────────────────────────────────────────────────────┘
Native process 44658 In: main Line: 24 PC: 0x40052b

(gdb) start
Temporary breakpoint 1 at 0x40052b: file a.c, line 24.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:24
(gdb)
```

You can see that the source code is shown above, and the assembly code is shown below.
See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/TUI-Commands.html).

##Contributors

Nanxiao

