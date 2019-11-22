#print index index subscript

##example

```
#include <stdio.h>

Int num[10] = {
1 << 0,
1 << 1,
1 << 2,
1 << 3,
1 << 4,
1 << 5,
1 << 6,
1 << 7,
1 << 8,
1 << 9
};

Int main (void) {
Int i;

For (i = 0; i < 10; i++)
Printf ("num[%d] = %d\n", i, num[i]);

Return 0;
}
```

##Tips

In gdb, when printing an array, the default is not to print the index subscript:

```
(gdb) p num
$1 = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512}

If you want to print an index subscript, you can set it by the following command:

(gdb) set print array-indexes on

(gdb) p num
$2 = {[0] = 1, [1] = 2, [2] = 4, [3] = 8, [4] = 16, [5] = 32, [6] = 64, [7] = 128 , [8] = 256, [9] = 512}
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Print-Settings.html#index-set-print)for details 

##Contributors

Xmj
