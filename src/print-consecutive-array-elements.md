# Print the value of any consecutive element in the array

## Examples

	int main(void)
	{
	  int array[201];
	  int i;
	
	  for (i = 0; i < 201; i++)
	    array[i] = i;
	
	  return 0;
	}

## Tips

In gdb, if you want to print the value of any consecutive element in the array, you can use the &quot;` p array [index] @ num` &quot;command (` p` is the abbreviation of the `print` command). Where `index` is the array index (counting from 0), and` num` is how many consecutive elements. Take the above code as an example:

	(gdb) p array
	$8 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
	  32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
	  63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
	  94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
	  120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
	  145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169,
	  170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
	  195, 196, 197, 198, 199...}
	(gdb) p array[60]@10
	$9 = {60, 61, 62, 63, 64, 65, 66, 67, 68, 69}


You can see that the values of the 60th to 69th elements of the `array` array are printed.
If you want to print the values of consecutive elements from the beginning of the array, you can also use this command: &quot;` p * array @ num` &quot;:

	(gdb) p *array@10
	$2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


See [gdb manual] for details (https://sourceware.org/gdb/current/onlinedocs/gdb/Arrays.html#Arrays)
## Contributor

nanxiao



