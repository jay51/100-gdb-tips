#Display shared link library information
##example

```
#include <hiredis/hiredis.h>

Int main(void)
{
Char a[1026] = {0};
redisContext *c = NULL;
Void *reply = NULL;

Memset(a, 'a', (sizeof(a) - 1));
c = redisConnect("127.0.0.1", 6379);
If (NULL != c)
{
Reply = redisCommand(c, "set 1 %s", a);
freeReplyObject(reply);

Reply = redisCommand(c, "get 1");
freeReplyObject(reply);

redisFree(c);
}
Return 0;
}

```

## Tips
Use the "`info sharedlibrary regex`" command to display the shared link library information loaded by the program, where `regex` can be a regular expression, meaning that the shared link library whose name matches `regex` is displayed. If there is no `regex`, all the libraries are listed. Take the above program as an example:

```
(gdb) start
Temporary breakpoint 1 at 0x109f0: file a.c, line 5.
Starting program: /export/home/nan/a
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
[Switching to Thread 1 (LWP 1)]

Temporary breakpoint 1, main () at a.c:5
5 char a[1026] = {0};
(gdb) info sharedlibrary
From To Syms Read Shared Object Library
0xff3b44a0 0xff3e3490 Yes (*) /usr/lib/ld.so.1
0xff3325f0 0xff33d4b4 Yes /usr/local/lib/libhiredis.so.0.11
0xff3137f0 0xff31a9f4 Yes (*) /lib/libsocket.so.1
0xff215fd4 0xff28545c Yes (*) /lib/libnsl.so.1
0xff0a3a20 0xff14fedc Yes (*) /lib/libc.so.1
0xff320400 0xff3234c8 Yes (*) /platform/SUNW,UltraAX-i2/lib/libc_psr.so.1
(*): Shared library is missing debugging information.

You can see that all loaded shared link library information is listed, with "`*`" indicating that the library lacks debugging information.

You can also use regular expressions:

(gdb) i sharedlibrary hiredi*
From To Syms Read Shared Object Library
0xff3325f0 0xff33d4b4 Yes /usr/local/lib/libhiredis.so.0.11
```

You can see that only one library information is listed.
See the [gdb manual] (https://sourceware.org/gdb/current/onlinedocs/gdb/Files.html#index-shared-libraries).

##Contributors

Nanxiao

