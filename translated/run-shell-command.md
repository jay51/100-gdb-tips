# Execute shell commands and make in gdb

## Tips

You can execute shell commands directly without leaving gdb, such as:

```
(gdb) shell ls

or

(gdb) !ls
```

Here, there is no need for spaces between the "!" and the command (ie, there are also).

Especially when you debug the program in the build environment (build directory), you can run make directly:

(gdb) make CFLAGS="-g -O0"

See the [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Shell-Commands.html#Shell-Commands)

## Contributors

Xmj


