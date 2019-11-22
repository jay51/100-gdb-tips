#Print memory value

##example

```
#include <stdio.h>

Int main(void) {
Int i = 0;
Char a[100];

For (i = 0; i < sizeof(a); i++) {
    a[i] = i;
}

Return 0;
}
```


##Tips
Use the "`x`" command in gdb to print the value of memory in the format "`x/nfu addr`". The meaning is to print the memory value of `n` length units starting from `addr` as `u` in `f` format. The specific meaning of the parameters is as follows:

a) n: The number of output units.

b) f: is the output format. For example, `x` is output in hexadecimal format, `o` is output in octal, and so on.

c) u: Indicate the length of a unit. `b` is a `byte`, `h` is two `byte` (halfword), `w` is four `byte` (word), `g` is eight `byte` (giant word).


Take the above program as an example:
(1) Print the value of `a`16 bytes before the array in hexadecimal format:

```
(gdb) x/16xb a
0x7fffffffe4a0: 0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07
0x7fffffffe4a8: 0x08 0x09 0x0a 0x0b 0x0c 0x0d 0x0e 0x0f
(2) Print the value of the first 16 bytes of the array `a` in unsigned decimal format:

(gdb) x/16ub a
0x7fffffffe4a0: 0 1 2 3 4 5 6 7
0x7fffffffe4a8: 8 9 10 11 12 13 14 15
(3) Print the values ​​of the first 16 `a`bytes of the array in binary format:

(gdb) x/16tb a
0x7fffffffe4a0: 00000000 00000001 00000010 00000011 00000100 00000101 00000110 00000111
0x7fffffffe4a8: 00001000 00001001 00001010 00001011 00001100 00001101 00001110 00001111
(4) Print the values ​​of the first 16 words (4 bytes) of the array `a` in hexadecimal format:

(gdb) x/16xw a
0x7fffffffe4a0: 0x03020100 0x07060504 0x0b0a0908 0x0f0e0d0c
0x7fffffffe4b0: 0x13121110 0x17161514 0x1b1a1918 0x1f1e1d1c
0x7fffffffe4c0: 0x23222120 0x27262524 0x2b2a2928 0x2f2e2d2c
0x7fffffffe4d0: 0x33323130 0x37363534 0x3b3a3938 0x3f3e3d3c
```

See the [gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/Memory.html).

##Contributors

Nanxiao

