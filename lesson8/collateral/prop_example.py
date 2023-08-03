
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = x * y


class Rectangle2:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def area(self):
        print("Computing area")
        return self._x * self._y

