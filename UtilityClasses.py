import numpy as np


class Vector:
    """
    Represents an n-dimensional quantity
    """

    def __init__(self, dim=2, pos: np.ndarray = None, rnorm=False):
        assert dim > 0
        self.dim = dim
        if pos is None:
            self.position = np.zeros(dim)
        else:
            assert len(pos) == dim
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
        """
        scalar or dot product
        """
        if type(other) in [float, int]:
            return Vector(dim=self.dim, pos=self.position * other)
        elif type(other) is Vector:
            assert self.dim == other.dim
            return sum([self.position[i] + other.position[i] for i in range(self.dim)])

    def __neg__(self):
        return Vector(dim=self.dim, pos=-self.position)

    def __repr__(self):
        return str(self.position)

    def __str__(self):
        return str(self.position)

    @staticmethod
    def zero(dim: int = 2):
        assert dim > 0
        return Vector(dim, np.zeros(dim))

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

    def normalized(self):
        """
        Returns another Vector, which is the normalised (magnitude 1) version of this
        """
        return Vector(self.dim, self.position / self.magnitude())

    def normalize(self):
        """
        Normalizes this vector
        """
        self.position /= self.magnitude()


def distance(v1: Vector, v2: Vector):
    """
    Returns the distance between two vectors
    """
    return (v1 - v2).magnitude()
