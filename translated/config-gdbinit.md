#Configure gdb init file

##Tips

When gdb starts, it will read the configuration files in the HOME directory and the current directory, and execute the commands inside. This file is usually ".gdbinit".

Here are some of the configurations that can be placed in ".gdbinit" as described in this document:

```
# Print the contents of the STL container
Python
Import sys
Sys.path.insert(0, "/home/xmj/project/gcc-trunk/libstdc++-v3/python")
From libstdcxx.v6.printers import register_libstdcxx_printers
Register_libstdcxx_printers (None)
End

#Save history command
Set history filename ~/.gdb_history
Set history save on

# Do not display prompt information when exiting
Set confirm off

# Print objects by derived type
Set print object on

# print index index subscript
Set print array-indexes on

#Print one structure member per line
Set print pretty on
```

Welcome to add.

##Contributors

Xmj


