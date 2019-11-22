#Do not display prompt information when starting

##example

```
$ gdb
GNU gdb (GDB) 7.7.50.20140228-cvs
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law. Type "show copying"
And "show warranty" for details.
This GDB was configured as "x86_64-unknown-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for guidelines related to "word".
```

## Tips
Gdb will display a similar message as above when it starts.

If you do not want to display this information, you can use the `-q` option to turn off the prompt:

```
$ gdb -q
(gdb)

You can set an alias for gdb in ~/.bashrc:

Alias ​​gdb="gdb -q"
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Invoking-GDB.html#Invoking-GDB) for details

##Contributors

Xmj

