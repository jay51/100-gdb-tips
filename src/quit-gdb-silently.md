# gdb does not display a prompt message when exiting


## Tips
gdb will prompt when exiting:

	A debugging session is active.

        Inferior 1 [process 29686    ] will be killed.

    Quit anyway? (y or n) n


If you do not want to display this information, you can use the following command in gdb to turn off the prompt:

	(gdb) set confirm off

You can also add this command to the .gdbinit file.

## Contributor

nanxiao

