import pytest
from src.Triangle import Triangle

@pytest.fixture()
def default_triangle():
    return Triangle(3, 4, 5)