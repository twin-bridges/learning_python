from rich import print


def alt_func(arg1, arg2, arg3, arg4, arg5):
    print(f"{arg1=}")
    print(f"{arg2=}")
    print(f"{arg3=}")
    print(f"{arg4=}")
    print(f"{arg5=}")


def my_func(*args, **kwargs):
    print(type(args))
    print(f"{args=}")
    print(type(kwargs))
    print(f"{kwargs=}")


print("\nFirst call: ")
my_func(1, 2, 3, arg4="hello", arg5="world")
print()
print("\nSecond call: ")
my_func(arg1=1, arg2=2, arg3=3, arg4="hello", arg5="world")
print()

