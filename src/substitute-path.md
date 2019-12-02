#Replace the directory where the source files are found

##example

```
#include <stdio.h>
#include <time.h>

Int main(void) {
Time_t now = time(NULL);
Struct tm local = {0};
Struct tm gmt = {0};

Localtime_r(&now, &local);
Gmtime_r(&now, &gmt);

Return 0;
}
```

##Tips

Sometimes when debugging a program, the source code file may have been moved to another folder. At this point you can use the `set substitute-path from to` command to set the new folder (`to`) directory to replace the old one (`from`). Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x400560: file a.c, line 5.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:5
5 a.c: No such file or directory.
(gdb) set substitute-path /home/nan /home/ki
(gdb) n
6 struct tm local = {0};
(gdb)
7 struct tm gmt = {0};
(gdb)
9 localtime_r(&now, &local);
(gdb)
10 gmtime_r(&now, &gmt);
(gdb)
12 return 0;
```

When debugging, because the source file has been moved to the `/home/ki` folder, gdb cannot find the source file. After using the `set substitute-path /home/nan /home/ki` command to set the lookup directory of the source file, gdb can parse the source code normally.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Source-Path.html).

##Contributors

Nanxiao

