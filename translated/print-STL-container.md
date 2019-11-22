#Print the contents of the STL container

##example

```
#include <iostream>
#include <vector>

Using namespace std;

Int main ()
{
Vector<int> vec(10); // 10 zero-initialized elements

For (int i = 0; i < vec.size(); i++)
Vec[i] = i;

Cout << "vec contains:";
For (int i = 0; i < vec.size(); i++)
Cout << ' ' << vec[i];
Cout << '\n';

Return 0;
}
```

## Tip 1

In gdb, if you want to print the contents of the C++ STL container, the default display results are poorly readable:

```
(gdb) p vec
$1 = {<std::_Vector_base<int, std::allocator<int> >> = {
_M_impl = {<std::allocator<int>> = {<__gnu_cxx::new_allocator<int>> = {<No data fields>}, <No data fields>}, _M_start = 0x404010, _M_finish = 0x404038,
              _M_end_of_storage = 0x404038}}, <No data fields>}
```

After gdb 7.0, you can use the python script provided by gcc to improve the display results:

```
(gdb) p vec
$1 = std::vector of length 10, capacity 10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

Some distributions (Fedora 11+) do not require additional setup work. Can be verified under the gdb command line (if it is not displayed, it can be set as follows).

```
(gdb) info pretty-printer

Methods as below:

1. Get the python script, it is recommended to use gcc to install by default.

Sudo find / -name "*libstdcxx*"
2. If the machine does not find the python script, it is recommended to download the gcc corresponding version source package, the relative directory is as follows

Gcc-4.8.1/libstdc++-v3/python
3. You can also download the latest version directly.

Svn co svn://gcc.gnu.org/svn/gcc/trunk/libstdc++-v3/python

4. Add the following code to the .gdbinit file (assuming the python script is located under /home/maude/gdb_printers/)

Python
Import sys
Sys.path.insert(0, '/home/maude/gdb_printers/python')
From libstdcxx.v6.printers import register_libstdcxx_printers
Register_libstdcxx_printers (None)
End
```

(from https://sourceware.org/gdb/wiki/STLSupport)

## Tip 2

The output of `p vec` can't be read, but we can give us a hint to get the tricks without scripting support:

```
(gdb) p *(vec._M_impl._M_start)@vec.size()
$2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

## Tip 3

Download [dbinit_stl_views] (http://www.yolinux.com/TUTORIALS/src/dbinit_stl_views-1.03.txt) and execute the command.
```shell
Cat dbinit_stl_views-1.03.txt >> ~/.gdbinit
```
You can
Some commonly used containers and their corresponding command relationships
```shell
Std::vector<T> pvector stl_variable
Std::list<T> plist stl_variable T
Std::map<T,T> pmap stl_variable
Std::multimap<T,T> pmap stl_variable
Std::set<T> pset stl_variable T
Std::multiset<T> pset stl_variable
Std::deque<T> pdequeue stl_variable
Std::stack<T> pstack stl_variable
Std::queue<T> pqueue stl_variable
Std::priority_queue<T> ppqueue stl_variable
Std::bitset<n><td> pbitset stl_variable
Std::string pstring stl_variable
Std::widestring pwstring stl_variable
```
For more details, refer to the help in the configuration.


## Contributors

Xmj

Xanpeng

Enjolras

