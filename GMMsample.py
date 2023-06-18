import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf

def GMMsample (gmm,n,b):

    num_bins = b
    s = np.random.uniform(0,1,n)
    pi = gmm['pi']
    idx0 = np.where(s<pi)
    idx1 = np.where(s>=pi)
    N = np.sum(s<pi)
    X = np.zeros((n,1))
    ###
    mean0 = np.matrix(gmm['mu'][0])
    covariance0 = np.matrix([(gmm['sigma'][0])**2])
    L0 = np.linalg.cholesky(covariance0)
    Y0 = np.random.normal(size=(1, N))
    X0 = L0.dot(Y0) + mean0
    ###
    mean1 = np.matrix(gmm['mu'][1])
    covariance1 = np.matrix([(gmm['sigma'][1])**2])
    L1 = np.linalg.cholesky(covariance1)
    Y1 = np.random.normal(size=(1, n-N))
    X1 = L1.dot(Y1) + mean1
    X[idx0] = X0.T
    X[idx1] = X1.T
    
    
    plt.figure()
    n, bins, patches = plt.hist(X0.T, num_bins,density=True, facecolor='blue', alpha=0.7)
    n, bins, patches = plt.hist(X1.T, num_bins,density=True, facecolor='red', alpha=0.7)
    plt.legend()
    plt.xlabel('x')
    plt.show()
    
    plt.figure()
    n, bins, patches = plt.hist(X, num_bins,density=True, facecolor='green', alpha=0.7)
    plt.legend()
    plt.xlabel('x')
    plt.title(" Gaussian mixture model")
    plt.show()

    return X