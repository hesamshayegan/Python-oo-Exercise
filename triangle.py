import math

class Triangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"<Triangle a={self.a} b={self.b}>"
    
    def get_hypotenuse(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)
    
    def get_area(self):
        return (self.a * self.b) / 2
    
    def describe(self):
        return f"My area is {self.get_area()}"

# This is a subclass of Triangle (parent)
class ColoredTriangle(Triangle):
    
    def __init__(self, a, b, color):
        # get parent class [`super()`], call its `__init__`
        super().__init__(a, b)

        self.color = color

    def describe(self):
        msg = super().describe() + f" I am {self.color}"
        return msg


# triangle = Triangle(3, 4)
# print(triangle)
# print(triangle.get_hypotenuse())
# print(triangle.get_area())
        
triangle = ColoredTriangle(3, 4, 'red')
print(triangle.describe())