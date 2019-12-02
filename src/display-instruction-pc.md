#Display the assembly instructions to be executed

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

When debugging an assembler with gdb, you can use the "`display /i $pc`" command to display the assembly instructions that will be executed when the program is stopped. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x400488: file a.c, line 9.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:9
9 change_var();
(gdb) display /i $pc
1: x/i $pc
=> 0x400488 <main+4>: mov $0x0, %eax
(gdb) si
0x000000000040048d 9 change_var();
1: x/i $pc
=> 0x40048d <main+9>: callq 0x400474 <change_var>
(gdb)
Change_var () at a.c:4
4 void change_var(){
1: x/i $pc
=> 0x400474 <change_var>: push %rbp
```

You can see that the assembly instructions that will be executed are printed. In addition, you can display multiple instructions at a time:

```
(gdb) display /3i $pc
2: x/3i $pc
=> 0x400474 <change_var>: push %rbp
0x400475 <change_var+1>: mov %rsp, %rbp
0x400478 <change_var+4>: movl $0x64,0x2003de(%rip) # 0x600860 <global_var>
You can see that the `3` command is displayed at a time.
```

To cancel the display, use the `undisplay` command.

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Auto-Display.html)for details

##Contributors

Nanxiao

