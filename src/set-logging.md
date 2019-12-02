# Record the process of executing gdb
## Examples
	#include <stdio.h>
	#include <wchar.h>
	
	int main(void)
	{
	        char str1[] = "abcd";
	        wchar_t str2[] = L"abcd";
	        
	        return 0;
	}

## Tips
When using gdb to debug the program, you can use the &quot;` set logging on` &quot;command to record the process of executing gdb for future reference or analysis by others. The default log file is &quot;` gdb.txt` &quot;, you can also use&quot; `set logging file file`&quot; to change it to another name. Take the above program as an example:

    (gdb) set logging file log.txt
	(gdb) set logging on
	Copying output to log.txt.
	(gdb) start
	Temporary breakpoint 1 at 0x8050abe: file a.c, line 6.
	Starting program: /data1/nan/a 
	[Thread debugging using libthread_db enabled]
	[New Thread 1 (LWP 1)]
	[Switching to Thread 1 (LWP 1)]
	
	Temporary breakpoint 1, main () at a.c:6
	6               char str1[] = "abcd";
	(gdb) n
	7               wchar_t str2[] = L"abcd";
	(gdb) x/s str1
	0x804779f:      "abcd"
	(gdb) n       
	9               return 0;
	(gdb) x/ws str2
	0x8047788:      U"abcd"
	(gdb) q
	A debugging session is active.
	
	        Inferior 1 [process 9931    ] will be killed.
	
	Quit anyway? (y or n) y

After execution, check the log.txt file:

	bash-3.2# cat log.txt 
	Temporary breakpoint 1 at 0x8050abe: file a.c, line 6.
	Starting program: /data1/nan/a 
	[Thread debugging using libthread_db enabled]
	[New Thread 1 (LWP 1)]
	[Switching to Thread 1 (LWP 1)]
	
	Temporary breakpoint 1, main () at a.c:6
	6               char str1[] = "abcd";
	7               wchar_t str2[] = L"abcd";
	0x804779f:      "abcd"
	9               return 0;
	0x8047788:      U"abcd"
	A debugging session is active.
	
	        Inferior 1 [process 9931    ] will be killed.
	
	Quit anyway? (y or n)
You can see that log.txt records the execution process of gdb in detail.

In addition, the &quot;` set logging overwrite on` &quot;command allows the output to overwrite the previous log file; and the&quot; `set logging redirect on`&quot; command will prevent gdb&#39;s logs from being printed to the terminal.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Logging-Output.html).

## Contributor

nanxiao
