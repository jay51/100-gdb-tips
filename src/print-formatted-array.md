#Print formated array

## example

Use the `call` function to control the output format of the array:

```
#include <stdio.h>

int matrix[10][10];

/* formatted output array */
void print(int matrix[][10], int m, int n) {
int i, j;
for (i u003d 0; i < m; ++i) {
for (j u003d 0; j < n; ++j)
printf("%d ", matrix[i][j]);
printf("\n");
}
}

int main(int argc, char const* argv[]) {
int i, j;
for (i u003d 0; i < 10; ++i)
for (j u003d 0; j < 10; ++j)
matrix[i][j] u003d i*10 + j;
return 0;
}
```

## Tips

```
(gdb) b 20
Breakpoint 1 at 0x40065e: file test.c, line 20.
(gdb) r
Starting program: /home/zhaoyu/codelab/algorithm/a.out

Breakpoint 1, main (argcu003d1, argvu003d0x7fffffffdc88) at test.c:20
20          return 0;
(gdb) call print(matrix, 10, 10) // format the output array by function call
0 1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47 48 49
50 51 52 53 54 55 56 57 58 59
60 61 62 63 64 65 66 67 68 69
70 71 72 73 74 75 76 77 78 79
80 81 82 83 84 85 86 87 88 89
90 91 92 93 94 95 96 97 98 99
```

## Contributors

vimerzhao
