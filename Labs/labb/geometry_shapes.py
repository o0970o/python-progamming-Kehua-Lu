import math

class Shape:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def translate(self, dx: float, dy: float):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise ValueError("dx and dy must be numeric.")
        self.x += dx
        self.y += dy

    def is_inside(self, px: float, py: float) -> bool:
        raise NotImplementedError("This method must be overridden in derived classes.")

    def __eq__(self, other):
        return isinstance(other, Shape) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y})"

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    @property
    def is_unit_circle(self) -> bool:
        return self.radius == 1

    def is_inside(self, px: float, py: float) -> bool:
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.radius ** 2

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius and super().__eq__(other)

    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius

    def __le__(self, other):
        return isinstance(other, Circle) and self.radius <= other.radius

    def __gt__(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    def __ge__(self, other):
        return isinstance(other, Circle) and self.radius >= other.radius

class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y)
        if width <= 0 or height <= 0:
            raise ValueError("Sides must be positive numbers.")
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def is_square(self) -> bool:
        return self.width == self.height

    def is_inside(self, px: float, py: float) -> bool:
        return (self.x - self.width / 2 <= px <= self.x + self.width / 2) and \
               (self.y - self.height / 2 <= py <= self.y + self.height / 2)

    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.width == other.width and self.height == other.height and super().__eq__(other)

    def __lt__(self, other):
        return isinstance(other, Rectangle) and self.area < other.area

    def __le__(self, other):
        return isinstance(other, Rectangle) and self.area <= other.area

    def __gt__(self, other):
        return isinstance(other, Rectangle) and self.area > other.area

    def __ge__(self, other):
        return isinstance(other, Rectangle) and self.area >= other.area

