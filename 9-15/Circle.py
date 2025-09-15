import Point

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle with center: {self.center} and radius {self.radius: .2f}"
    
circle = Circle(0, 5, 100.0)
print(circle)