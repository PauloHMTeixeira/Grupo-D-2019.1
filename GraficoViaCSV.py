#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy import genfromtxt
import matplotlib.pyplot as plt
per_data=genfromtxt('untitled.csv',delimiter=',')
plt.xlabel ('x stuff')
plt.ylabel ('y stuff')
plt.title('my test result')
plt.show()
plt.plot(per_data)


# In[ ]:




