# Print objects by derived type

## Examples

	#include <iostream>
	using namespace std;
	
	class Shape {
	 public:
	  virtual void draw () {}
	};
	
	class Circle : public Shape {
	 int radius;
	 public:
	  Circle () { radius = 1; }
	  void draw () { cout << "drawing a circle...\n"; }
	};
	
	class Square : public Shape {
	 int height;
	 public:
	  Square () { height = 2; }
	  void draw () { cout << "drawing a square...\n"; }
	};
	
	void drawShape (class Shape &p)
	{
	  p.draw ();
	}
	
	int main (void)
	{
	  Circle a;
	  Square b;
	  drawShape (a);
	  drawShape (b);
	  return 0;
	}

## Tips

In gdb, when printing an object, the default is to print according to the declared type:

	(gdb) frame
	#0  drawShape (p=...) at object.cxx:25
	25	  p.draw ();
	(gdb) p p
	$1 = (Shape &) @0x7fffffffde90: {_vptr.Shape = 0x400a80 <vtable for Circle+16>}

In this example, although p is declared as a class shape, its actual derived types may be class Circle and Square. If you want to print by derived type by default, you can set it by the following command:

	(gdb) set print object on

	(gdb) p p
	$2 = (Circle &) @0x7fffffffde90: {<Shape> = {_vptr.Shape = 0x400a80 <vtable for Circle+16>}, radius = 1}

This setting also works when printing object type information:

	(gdb) whatis p
	type = Shape &
	(gdb) ptype p
	type = class Shape {
	  public:
	    virtual void draw(void);
	} &

	(gdb) set print object on
	(gdb) whatis p
	type = /* real type = Circle & */
	Shape &
	(gdb) ptype p
	type = /* real type = Circle & */
	class Shape {
	  public:
	    virtual void draw(void);
	} &

See [gdb manual] for details (https://sourceware.org/gdb/onlinedocs/gdb/Print-Settings.html#index-set-print)

## Contributor

xmj

xanpeng

