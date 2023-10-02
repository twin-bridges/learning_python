import pdbr

pdbr.set_trace()
# Code Structure

# REUSABLE SECTION #####
# CONSTANTS
PI = 3.14


# Functions
def func1():
    print("Hello world")


# Classes
class SomeClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    # Main Program #####

    print("Main program")
    # do something
    func1()
    print(3 * PI)
