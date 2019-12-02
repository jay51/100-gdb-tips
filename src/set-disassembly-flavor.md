# Set assembly instruction format

## example

```
#include <stdio.h>
int global_var;

void change_var(){
global_v R u003d 100;
}

int main(void){
change_var ();
return 0;
}
```

## Tips

On Intel x86 processors, gdb displays the assembly instruction format by default in the AT&T format. E.g:

```
(gdb) disassemble main
Dump of assembler code for function main:
0x08050c0f <+0>:     push   %ebp
0x08050c10 <+1>:     mov    %esp,%ebp
0x08050c12 <+3>:     call   0x8050c00 <change_var>
0x08050c17 <+8>:     mov    $0x0,%eax
0x08050c1c <+13>:    pop    %ebp
0x08050c1d <+14>: ret
End of assembler dump.
```


You can change the format to intel with the "set disassembly-flavor" command:

```
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
0x08050c0f <+0>:     push   ebp
0x08050c10 <+1>:     mov    ebp,esp
0x08050c12 <+3>:     call   0x8050c00 <change_var>
0x08050c17 <+8>:     mov    eax,0x0
0x08050c1c <+13>:    pop    ebp
0x08050c1d <+14>: ret
End of assembler dump.
```

Currently the "set disassembly-flavor" command can only be used on Intel x86 processors, and the values only "intel" and "att".

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Machine-Code.html)

## Contributors

nanxiao



