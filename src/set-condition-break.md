# Set conditional breakpoints

## example

```
#include <stdio.h>

int main(void)
{
int i u003d 0;
int sum u003d 0;

for (i u003d 1; i <u003d 200; i++)
{
sum +u003d i;
}

printf("%d\n", sum);
return 0;
}
```

## Tips

Gdb can set conditional breakpoints, that is, the breakpoint will only be triggered when the condition is met. The command is "`break ... if cond`". Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x4004cc: file a.c, line 5.
Starting program: /data2/home/nanxiao/a

Temporary breakpoint 1, main () at a.c:5
5                       int i u003d 0;
(gdb) b 10 if iu003du003d101
Breakpoint 2 at 0x4004e3: file a.c, line 10.
(gdb) r
Starting program: /data2/home/nanxiao/a

Breakpoint 2, main () at a.c:10
10                                      sum +u003d i;
(gdb) p sum
$1 u003d 5050
```
It can be seen that the set breakpoint is only triggered when the value of `i` is `101`, and the value of `sum` is printed as `5050`.

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Set-Breaks.html)

## Contributors

nanxiao



