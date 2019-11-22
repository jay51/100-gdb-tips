#How to parse the script file

##example

```
#include <stdio.h>

Typedef struct {
    Int a;
    Int b;
    Int c;
    Int d;
}ex_st;

Int main(void) {
Ex_st st = {1, 2, 3, 4};
Printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
Return 0;
}
```

##Tips

There are two kinds of script files supported by gdb: one is a script that only contains gdb's own commands, such as the ".gdbinit" file. When gdb starts, it will execute the commands in the ".gdbinit" file. In addition, gdb also Support for script files written in other languages ​​(such as python).

Gdb uses the "`set script-extension`" command to determine which format to parse the script file. It can take 3 values:

a) `off`: all script files are parsed into gdb command scripts;

b) `soft`: Decide how to parse the script based on the script file extension. If gdb supports parsing this scripting language (such as python), it will parse in this language, otherwise it will be parsed by command script;

c) `strict`: Determines how to parse the script based on the script file extension. If gdb supports parsing this scripting language (such as python), it will parse in this language, otherwise it will not be parsed;

Take the above program as an example to debug:

```
(gdb) start
Temporary breakpoint 1 at 0x4004cd: file a.c, line 12.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:12
12 ex_st st = {1, 2, 3, 4};
(gdb) q
A debugging session is active.

Inferior 1 [process 24249] will be killed.

Quit anyway? (y or n) y


You can see that when gdb exits, the default behavior will prompt the user to quit.
```

Write a script file (gdb.py) below, but the content is a gdb command, not a real python script. The purpose is not to prompt when exiting gdb:

```
Set confirm off
Start debugging again:

(gdb) start
Temporary breakpoint 1 at 0x4004cd: file a.c, line 12.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:12
12 ex_st st = {1, 2, 3, 4};
(gdb) show script-extension
Script filename extension recognition is "soft".
(gdb) source gdb.py
File "gdb.py", line 1
Set confirm off
^
SyntaxError: invalid syntax


You can see that the default value of `script-extension` is `soft`. Next, execute ``source gdb.py`', and the gdb.py file will be parsed according to the pyhton language, but since this file is essentially a gdb command script , so the parsing error.
Execute again:

(gdb) start
Temporary breakpoint 1 at 0x4004cd: file a.c, line 12.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:12
12 ex_st st = {1, 2, 3, 4};
(gdb) set script-extension off
(gdb) source gdb.py
(gdb) q
[root@linux:~]$
```

This time, change the value of "`script-extension`" to `off`, so the script will parse it according to the gdb command script. You can see that the script command takes effect.
  
See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Extending-GDB.html)
## Contributors

Nanxiao




