class Point:
    '''
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x, self.y}"
    def __eq__(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False
    def __add__(self, other_point):
        if isinstance(other_point, Point):
            return Point(self.x + other_point.x, self.y + other_point.y)
        elif isinstance(other_point, (int, float)):
            return Point(self.x + other_point, self.y + other_point)
        else:
            raise TypeError(f"unsupported type: {type(other_point)}")

# coord = Point()
# coord.x = 0
# coord.y = 0

coord1 = Point(1, 2)
coord2 = Point(1, 4)
print(coord1 == coord2)