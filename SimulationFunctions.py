from Person import *


def get_new_prey_waypoint(predator: Person, minWaypointDist=5, maxWaypointDist=7, numPoints = 100):
    """
    Get a new waypoint for the prey
    """
    dim = predator.position.dim
    pts = [Vector(dim=dim, rnorm=True) for i in range(numPoints)]
    weighted = [(pts[i], (pts[i] - predator.position).sqrmagnitude()) for i in range(numPoints)]
    weighted.sort(key=lambda x: x[1])
    f = np.random.rand() * weighted[-1][2]
    i = 0
    while f > weighted[i][2]:
        f -= weighted[i][2]
        i += 1

    return weighted[i][0] * (np.random.rand() + minWaypointDist) * (maxWaypointDist - minWaypointDist)
