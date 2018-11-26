# get_r.py

import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    assert (alpha >= 0 and alpha < 1), "alpha outside (0,1) range"
    assert (delta >= 0 and delta < 1), "delta outside (0,1) range"
    assert Z > 0, "Z is not strictly positive"
    count = 0

    if np.isscalar(K) and np.isscalar(L):
        assert K > 0, "K is not strictly positive"
        assert L > 0, "L is not strictly positive"
        r = alpha*Z*((L/K)**(1 - alpha)) - delta
        return r

    assert np.all([x > 0 for x in np.nditer(K)]), "K requires strictly positive value(s)"
    assert np.all([x > 0 for x in np.nditer(L)]), "L requires strictly positive value(s)"    
    #r = []

    #for i, values in enumerate(K):
        #r.append(alpha*Z*((L[i]/values)**(1 - alpha)) - delta)
    r = alpha*Z*((L/K)**(1 - alpha)) - delta


    return r