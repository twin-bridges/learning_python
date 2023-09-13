# Constants
E = 2.718


# Functions
def func1():
    print("Hello")


def func2():
    print("Something else")


def main():
    obj1 = SomeClass()
    obj1.print_e()


# Classes
class SomeClass:
    def __init__(self):
        self.e = E

    def print_e(self):
        print(f"{self.e}")


if __name__ == "__main__":
    main()
