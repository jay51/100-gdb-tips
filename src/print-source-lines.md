#Print source line

## example

```
$ gdb -q `which gdb`
(gdb) l
15
16	   You should have received a copy of the GNU General Public License
17	   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */
18
19	#include "defs.h"
20	#include "main.h"
21	#include <string.h>
22	#include "interps.h"
23
24	int
```

## Tips

As shown above, the `list` (short for l) command can be used in gdb to display the source code and line number.
The `list` command can specify the line number, function:


```
(gdb) l 24
(gdb) l main
```

You can also specify to print forward or backward:
```
(gdb) l -
(gdb) l +
```

You can also specify a range:

```
(gdb) l 1,10
```

See the for details[gdb manual] (https://sourceware.org/gdb/onlinedocs/gdb/List.html#List)

#Contributor
xmj





