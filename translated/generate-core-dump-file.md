# Generate a core dump file for the debugging process

#Tip
When debugging a program with gdb, we sometimes want the debugged process to generate a core dump file that records the state of the current process for later analysis. You can use the "generate-core-file" command to generate a core dump file:

```
(gdb) help generate-core-file
Save a core file with the current state of the debugged process.
Argument is optional filename. Default filename is 'core.<process_id>'.

(gdb) start
Temporary breakpoint 1 at 0x8050c12: file a.c, line 9.
Starting program: /data1/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Temporary breakpoint 1, main () at a.c:9
9 change_var();
(gdb) generate-core-file
Saved corefile core.12955

You can also use the "gcore" command:

(gdb) help gcore
Save a core file with the current state of the debugged process.
Argument is optional filename. Default filename is 'core.<process_id>'.
(gdb) gcore
Saved corefile core.13256
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Core-File-Generation.html)

##Contributors

Nanxiao
