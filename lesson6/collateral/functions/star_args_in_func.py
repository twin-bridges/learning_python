from rich import print


def print_ips(*args):
    """Take any number of positional arguments."""
    print(type(args))
    print(args)


print_ips("10.1.1.1", "10.1.1.2", "10.1.1.3")
