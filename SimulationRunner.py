from Simulation import *
from matplotlib import pyplot as plt

dimensions = [1, 2, 3, 4]
initialSeparation = 20
catchRadius = 5   # maximum separation between predator and prey so that prey is caught
arrivedAtTolerance = 2       # tolerance within which we assume two positions are identical (for waypoint navigation)
iterations = 10000  # maximum number of iterations the simulation is run for
minWaypointDist = 20     # minimum distance prey travels to next waypoint
maxWaypointDist = 50     # maximum distance
samplePoints = 100      # number of points to generate while getting next waypoint
preySpeed = 1

maxSimulations = 20
niterPerDim = {}
predatorSpeedPerDim = {}
for dimension in dimensions:
    niterPerDim[dimension] = []
    predatorSpeedPerDim[dimension] = []
    predatorSpeed = 2
    for i in range(maxSimulations):
        caught, preyPosition, predatorPosition, separation, waypoints, niter = simulate(dimension, initialSeparation,
                                                                                        catchRadius, arrivedAtTolerance,
                                                                                        iterations, minWaypointDist,
                                                                                        maxWaypointDist, samplePoints,
                                                                                        predatorSpeed, preySpeed)
        save_data(dimension, initialSeparation, catchRadius, arrivedAtTolerance, iterations, niter, minWaypointDist,
                  maxWaypointDist, samplePoints, preySpeed, predatorSpeed, preyPosition, predatorPosition, separation,
                  waypoints, caught)

        predatorSpeed = (predatorSpeed + preySpeed) / 2
        niterPerDim[dimension].append(niter)
        predatorSpeedPerDim[dimension].append(predatorSpeed)

        if not caught:
            break


for dim in dimensions:
    plt.xscale("log")
    plt.plot(predatorSpeedPerDim[dim], niterPerDim[dim])
    plt.show()

plt.xscale("linear")
plt.plot(dimensions, [predatorSpeedPerDim[x][-1] for x in dimensions])
plt.show()
