import numpy as np
import math as maths
import random
import matplotlib.pyplot as plt
import copy
from progress.bar import Bar


class drankard:
    """ Each object of this class represents a single drunkard. When initialised, takes the number of dimensions the drunkard exists on. Has the ability to take a step in a random direction"""

    def __init__(self, dimensions):
        self.coordinates = np.zeros(dimensions)

    def step(self):
        direction = random.choice([1,-1])
        self.coordinates[maths.floor(random.random()*len(self.coordinates))] += direction


def simulation(potential, j, drankard_number, max_step):
    dimensions = potential(return_dimensions = True)

    drankards = []
    for i in range(drankard_number):
        drankards.append(drankard(dimensions))

    step = 0
    ks = []
    kills = []
    with Bar('Simulating drankards', max=max_step, fill='█',empty_fill = '∙') as bar:
        while (len(drankards)>100) and (step<max_step):
            killed = 0
            step += 1
            for i in range(len(drankards) - 1, -1, -1):
                drankards[i].step()
                if not(potential(coordinates = drankards[i].coordinates, j=j)):
                    del(drankards[i])
                    killed += 1
            kills.append(killed)
            ks.append(len(drankards))
            bar.next()
    return(ks, kills)


def one_d_inf_sqare_well_E1(return_dimensions=False, coordinates = [0], j=8):

    if return_dimensions:
        return(1)

    return(abs(coordinates[0]) < j)


def best_fit_slope_and_intercept(xs,ys):
    '''
    Takes two arrays, one for values of x and one for values of y, calculates the line best fit.
    Returns as a Touple in that order the following: slope, intercept, uncertainty of slope, uncertainty of intercept
    Doesnt take in account uncertainties in x and y values
    Uses formulas from book "Measurments and their uncertainties"
    '''
    SigmaXs = 0.
    for i in range (0, len(xs)):
        SigmaXs = SigmaXs + xs[i]

    SigmaXsSq = 0.
    for i in range (0, len(xs)):
        SigmaXsSq = SigmaXsSq + (xs[i]*xs[i])

    SigmaYs = 0.
    for i in range (0, len(ys)):
        SigmaYs = SigmaYs + ys[i]

    SigmaXsYs = 0.
    for i in range (0, len(xs)):
        SigmaXsYs = SigmaXsYs + xs[i]*ys[i]

    Delta= len(xs)*SigmaXsSq - (SigmaXs)*(SigmaXs)

    c = (SigmaXsSq*SigmaYs-SigmaXs*SigmaXsYs)/Delta
    m = (len(xs)*SigmaXsYs-SigmaXs*SigmaYs)/Delta

    SigmaYsminMXsminCq = 0.
    for i in range (len(xs)):
        SigmaYsminMXsminCq = SigmaYsminMXsminCq + (ys[i]-m*xs[i]-c)**2

    aCU = maths.sqrt(SigmaYsminMXsminCq/(len(xs)-2))

    am = aCU*maths.sqrt(len(xs)/Delta)
    ac = aCU*maths.sqrt(SigmaXsSq/Delta)

    return m, c, am, ac




ks, dead = simulation(one_d_inf_sqare_well_E1, 8, 10000, 150)
ks_copy=copy.deepcopy(ks)
for i in range(100):
    del(ks[0])

k = np.array(ks)
m, c, am, ac = best_fit_slope_and_intercept(range(len(k)),np.log(k))
xs = range(len(k))


print(-8*m*64/pow(maths.pi,2))
print(-8*am*64/pow(maths.pi,2))

plt.plot(range(len(dead)),dead)
plt.show()
plt.clf()
plt.subplot(1,2,1)
plt.plot(range(len(ks_copy)),ks_copy)
plt.subplot(1,2,2)
plt.scatter(xs,np.log(k), s=1, marker='x')
plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
plt.show()
