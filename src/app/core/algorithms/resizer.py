#!/usr/bin/python3

"""
resizer.py
"""

from .seam_energy import SeamEnergy

def compute_vertical_seam(energy_data):
    """
    Finds the lowest-energy vertical seam given the energy of each pixel.

    Returns a list of seam energy objects that represent the optimal seam
    """

    dp = [[None for _ in row] for row in energy_data]

    if len(energy_data) <= 0:
        raise RuntimeError('Energy data cannot be empty.')

    h = len(energy_data)
    w = len(energy_data[0])

    for x in range(w):
        dp[0][x] = SeamEnergy(energy_data[0][x])

    for y in range(1, h):
        for x in range(w):
            leftmost_x = max(x - 1, 0)
            rightmost_x = min(x + 1, w - 1)

            min_x_previous_row = min(range(leftmost_x, rightmost_x + 1), key=lambda _x: dp[y - 1][_x].energy)

            dp[y][x] = SeamEnergy(energy_data[y][x] + dp[y - 1][min_x_previous_row].energy, min_x_previous_row)

    min_x_bottom_row = min(enumerate(dp[-1]), key=lambda m: m[1].energy)[0]

    seam_path = []
    last_x = min_x_bottom_row
    for y in range(h - 1, -1, -1):
        seam_path.append(last_x)
        last_x = dp[y][last_x].previous_x

    seam_path.reverse()

    return seam_path

def remove_seam_from_image(pixels, seam_path):
    """
    Removes a seam from a 2D array of color objects.
    """

    new_pixels = [
        [
            p
            for x, p in enumerate(row)
            if x != seam_path[y]
        ]
        for (y, row) in enumerate(pixels)
    ]

    return new_pixels



