#Use the "$_exitcode" variable

##example

```
Int main(void) {
Return 0;
}
```

##Tips

When the program being debugged exits normally, gdb will use the ``convenience variable`' of `$_exitcode` to record the "`exit code`" when the program exits. Take the above program as an example:

```
[root@localhost nan]# gdb -q a
Reading symbols from a...done.
(gdb) start
Temporary breakpoint 1 at 0x400478: file a.c, line 3.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:3
3 return 0;
(gdb) n
4 }
(gdb)
0x00000034e421ed1d in __libc_start_main () from /lib64/libc.so.6
(gdb)
Single stepping until exit from function __libc_start_main,
Which has no line number information.
[Inferior 1 (process 1185) exited normally]
(gdb) p $_exitcode
$1 = 0
```

You can see that the value of printed `$_exitcode` is `0`.
Change the program and change the return value to `1`:

```
Int main(void)
{
Return 1;
}
Then debug:

[root@localhost nan]# gdb -q a
Reading symbols from a...done.
(gdb) start
Temporary breakpoint 1 at 0x400478: file a.c, line 3.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:3
3 return 1;
(gdb)
(gdb) n
4 }
(gdb)
0x00000034e421ed1d in __libc_start_main () from /lib64/libc.so.6
(gdb)
Single stepping until exit from function __libc_start_main,
Which has no line number information.
[Inferior 1 (process 2603) exited with code 01]
(gdb) p $_exitcode
$1 = 1
```
You can see that the value of the printed `$_exitcode` becomes `1`.


See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Convenience-Vars.html).

##Contributors

Nanxiao

