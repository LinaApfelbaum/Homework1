import pytest
from src.Triangle import Triangle
from src.Circle import Circle

@pytest.fixture()
def default_triangle():
    return Triangle(3, 4, 5)

@pytest.fixture()
def default_circle():
    return Circle(5)

