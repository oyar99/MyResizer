#!/usr/bin/python3

"""
color.py
"""

class Color:
    """
    Represents a color as an RGB value.
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self):
        return f'rgb({self.r, self.g, self.b})'