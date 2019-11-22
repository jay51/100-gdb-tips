#Set catchpoint for system calls

##example

```
#include <stdio.h>

Int main(void) {
Char p1[] = "Sam";
Char *p2 = "Bob";

Printf("p1 is %s, p2 is %s\n", p1, p2);
Return 0;
}
```

##Tips

When using the gdb debugger, you can use `catch syscall [name | number]` to set `catchpoint` for the system call of interest, using the above program as an example:

```
(gdb) catch syscall mmap
Catchpoint 1 (syscall 'mmap' [9])
(gdb) r
Starting program: /home/nan/a

Catchpoint 1 (call to syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
(gdb) c
Continuing.

Catchpoint 1 (returned from syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
```

It can be seen that gdb will suspend the running of the program when the `mmap` call occurs.
You can also use the number of the system call to set `catchpoint`, still use the above program as an example:

```
(gdb) catch syscall 9
Catchpoint 1 (syscall 'mmap' [9])
(gdb) r
Starting program: /home/nan/a

Catchpoint 1 (call to syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
(gdb) c
Continuing.

Catchpoint 1 (returned from syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
(gdb) c
Continuing.

Catchpoint 1 (call to syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
You can see the same effect as using `catch syscall mmap`. (The system call and number mapping refer to the specific `xml` file. For example, my system is `amd64-linux.xml` in the `/usr/local/share/gdb/syscalls` folder.)

If you do not specify a specific system call, then set `catchpoint` for all system calls, still use the above program as an example:

(gdb) catch syscall
Catchpoint 1 (any syscall)
(gdb) r
Starting program: /home/nan/a

Catchpoint 1 (call to syscall brk), 0x00000034e3a1618a in brk ()
From /lib64/ld-linux-x86-64.so.2
(gdb) c
Continuing.

Catchpoint 1 (returned from syscall brk), 0x00000034e3a1618a in brk ()
From /lib64/ld-linux-x86-64.so.2
(gdb)
Continuing.

Catchpoint 1 (call to syscall mmap), 0x00000034e3a16f7a in mmap64 ()
From /lib64/ld-linux-x86-64.so.2
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Set-Catchpoints.html).

##Contributors

Nanxiao

