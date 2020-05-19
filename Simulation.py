from SimulationFunctions import *
import time
import json
from os import path

dimensions = 3
initialSeparation = 20
catchRadius = 2   # maximum separation between predator and prey so that prey is caught
arrivedAtTolerance = 5       # tolerance within which we assume two positions are identical
iterations = 10000  # maximum number of iterations the simulation is run for
minWaypointDist = 20     # minimum distance prey travels to next waypoint
maxWaypointDist = 50     # maximum distance
samplePoints = 100      # number of points to generate while getting next waypoint

predator = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions)), speed=1.4)
prey = Person(dim=dimensions, pos=Vector(dimensions, np.zeros(dimensions) + initialSeparation), speed=1)

predatorDirection = Vector.zero(dimensions)     # the direction the predator will move in. Zero, if not decided
previousSeparation = None   # the separation between the predator and prey in the last iteration
preyWaypoint = get_new_prey_waypoint(predator, prey, minWaypointDist, maxWaypointDist, samplePoints)

caught = False      # has the prey been caught yet

# fields to save
preyPosition = []
predatorPosition = []
separation = []
waypoints = []
niter = 0

for i in range(iterations):
    currentSeparation = distance(prey.position, predator.position)

    # data saving
    preyPosition.append(tuple(prey.position.position))
    predatorPosition.append(tuple(predator.position.position))
    separation.append(currentSeparation)
    waypoints.append(tuple(preyWaypoint.position))
    niter = i + 1

    # is the prey close enough to be caught
    if currentSeparation <= catchRadius:
        caught = True
        break

    thisIterationTime = time.time()

    # if the prey is at its target waypoint
    if distance(prey.position, preyWaypoint) <= arrivedAtTolerance:
        preyWaypoint = get_new_prey_waypoint(predator, prey, minWaypointDist, maxWaypointDist, samplePoints)

    # move the prey
    prey.position += (preyWaypoint - prey.position).normalized() * prey.speed

    # predator knows only distance between it and prey
    if previousSeparation is None:      # is this the first simulated step
        # just go in a random direction
        predatorDirection = get_random_direction(dimensions)
    elif previousSeparation < currentSeparation:   # have we started moving away from the prey
        # if we are moving away from the prey, the prey must be in the hyper-hemisphere facing opposite to our current
        # direction of movement
        predatorDirection = get_random_hemisphere_direction(-predatorDirection.normalized())

    # move toward where we think the prey is. If the prey is closer than we would move in one step, move only the
    # distance to the prey. This is equivalent to slowing down temporarily, and prevents overshooting
    predator.position += predatorDirection * predator.speed

    previousSeparation = currentSeparation

last = 0
all_data = {}
if path.isfile("simulationData.txt"):
    with open("simulationData.txt", mode="r") as f:
        all_data = json.load(f)
    last = max(all_data.keys)

all_data[last + 1] = {"dimensions": dimensions,
                      "initialSeparation": initialSeparation,
                      "catchRadius": catchRadius,
                      "arrivedAtTolerance": arrivedAtTolerance,
                      "maxIterations": iterations,
                      "nIterations": niter,
                      "minWaypointDist": minWaypointDist,
                      "maxWaypointDist": maxWaypointDist,
                      "samplePoints": samplePoints,
                      "preyPosition": preyPosition,
                      "predatorPosition": predatorPosition,
                      "separation": separation,
                      "waypoints": waypoints,
                      "caught": caught}

with open("simulationData.txt", mode="w") as f:
    json.dump(all_data, f)

print(caught)
