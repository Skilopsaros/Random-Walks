import math as maths

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
