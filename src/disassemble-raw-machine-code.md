#Show program original machine code

##example

```
#include <stdio.h>

Int main(void)
{
Printf("Hello, world\n");
Return 0;
}
```

## Tips

Use the "disassemble /r" command to display the original machine code of the program in hexadecimal format. Take the above program as an example:

```
(gdb) disassemble /r main
Dump of assembler code for function main:
0x0000000000400530 <+0>: 55 push %rbp
0x0000000000400531 <+1>: 48 89 e5 mov %rsp, %rbp
0x0000000000400534 <+4>: bf e0 05 40 00 mov $0x4005e0, %edi
0x0000000000400539 <+9>: e8 d2 fe ff ff callq 0x400410 <puts@plt>
0x000000000040053e <+14>: b8 00 00 00 00 mov $0x0, %eax
0x0000000000400543 <+19>: 5d pop %rbp
0x0000000000400544 <+20>: c3 retq
End of assembler dump.
(gdb) disassemble /r 0x0000000000400534, +4
Dump of assembler code from 0x400534 to 0x400538:
0x0000000000400534 <main+4>: bf e0 05 40 00 mov $0x4005e0, %edi
End of assembler dump.
```

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Machine-Code.html) for details

##Contributors

Nanxiao

