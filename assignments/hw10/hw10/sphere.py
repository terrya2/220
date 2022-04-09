"""
Autumn Terry
sphere.py
Create programs using decision and repetition structures, boolean values, classes, and objects.
I certify that this assignment is entirely my own work.
"""

import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        volume = (4/3) * math.pi  * (self.radius)**3
        radius = (3 * (volume / 4 * math.pi)) ** 1/3
        return radius
    def surface_area(self):
        area = 4 * math.pi  * (self.radius)**2
        return area

    def volume(self):
        volume = (4/3) * math.pi  * (self.radius)**3
        return volume