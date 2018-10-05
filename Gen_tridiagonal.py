
# coding: utf-8

# In[1]:

import numpy as np
from Generate_A_from_sparsity import generate_A


# In[2]:

def sparsity_pattern(n = 30):
    sparsity = np.zeros(shape = (n*(n-1)/2, ))
    for i in range(n-1):
        sparsity[(i+1)*(i+2)/2 - 1] = 1
#     for i in xrange(1,n):
# #     for j in range(i):
#         print sparsity[i*(i-1)/2: i*(i-1)/2+i]
#         print "\n"
    return sparsity


# In[3]:

def tridiagonal_theta(n):
    sparsity = sparsity_pattern(n)
    A = generate_A(sparsity, n)
    theta = np.dot(A.T, A)
    return theta, sparsity


# In[4]:

# tridiagonal_theta(10)


# In[ ]:




# In[ ]:



