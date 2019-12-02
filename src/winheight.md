# Resize window
## Examples
	#include <stdio.h>
	
	void fun1(void)
	{
	        int i = 0;
	
	        i++;
	        i = i * 2;
	        printf("%d\n", i);
	}
	
	void fun2(void)
	{
	        int j = 0;
	
	        fun1();
	        j++;
	        j = j * 2;
	        printf("%d\n", j);
	}
	
	int main(void)
	{
	        fun2();
	        return 0;
	}


## Tips
When using the gdb graphical debugging interface, you can use &quot;` winheight <win_name> [+ |-] count` ”to adjust the window size (` winheight` is abbreviated as `win`.` win_name` can be `src`,` cmd`, `asm`, and` regs`). Take debugging the above program as an example This is the original `src` window size:

	   ┌──a.c──────────────────────────────────────────────────────────────────────────────────────────┐
	   │17              j++;                                                                           │
	   │18              j = j * 2;                                                                     │
	   │19              printf("%d\n", j);                                                             │
	   │20      }                                                                                      │
	   │21      int main(void)                                                                        22
	   │23      {                                                                                      │
	   │24              fun2();                                                                        │
	B+>│25                                                                                             │
	   │                return 0;                                                                      │
	   │26      }                                                                                      │
	   │27                                                                                            32
	   │                                                                                               │
	   │                                                                                               │
	   │                                                                                               │
	   │                                                                                               │
	   │                                                                                               │
	   └───────────────────────────────────────────────────────────────────────────────────────────────┘
	native process 9667 In: main                                                Line: 24   PC: 0x40052b
	Usage: winheight <win_name> [+ | -] <#lines>
	(gdb) start
	Temporary breakpoint 1 at 0x40052b: file a.c, line 24.
	Starting program: /home/nan/a
	
	Temporary breakpoint 1, main () at a.c:24

After executing the &quot;` winheight src -5` &quot;command:

	   ┌──a.c──────────────────────────────────────────────────────────────────────────────────────────┐
	   │17              j++;                                                                           │
	   │18              j = j * 2;                                                                     │
	   │19              printf("%d\n", j);                                                             │
	   │20      }                                                                                      │
	   │21                                                                                             │
	   │22      int main(void)                                                                         │
	   │23      {                                                                                      │
	  >│24              fun2();                                                                        │
	   │25              return 0;                                                                      │
	   │26      }                                                                                      │
	   │27                                                                                             │
	   └───────────────────────────────────────────────────────────────────────────────────────────────┘
	native process 9667 In: main                                               Line: 24   PC: 0x40052b
	Usage: winheight <win_name> [+ | -] <#lines>
	(gdb)
You can see that the window has become smaller.
Then execute the &quot;` winheight src + 5` &quot;command:

	   ┌──a.c──────────────────────────────────────────────────────────────────────────────────────────┐
	   │17              j++;                                                                           │
	   │18              j = j * 2;                                                                     │
	   │19              printf("%d\n", j);                                                             │
	   │20      }                                                                                      │
	   │21                                                                                             │
	   │22      int main(void)                                                                         │
	   │23      {                                                                                      │
	  >│24              fun2();                                                                        │
	   │25              return 0;                                                                      │
	   │26      }                                                                                      │
	   │27                                                                                             │
	   │28                                                                                             │
	   │29                                                                                             │
	   │30                                                                                             │
	   │31                                                                                             │
	   │32                                                                                             │
	   └───────────────────────────────────────────────────────────────────────────────────────────────┘
	native process 9667 In: main                                               Line: 24   PC: 0x40052b
	Usage: winheight <win_name> [+ | -] <#lines>
	(gdb)
You can see that the window is restored.
See [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/TUI-Commands.html).

## Contributor

nanxiao
