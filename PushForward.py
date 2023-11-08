import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf

def PushForward (Z,gmm):
    lb = -100
    ub = 100
    maxiter = 500
    tol = 1e-8
    b = 50
    num_bins = b
    XX = np.zeros((len(Z),1))
    for j in range(len(Z)):
        lb = -100
        ub = 100
        F_lb = gmm['pi'] * 1/2 * (1+erf((lb-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((lb-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        F_ub = gmm['pi'] * 1/2 * (1+erf((ub-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((ub-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        u  = 1/2 * (1+erf(Z[j]/np.sqrt(2)))     
        while F_lb > u:
            ub = lb
            lb = lb/2
            F_lb = gmm['pi'] * 1/2 * (1+erf((lb-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((lb-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        while F_ub < u:
            lb = ub
            ub = ub*2
            F_ub = gmm['pi'] * 1/2 * (1+erf((ub-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((ub-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        for i in range(maxiter):
            xx = (lb+ub)/2
            t = gmm['pi'] * 1/2 * (1+erf((xx-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((xx-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
            if t>u :
                ub = xx
            else: 
                lb = xx
            XX[j]=xx
            if np.abs(t - u)<= tol:
                break        

    
    plt.figure()
    n, bins, patches = plt.hist(XX, num_bins,density=True, facecolor='green', alpha=0.7) 
    plt.xlabel('x_tilde = T(z)')
    return XX

