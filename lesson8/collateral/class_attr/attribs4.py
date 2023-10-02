"""
We can also access the class attribute directly regardless of whether
we have an instance attribute or not (we are not looking/using the instance).
"""
import pdbr


class A:
    my_attr = 100

    def __init__(self):
        my_attr = 10  # noqa


print(A.my_attr)

pdbr.set_trace()
