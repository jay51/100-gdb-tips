#Direct execution function

##example

```
#include <stdio.h>

Int global = 1;

Int func(void)
{
Return (++global);
}

Int main(void)
{
Printf("%d\n", global);
Return 0;
}
 ```



## Tips
When using the gdb debugger, you can call the function directly using the "`call`" or "`print`" command. Take the above program as an example:
 
 ```
 (gdb) start
 Temporary breakpoint 1 at 0x4004e3: file a.c, line 12.
 Starting program: /data2/home/nanxiao/a

 Temporary breakpoint 1, main () at a.c:12
 12 printf("%d\n", global);
 (gdb) call func()
 $1 = 2
 (gdb) print func()
 $2 = 3
 (gdb) n
 3
 13 return 0;
 ```

 It can be seen that after executing the `func` function twice, the value of `global` becomes `3`.
 See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Calling.html).

 ##Contributors

 Nanxiao


