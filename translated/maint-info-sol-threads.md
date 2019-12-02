# View the thread information using the maintenance command on Solaris




## Tips
When debugging multithreaded programs with gdb, if you want to view the thread information, you can use the &quot;i threads&quot; command (i is the abbreviation of the info command), for example:

	(gdb) i threads
    106 process 2689429      0xff04af84 in __lwp_park () from /lib/libc.so.1
    105 process 2623893      0xff04af84 in __lwp_park () from /lib/libc.so.1
    104 process 2558357      0xff04af84 in __lwp_park () from /lib/libc.so.1
    103 process 2492821      0xff04af84 in __lwp_park () from /lib/libc.so.1



On the Solaris operating system, gdb tailored a command for viewing thread information for Solaris: &quot;maint info sol-threads&quot; (maint is the abbreviation of the maintenance command), for example:

	(gdb) maint info sol-threads
	user   thread #1, lwp 1, (active)
	user   thread #2, lwp 2, (active)    startfunc: monitor_thread
	user   thread #3, lwp 3, (asleep)    startfunc: mem_db_thread
    - Sleep func: 0x000aa32c


You can see that the maintenance command shows more information than the info command. For example, the current state of the thread (active, asleep), entry function (startfunc), etc.

See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Threads.html)

## Contributor

nanxiao

