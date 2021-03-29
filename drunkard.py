import numpy as np
import math as maths
import random
from progress.bar import Bar

class drunkard:
    """ Each object of this class represents a single drunkard. When initialised, takes the number of dimensions the drunkard exists on. Has the ability to take a step in a random direction"""
    #this objects is in reality just a set of coordinates, with the ability to increase or decrease some randomly
    def __init__(self, dimensions, starting_point = False):
        if starting_point is False:
            starting_point_final = np.zeros(dimensions) #if you don't have a specified starting point, start from the origin
        else:
            starting_point_final = np.array(starting_point) # otherwise start from the specified starting point
        self.coordinates = starting_point_final

    def step(self):
        direction = random.choice([1,-1]) #pick forwards or backwards
        self.coordinates[maths.floor(random.random()*len(self.coordinates))] += direction #pick a coordinate and move in the specified direction

####################################################################################
# the potentials are all in potentials.py
def simulation(potential, j, drunkard_number, max_step, starting_points = [False]):
'''this function takes a potential and simulates a specified number of drunkards, for a specified number of steps, with a paramtre to be given to the potential and a set of starting points for the drunkards'''
    dimensions = potential(return_dimensions = True) #check how many dimensions the problem has

    drunkards = []
    for i in range(len(starting_points)): #generate your drunkards dividing them equally between starting points
        for k in range(maths.floor(drunkard_number/len(starting_points))):
            drunkards.append(drunkard(dimensions,starting_points[i]))
    step = 0
    ks = []
    kills = []
    with Bar('Simulating drunkards', max=max_step, fill='█',empty_fill = '∙') as bar: #add a nice progress bar that looks cool and makes me happy
        while (len(drunkards)>100) and (step<max_step): #if you have too few drunkards, just give up
            killed = 0
            step += 1
            for i in range(len(drunkards) - 1, -1, -1): #for every drunkard, itterating backwards because otherwise we are going to mess things up
                drunkards[i].step() #take a random step
                if not(potential(coordinates = drunkards[i].coordinates, j=j)): #check with the potential to see you're not removed
                    del(drunkards[i])
                    killed += 1
            kills.append(killed)
            ks.append(len(drunkards)) #add how many have survived up to this step
            bar.next() #I just really like progress bars
    return(ks, kills)
