import pytest
from src.Triangle import Triangle


def test_create_triangle(default_triangle):
    """Check the figure is created"""
    assert default_triangle.a == 3
    assert default_triangle.b == 4
    assert default_triangle.c == 5
    assert default_triangle.angles == 3


def test_calculate_area(default_triangle):
    """Check the area is calculated"""
    assert default_triangle.area == 6


def test_calculate_perimeter(default_triangle):
    """Check the perimeter is calculated"""
    assert default_triangle.perimeter == 12


def test_add_area(default_triangle):
    """Check two figures are summed up"""
    triangle = Triangle(3, 4, 5)
    assert default_triangle.add_area(triangle) == 12


def test_add_area_error(default_triangle):
    """Check an error raises if argument 'figure' doesn't belong to 'Figure' class"""
    with pytest.raises(ValueError):
        default_triangle.add_area(528)
