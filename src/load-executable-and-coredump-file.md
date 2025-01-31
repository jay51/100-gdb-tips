#Load executable and core dump files

##example

```
#include <stdio.h>

Int main(void) {
Int *p = NULL;
Printf("hello world\n");
*p = 0;
Return 0;
}
```

##Tips

The example program accesses a null pointer, so the program crashes and produces a core dump file. Use gdb to debug the core dump file. Usually use this command form: "gdb path/to/the/executable path/to/the/coredump", then gdb will display the location of the program crash:

```
Bash-3.2# gdb -q /data/nan/a /var/core/core.a.22268.1402638140
Reading symbols from /data/nan/a...done.
[New LWP 1]
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
Core was generated by `./a'.
Program terminated with signal 11, Segmentation fault.
#0 0x0000000000400cdb in main () at a.c:6
6 *p = 0;
```

Sometimes we want to dynamically load the executable and core dump files after gdb is started. You can use the "file" and "core" (core-file command abbreviations) commands. The "file" command is used to read the symbol table information of the executable file, and the "core" command is to specify the location of the core dump file:

```
Bash-3.2# gdb -q
(gdb) file /data/nan/a
Reading symbols from /data/nan/a...done.
(gdb) core /var/core/core.a.22268.1402638140
[New LWP 1]
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
Core was generated by `./a'.
Program terminated with signal 11, Segmentation fault.
#0 0x0000000000400cdb in main () at a.c:6
6 *p = 0;
```

You can see that gdb also shows the location of the program crash.

These two commands can be found in the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Files.html#index-core-dump-file)

##Contributors

Nanxiao

