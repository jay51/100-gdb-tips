#Set the environment variable of the program being debugged

##example

```
(gdb) u 309
Warning: couldn't activate thread debugging using libthread_db: Cannot find new threads: generic error

Warning: couldn't activate thread debugging using libthread_db: Cannot find new threads: generic error

Warning: Unable to find libthread_db matching inferior's thread library, thread debugging will not be available.
```

## Tips

In gdb, you can set the environment variable of the program being debugged by the command `set env varname=value`. For the above example, some solutions can be found online, one of which is to set the LD_PRELOAD environment variable:

```
Set env LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0

Note that this actual path may be different in different machine environments. Add this command to the ~/.gdbinit file and you're done.
```
See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Environment.html#Environment)

## Contributors

Xmj

