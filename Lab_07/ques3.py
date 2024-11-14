class Shape:
    def __init__(self, color):
        self.color = color
    def draw(self):
        return f"Drawing a {self.color} shape"
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def draw(self):
        return f"Drawing a {self.color} circle with radius {self.radius}"
    
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        return f"Drawing a {self.color} square with side length {self.side_length}"

circle_instance = Circle("Red", 5)
square_instance = Square("Blue", 4)

print(circle_instance.draw())  
print(square_instance.draw())