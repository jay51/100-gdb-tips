#Breakpoint in the first assembly instruction of the function

##example

```
#include <stdio.h>
Int global_var;

Void change_var(){
Global_var=100;
}

Int main(void){
Change_var();
Return 0;
}

```

## Tips

The command that usually breaks the function: "b func" (b is the abbreviation of the break command), does not set the breakpoint at the beginning of the assembly instruction hierarchy function, for example:

```
(gdb) b main
Breakpoint 1 at 0x8050c12: file a.c, line 9.
(gdb) r
Starting program: /data1/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Breakpoint 1, main () at a.c:9
9 change_var();
(gdb) disassemble
Dump of assembler code for function main:
0x08050c0f <+0>: push %ebp
0x08050c10 <+1>: mov %esp, %ebp
=> 0x08050c12 <+3>: call 0x8050c00 <change_var>
0x08050c17 <+8>: mov $0x0, %eax
0x08050c1c <+13>: pop %ebp
0x08050c1d <+14>: ret
End of assembler dump.
```

It can be seen that the program is stopped at the third assembly instruction (the position indicated by the arrow). If you want to set the breakpoint at the beginning of the assembly instruction hierarchy function, use the following command: "b *func", for example:

```
(gdb) b *main
Breakpoint 1 at 0x8050c0f: file a.c, line 8.
(gdb) r
Starting program: /data1/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Breakpoint 1, main () at a.c:8
8 int main(void){
(gdb) disassemble
Dump of assembler code for function main:
=> 0x08050c0f <+0>: push %ebp
0x08050c10 <+1>: mov %esp, %ebp
0x08050c12 <+3>: call 0x8050c00 <change_var>
0x08050c17 <+8>: mov $0x0, %eax
0x08050c1c <+13>: pop %ebp
0x08050c1d <+14>: ret
End of assembler dump.
```

You can see that the program is stopped at the first assembly instruction (the position pointed by the arrow).


##Contributors

Nanxiao

