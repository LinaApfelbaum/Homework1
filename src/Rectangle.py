from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__('Rectangle', 4)
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)
