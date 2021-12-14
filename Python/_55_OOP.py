'''
A important concept of OO is Inheritance
Inheritance means one class (Sub/Derived Class) can extend another one (Super/Base Class)

class DeridedClassName (BaseClassName):
  Attributes
'''


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, borderColor: str, borderWidth: int):
        self.borderColor = borderColor
        self.borderWidth = borderWidth

    def draw(self):
        print(f'borderColor: {self.borderColor}; ', end='')
        print(f'borderWidth: {self.borderWidth}; ', end='')


class Circle(Shape):
    def __init__(self, borderColor: str, borderWidth: int, 
                 center: Point, radius: float):
        super().__init__(borderColor, borderWidth)
        self.center = center
        self.radius = radius

    @property
    def Diameter(self):
        return 2 * self.radius

    def draw(self):
        print('circle: ', end='')
        super().draw()
        print(f'center: [{self.center.x}, {self.center.y}]; ', end='')
        print(f'radius: {self.radius}')


class Square(Shape):
    def __init__(self, borderColor, borderWidth, 
                 topLeft: Point, bottomRight: Point):
        super().__init__(borderColor, borderWidth)
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def draw(self):
        print('Square: ', end='')
        super().draw()
        print(f'topLeft: [{self.topLeft.x}, {self.topLeft.y}]; ', end='')
        print(f'bottomRight: [{self.bottomRight.x}, {self.bottomRight.y}]', '')


circle = Circle('Blue', 2, Point(0, 0), 35.7)
print(circle.borderColor) # Got this from Shape
circle.draw()
print('circle.Diameter: ', circle.Diameter)

square = Square('Black', 3, Point(1, 1), Point(1, 7))
square.draw()

shapes = list()
shapes.append(circle)
shapes.append(square)
print('-------------------------------------------------')
for s in shapes:
    s.draw()
