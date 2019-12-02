#Execute the cd and pwd commands in gdb

##Tips

Yes, gdb does support these two commands, although I didn't think they have any special use.

Maybe, when you start gdb, you find that you need to switch the working directory, but do not want to exit gdb:

```
(gdb) pwd
Working directory /home/xmj.
(gdb) cd tmp
Working directory /home/xmj/tmp.
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Working-Directory.html#Working-Directory)for details 

##Contributors

Xmj


