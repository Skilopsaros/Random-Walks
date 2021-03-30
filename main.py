import drunkard as drk
import matplotlib.pyplot as plt
import slope as slp
import math as maths
import potentials as pnt
import numpy as np
import copy
# This is the program you are running
# You can run each energy level many times
while input('Run Energy level 1 of one dimentional infinite square well? (Y/N) ')=='Y': # This is for running the 1 dimensional infinite square well, first energy level
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N)')) # All of these are just inputs to see the parameters you are running with
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.one_d_inf_sqare_well_E1, J, number_of_drunkards, number_of_runs) #This runs the simulation. To see how this runs, go to drunkard.py
    ks_copy=copy.deepcopy(ks) #copying things to make sure we don't loose the original data when we alter it
    for i in range(number_to_cut): #this cuts the first few steps, because the distribution of drunkards is not yet stable
        del(ks[0])
    xs = range(len(ks))
    k = np.array(ks)
    if decouple: # to decouple we only need every other point
        ks_decoupled = ks[::2] #use every second value of number of surviving drunkards
        xs_decoupled = xs[::2] # this is done to give us the right result
        xs = xs_decoupled # use the decoupled values
        k = np.array(ks_decoupled)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k)) #this is a function to find the best fit slope. It works. Find it in slope.py. I tested it with scipy stuff too.
    print('This is the value of the Energy divided by pi squared and multiplied by 8, in units where hbar squared over ma^2 is 1')
    print('to make a long story short, we expect this number to be 1')
    print(-8*m*J*J/pow(maths.pi,2))
    print('and this is the error of the above number')
    print(-8*am*J*J/pow(maths.pi,2)) #this error is too small


    plt.plot(range(len(dead)),dead) #plot how many died each turn
    plt.show()
    plt.clf()
    plt.subplot(1,2,1) #plot the survivng number every turn
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2) #plot the log of that with a fit
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()

while input('Run Energy level 2 of one dimentional infinite square well? (Y/N) ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N)'))
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.one_d_inf_sqare_well_E2, J, number_of_drunkards, number_of_runs, starting_points = [[-J/2],[J/2]])
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    ks_decoupled = ks[::2]
    xs = range(len(ks))
    xs_decoupled = xs[::2]
    k = np.array(ks)
    if decouple:
        xs = xs_decoupled
        k = np.array(ks_decoupled)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    print(-2*m*J*J/pow(maths.pi,2))
    print(-2*am*J*J/pow(maths.pi,2))


    plt.plot(range(len(dead)),dead)
    plt.show()
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2)
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()

while input('Run Energy level 1 of two dimentional infinite circle well? (Y/N) ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N)'))
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.two_d_inf_cyrcle_well_E1, J, number_of_drunkards, number_of_runs)
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    ks_decoupled = ks[::2]
    xs = range(len(ks))
    xs_decoupled = xs[::2]
    k = np.array(ks)
    if decouple:
        xs = xs_decoupled
        k = np.array(ks_decoupled)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    print(-2*m*J*J/pow(maths.pi,2))
    print(-2*am*J*J/pow(maths.pi,2))


    plt.plot(range(len(dead)),dead)
    plt.show()
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2)
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()

while input('Run Energy level 2 of two dimentional infinite circle well? (Y/N) ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N) '))
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.two_d_inf_cyrcle_well_E2, J, number_of_drunkards, number_of_runs, starting_points = [[-J/2,0],[J/2,0]])
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    ks_decoupled = ks[::2]
    xs = range(len(ks))
    xs_decoupled = xs[::2]
    k = np.array(ks)
    if decouple:
        xs = xs_decoupled
        k = np.array(ks_decoupled)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    print(-2*m*J*J/pow(maths.pi,2))
    print(-2*am*J*J/pow(maths.pi,2))


    plt.plot(range(len(dead)),dead)
    plt.show()
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2)
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()


while input('Run Energy level 3 of two dimentional infinite circle well? (Y/N) ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N) '))
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.two_d_inf_cyrcle_well_E3, J, number_of_drunkards, number_of_runs, starting_points = [[-J/2,-J/2],[J/2,-J/2],[-J/2,J/2],[J/2,J/2]])
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    ks_decoupled = ks[::2]
    xs = range(len(ks))
    xs_decoupled = xs[::2]
    k = np.array(ks)
    if decouple:
        xs = xs_decoupled
        k = np.array(ks_decoupled)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    print(-2*m*J*J/pow(maths.pi,2))
    print(-2*am*J*J/pow(maths.pi,2))


    plt.plot(range(len(dead)),dead)
    plt.show()
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2)
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()


while input('Run Energy level 1 of SHO? (Y/N) ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))

    ks, dead = drk.simulation(pnt.one_d_SHO_E1, J, number_of_drunkards, number_of_runs)
    ks_copy=copy.deepcopy(ks)
    for i in range(number_to_cut):
        del(ks[0])
    xs = range(len(ks))
    k = np.array(ks)
    m, c, am, ac = slp.best_fit_slope_and_intercept(xs,np.log(k))
    print(-m*J)
    print(am)


    plt.plot(range(len(dead)),dead)
    plt.show()
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(range(len(ks_copy)),ks_copy)
    plt.subplot(1,2,2)
    plt.scatter(xs,np.log(k), s=1, marker='x')
    plt.plot([xs[0],xs[len(xs)-1]],[(m*xs[0]+c),(m*xs[len(xs)-1]+c)])
    plt.show()
    plt.clf()
