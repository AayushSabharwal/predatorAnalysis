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
    return np.random.choice([x[0] for x in weighted], p=[x[1] for x in weighted])


p = get_new_prey_waypoint(Person(), Person(pos=Vector(pos=np.zeros(2) + 2)))
print(type(p), p.position)