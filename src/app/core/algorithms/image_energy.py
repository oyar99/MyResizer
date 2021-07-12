#!/usr/bin/python3

"""
image_energy.py
"""

from .color import Color

def energy_at(pixels, x, y):
    """
    Compute the energy of the pixel at position (x, y).

    The energy of the pixel is calculated by looking at neighboring pixels.

    Returns a single numerical value representing the energy at that point.
    """

    if len(pixels) <= 0:
        raise RuntimeError('Pixels cannot be empty.')

    height = len(pixels)
    width = len(pixels[0])

    left_pixel = pixels[y][x] if  x <= 0 else pixels[y][x-1]
    right_pixel = pixels[y][x] if x >= width - 1 else pixels[y][x+1]
    top_pixel = pixels[y][x] if y <= 0 else pixels[y-1][x]
    bottom_pixel = pixels[y][x] if y >= height - 1 else pixels[y+1][x]

    delta_x_2 = (left_pixel.r - right_pixel.r)**2 + (left_pixel.g - right_pixel.g)**2 + (left_pixel.b - right_pixel.b)**2
    delta_y_2 = (top_pixel.r - bottom_pixel.r)**2 + (top_pixel.g - bottom_pixel.g)**2 + (top_pixel.b - bottom_pixel.b)**2

    return delta_x_2 + delta_y_2

def compute_energy(pixels):
    """
    Compute the energy values of the given pixels.

    The input is a 2D array of color objects.

    Returns a 2D array of numerical values representing the energy at every point.
    """
    energy = [[0 for _ in row] for row in pixels]

    for y, row in enumerate(pixels):
        for x, _ in enumerate(row):
            energy[y][x] = energy_at(pixels, x, y)

    return energy

def energy_data_to_colors(energy_data):
    """
    Convert the energy values at each pixel into colors that can be used to
    visualize the energy of the image.

    First, we normalize the energy values to be between 0 and 255.
    Second, we convert these values into grayscale colors.
    """

    colors = [[0 for _ in row] for row in energy_data]

    max_energy = max(
        energy
        for row in energy_data
        for energy in row
    )

    for y, row in enumerate(energy_data):
        for x, energy in enumerate(row):
            energy_normalized = round(energy / max_energy * 255)
            colors[y][x] = Color(
                energy_normalized,
                energy_normalized,
                energy_normalized
            )

    return colors

