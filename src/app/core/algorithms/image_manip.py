#!/usr/bin/python3

"""
image_manip.py
"""

from .color import Color
from PIL import Image

def read_image_as_2D_array(img):
    """
    Converts an image from an Image object to a 2D array of color objects.
    """

    w, h = img.size
    
    pixels = list(Color(pixel[0], pixel[1], pixel[2]) for pixel in img.getdata())
    return [pixels[n:(n + w)] for n in range(0, w * h, w)]

def write_2D_array_as_image(pixels):
    """
    Converts a 2D array of color objects into an image object.
    """

    if len(pixels) <= 0:
        raise RuntimeError('Pixels cannot be empty.')

    height = len(pixels)
    width = len(pixels[0])

    img = Image.new('RGB', (width, height))

    output_pixels = img.load()

    for y, row in enumerate(pixels):
        for x, color in enumerate(row):
            output_pixels[x, y] = (color.r, color.g, color.b)

    return img

