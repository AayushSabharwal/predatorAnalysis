from UtilityClasses import *


class Person:
    """
    An n-dimensional person with a position and speed
    """
    def __init__(self, dim=2, pos: Vector = Vector(), speed=1):
        if pos.dim == dim:
            self.position = pos
        else:
            self.position = Vector(dim)

        self.speed = speed
