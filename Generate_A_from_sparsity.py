
# coding: utf-8

# In[4]:

import numpy as np
import numpy.random as rand
from scipy.linalg import null_space as null
import numpy.linalg as la


# In[5]:

def perp_vec(vecs):
    null1 = null(vecs.T)
    m = null1.shape[1]
    rand_coeff = rand.normal(size = [m,1])
    perp = np.dot(null1,rand_coeff)
    perp = perp/la.norm(perp)
    return perp


# In[8]:

#Generate A such that A.T A has the given sparsity structure. This is obtained by 
#choosing columns of A such that i,j columns are orthogonal wherever we need 0 in 
#theta.
#lower triangular off diagonal raster scan style binary for sparsity pattern input
def generate_A(sparsity, n = 30):
    A = np.ones(shape = [n,n])
    A = A/n**0.5
    v = np.zeros(shape = [n])
    v[0] = 1
    count_empty_vec = 0
    for i in xrange(1,n):
        vecs = []
        start_ind = i*(i-1)/2
        for j in range(i):
            if sparsity[start_ind + j] == 0: 
                vecs.append(A[:,j])
        vecs = np.matrix(vecs)
        if vecs.shape[1] == 0:
            A[:,i] = 0.1*A[:,count_empty_vec] + 0.9*v
            count_empty_vec = count_empty_vec + 1
        else:
            choose = 0
            perp = perp_vec(vecs.T)
            perp = np.reshape(perp,n)
            A[:,i] = perp
    return A 


# In[ ]:



