
# coding: utf-8

# In[7]:


import pandas as panda
df = panda.read_excel("stocksf081a85.xlsx")


# In[9]:


df


# In[11]:


df.to_csv("stocksinfo.csv", sep=",", encoding="utf-8")


# In[13]:


df2 = panda.read_csv("prices763fefc.csv")


# In[15]:


df2


# In[16]:


df2.to_csv("histodataforindex.csv",sep=',',encoding='utf-8')

