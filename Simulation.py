from SimulationFunctions import *
import time

dimensions = 2
initialSeparation = 5
catchRadius = 5   # maximum separation between predator and prey so that prey is caught
arrivedAtTolerance = 1       # tolerance within which we assume two positions are identical
iterations = 10000  # maximum number of iterations the simulation is run for
minWaypointDist = 20     # minimum distance prey travels to next waypoint
maxWaypointDist = 50     # maximum distance
samplePoints = 100      # number of points to generate while getting next waypoint

predator = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions)), speed=1)
prey = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions) + initialSeparation), speed=5)

predatorDirection = Vector.zero(dimensions)     # the direction the predator will move in. Zero, if not decided
previousSeparation = None   # the separation between the predator and prey in the last iteration
preyWaypoint = prey.position

caught = False      # has the prey been caught yet
lastIterationTime = time.time()     # time since last iteration

preypos = []
predpos = []
sep = []
dt = []
for i in range(iterations):
    preypos.append(prey.position.position)
    predpos.append(predator.position.position)
    print(i, predator.position, prey.position, (prey.position - predator.position).normalized(), predatorDirection)
    # is the prey close enough to be caught
    if distance(predator.position, prey.position) <= catchRadius:
        caught = True
        break

    thisIterationTime = time.time()
    deltaTime = thisIterationTime - lastIterationTime

    # if the prey is at its target waypoint
    if distance(prey.position, preyWaypoint) <= arrivedAtTolerance:
        preyWaypoint = get_new_prey_waypoint(predator, prey, minWaypointDist, maxWaypointDist, samplePoints)

    # move the prey
    prey.position += (preyWaypoint - prey.position).normalized() * prey.speed * deltaTime

    # predator knows only distance between it and prey
    separation = distance(prey.position, predator.position)

    if previousSeparation is None:      # is this the first simulated step
        # just go in a random direction
        predatorDirection = get_random_direction(dimensions)
    elif previousSeparation < separation:   # have we started moving away from the prey
        # if we are moving away from the prey, the prey must be in the hyper-hemisphere facing opposite to our current
        # direction of movement
        predatorDirection = get_random_hemisphere_direction(-predatorDirection.normalized())

    # move toward where we think the prey is. If the prey is closer than we would move in one step, move only the
    # distance to the prey. This is equivalent to slowing down temporarily, and prevents overshooting
    predator.position += predatorDirection * predator.speed * deltaTime

    previousSeparation = separation
    sep.append(separation)

from matplotlib import pyplot as plt
plt.clf()
# plt.plot([predpos[i][0] for i in range(len(predpos))], [predpos[i][1] for i in range(len(predpos))])
# plt.plot([preypos[i][0] for i in range(len(preypos))], [preypos[i][1] for i in range(len(preypos))])
plt.plot(sep)
print(min(sep))
plt.show()
print(caught)