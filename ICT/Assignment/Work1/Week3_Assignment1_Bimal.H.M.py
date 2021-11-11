#!/usr/bin/env python
# coding: utf-8

# # Week 3 : Assignment 1 - Bimal H M

# ## Python Analysis on IRIS Dataset

# ### STEP 1 : Importing all Necessary Libraries in to Notebook

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Q1 : Reading the Data set in to Notebook 

# In[2]:


iris = pd.read_excel('iris.xls')


# ### Q2 : Displaying the Data set 

# #### A) Displaying the whole Dataset

# In[3]:


iris


# #### B) Displaying/Checking the column names

# In[4]:


iris.columns


# #### C) Displaying Columns with info

# In[5]:


iris.info()


# ### Q3 : Calculating the mean of each column of Dataset 

# In[6]:


np.mean(iris,0)


# ### Q4 : Checking for the null values present in the Dataset

# In[7]:


iris.isnull().sum()


# ### Q5 : Performing Meaningful Visualizations 

# #### A) Count Plot Of Classification Column

# In[8]:


plt.title("Count Plot Of Clasification")
CP = sns.countplot(x = 'Classification', data = iris)
for i in CP.patches:
    CP.annotate(i.get_height() , (i.get_x()+0.4, i.get_height()-10))   #To Display count in graph
plt.show()


# #### B) Box Plot of SL, SW, PL, PW 

# In[9]:


def BoxP(y):
    sns.boxplot(x = 'Classification', y = y, data = iris)

plt.figure(figsize = (12,12))
plt.title("OK")
#Now Separately Ploting Each Subplot of SL,Sw,PL,PW
plt.subplot(2,2,1)
BoxP('SL')
plt.gca().set_title('Box Plot Of SL')
  
plt.subplot(2,2,2)
BoxP('SW')
plt.gca().set_title('Box Plot Of SW')
  
plt.subplot(2,2,3)
BoxP('PL')
plt.gca().set_title('Box Plot Of PL')
  
plt.subplot(2,2,4)
BoxP('PW')
plt.gca().set_title('Box Plot Of PW')
  
plt.show()

    


# #### C) Pair Plot With Respect to Classification  

# In[10]:


PP = sns.pairplot(iris,hue = 'Classification')
PP.fig.set_size_inches(11,11)
PP.fig.suptitle("Pair Plot Based On Classification",y = 1.06)
plt.show()


# #### D) Heatmap of Dataset

# In[11]:


HM = sns.heatmap(iris.corr(),annot = True)
HM.set_title("Heat Map of DataSet",y = 1.01)
plt.show()


# In[ ]:




