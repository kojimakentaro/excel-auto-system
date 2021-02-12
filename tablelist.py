#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', '')


# In[23]:


train = pd.read_csv("train.csv")


# In[24]:


train.head()


# In[25]:


train.describe()


# In[26]:


train.info()


# In[27]:


train["y"].mean()


# In[28]:


train["y"].median()


# In[29]:


train[train["y"]>=150]


# In[30]:


train[train["y"]<=40]


# In[31]:


train[train["week"]=="月"]


# In[32]:


train[train["week"]=="火"].sort_values(by="y")


# In[33]:


train[train["week"]=="火"].sort_values(by="y",ascending=False)


# In[34]:


train[train["week"]=="月"]["y"].mean()


# In[36]:


train.describe()


# In[38]:


train["temperature"].mean()


# In[40]:


train[train["temperature"]>=train["temperature"].mean()]


# In[42]:


train[["y","week","temperature"]]


# In[ ]:




