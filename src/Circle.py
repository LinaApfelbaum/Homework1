import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__('Circle', 0)
        self.radius = radius

    @property
    def area(self):
        area = math.pi * math.pow(self.radius, 2)
        return round(area)

    @property
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter)
