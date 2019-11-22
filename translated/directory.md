#Set source file search path

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

## Tips
Sometimes gdb can't accurately locate the location of the source file (such as files are removed, etc.), you can use the `directory` command to set the path to find the source file. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x400560: file a.c, line 5.
Starting program: /home/nan/a

Temporary breakpoint 1, main () at a.c:5
5 a.c: No such file or directory.
(gdb) directory ../ki/
Source directories searched: /home/nan/../ki:$cdir:$cwd
(gdb) n
6 struct tm local = {0};
(gdb)
7 struct tm gmt = {0};
(gdb)
9 localtime_r(&now, &local);
(gdb)
10 gmtime_r(&now, &gmt);
(gdb) q
```
As you can see, after using the `directory` (or `dir`) command to set the lookup directory of the source file, gdb can parse the source code normally.

If you want to load the code location when gdb starts, avoid using the `-d` parameter of gdb every time you enter the command again in gdb.

```shell
Gdb -q a.out -d /search/code/some
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Source-Path.html).

## Contributors

Nanxiao

