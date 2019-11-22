#Break the breakpoint at the program address

##example

```
0000000000400522 <main>:
400522: 55 push %rbp
400523: 48 89 e5 mov %rsp, %rbp
400526: 8b 05 00 1b 00 00 mov 0x1b00 (%rip), %eax # 40202c <he+0xc>
40052c: 85 c0 test %eax, %eax
40052e: 75 07 jne 400537 <main+0x15>
400530: b8 7c 06 40 00 mov $0x40067c, %eax
400535: eb 05 jmp 40053c <main+0x1a>
```

##Tips

When debugging an assembler, or a program without debugging information, it is often necessary to break points at the program address by `b *address`. E.g:

```
(gdb) b *0x400522
```

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Specify-Location.html#Specify-Location) for details 

## Contributors

Xmj


