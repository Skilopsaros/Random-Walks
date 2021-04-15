import numpy as np
import math as maths
import random
from progress.bar import Bar
import copy
import matplotlib.pyplot as plt
#import potentials as pnt

###############################################################################
######################## Class deffinition of drunkard ########################
###############################################################################
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

###############################################################################
########################### Defining the simulation ###########################
###############################################################################

def simulation(potential, j, drunkard_number, max_step, return_positions = False):
    '''this function takes a potential and simulates a specified number of drunkards, for a specified number of steps, with a paramtre to be given to the potential and a set of starting points for the drunkards'''
    dimensions = potential(return_dimensions = True) #check how many dimensions the problem has
    starting_points = potential(return_starting_pints = True)
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
    if return_positions:
        drunkards_copy = copy.deepcopy(drunkards)
        for i in range(len(drunkards) - 1, -1, -1): #for every drunkard, itterating backwards because otherwise we are going to mess things up
            drunkards[i].step() #take a random step
            if not(potential(coordinates = drunkards[i].coordinates, j=j)): #check with the potential to see you're not removed
                del(drunkards[i])
        drunkards.extend(drunkards_copy)
        furthest_position = 0
        for i in range(len(drunkards)):
            for j in range(len(drunkards[i].coordinates)):
                if abs(drunkards[i].coordinates[j])>furthest_position:
                    furthest_position = abs(drunkards[i].coordinates[j])
        furthest_position+=1
        shape = []
        for i in range(dimensions):
            shape.append(int(2*furthest_position+1))
        lattice = np.zeros(shape).astype(int)
        for i in range(len(drunkards)):
            lattice[tuple((drunkards[i].coordinates+furthest_position).astype(int))]+=1
        return(lattice)

    return(ks, kills)

###############################################################################
############################ Line Fitting function ############################
###############################################################################

def best_fit_slope_and_intercept(xs,ys):
    '''
    Takes two arrays, one for values of x and one for values of y, calculates the line best fit.
    Returns as a Touple in that order the following: slope, intercept, uncertainty of slope, uncertainty of intercept
    Doesnt take in account uncertainties in x and y values
    Uses formulas from book "Measurments and their uncertainties"
    '''
    SigmaXs = 0.
    for i in range (0, len(xs)):
        SigmaXs += xs[i]

    SigmaXsSq = 0.
    for i in range (0, len(xs)):
        SigmaXsSq += (xs[i]*xs[i])

    SigmaYs = 0.
    for i in range (0, len(ys)):
        SigmaYs += ys[i]

    SigmaXsYs = 0.
    for i in range (0, len(xs)):
        SigmaXsYs += xs[i]*ys[i]

    Delta= len(xs)*SigmaXsSq - (SigmaXs)*(SigmaXs)

    c = (SigmaXsSq*SigmaYs-SigmaXs*SigmaXsYs)/Delta
    m = (len(xs)*SigmaXsYs-SigmaXs*SigmaYs)/Delta

    SigmaYsminMXsminCq = 0.
    for i in range (len(xs)):
        SigmaYsminMXsminCq += (ys[i]-m*xs[i]-c)**2

    aCU = maths.sqrt(SigmaYsminMXsminCq/(len(xs)-2))

    am = aCU*maths.sqrt(len(xs)/Delta)
    ac = aCU*maths.sqrt(SigmaXsSq/Delta)

    return m, c, am, ac

###############################################################################
########################### Defining the potentials ###########################
###############################################################################

# here we have the different potentials. Each potential has all the information one might need
# specifically, how many dimensions it is in, what to use to calculate energy, what starting points to initiate the drunkards
# and of course it calculates if a drunkard survives at a point
def one_d_inf_sqare_well_E1(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0): #this is the first potential
    if return_results:
        return(-m*j*j*8/pow(maths.pi,2),am*j*j*8/pow(maths.pi,2))#what results to display
    if return_dimensions:
        return(1) #the one dimentional infinite square well has one dimension
    if return_starting_pints:
        return([False]) #start from the origin
    return(abs(coordinates[0]) < j) #keep them alive only if their coordinate is lower than J

def one_d_inf_sqare_well_E2(return_dimensions=False, coordinates=[0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-m*j*j*2/pow(maths.pi,2),am*j*j*2/pow(maths.pi,2))
    if return_dimensions:
        return(1)
    if return_starting_pints:
        return([[-maths.ceil(j/2)],[maths.ceil(j/2)]])#start from a different starting point
    if 0==coordinates[0]:
        return(False)
    return(abs(coordinates[0]) < j)

def two_d_inf_cyrcle_well_E1(return_dimensions=False, coordinates=[0,0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return((-m*j*j),(am*j*j))
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([False])
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def two_d_inf_cyrcle_well_E2(return_dimensions=False, coordinates=[0,0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-m*j*j,am*j*j)
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([[-maths.ceil(j/2),0],[maths.ceil(j/2),0]])
    if 0==coordinates[0]:
        return(False)
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def two_d_inf_cyrcle_well_E3(return_dimensions=False, coordinates=[0,0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-m*j*j,am*j*j)
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([[-maths.ceil(j/2),-maths.ceil(j/2)],[maths.ceil(j/2),-maths.ceil(j/2)],[-maths.ceil(j/2),maths.ceil(j/2)],[maths.ceil(j/2),maths.ceil(j/2)]])
    if 0==coordinates[0] or 0==coordinates[1]:
        return(False)
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def one_d_SHO_E1(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-m*j,am*j)
    if return_dimensions:
        return(1)
    if return_starting_pints:
        return([False])
    return(random.random()>pow(coordinates[0],2)/(2*j*j))

def one_d_SHO_E2(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-m*j,am*j)
    if return_dimensions:
        return(1)
    if return_starting_pints:
        return([[-maths.ceil(j/4)],[maths.ceil(j/4)]])
    if 0==coordinates[0]:
        return(False)
    return(random.random()>pow(coordinates[0],2)/(2*j*j))

def two_d_SHO_E1(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-2*m*j,2*am*j)
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([False])
    return(random.random()>(pow(coordinates[0],2)+pow(coordinates[1],2))/(4*j*j))

def two_d_SHO_E2(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-2*m*j,2*am*j)
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([[-maths.ceil(j/2),0],[maths.ceil(j/2),0]])
    if 0==coordinates[0]:
        return(False)
    return(random.random()>(pow(coordinates[0],2)+pow(coordinates[1],2))/(4*j*j))

def two_d_SHO_E3(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    if return_results:
        return(-2*m*j,2*am*j)
    if return_dimensions:
        return(2)
    if return_starting_pints:
        return([[-maths.ceil(j/2),-maths.ceil(j/2)],[maths.ceil(j/2),-maths.ceil(j/2)],[-maths.ceil(j/2),maths.ceil(j/2)],[maths.ceil(j/2),maths.ceil(j/2)]])
    if 0==coordinates[0] or 0==coordinates[1]:
        return(False)
    return(random.random()>(pow(coordinates[0],2)+pow(coordinates[1],2))/(4*j*j))


def hydrogen_E1(return_dimensions=False, coordinates = [0], j=8, return_starting_pints = False, return_results = False, m=0, am = 0):
    #this gives a wrong result
    if return_results:
        return((-m*j*j-j)*2/3)
    if return_dimensions:
        return(3)
    if return_starting_pints:
        return([False])
    r = maths.sqrt(pow(coordinates[0],2)+pow(coordinates[1],2)+pow(coordinates[2],2))
    if 0==r:
        return(True)
    return(random.random()>(1-1/r)/j)

###############################################################################
########################## Putting it all togeather ###########################
###############################################################################

def run(text,ask_decouple,potential):
    while input('Run '+text+'? (Y/N) ')=='Y':
        J = int(input('input the value of J: '))
        number_of_drunkards = int(input('input the number of drunkards: '))
        number_of_cycles = int(input('input the number of cycles: '))
        number_to_cut = int(input('input the number to cut: '))
        if ask_decouple:
            decouple = (input('do you want to decouple? (Y/N) ')) # All of these are just inputs to see the parameters you are running with
            if decouple == 'Y':
                decouple = True
            else:
                decouple = False
        else:
            decouple = False

        ks, dead = simulation(potential, J, number_of_drunkards, number_of_cycles) #This runs the simulation. To see how this runs, go to drunkard.py
        ks_copy=copy.deepcopy(ks) #copying things to make sure we don't loose the original data when we alter it
        xs = list(range(len(ks)))
        for i in range(number_to_cut): #this cuts the first few steps, because the distribution of drunkards is not yet stable
            del(ks[0])
            del(xs[0])
        k = np.array(ks)
        if decouple: # to decouple we only need every other point
            ks_decoupled = ks[::2] #use every second value of number of surviving drunkards
            xs_decoupled = xs[::2] # this is done to give us the right result
            xs = xs_decoupled # use the decoupled values
            k = np.array(ks_decoupled)
        m, c, am, ac = best_fit_slope_and_intercept(xs,np.log(k)) #this is a function to find the best fit slope. It works. Find it in slope.py. I tested it with scipy stuff too.
        print(potential(j=J, return_results=True, m=m, am=am))

        plt.plot(range(len(dead)),dead) #plot how many died each turn
        plt.xlabel("Step")
        plt.ylabel("Walks Terminated")
        plt.show()
        plt.clf()
        plt.subplot(1,2,1) #plot the survivng number every turn
        plt.xlabel("Step")
        plt.ylabel("Surviving Drunkards")
        plt.plot(range(len(ks_copy)),ks_copy)
        plt.subplot(1,2,2) #plot the log of that with a fit
        plt.xlabel("Step")
        plt.ylabel("Log of surviving Drunkards")
        plt.scatter(xs,np.log(k), s=1, marker='x')
        plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
        plt.show()
        plt.clf()

def run_bare(decouple,potential,J,number_of_drunkards,number_of_cycles,number_to_cut): #Same as the above but without asking for inputs or plotting anything, for use later
    ks, dead = simulation(potential, J, number_of_drunkards, number_of_cycles)
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    xs = range(len(ks))
    k = np.array(ks)
    if decouple:
        ks_decoupled = ks[::2]
        xs_decoupled = xs[::2]
        xs = xs_decoupled
        k = np.array(ks_decoupled)
    m, c, am, ac = best_fit_slope_and_intercept(xs,np.log(k))
    return(potential(j=J, return_results=True, m=m, am=am))

def run_heatmap(text,potential): #Runs the program to show the shape of the distribution
    while input('Run '+text+'? (Y/N) ')=='Y':
        J = int(input('input the value of J: '))
        number_of_drunkards = int(input('input the number of drunkards: '))
        number_of_cycles = int(input('input the number of cycles: '))
        tick_multiples = int(input('input the frequency of ticks in the graph (if 2D): '))

        lattice = simulation(potential, J, number_of_drunkards, number_of_cycles, return_positions=True) #This runs the simulation. To see how this runs, go to drunkard.py
        if potential(return_dimensions = True) == 1:
            plt.clf()
            plt.plot(range(int(-(len(lattice)-1)/2),int((len(lattice)-1)/2+1)),lattice)
            plt.show()
            plt.clf()

        if potential(return_dimensions = True) == 2:
            plt.clf()
            tick = list(range(int(-(len(lattice)-1)/2),int((len(lattice)-1)/2+1)))
            tick_str = []
            for i in range(len(tick)):
                if i%tick_multiples == 0:
                    tick_str.append(str(tick[i]))
                else:
                    tick_str.append('')
            plt.clf()
            plt.xticks(ticks=np.arange(len(tick_str)),labels=tick_str)
            plt.yticks(ticks=np.arange(len(tick_str)),labels=tick_str)
            plt.imshow(lattice, cmap='hot',interpolation="nearest")#inferno colours are cooler
            plt.show()
            plt.clf()


def run_generation(text,ask_decouple,potential):#runs multiple different runs with the same parameters, produces a mean and standard deviation
    if input('Run '+text+'? (Y/N) ')=='Y':
        number_of_runs = int(input('input the number of runs: '))
        J = int(input('input the value of J: '))
        number_of_drunkards = int(input('input the number of drunkards: '))
        number_of_cycles = int(input('input the number of cycles in each run: '))
        number_to_cut = int(input('input the number to cut: '))
        if ask_decouple:
            decouple = (input('do you want to decouple? (Y/N) ')) # All of these are just inputs to see the parameters you are running with
            if decouple == 'Y':
                decouple = True
            else:
                decouple = False
        else:
            decouple = False
        ms = []
        for i in range(number_of_runs):
            print('Run '+str(i+1) +'/'+str(number_of_runs))
            ms.append(run_bare(decouple,potential,J,number_of_drunkards,number_of_cycles,number_to_cut)[0])
        ms.sort()
        ms = np.array(ms)
        print('mean m')
        print(np.average(ms))
        print('standard deviation')
        print(np.std(ms))
        plt.hist(ms)
        plt.xlabel("Results of simulations")
        plt.ylabel("Frequency")
        plt.show()

if input('Run Seperate tests? (Y/N) ')== 'Y':
    run('Energy level 1 of 1 dimentional infinite square well',True,one_d_inf_sqare_well_E1)
    run('Energy level 2 of 1 dimentional infinite square well',True,one_d_inf_sqare_well_E2)
    run('Energy level 1 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E1)
    run('Energy level 2 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E2)
    run('Energy level 3 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E3)
    run('Energy level 1 of SHO',False,one_d_SHO_E1)
    run('Energy level 2 of SHO',False,one_d_SHO_E2)
    run('Energy level 1 of 2D SHO',False,two_d_SHO_E1)
    run('Energy level 2 of 2D SHO',False,two_d_SHO_E2)
    run('Energy level 3 of 2D SHO',False,two_d_SHO_E3)
    run('Energy level 1 of Hydrogen',False,hydrogen_E1)

if input('Run entire tests? (Y/N) ')== 'Y':
    run_generation('Energy level 1 of 1 dimentional infinite square well',True,one_d_inf_sqare_well_E1)
    run_generation('Energy level 2 of 1 dimentional infinite square well',True,one_d_inf_sqare_well_E2)
    run_generation('Energy level 1 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E1)
    run_generation('Energy level 2 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E2)
    run_generation('Energy level 3 of 2 dimentional infinite circle well',True,two_d_inf_cyrcle_well_E3)
    run_generation('Energy level 1 of SHO',False,one_d_SHO_E1)
    run_generation('Energy level 2 of SHO',False,one_d_SHO_E2)
    run_generation('Energy level 1 of 2D SHO',False,two_d_SHO_E1)
    run_generation('Energy level 2 of 2D SHO',False,two_d_SHO_E2)
    run_generation('Energy level 3 of 2D SHO',False,two_d_SHO_E3)
    run_generation('Energy level 1 of Hydrogen',False,hydrogen_E1)

if input('Run heatmaps? (Y/N) ')== 'Y':
    run_heatmap('Energy level 1 of 1 dimentional infinite square well',one_d_inf_sqare_well_E1)
    run_heatmap('Energy level 2 of 1 dimentional infinite square well',one_d_inf_sqare_well_E2)
    run_heatmap('Energy level 1 of 2 dimentional infinite circle well',two_d_inf_cyrcle_well_E1)
    run_heatmap('Energy level 2 of 2 dimentional infinite circle well',two_d_inf_cyrcle_well_E2)
    run_heatmap('Energy level 3 of 2 dimentional infinite circle well',two_d_inf_cyrcle_well_E3)
    run_heatmap('Energy level 1 of SHO',one_d_SHO_E1)
    run_heatmap('Energy level 2 of SHO',one_d_SHO_E2)
    run_heatmap('Energy level 1 of 2D SHO',two_d_SHO_E1)
    run_heatmap('Energy level 2 of 2D SHO',two_d_SHO_E2)
    run_heatmap('Energy level 3 of 2D SHO',two_d_SHO_E3)
