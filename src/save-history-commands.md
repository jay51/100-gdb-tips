#Save history command

##Tips

In gdb, the default is to not save history commands. You can set the save history command with the following command:

```
(gdb) set history save on

However, the history command is saved by default in the .gdb_history file in the current directory. You can set the file name and path to save by the following command:

(gdb) set history filename fname

Now let's put these two commands in the $HOME/.gdbinit file:

Set history filename ~/.gdb_history
Set history save on

Ok, the next time you start gdb, you can directly find the history commands before using it.
```

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Command-History.html#Command-History) for details

##Contributors

Xmj

