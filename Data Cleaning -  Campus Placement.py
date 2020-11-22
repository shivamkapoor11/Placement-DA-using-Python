#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning with Python

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[120]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('Placements.csv')


# In[5]:


df.head(3)


# # lets check the columns and their data types

# In[20]:


df.info()


# In[ ]:


# Heatmap below shows the area where the null value exists. We can see Column Salary, X & Y have the null values.


# In[18]:


sns.heatmap(df.isnull(),yticklabels = False,cbar = False,cmap = 'Blues')
plt.figure(figsize = (16,8))


# In[ ]:


#Total Null Values by columns 


# In[8]:


df.isnull().sum()


# In[23]:


# dropping unwanted columns like X and Y


# In[31]:


to_drop = ['X','Y']


# In[32]:


df.drop(columns = to_drop, inplace = True)


# In[27]:


df.head(2)


# In[34]:


df.drop(columns = 'sl_no', inplace = True)


# In[35]:


# Renaming columns


# In[37]:


df.columns = ['Gender','Senior Secondary %','Senior Secondary Board','Higher Secondary %','Higher Secondary Board','Higher Secondary Stream','Graduation %','Graduation Degree','Work Experience','Etest','MBA Stream','MBA %','Status','Salary']


# In[39]:


df.head(2)


# In[41]:


# Dealing with Null Values - As there are values in Salary column and it is a numerical column, we will take mean of other values


# In[46]:


df['Salary'] = df['Salary'].replace(np.NaN,df['Salary'].mean())


# In[47]:


# Changing the datatype of numerical column like Salary from float to int


# In[50]:


df['Salary'] = df['Salary'].astype(int)


# In[51]:


df.head()


# In[52]:


# Editing the data in dataframe


# In[55]:


df['Gender'] = df['Gender'].replace('M','Male')


# In[57]:


df['Gender'] = df['Gender'].replace('F','Female')


# In[64]:


df['Graduation Degree'] = df['Graduation Degree'].replace('Sci&Tech','B.Tech')


# In[67]:


df['Graduation Degree'] = df['Graduation Degree'].replace('Comm&Mgmt','B.com')


# In[74]:


df['MBA Stream'] = df['MBA Stream'].replace('Mkt&HR','Marketing & HR')


# In[77]:


df['MBA Stream'] = df['MBA Stream'].replace('Mkt&Fin','Marketing & Finance')


# In[78]:


df.head(5)


# In[68]:


# Removing unwanted column


# In[70]:


df.drop(columns = ['Etest'], inplace = True)


# # Data Visualization using Matplotlib & Seaborn

# In[91]:


df['Gender'].value_counts().plot(kind = 'bar', color = 'orange')


# In[109]:


sns.barplot(x = 'Gender', y = 'Salary', data = df, palette = 'Blues_d')


# - It can be seen using Seabborn that Male employees fetched more salary on an average than Female employees.

# In[100]:


sns.set(style = 'whitegrid')
sns.countplot(x = 'Gender', data = df, palette = 'Blues_d')


# - Male employees outnumber the female employees by almost 67 more employees.

# In[122]:


sns.countplot(x = 'Higher Secondary Stream',data = df)


# - The most students belonged to Commerce background, followed by Science & the least belonged to Arts

# In[124]:


sns.countplot(x = 'Graduation Degree', data = df)


# - 140+ students out of 227 belonged to B.com degree which was the highest , followed by B.Tech.

# In[131]:


sns.distplot(df['Salary'], bins = 40)


# - Using the distplot we can conclude that the mean salary fallsin the range of 300000.

# In[132]:


sns.countplot(x = df['MBA Stream'], data = df)


# In[ ]:




