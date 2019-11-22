#Whether to suspend the program when the signal occurs

##Example

```
#include <stdio.h>
#include <signal.h>

void handler(int sig);

void handler(int sig) {
    signal(sig, handler);
    printf("Receive signal: %d\n", sig);
}

int main(void) {
    signal(SIGHUP, handler);
    while (1) {
            sleep(1);
    }
    return 0;
}
```

##Tip
When debugging a program with gdb, you can use the "handle signal stop / nostop" command to set whether to suspend the execution of the program when the signal occurs. Take the above program as an example:

```
(gdb) i signals 
Signal        Stop      Print   Pass to program Description

SIGHUP        Yes       Yes     Yes             Hangup
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

It can be seen that by default, when the SIGHUP signal occurs, gdb will suspend the execution of the program and print the information of the received signal.
At this point, you need to execute the continue command to continue the execution of the program.

Next, use the "handle SIGHUP nostop" command to set gdb to not suspend the program when the SIGHUP signal occurs. The execution is as follows:

```
(gdb) handle SIGHUP nostop
Signal        Stop      Print   Pass to program Description
SIGHUP        No        Yes     Yes             Hangup
(gdb) c
Continuing.

Program received signal SIGHUP, Hangup.
Receive signal: 1
```

It can be seen that when the program receives the SIGHUP signal, it does not pause, 
but continues to execute.

If you want to restore the previous behavior, use the "handle SIGHUP stop" command. 
It should be noted that while setting stop, print is also set by default 
(for print, see whether to print signal information when the signal occurs).

see[gdb manual](https://sourceware.org/gdb/onlinedocs/gdb/Signals.html).

##Contributor

nanxiao
