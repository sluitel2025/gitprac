class Point:
    '''
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x, self.y}"
    def equals(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False
# coord = Point()
# coord.x = 0
# coord.y = 0

coord2 = Point(1, 4)
print(coord2)