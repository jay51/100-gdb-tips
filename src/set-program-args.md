#Set the parameters of the program being debugged

##Tips

You can specify the parameters of the program being debugged by the option when gdb starts, for example:

```
$ gdb -args ./a.out a b c

It can also be set in gdb by command, for example:

(gdb) set args a b c
(gdb) show args
Argument list to give program being debugged when it is started is "a b c".
```

You can also specify directly when you run the program:

```
(gdb) r a b
Starting program: /home/xmj/tmp/a.out a b
(gdb) show args
Argument list to give program being debugged when it is started is "a b".
(gdb) r
Starting program: /home/xmj/tmp/a.out a b
```

It can be seen that the parameters have been saved, and the `run` command can be run directly at the next run.

```
Interestedly, what if I want to leave the parameters empty? Yes, directly:

(gdb) set args
```

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Arguments.html#Arguments) for details

##Contributors

Xmj

