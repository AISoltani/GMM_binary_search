import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf

def BinarySearch (gmm, U, LB, UB, maxiter, tol):
    num_bins = 50
    XX = np.zeros((len(U),1))
    for j in range(len(U)):
        lb = LB
        ub = UB
        F_lb = gmm['pi'] * 1/2 * (1+erf((lb-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((lb-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        F_ub = gmm['pi'] * 1/2 * (1+erf((ub-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((ub-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        u  = U[j]     
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
    return XX


# def BinarySearch (U, LB, UB, maxiter, tol):
#     XX = np.zeros((len(U),1))
#     for j in range(len(U)):
#         lb = LB
#         ub = UB
#         F_lb = F(lb)
#         F_ub = F(ub)
#         u  = U[j]     
#         while F_lb > u:
#             ub = lb
#             lb = lb/2
#             F_lb = F(lb)
#         while F_ub < u:
#             lb = ub
#             ub = ub*2
#             F_ub = F(ub)
#         for i in range(maxiter):
#             xx = (lb+ub)/2
#             t = F(xx)
#             print(i)
#             if t>u :
#                 ub = xx
#             else: 
#                 lb = xx
#             XX[j]=xx
#             if np.abs(t - u)<= tol:
#                 break        
#     plt.figure()
#     plt.plot(z,XX,  linewidth = 2)
#     plt.figure()
#     n, bins, patches = plt.hist(XX, num_bins, facecolor='green', alpha=0.7)
#     return xx
