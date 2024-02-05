class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

obj1 = Shape()
obj2 = Square(5)         

print(obj1.area())
print(obj2.area())