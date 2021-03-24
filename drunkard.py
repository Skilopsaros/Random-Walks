import numpy as np
import math as maths
import random
from progress.bar import Bar

class drunkard:
    """ Each object of this class represents a single drunkard. When initialised, takes the number of dimensions the drunkard exists on. Has the ability to take a step in a random direction"""

    def __init__(self, dimensions, starting_point = False):
        if starting_point is False:
            starting_point = np.zeros(dimensions)
        self.coordinates = starting_point

    def step(self):
        direction = random.choice([1,-1])
        self.coordinates[maths.floor(random.random()*len(self.coordinates))] += direction

####################################################################################

def simulation(potential, j, drunkard_number, max_step, starting_points = [False]):
    dimensions = potential(return_dimensions = True)

    drunkards = []
    for i in range(len(starting_points)):
        for k in range(maths.floor(drunkard_number/len(starting_points))):
            drunkards.append(drunkard(dimensions,np.array(starting_points[i])))

    print(len(drunkards))
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





#plt.clf()
#
#ks, dead = simulation(one_d_inf_sqare_well_E2, 16, 20000, 150, starting_points = [[-8],[8]])
#ks_copy=copy.deepcopy(ks)
#for i in range(100):
#    del(ks[0])
#
#k = np.array(ks)
#m, c, am, ac = best_fit_slope_and_intercept(range(len(k)),np.log(k))
#xs = range(len(k))


#print(-2*m*256/pow(maths.pi,2))
#print(-2*am*256/pow(maths.pi,2))

#plt.plot(range(len(dead)),dead)
#plt.show()
#plt.clf()
#plt.subplot(1,2,1)
#plt.plot(range(len(ks_copy)),ks_copy)
#plt.subplot(1,2,2)
#plt.scatter(xs,np.log(k), s=1, marker='x')
#plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
#plt.show()
