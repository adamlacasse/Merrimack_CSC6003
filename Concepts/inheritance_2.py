class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"Shape(color={self.color})"

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"

rectangle = Rectangle(10, 5, "red")
circle = Circle(7, "blue")
print(rectangle)  # Rectangle(width=10, height=5, color=red)
print(circle)     # Circle(radius=7, color=blue)
print(f"Area of rectangle: {rectangle.area()}")  # Area of rectangle: 50
print(f"Area of circle: {circle.area()}")      # Area of circle: 153.86

other_shape = Shape("green")  # This will raise an error if area() is called
other_shape.area()  # NotImplementedError: Subclasses must implement this method
