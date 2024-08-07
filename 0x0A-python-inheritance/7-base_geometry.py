#!/usr/bin/python3

"""
Create a 'BaseGeometry'
"""
class BaseGeometry:
    """
    A class representing BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        :param name: A string representing the name of the value.
        :param value: The value to validate.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        pass

