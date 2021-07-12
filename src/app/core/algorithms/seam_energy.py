#!/usr/bin/python3

"""
seam_energy.py
"""

class SeamEnergy:
    """
    Represents the total energy of a seam along with a back pointer
    """

    def __init__(self, energy, previous_x=None):
        self.energy = energy
        self.previous_x = previous_x
    
    def __str__(self):
        return f'seam with total energy {self.energy} and comes from column {self.previous_x}'