#!/usr/bin/env python
# coding: utf-8

# # Investment Competition
# 
# 
# # Some Code

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,1,100)
sr = (2*w+(1-w))/np.sqrt(20*w**2+10*(1-w)**2)

print( w[np.argmax(sr)], np.max(sr) )


# In[ ]:


plt.plot(w,sr)
plt.show()

