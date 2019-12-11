# Do not pause output when the output information is too long

## Tips
Sometimes gdb will pause output when gdb outputs more information, and will print a message such as "`---Type <return> to continue, or q <return> to quit---`", as shown below:
```
81 process 2639102 0xff04af84 in __lwp_park () from /usr/lib/libc.so.1
80 process 2573566 0xff04af84 in __lwp_park () from /usr/lib/libc.so.1
---Type <return> to continue, or q <return> to quit---Quit
```


The solution is to use the "`set pagination off`" or "`set height 0`" command. This way gdb will be all output, and will not pause in the middle.
See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Screen-Size.html).

## Contributors

Nanxiao

