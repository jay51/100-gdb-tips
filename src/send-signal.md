#Send a signal to the program

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
In the process of debugging the program with gdb, when the program is stopped, you can use the "`signal signal_name`" command to continue the program, but will immediately send a signal to the program. Take the above program as an example:

```
(gdb) r
`/data1/nan/test' has changed; re-reading symbols.
Starting program: /data1/nan/test
[Thread debugging using libthread_db enabled]
^C[New Thread 1 (LWP 1)]

Program received signal SIGINT, Interrupt.
[Switching to Thread 1 (LWP 1)]
0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
(gdb) signal SIGHUP
Continuing with signal SIGHUP.
Receive signal: 1
```

It can be seen that when the program is paused, the `signal SIGHUP` command is executed and gdb sends a signal to the program for processing.

You can use the "`signal 0`" command to rerun the program without sending any signals to the process. Still take the above program as an example:

```
Program received signal SIGHUP, Hangup.
0xfeeeae55 in ___nanosleep () from /lib/libc.so.1
(gdb) signal 0
Continuing with no signal.

It can be seen that when the `SIGHUP` signal occurs, gdb stops the program, but since the "`signal 0`" command is executed, the program does not receive the `SIGHUP` signal after it is re-run.
```

The difference between using the `signal` command and sending a signal to the program using the `kill` command in the shell environment is that in the shell environment, the `kill` command is used to send a signal to the program, and gdb will decide whether to send the signal to the process based on the current settings. Use the `signal` command to send the signal directly to the process.

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Signaling.html#Signaling).

##Contributors

Nanxiao

