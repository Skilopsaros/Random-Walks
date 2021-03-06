import math as maths
import random
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
