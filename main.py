import drunkard as drk
import matplotlib.pyplot as plt
import slope as slp
import math as maths
import potentials as pnt
import numpy as np
import copy
# This is the program you are running
# You can run each energy level many times
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

        ks, dead = drk.simulation(potential, J, number_of_drunkards, number_of_cycles) #This runs the simulation. To see how this runs, go to drunkard.py
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
        m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k)) #this is a function to find the best fit slope. It works. Find it in slope.py. I tested it with scipy stuff too.
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

def run_bare(decouple,potential,J,number_of_drunkards,number_of_cycles,number_to_cut):
    ks, dead = drk.simulation(potential, J, number_of_drunkards, number_of_cycles)
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
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    return(potential(j=J, return_results=True, m=m, am=am))

def run_generation(text,ask_decouple,potential):
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
        plt.show()

if input('Run Seperate tests? (Y/N) ')== 'Y':
    run('Energy level 1 of 1 dimentional infinite square well',True,pnt.one_d_inf_sqare_well_E1)
    run('Energy level 2 of 1 dimentional infinite square well',True,pnt.one_d_inf_sqare_well_E2)
    run('Energy level 1 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E1)
    run('Energy level 2 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E2)
    run('Energy level 3 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E3)
    run('Energy level 1 of SHO',False,pnt.one_d_SHO_E1)
    run('Energy level 2 of SHO',False,pnt.one_d_SHO_E2)
    run('Energy level 1 of Hydrogen',False,pnt.hydrogen_E1)

if input('Run entire tests? (Y/N) ')== 'Y':
    run_generation('Energy level 1 of 1 dimentional infinite square well',True,pnt.one_d_inf_sqare_well_E1)
    run_generation('Energy level 2 of 1 dimentional infinite square well',True,pnt.one_d_inf_sqare_well_E2)
    run_generation('Energy level 1 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E1)
    run_generation('Energy level 2 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E2)
    run_generation('Energy level 3 of 2 dimentional infinite circle well',True,pnt.two_d_inf_cyrcle_well_E3)
    run_generation('Energy level 1 of SHO',False,pnt.one_d_SHO_E1)
    run_generation('Energy level 2 of SHO',False,pnt.one_d_SHO_E2)
    run_generation('Energy level 1 of Hydrogen',False,pnt.hydrogen_E1)
