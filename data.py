#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


train = pd.read_csv("train.csv")


# In[4]:


train.head()


# In[6]:


train.tail()


# In[8]:


train.shape


# In[10]:


test=pd.read_csv("test.csv")
sample=pd.read_csv("sample.csv")


# In[11]:


test.shape


# In[14]:


test.head()


# In[15]:


test.head(10)


# In[16]:


sample.head()


# In[17]:


sample = pd.read_csv("sample.csv",header=None)


# In[18]:


sample.head()


# In[ ]:




