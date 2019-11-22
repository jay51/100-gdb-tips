#Map source and assembly instructions

##example

```
#include <stdio.h>

Typedef struct
{
Int a;
Int b;
Int c;
Int d;
}ex_st;

Int main(void) {
Ex_st st = {1, 2, 3, 4};
Printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
Return 0;
}
```

## Tip 1

You can use the "disas /m fun" (disas is disassemble command abbreviation) command to map function code and assembly instructions, using the above code as an example:

```
(gdb) disas /m main
Dump of assembler code for function main:
11 int main(void) {
0x00000000004004c4 <+0>: push %rbp
0x00000000004004c5 <+1>: mov %rsp, %rbp
0x00000000004004c8 <+4>: push %rbx
0x00000000004004c9 <+5>: sub $0x18, %rsp

12 ex_st st = {1, 2, 3, 4};
0x00000000004004cd <+9>: movl $0x1, -0x20 (%rbp)
0x00000000004004d4 <+16>: movl $0x2, -0x1c (%rbp)
0x00000000004004db <+23>: movl $0x3, -0x18 (%rbp)
0x00000000004004e2 <+30>: movl $0x4, -0x14 (%rbp)

13 printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
0x00000000004004e9 <+37>: mov -0x14(%rbp), %esi
0x00000000004004ec <+40>: mov -0x18(%rbp), %ecx
0x00000000004004ef <+43>: mov -0x1c(%rbp), %edx
0x00000000004004f2 <+46>: mov -0x20(%rbp), %ebx
0x00000000004004f5 <+49>: mov $0x400618, %eax
0x00000000004004fa <+54>: mov %esi, %r8d
0x00000000004004fd <+57>: mov %ebx, %esi
0x00000000004004ff <+59>: mov %rax, %rdi
0x0000000000400502 <+62>: mov $0x0, %eax
0x0000000000400507 <+67>: callq 0x4003b8 <printf@plt>

14 return 0;
0x000000000040050c <+72>: mov $0x0, %eax

15 }
0x0000000000400511 <+77>: add $0x18, %rsp
0x0000000000400515 <+81>: pop %rbx
0x0000000000400516 <+82>: leaveq
0x0000000000400517 <+83>: retq
```

End of assembler dump.

You can see that each C statement is the corresponding assembly code.

## Tip 2

If you only want to see the address range corresponding to a row, you can:

```
(gdb) i line 13
Line 13 of "foo.c" starts at address 0x4004e9 <main+37> and ends at 0x40050c <main+72>.
```


If you only want to see the assembly code for this statement, you can use the "`disassemble [Start], [End]`" command:

```
(gdb) disassemble 0x4004e9, 0x40050c
Dump of assembler code from 0x4004e9 to 0x40050c:
0x00000000004004e9 <main+37>: mov -0x14(%rbp), %esi
0x00000000004004ec <main+40>: mov -0x18(%rbp), %ecx
0x00000000004004ef <main+43>: mov -0x1c(%rbp), %edx
0x00000000004004f2 <main+46>: mov -0x20(%rbp), %ebx
0x00000000004004f5 <main+49>: mov $0x400618, %eax
0x00000000004004fa <main+54>: mov %esi, %r8d
0x00000000004004fd <main+57>: mov %ebx, %esi
0x00000000004004ff <main+59>: mov %rax, %rdi
0x0000000000400502 <main+62>: mov $0x0, %eax
0x0000000000400507 <main+67>: callq 0x4003b8 <printf@plt>
End of assembler dump.
```

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Machine-Code.html)

## Contributors

Nanxiao

Xmj


