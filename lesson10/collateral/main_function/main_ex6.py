import pdbr

pdbr.set_trace()
# Code Structure

# REUSABLE SECTION #####
# CONSTANTS
PI = 3.14


# Functions
def func1():
    print("Hello world")


def main():
    """Main Program"""
    print("Main program")
    # do something
    func1()
    print(3 * PI)


if __name__ == "__main__":
    main()
