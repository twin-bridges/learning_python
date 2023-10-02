def main():
    """Main Program"""
    # some_var is now local to the "main()" function
    some_var = 42
    my_func(some_var)


def my_func(some_var):
    print(some_var)


if __name__ == "__main__":
    main()
