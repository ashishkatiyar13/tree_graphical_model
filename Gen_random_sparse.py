
# coding: utf-8

# In[1]:

import numpy as np
import numpy.random as rand
# from numpy.linalg import svd
# import scipy
# import scipy.linalg as la
# from scipy.linalg import null_space as null
# import scipy.stats as stats
# import scipy.sparse as sparse
# import scipy.sparse.linalg as spla
# from scipy.sparse import csr_matrix as csr
# from scipy.sparse import identity as eye
# import matplotlib.pyplot as plt
# from scipy.optimize import fsolve
# import math
from Generate_A_from_sparsity import generate_A


# In[2]:

# Generate random sparsity pattern. Represent using 1-D array of size n(n-1)/2 for all the off diagonal elements
# k is the density of zeros
def sparsity_pattern(n = 30, k = 0.8):
    rand.seed(0)
    sparsity = rand.choice([0,1], size = (n*(n-1)/2, ), p = (k, 1-k))
#     for i in xrange(1,n):
# #         for j in range(i):
#         print sparsity[i*(i-1)/2: i*(i-1)/2+i]
#         print "\n"
    return sparsity


# In[3]:

#vecs is a n x k matrix with each column being a vector
#perp_vec returns a vector perpendicular to the k vectors in  perp_vec
# def perp_vec(vecs):
# #     print i
#     null1 = null(vecs.T)
#     m = null1.shape[1]
#     rand_coeff = rand.normal(size = [m,1])
#     return np.dot(null1,rand_coeff)


# In[4]:


# def generate_A(sparsity, n = 30):
#     A = np.ones(shape = [n,n])
#     A = A/n**0.5
#     v = np.zeros(shape = [n])
#     v[0] = 1
#     count_empty_vec = 0
#     for i in xrange(1,n):
#         vecs = []
#         start_ind = i*(i-1)/2
#         for j in range(i):
#             if sparsity[start_ind + j] == 0: 
#                 vecs.append(A[:,j])
#         vecs = np.matrix(vecs)
#         if vecs.shape[1] == 0:
#             A[:,i] = 0.1*A[:,count_empty_vec] + 0.9*v
#             count_empty_vec = count_empty_vec + 1
#         else:
#             choose = 0
#             perp = perp_vec(vecs.T)
#             perp = np.reshape(perp,n)
#             A[:,i] = perp
#     return A 


# In[5]:

def random_sparsity_theta(n = 30, k = 0.8):
    sparsity = sparsity_pattern(n,k)
    A = generate_A(sparsity, n)
#     print A
    theta = np.dot(A.T, A)
#     print theta
    return theta, sparsity


# In[6]:

# random_sparsity_theta(15, 0.8)


# In[ ]:




# In[ ]:



