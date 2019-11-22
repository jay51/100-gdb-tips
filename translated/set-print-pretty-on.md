#Print one structure member per line

##example

```
#include <stdio.h>
#include <pthread.h>

Typedef struct
{
Int a;
Int b;
Int c;
Int d;
Pthread_mutex_t mutex;
}ex_st;

Int main(void) {
Ex_st st = {1, 2, 3, 4, PTHREAD_MUTEX_INITIALIZER};
Printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
Return 0;
}
```

##Tips

By default, gdb prints structures in a "compact" way. Take the above code as an example:

```
(gdb) n
15 printf("%d,%d,%d,%d\n", st.a, st.b, st.c, st.d);
(gdb) p st
$1 = {a = 1, b = 2, c = 3, d = 4, mutex = {__data = {__lock = 0, __count = 0, __owner = 0, __nusers = 0, __kind = 0,
__spins = 0, __list = {__prev = 0x0, __next = 0x0}}, __size = '\000' <repeats 39 times>, __align = 0}}
```

It can be seen that the display of the structure is very confusing, especially when other structures are nested in the structure.

You can execute the "set print pretty on" command so that only one member of the structure is displayed per line, and it is indented based on the defined level of the member:

```
(gdb) set print pretty on
(gdb) p st
$2 = {
a = 1,
b = 2,
c = 3,
d = 4,
Mutex = {
__data = {
__lock = 0,
__count = 0,
__owner = 0,
__nusers = 0,
__kind = 0,
__spins = 0,
__list = {
__prev = 0x0,
__next = 0x0
}
},
__size = '\000' <repeats 39 times>,
__align = 0
}
}
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Print-Settings.html#index-print-settings) for details

##Contributors

Nanxiao

