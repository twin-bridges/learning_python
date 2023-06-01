from rich import print


def test_func(x, y, z):
    return x + y + z


result = test_func(7, 9, 1)
print(result)
