def one_d_inf_sqare_well_E1(return_dimensions=False, coordinates = [0], j=8):

    if return_dimensions:
        return(1)
    return(abs(coordinates[0]) < j)

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
