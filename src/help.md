# Get help information for the command

## Tips

Use `help` command to get gdb command help information:

(1) `help` command without any parameters will get the classification of the command:

	(gdb) help
	List of classes of commands:
	
	aliases -- Aliases of other commands
	breakpoints -- Making program stop at certain points
	data -- Examining data
	files -- Specifying and examining files
	internals -- Maintenance commands
	obscure -- Obscure features
	running -- Running the program
	stack -- Examining the stack
	status -- Status inquiries
	support -- Support facilities
	tracepoints -- Tracing of program execution without stopping the program
	user-defined -- User-defined commands
	
	Type "help" followed by a class name for a list of commands in that class.
	Type "help all" for the list of all commands.
	Type "help" followed by command name for full documentation.
	Type "apropos word" to search for commands related to "word".
	Command name abbreviations are allowed if unambiguous.
(2) When you enter the `help class` command, you can get a list of all commands and command functions in this category:

	(gdb) help data
	Examining data.
	
	List of commands:
	
	append -- Append target code/data to a local file
	append binary -- Append target code/data to a raw binary file
	append binary memory -- Append contents of memory to a raw binary file
	append binary value -- Append the value of an expression to a raw binary file
	append memory -- Append contents of memory to a raw binary file
	append value -- Append the value of an expression to a raw binary file
	call -- Call a function in the program
	disassemble -- Disassemble a specified section of memory
	display -- Print value of expression EXP each time the program stops
	dump -- Dump target code/data to a local file
	dump binary -- Write target code/data to a raw binary file
	dump binary memory -- Write contents of memory to a raw binary file
	dump binary value -- Write the value of an expression to a raw binary file
	......
(3) You can also use `help command` command to get the usage of a specific command:

	(gdb) help mem
	Define attributes for memory region or reset memory region handling totarget-based.
	Usage: mem auto
       mem <lo addr> <hi addr> [<mode> <width> <cache>],
	where <mode>  may be rw (read/write), ro (read-only) or wo (write-only),
      <width> may be 8, 16, 32, or 64, and
      <cache> may be cache or nocache

(4) Use the `apropos regexp` command to find all command information that matches the` regexp` regular expression:

	(gdb) apropos set
	awatch -- Set a watchpoint for an expression
	b -- Set breakpoint at specified line or function
	br -- Set breakpoint at specified line or function
	bre -- Set breakpoint at specified line or function
	brea -- Set breakpoint at specified line or function
	......

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Help.html)

## Contributor

nanxiao



