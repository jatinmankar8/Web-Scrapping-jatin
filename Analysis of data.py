#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("RealEstate.csv")


# In[2]:


data


# ## Below is plot for comparing prices for different locality

# In[11]:


plt.figure(figsize=(30,6))
plt.plot(data['Address'], data['Plot Price'])


# ## Below is plot for comparing the Locality/Town with other towns

# In[3]:


price_avg = data.groupby(['Locality']).mean()
price_avg


# In[4]:


plt.figure(figsize=(25,4))
plt.plot(price_avg.index, price_avg['Bed Info'])


# In[5]:


price_avg.index


# In[6]:


plt.pie(price_avg['Plot Price'], labels=price_avg.index)


# In[ ]:




