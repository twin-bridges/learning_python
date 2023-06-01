from rich import print


def my_func(*args, **kwargs):
    print(type(args))
    print(f"{args=}")
    print(type(kwargs))
    print(f"{kwargs=}")


print("\nCall function: ")
my_func(1, 2, 3, arg4="hello", arg5="world")
print()


