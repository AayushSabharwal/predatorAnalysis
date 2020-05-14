from Person import *
import time

dimensions = 2
initialSeparation = 5
catchRadius = 0.5   # maximum separation between predator and prey so that prey is caught
arrivedAtTolerance = 0.01       # tolerance within which we assume two positions are identical
iterations = 10000  # maximum number of iterations the simulation is run for

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

    if distance(prey.position, preyWaypoint) <= arrivedAtTolerance:
        pass