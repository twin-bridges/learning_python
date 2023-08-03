from math import pi as PI


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        "Radius of a circle"
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set new radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

    @property
    def circumference(self):
        return 2 * PI * self.radius

    @property
    def area(self):
        return PI * self.radius**2

class Circle2:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        "Radius of a circle"
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set new radius")
        self._radius = value

    @property
    def area(self):
        return PI * self.radius**2

    @area.setter
    def area(self, value):
        self.radius = (value/PI)**(1/2)


class Circle3:
    def __init__(self, radius):
        self._radius = radius
        self.__foo = 42
