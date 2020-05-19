from Person import *


def get_new_prey_waypoint(predator: Person, prey: Person, minWaypointDist=5, maxWaypointDist=7, numPoints=100):
    """
    Get a new waypoint for the prey
    """
    dim = predator.position.dim
    pts = [Vector(dim=dim, rnorm=True) + prey.position for i in range(numPoints)]
    weighted = [(pts[i], (pts[i] - predator.position).sqrmagnitude()) for i in range(numPoints)]
    weighted.sort(key=lambda x: x[1])
    s = sum([x[1] for x in weighted])
    weighted = [(x[0], x[1]/s) for x in weighted]
    return np.random.choice([x[0] for x in weighted], p=[x[1] for x in weighted]) \
        * (minWaypointDist + np.random.rand() * (maxWaypointDist - minWaypointDist))


def get_random_direction(dim: int, numPoints: int = 100):
    """
    Get a unit vector in a random direction in dim dimensional space
    """
    return np.random.choice([Vector(dim, rnorm=True) for i in range(numPoints)])


def get_random_hemisphere_direction(orientation: Vector, numPoints: int = 100):
    """
    Get a unit vector in a hemisphere oriented around orientation
    """

    pts = [Vector(orientation.dim, rnorm=True) for i in range(numPoints)]
    for i in range(numPoints):
        if orientation * pts[i] < 0:
            pts[i] *= -1
    return np.random.choice(pts)


