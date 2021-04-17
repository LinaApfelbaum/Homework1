import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__('Triangle', 3)
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        semi_perimeter = (self.a + self.b + self.c)/2
        return math.sqrt(semi_perimeter*(semi_perimeter-self.a)*(semi_perimeter-self.b)*(semi_perimeter-self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
