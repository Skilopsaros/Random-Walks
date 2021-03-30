import math as maths
import random

def one_d_inf_sqare_well_E1(return_dimensions=False, coordinates = [0], j=8): #this is the first potential
    if return_dimensions:
        return(1) #the one dimentional infinite square well has one dimension
    return(abs(coordinates[0]) < j) #keep them alive only if their coordinate is lower than J

def one_d_inf_sqare_well_E2(return_dimensions=False, coordinates=[0], j=8):
    if return_dimensions:
        return(1)
    if 0==coordinates[0]:
        return(False)
    return(abs(coordinates[0]) < j)

def two_d_inf_cyrcle_well_E1(return_dimensions=False, coordinates=[0,0], j=8):
    if return_dimensions:
        return(2)
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def two_d_inf_cyrcle_well_E2(return_dimensions=False, coordinates=[0,0], j=8):
    if return_dimensions:
        return(2)
    if 0==coordinates[0]:
        return(False)
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def two_d_inf_cyrcle_well_E3(return_dimensions=False, coordinates=[0,0], j=8):
    if return_dimensions:
        return(2)
    if 0==coordinates[0] or 0==coordinates[1]:
        return(False)
    return(pow(abs(coordinates[0]),2)+pow(abs(coordinates[1]),2) < pow(j,2))

def one_d_SHO_E1(return_dimensions=False, coordinates = [0], j=8):
    if return_dimensions:
        return(1)
    return(random.random()>pow(coordinates[0],2)/(2*j*j))
