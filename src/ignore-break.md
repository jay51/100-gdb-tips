# Ignore breakpoints

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

After setting the breakpoint, you can ignore the breakpoint. The command is "`ignore bnum count`": meaning that the next `count` breakpoint trigger with `bnum` will not interrupt the program, only the `count + The 1` breakpoint trigger will interrupt the program. Take the above program as an example:

```
(gdb) b 10
Breakpoint 1 at 0x4004e3: file a.c, line 10.
(gdb) ignore 1 5
Will ignore next 5 crossings of breakpoint 1.
(gdb) r
Starting program: /data2/home/nanxiao/a

Breakpoint 1, main () at a.c:10
10                                      sum +u003d i;
(gdb) p i
$1 u003d 6
```


You can see that after setting the 5th trigger before ignoring the breakpoint, the value of the printed `i` is `6` when the first breakpoint is hit.
If you want the breakpoint to take effect next time, you can set `count` to `0`: "`ignore 1 0`".

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Conditions.html)for details

## Contributors

nanxiao (translate to Boys School)




