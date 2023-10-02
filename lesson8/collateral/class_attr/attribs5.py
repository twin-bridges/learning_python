class Circle:
    PI = 3.14159

    def __init__(self, radius, units):
        self.radius = radius
        self.units = units

    def area(self):
        return Circle.PI * self.radius**2

    def circumference(self):
        return 2 * Circle.PI * self.radius


c1 = Circle(radius=2, units="inches")
print(f"Area: {c1.area()} square-{c1.units}")
