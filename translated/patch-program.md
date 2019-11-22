#Modify the binary of the debugged program

##example

```
#include <stdio.h>
#include <stdlib.h>

Void drawing (int n)
{
If (n != 0)
Puts ("Try again?\nAll you need is a dollar, and a dream.");
Else
Puts ("You win $3000!");
}

Int main (void)
{
Int n;

Srand (time (0));
n = rand () % 10;
Printf ("Your number is %d\n", n);
Drawing (n);

Return 0;
}
```

## Tips

Gdb can be used not only to debug programs, but also to modify the program's binary code.

By default, gdb loads programs programmatically. Can be specified as writable by command line options:

```
$ gcc -write ./a.out
(gdb) show write
Writing into executable and core files is on.
```

You can also use the command to set and reload the program in gdb:

```
(gdb) set write on
(gdb) file ./a.out
```

Next, look at the disassembly:

```
(gdb) disassemble /mr drawing
Dump of assembler code for function drawing:
5 {
0x0000000000400642 <+0>: 55 push %rbp
0x0000000000400643 <+1>: 48 89 e5 mov %rsp, %rbp
0x0000000000400646 <+4>: 48 83 ec 10 sub $0x10, %rsp
0x000000000040064a <+8>: 89 7d fc mov %edi, -0x4 (%rbp)

6 if (n != 0)
0x000000000040064d <+11>: 83 7d fc 00 cmpl $0x0, -0x4 (%rbp)
0x0000000000400651 <+15>: 74 0c je 0x40065f <drawing+29>

7 puts ("Try again?\nAll you need is a dollar, and a dream.");
0x0000000000400653 <+17>: bf e0 07 40 00 mov $0x4007e0, %edi
0x0000000000400658 <+22>: e8 b3 fe ff ff callq 0x400510 <puts@plt>
0x000000000040065d <+27>: eb 0a jmp 0x400669 <drawing+39>

8 else
9 puts ("You win $3000!");
0x000000000040065f <+29>: bf 12 08 40 00 mov $0x400812,%edi
0x0000000000400664 <+34>: e8 a7 fe ff ff callq 0x400510 <puts@plt>

10 }
0x0000000000400669 <+39>: c9 leaveq
0x000000000040066a <+40>: c3 retq

End of assembler dump.

Modify the binary code (note the size and length of the instruction):

(gdb) set variable *(short*)0x400651=0x0ceb
(gdb) disassemble /mr drawing
Dump of assembler code for function drawing:
5 {
0x0000000000400642 <+0>: 55 push %rbp
0x0000000000400643 <+1>: 48 89 e5 mov %rsp, %rbp
0x0000000000400646 <+4>: 48 83 ec 10 sub $0x10, %rsp
0x000000000040064a <+8>: 89 7d fc mov %edi, -0x4 (%rbp)

6 if (n != 0)
0x000000000040064d <+11>: 83 7d fc 00 cmpl $0x0, -0x4 (%rbp)
0x0000000000400651 <+15>: eb 0c jmp 0x40065f <drawing+29>

7 puts ("Try again?\nAll you need is a dollar, and a dream.");
0x0000000000400653 <+17>: bf e0 07 40 00 mov $0x4007e0, %edi
0x0000000000400658 <+22>: e8 b3 fe ff ff callq 0x400510 <puts@plt>
0x000000000040065d <+27>: eb 0a jmp 0x400669 <drawing+39>

8 else
9 puts ("You win $3000!");
0x000000000040065f <+29>: bf 12 08 40 00 mov $0x400812,%edi
0x0000000000400664 <+34>: e8 a7 fe ff ff callq 0x400510 <puts@plt>

10 }
0x0000000000400669 <+39>: c9 leaveq
0x000000000040066a <+40>: c3 retq

End of assembler dump.
```

It can be seen that the conditional jump instruction "je" has been changed to the unconditional jump "jmp".

Exit, run it:

$ ./a.out
Your number is 2
You win $3000!

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Patching.html#Patching)for details

## Contributors

Xmj


