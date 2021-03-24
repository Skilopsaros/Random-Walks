import drunkard as drk
import matplotlib.pyplot as plt
import slope as slp
import math as maths
import potentials as pnt
import numpy as np
import copy

E1 = 0
E2 = 0
E3 = 0
while input('Type  Y to run Energy level 1 of one dimentional infinite square well ')=='Y':
    J = int(input('input the value of J: '))
    number_of_drunkards = int(input('input the number of drunkards: '))
    number_of_runs = int(input('input the number of runs: '))
    number_to_cut = int(input('input the number to cut: '))
    decouple = (input('do you want to decouple? (Y/N)'))
    if decouple == 'Y':
        decouple = True
    else:
        decouple = False

    ks, dead = drk.simulation(pnt.one_d_inf_sqare_well_E1, J, number_of_drunkards, number_of_runs)
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
    print(-8*m*J*J/pow(maths.pi,2))
    print(-8*am*J*J/pow(maths.pi,2))


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

while input('Type  Y to run Energy level 2 of one dimentional infinite square well ')=='Y':
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

while input('Type  Y to run Energy level 1 of two dimentional infinite circle well ')=='Y':
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

while input('Type  Y to run Energy level 2 of two dimentional infinite circle well ')=='Y':
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


while input('Type  Y to run Energy level 3 of two dimentional infinite circle well ')=='Y':
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
