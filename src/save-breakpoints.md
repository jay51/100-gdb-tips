#Save the breakpoint that has been set

##example

```
$ gdb -q `which gdb`
Reading symbols from /home/xmj/install/binutils-trunk/bin/gdb...done.
(gdb) b gdb_main
Breakpoint 1 at 0x5a7af0: file /home/xmj/project/binutils-trunk/gdb/main.c, line 1061.
(gdb) b captured_main
Breakpoint 2 at 0x5a6bd0: file /home/xmj/project/binutils-trunk/gdb/main.c, line 310.
(gdb) b captured_command_loop
Breakpoint 3 at 0x5a68b0: file /home/xmj/project/binutils-trunk/gdb/main.c, line 261.
```

##Tips

In gdb, you can use the following command to save the set breakpoints:

<pre><code>(gdb) save breakpoints <i>file-name-to-save</i></code></pre>

When debugging this way, you can use the following commands to set the saved breakpoints in batches:

```
<pre><code>(gdb) source <i>file-name-to-save</i></code></pre>

(gdb) info breakpoints
Num Type Disp Enb Address What
1 breakpoint keep y 0x00000000005a7af0 in gdb_main at /home/xmj/project/binutils-trunk/gdb/main.c:1061
2 breakpoint keep y 0x00000000005a6bd0 in captured_main at /home/xmj/project/binutils-trunk/gdb/main.c:310
3 breakpoint keep y 0x00000000005a68b0 in captured_command_loop at /home/xmj/project/binutils-trunk/gdb/main.c:261
```

See the [gdb manual](https://sourceware.org/gdb/download/onlinedocs/gdb/Save-Breakpoints.html#Save-Breakpoints) for details 

## Contributors

Xmj
