import pytest

def test_create_square(default_square):
    """Check the figure is created"""
    assert default_square.side == 7
    assert default_square.angles == 4

def test_calculate_area(default_square):
    """Check the area is calculated"""
    assert default_square.area == 49

def test_calculate_perimeter(default_square):
    """Check the perimeter is calculated"""
    assert default_square.perimeter == 28

def test_add_area(default_square):
    """Check two figures are summed up"""
    assert default_square.add_area(default_square) == 98

def test_add_area_error(default_square):
    """Check an error raises if argument 'figure' doesn't belong to 'Figure' class"""
    with pytest.raises(ValueError):
        default_square.add_area(({'###': '///'}))
