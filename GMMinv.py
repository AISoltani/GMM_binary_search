import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf
def GMMinv(X, gmm, b):
    num_bins = b
    n = X.shape[0]
    F = np.zeros((n,1))
    UU = np.zeros((n,1))
    for i in range(n):
        F[i] = gmm['pi'] * 1/2 * (1+erf((X[i]-(gmm['mu'][0]))/((gmm['sigma'][0])*np.sqrt(2)))) + (1 - gmm['pi']) * 1/2 * (1+erf((X[i]-(gmm['mu'][1]))/((gmm['sigma'][1])*np.sqrt(2))))
        UU[i] = norm.ppf(F[i])
    return UU