from GMMsample import GMMsample
from GMMinv import GMMinv
from BinarySearch import BinarySearch
from PushForward import PushForward
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import erf


#### Part 1
gmm ={'pi':0.5,'mu':[-1,1],'sigma':[0.5,0.5]}
n = 1000
b = 50
num_bins = b
X = GMMsample(gmm, n, b)

#### Part 2
U = GMMinv(X, gmm, b)
plt.figure()
n, bins, patches = plt.hist(U, num_bins,density=True, facecolor='blue', alpha=0.7)
plt.xlabel('U')
#### part 3
z = np.linspace(-5,5,101)
UU = np.zeros((len(z),1))
for j in range(len(z)):
    UU[j]  = 1/2 * (1+erf(z[j]/np.sqrt(2)))   
lb = -100
ub = 100
maxiter = 100
tol = 10**-7
XX = BinarySearch(gmm, UU, lb, ub, maxiter, tol)
plt.figure()
plt.plot(z,XX,  linewidth = 2)
plt.xlabel('z')
plt.ylabel("T(z)=Q(Phi(z))")
plt.figure()
plt.plot(z,UU,  linewidth = 2)
plt.xlabel('z')
plt.ylabel("Phi(z)")
plt.figure()
plt.plot(XX,UU,  linewidth = 2)
plt.xlabel('T(z)=Q(Phi(z))')
plt.ylabel("Phi(z)=F(Q(Phi(z)))")
#### Part 4
mean2 = np.matrix([0])
covariance2 = np.matrix([1])
L2 = np.linalg.cholesky(covariance2)
Y2 = np.random.normal(size=(1, 1000))
X2 = L2.dot(Y2) + mean2
Z = X2.T
X_t = PushForward (Z,gmm)
#### Part 5
U_t = GMMinv(X_t, gmm, b)
plt.figure()
n, bins, patches = plt.hist(U_t, num_bins,density=True, facecolor='blue', alpha=0.7)
plt.xlabel('U_telde')
