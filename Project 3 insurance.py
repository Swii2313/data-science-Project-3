#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("C:\\Users\\DELL\\Downloads\\insurance.csv")


# In[36]:


df.head(10)


# # data preprocessing

# In[5]:


df.isnull().any()


# # EDA

# In[6]:


import seaborn as sns


# In[7]:


tc=df.corr()


# In[8]:


tc


# In[10]:


sns.heatmap(tc)


# In[11]:


sns.pairplot(df)


# In[12]:


df.shape


# # REmoving outliers using IQR ratio

# In[27]:


Q1_df=df.quantile(0.25)
Q3_df=df.quantile(0.75)
IQR=Q3_df-Q1_df
print(IQR)


# In[28]:


lower_bound = Q1_df - 1.5*IQR
upper_bound = Q3_df + 1.5*IQR
#create conditions to isolate the outliers
outliers = df[(df < lower_bound) | (df > upper_bound).any(axis=1)]
df_out.shape


# In[29]:


df_out.columns


# In[30]:


df.isnull().any()


# # Encoding

# In[31]:


from sklearn.preprocessing import LabelEncoder


# In[35]:


df_out['sex']=LabelEncoder().fit_transform(df_out['sex'])


# In[37]:


df_out['smoker']=LabelEncoder().fit_transform(df_out['smoker'])


# In[38]:


df_out['region']=LabelEncoder().fit_transform(df_out['region'])


# In[39]:


df_out.head()


# In[40]:


df_out.isnull().sum()


# # Define x and y

# In[45]:


df_out.columns


# In[46]:


x=df_out[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]


# In[47]:


y=df_out[['charges']]


# # Model development

# In[48]:


from sklearn.model_selection import train_test_split


# In[49]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[50]:


x_train.head()


# In[52]:


from sklearn import tree


# In[54]:


model=tree.DecisionTreeRegressor()


# In[55]:


model.fit(x_train,y_train)


# In[57]:


y_pred=model.predict(x_test)


# In[58]:


y_pred


# In[60]:


from sklearn import metrics
import numpy as np


# In[62]:


print(metrics.mean_absolute_error(y_test,y_pred))
print(metrics.mean_absolute_error(y_test,y_pred))
print(np.sqrt(metrics.mean_absolute_error(y_test,y_pred)))


# In[ ]:




