import pytest


def test_create_circle(default_circle):
    """Check the figure is created"""
    assert default_circle.radius == 5
    assert default_circle.angles == 0


def test_calculate_area(default_circle):
    """Check the area is calculated"""
    assert default_circle.area == 79


def test_calculate_perimeter(default_circle):
    """Check the perimeter is calculated"""
    assert default_circle.perimeter == 31


def test_add_area(default_circle, default_triangle):
    """Check two figures are summed up"""
    assert default_circle.add_area(default_triangle) == 85


def test_add_area_error(default_circle):
    """Check an error raises if argument 'figure' doesn't belong to 'Figure' class"""
    with pytest.raises(ValueError):
        default_circle.add_area('hey')
