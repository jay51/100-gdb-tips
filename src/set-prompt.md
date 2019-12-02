#Setting up a command prompt

##example

```
$ gdb -q `which gdb`
Reading symbols from /home/xmj/install/binutils-gdb-git/bin/gdb...done.
(gdb) r -q
Starting program: /home/xmj/install/binutils-gdb-git/bin/gdb -q
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
(gdb)
```

##Tips

When you use gdb to debug gdb, you can help you distinguish between the two gdbs by setting a command prompt:

```
$ gdb -q `which gdb`
Reading symbols from /home/xmj/install/binutils-gdb-git/bin/gdb...done.
(gdb) set prompt (main gdb)
(main gdb) r -q
Starting program: /home/xmj/install/binutils-gdb-git/bin/gdb -q
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
(gdb)
```

Note that there is a space at the end of `set prompt (main gdb)`.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Prompt.html#Prompt)for details 

##Contributors

Xmj
