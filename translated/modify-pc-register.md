#Modify the value of the PC register

##example

```
#include <stdio.h>
Int main(void)
{
Int a =0;

a++;
a++;
Printf("%d\n", a);
Return 0;
}
```

## Tips
The PC register stores the next instruction to be executed by the program. By modifying the value of this register, the purpose of changing the execution flow of the program can be achieved.
The above program will output "`a=2`". Here's how to change the program execution flow by modifying the value of the PC register.

```
4 int a =0;
(gdb) disassemble main
Dump of assembler code for function main:
0x08050921 <main+0>: push %ebp
0x08050922 <main+1>: mov %esp, %ebp
0x08050924 <main+3>: sub $0x8, %esp
0x08050927 <main+6>: and $0xfffffff0, %esp
0x0805092a <main+9>: mov $0x0, %eax
0x0805092f <main+14>: add $0xf, %eax
0x08050932 <main+17>: add $0xf, %eax
0x08050935 <main+20>: shr $0x4, %eax
0x08050938 <main+23>: shl $0x4, %eax
0x0805093b <main+26>: sub %eax, %esp
0x0805093d <main+28>: movl $0x0, -0x4 (%ebp)
0x08050944 <main+35>: lea -0x4(%ebp), %eax
0x08050947 <main+38>: incl (%eax)
0x08050949 <main+40>: lea -0x4(%ebp), %eax
0x0805094c <main+43>: incl (%eax)
0x0805094e <main+45>: sub $0x8, %esp
0x08050951 <main+48>: pushl -0x4(%ebp)
0x08050954 <main+51>: push $0x80509b4
0x08050959 <main+56>: call 0x80507cc <printf@plt>
0x0805095e <main+61>: add $0x10, %esp
0x08050961 <main+64>: mov $0x0, %eax
0x08050966 <main+69>: leave
0x08050967 <main+70>: ret
End of assembler dump.
(gdb) info line 6
Line 6 of "a.c" starts at address 0x8050944 <main+35> and ends at 0x8050949 <main+40>.
(gdb) info line 7
Line 7 of "a.c" starts at address 0x8050949 <main+40> and ends at 0x805094e <main+45>.

The "`info line 6`" and "`info line 7`" commands can be used to know that the assembly start addresses of the two "a++;`" statements are `0x8050944` and `0x8050949`, respectively.

(gdb) n
6 a++;
(gdb) p $pc
$3 = (void (*)()) 0x8050944 <main+35>
(gdb) set var $pc=0x08050949
```

When the program wants to execute the first "`a++;`" statement, print the value of the `pc` register and see that the value of the `pc` register is `0x8050944`, which is consistent with the "`info line 6`" command. Next, change the value of the `pc` register to `0x8050949`, which is the starting address of the second "a++;`" statement obtained by the "`info line 7`" command.


```
(gdb) n
8 printf("a=%d\n", a);
(gdb)
a=1
9 return 0;
```

Next, you can see that the program output "`a=1`", that is, skip the first "`a++;`" statement.
##Contributors

Nanxiao
