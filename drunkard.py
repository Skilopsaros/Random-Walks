import numpy as np
import math as maths
import random
from progress.bar import Bar

class drunkard:
    """ Each object of this class represents a single drunkard. When initialised, takes the number of dimensions the drunkard exists on. Has the ability to take a step in a random direction"""

    def __init__(self, dimensions, starting_point = False):
        if starting_point is False:
            starting_point_final = np.zeros(dimensions)
        else:
            starting_point_final = np.array(starting_point)
        self.coordinates = starting_point_final

    def step(self):
        direction = random.choice([1,-1])
        self.coordinates[maths.floor(random.random()*len(self.coordinates))] += direction

####################################################################################

def simulation(potential, j, drunkard_number, max_step, starting_points = [False]):
    dimensions = potential(return_dimensions = True)

    drunkards = []
    for i in range(len(starting_points)):
        for k in range(maths.floor(drunkard_number/len(starting_points))):
            drunkards.append(drunkard(dimensions,starting_points[i]))
    step = 0
    ks = []
    kills = []
    with Bar('Simulating drunkards', max=max_step, fill='█',empty_fill = '∙') as bar:
        while (len(drunkards)>100) and (step<max_step):
            killed = 0
            step += 1
            for i in range(len(drunkards) - 1, -1, -1):
                drunkards[i].step()
                if not(potential(coordinates = drunkards[i].coordinates, j=j)):
                    del(drunkards[i])
                    killed += 1
            kills.append(killed)
            ks.append(len(drunkards))
            bar.next()
    return(ks, kills)
