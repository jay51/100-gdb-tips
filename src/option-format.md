#Command line option format

##Tips

Gdb's help information and online documentation use different styles for long options. You may be a bit confused, should gdb's long option be "-" or "--"?

Yes, both methods are fine. E.g:

```
$ gdb -help
$ gdb --help

$ gdb -args ./a.out a b c
$ gdb --args ./a.out a b c

Ok, use short ones.
```

##Contributors

Xmj


