# Set a breakpoint in the anonymous space

## Examples
	namespace Foo
	{
	  void foo()
	  {
	  }
	}

	namespace
	{
	  void bar()
	  {
	  }
	}

## Tips

In gdb, if you want to set a breakpoint for the foo function in namespace Foo, you can use the following command:

	(gdb) b Foo::foo

If you want to set a breakpoint for the bar function in the anonymous space, you can use the following command:

	(gdb) b (anonymous namespace)::bar

## Contributor

xmj

