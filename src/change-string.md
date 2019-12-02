#Change the value of a string

##example

```
#include <stdio.h>

Int main(void)
{
Char p1[] = "Sam";
Char *p2 = "Bob";

Printf("p1 is %s, p2 is %s\n", p1, p2);
Return 0;
}
```



## Tips
When using gdb debugger, you can use the "`set`" command to change the value of the string, for example, the above program:

```
(gdb) start
Temporary breakpoint 1 at 0x8050af0: file a.c, line 5.
Starting program: /data1/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Temporary breakpoint 1, main () at a.c:5
5 char p1[] = "Sam";
(gdb) n
6 char *p2 = "Bob";
(gdb)
8 printf("p1 is %s, p2 is %s\n", p1, p2);
(gdb) set main::p1="Jil"
(gdb) set main::p2="Bill"
(gdb) n
P1 is Jil, p2 is Bill
9 return 0;
```

You can see that the strings that executed `p1` and `p2` have changed. You can also change the value of a string by accessing the memory address:

```
Starting program: /data1/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Temporary breakpoint 2, main () at a.c:5
5 char p1[] = "Sam";
(gdb) n
6 char *p2 = "Bob";
(gdb) p p1
$1 = "Sam"
(gdb) p &p1
$2 = (char (*)[4]) 0x80477a4
(gdb) set {char [4]} 0x80477a4 = "Ace"
(gdb) n
8 printf("p1 is %s, p2 is %s\n", p1, p2);
(gdb)
P1 is Ace, p2 is Bob
9 return 0;
```

When changing the value of a string, be sure to pay attention to the problem of memory out of bounds.

See [stackoverflow](http://stackoverflow.com/questions/19503057/in-gdb-how-can-i-write-a-string-to-memory).

##Contributors

Nanxiao

