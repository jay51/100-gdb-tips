#Print ASCII and wide character strings

##example

```
#include <stdio.h>
#include <wchar.h>

Int main(void) {
Char str1[] = "abcd";
Wchar_t str2[] ​​= L"abcd";

Return 0;
}
```

##Tips

When debugging a program with gdb, you can print an ASCII string using the "`x/s`" command. Take the above program as an example:

```
Temporary breakpoint 1, main () at a.c:6
6 char str1[] = "abcd";
(gdb) n
7 wchar_t str2[] ​​= L"abcd";
(gdb)
9 return 0;
(gdb) x/s str1
0x804779f: "abcd"
```

You can see that the value of the `str1` string is printed.

When printing a wide character string, decide how to print based on the length of the wide character. Still take the above program as an example:

```
Temporary breakpoint 1, main () at a.c:6
6 char str1[] = "abcd";
(gdb) n
7 wchar_t str2[] ​​= L"abcd";
(gdb)
9 return 0;
(gdb) p sizeof(wchar_t)
$1 = 4
(gdb) x/ws str2
0x8047788: U"abcd"
```

Since the length of the current platform wide character is 4 bytes, the "`x/ws`" command is used. If it is 2 bytes, use the "`x/hs`" command.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Memory.html).

##Contributors

Nanxiao

