"""Instance attribute will take precedence over class attribute"""
import pdbr


class A:
    my_attr = 100

    def __init__(self):
        self.my_attr = 10


obj = A()
print(obj.my_attr)

pdbr.set_trace()
