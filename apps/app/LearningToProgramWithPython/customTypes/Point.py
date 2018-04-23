class Point:
    # This special method is known as a constructor, or initializer.
    # The first parameter of this constructor, named self, is a
    # reference to the object being created.
    def __init__(self, x, y):
        self.x = x;
        self.y = y;


pt = Point(2.5, 6)
print("(", pt.x, ",", pt.y, ")", sep="")
