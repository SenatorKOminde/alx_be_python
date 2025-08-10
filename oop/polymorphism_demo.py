import math

class Shape:
    def area(self):
        """Compute the area of the shape.

        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f"Circle({self.radius})"
