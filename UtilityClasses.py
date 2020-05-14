import numpy as np


class Vector:
    """
    Represents an n-dimensional quantity
    """

    def __init__(self, dim=2, pos: np.ndarray = np.zeros(2), rnorm=False):
        assert dim > 0
        self.dim = dim
        if pos == np.zeros(2):
            self.position = np.zeros(dim)
        else:
            self.position = pos

        if rnorm:
            for i in range(dim):
                self.position[i] = np.random.normal()
            self.normalize()

    def __add__(self, other):
        assert self.dim == other.dim
        return Vector(dim=self.dim, pos=self.position + other.position)

    def __sub__(self, other):
        assert self.dim == other.dim
        return Vector(dim=self.dim, pos=self.position - other.position)

    def __mul__(self, other):
        assert type(other) in [float, int]
        return Vector(dim=self.dim, pos=self.position * other)

    def __neg__(self):
        return Vector(dim=self.dim, pos=-self.position)

    def sqrmagnitude(self):
        """
        Returns square magnitude of this vector
        """
        smagn = 0
        for i in range(self.dim):
            smagn += self.position[i] ** 2

        return smagn

    def magnitude(self):
        """
        Returns the magnitude of this vector
        """
        return self.sqrmagnitude() ** 0.5

    def normalize(self):
        """
        Returns another Vector, which is the normalised (magnitude 1) version of this
        """
        return Vector(self.dim, self.position / self.magnitude())


def distance(v1: Vector, v2: Vector):
    """
    Returns the distance between two vectors
    """
    assert v1.dim == v2.dim
    dist = 0
    for i in range(v1.dim):
        dist += (v1.position[i] - v2.position[i]) ** 2

    return dist ** 0.5
