#When the signal occurs, whether to throw the signal to the program processing

## example

```
#include <stdio.h>
#include <signal.h>

Void handler(int sig);

Void handler(int sig)
{
Signal(sig, handler);
Printf("Receive signal: %d\n", sig);
}

Int main(void) {
Signal(SIGHUP, handler);

While (1)
{
Sleep(1);
}
Return 0;
}
```

## Tips
When debugging a program with gdb, you can use the "`handle signal pass(noignore)/nopass(ignore)`"" command to set whether the signal is thrown to the program when the signal occurs. The meanings of `pass` and `noignore` are the same. Nopass` and `ignore` have the same meaning. Take the above program as an example:

```
(gdb) i signals
Signal Stop Print Pass to program Description

SIGHUP Yes Yes Yes Hangup
......

(gdb) r
Starting program: /data1/nan/test
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]

Program received signal SIGHUP, Hangup.
[Switching to Thread 1 (LWP 1)]
0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
(gdb) c
Continuing.
Receive signal: 1
```

As you can see, by default, when the `SIGHUP` signal occurs, gdb will throw the signal to the program.

Next, use the "`handle SIGHUP nopass`" command to set when the `SIGHUP` signal occurs, gdb does not throw the signal to the program, as follows:

```
(gdb) handle SIGHUP nopass
Signal Stop Print Pass to program Description
SIGHUP Yes Yes No Hangup
(gdb) c
Continuing.

Program received signal SIGHUP, Hangup.
0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
(gdb) c
Continuing.

It can be seen that when the `SIGHUP` signal occurs, the program does not print "Receive signal: 1", indicating that gdb does not throw the signal to the program.
```

If you want to restore the previous behavior, use the "`handle SIGHUP pass`" command.

See the [gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Signals.html).

##Contributors

Nanxiao

