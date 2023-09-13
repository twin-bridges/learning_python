import pdbr
pdbr.set_trace()

def main():
    """Main Program"""
    # some_var is now local to the "main()" function
    some_var = 42
    my_func()

def my_func():
    print(some_var)

if __name__ == "__main__":
    main()


