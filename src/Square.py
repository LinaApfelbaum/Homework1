import math

from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__('Square', 4)
        self.side = side

    @property
    def area(self):
        return math.pow(self.side, 2)

    @property
    def perimeter(self):
        return 4 * self.side
