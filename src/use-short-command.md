#Using the abbreviated form of the command

##Tips

In gdb, you don't have to enter the full command, just the first few letters of the command. The rule is that as long as the abbreviation is not ambiguous with other commands (note, if there is ambiguity, this rule is not visible from the documentation, it seems that you need to look at the source code of gdb, or summarize it in actual use). You can also use the tab key to complete the command.

Many of these commonly used commands can only use the first letter, such as:

```
b -> break
c -> continue
d -> delete
f -> frame
i -> info
j -> jump
l -> list
n -> next
p -> print
r -> run
s -> step
u -> until

There are also two or more letters, such as:

Aw -> awatch
Bt -> backtrace
Dir -> directory
Disas -> disassemble
Fin -> finish
Ig -> ignore
Ni -> nexti
Rw -> rwatch
Si -> stepi
Tb -> tbreak
Wa -> watch
Win -> winheight
```

In addition, if you press the Enter key directly, the previous command will be executed repeatedly.

##Contributors

Xmj
Nanxiao


