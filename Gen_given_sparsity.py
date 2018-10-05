
# coding: utf-8

# In[1]:

import numpy as np
import numpy.random as rand
from Generate_A_from_sparsity import generate_A


# In[14]:

"""
Sparsity -> n(n-1)/2 length vector specifying the required zero pattern in a raster scan manner.
"""
def specific_sparsity_theta(n = 30, sparsity = []):
#     sparsity = sparsity_pattern(n,k)
    A = generate_A(sparsity, n)
#     print A
    theta = np.dot(A.T, A)
#     print theta
    return theta, sparsity


# In[ ]:



