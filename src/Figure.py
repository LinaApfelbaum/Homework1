class Figure:
    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    @property
    def area(self):
        raise NotImplementedError(
            "Method must be implemented in child classes")

    @property
    def perimeter(self):
        raise NotImplementedError(
            "Method must be implemented in child classes")

    def add_area(self, figure):
        if not issubclass(type(figure), Figure):
            raise ValueError("Argument 'figure' must belong to Figure class")

        return self.area + figure.area
