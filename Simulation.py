from SimulationFunctions import *
import time

dimensions = 2
initialSeparation = 5
catchRadius = 0.5   # maximum separation between predator and prey so that prey is caught
arrivedAtTolerance = 0.01       # tolerance within which we assume two positions are identical
iterations = 10000  # maximum number of iterations the simulation is run for
minWaypointDist = 5     # minimum distance prey travels to next waypoint
maxWaypointDist = 7     # maximum distance
samplePoints = 100      # number of points to generate while getting next waypoint

predator = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions)), speed=1)
prey = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions) + initialSeparation), speed=1)
preyWaypoint = prey.position

caught = False      # has the prey been caught yet
lastIterationTime = time.time()     # time since last iteration
for i in range(iterations):
    # is the prey close enough to be caught
    if distance(predator.position, prey.position) <= catchRadius:
        caught = True
        break

    thisIterationTime = time.time()
    deltaTime = thisIterationTime - lastIterationTime
    # move the prey

    # if the prey is at its target waypoint
    if distance(prey.position, preyWaypoint) <= arrivedAtTolerance:
        preyWaypoint = get_new_prey_waypoint(predator, minWaypointDist, maxWaypointDist, samplePoints)

    prey.position += (preyWaypoint - prey.position).normalized() * prey.speed * deltaTime