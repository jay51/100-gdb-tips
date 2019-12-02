#Print register value

## Tips
When debugging a program with gdb, if you want to view the value of the register, you can use the "i registers" command (i is the abbreviation for the info command), for example:

```
(gdb) i registers
Rax 0x7ffff7dd9f60 140737351884640
Rbx 0x0 0
Rcx 0x0 0
Rdx 0x7fffffffe608 140737488348680
Rsi 0x7fffffffe5f8 140737488348664
Rdi 0x1 1
Rbp 0x7fffffffe510 0x7fffffffe510
Rsp 0x7fffffffe4c0 0x7fffffffe4c0
R8 0x7ffff7dd8300 140737351877376
R9 0x7ffff7deb9e0 140737351956960
R10 0x7fffffffe360 140737488348000
R11 0x7ffff7a68be0 140737348275168
R12 0x4003e0 4195296
R13 0x7fffffffe5f0 140737488348656
R14 0x0 0
R15 0x0 0
Rip 0x4004cd 0x4004cd <main+9>
Eflags 0x206 [ PF IF ]
Cs 0x33 51
Ss 0x2b 43
Ds 0x0 0
Es 0x0 0
Fs 0x0 0
Gs 0x0 0
```
The above output does not include the contents of the floating point register and vector register. Use the "i all-registers" command to output the contents of all registers:


```
(gdb) i all-registers
Rax 0x7ffff7dd9f60 140737351884640
Rbx 0x0 0
Rcx 0x0 0
Rdx 0x7fffffffe608 140737488348680
Rsi 0x7fffffffe5f8 140737488348664
Rdi 0x1 1
Rbp 0x7fffffffe510 0x7fffffffe510
Rsp 0x7fffffffe4c0 0x7fffffffe4c0
R8 0x7ffff7dd8300 140737351877376
R9 0x7ffff7deb9e0 140737351956960
R10 0x7fffffffe360 140737488348000
R11 0x7ffff7a68be0 140737348275168
R12 0x4003e0 4195296
R13 0x7fffffffe5f0 140737488348656
R14 0x0 0
R15 0x0 0
Rip 0x4004cd 0x4004cd <main+9>
Eflags 0x206 [ PF IF ]
Cs 0x33 51
Ss 0x2b 43
Ds 0x0 0
Es 0x0 0
Fs 0x0 0
Gs 0x0 0
St0 0 (raw 0x00000000000000000000)
St1 0 (raw 0x00000000000000000000)
St2 0 (raw 0x00000000000000000000)
St3 0 (raw 0x00000000000000000000)
St4 0 (raw 0x00000000000000000000)
St5 0 (raw 0x00000000000000000000)
St6 0 (raw 0x00000000000000000000)
St7 0 (raw 0x00000000000000000000)
......
```

To print the value of a single register, you can use "i registers regname" or "p $regname", for example:

```
(gdb) i registers eax
Eax 0xf7dd9f60 -136470688
(gdb) p $eax
$1 = -136470688
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Registers.html).

##Contributors

Nanxiao

