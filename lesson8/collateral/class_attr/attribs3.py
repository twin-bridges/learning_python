"""
We can access the class attribute via the instance if there is no instance
attribute.
"""
import pdbr

class A:
    my_attr = 100

    def __init__(self):
        pass

obj = A()
print(obj.my_attr)

pdbr.set_trace()
