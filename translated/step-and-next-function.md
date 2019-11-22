# Whether to enter the function with debugging information

## example

```
#include <stdio.h>

int func(void)
{
return 3;
}

int main(void)
{
int a u003d 0;

a u003d func();
printf("%d\n", a);
return 0;
}

```

## Tips

When using gdb to debug a function, use the step command (abbreviated as s) to enter the function (the function must have debugging information).
Take the above code as an example:

```
(gdb) n
12              a u003d func();
(gdb) s
func () at a.c:5
5               return 3;
(gdb) n
6       }
(gdb)
main () at a.c:13
13              printf("%d\n", a);

```

You can see that gdb has entered the func function.

You can use the next command (abbreviated as n) to not enter the function, gdb will wait for the function to execute, 
and then display the program code to be executed on the next line:

```
(gdb) n
12              a u003d func();
(gdb) n
13              printf("%d\n", a);
(gdb) n
3
14              return 0;
```


You can see that gdb does not enter the func function.

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Continuing-and-Stepping.html)

## Contributors

nanxiao



