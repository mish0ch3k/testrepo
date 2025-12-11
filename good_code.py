"""
Module for calculating geometric shapes area.
This module demonstrates clean code principles.
"""

def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The calculated area.
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    
    return width * height

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    pi_approx = 3.14159
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return pi_approx * (radius ** 2)