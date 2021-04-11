import pytest

def test_create_rectangle(default_rectangle):
    """Check the figure is created"""
    assert default_rectangle.length == 6
    assert default_rectangle.width == 4
    assert default_rectangle.angles == 4

def test_calculate_area(default_rectangle):
    """Check the area is calculated"""
    assert default_rectangle.area == 24

def test_calculate_perimeter(default_rectangle):
    """Check the perimeter is calculated"""
    assert default_rectangle.perimeter == 20

def test_add_area(default_rectangle, default_circle):
    """Check two figures are summed up"""
    assert default_rectangle.add_area(default_circle) == 103

def test_add_area_error(default_rectangle):
    """Check an error raises if argument 'figure' doesn't belong to 'Figure' class"""
    with pytest.raises(ValueError):
        default_rectangle.add_area({'abc': 'xyz'})