#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
car=pd.read_csv('Quikrcars.csv')


# In[2]:


car


# In[3]:


car.shape


# In[4]:


car.info()


# # we have first to clean the data

# In[5]:


#first to check quality of data
car['Year'].unique()


# # price object to int
# ###car['Price'].unique()
# ###car['Kms_driven'].unique() #we have kms with kms driven ...also change from object to int..remove ##nan value
# ###car['Fuel_type'].unique()
# ###we have to keep first 3 words of the name
# 

# # cleaning

# In[6]:


backup=car.copy()


# In[7]:


#car['Year'].st.isnumeric()# if data types is object type to check it whether 
#which one is integer and which one is object value
car['Year']


# In[8]:


#car['Price'] = car['Price'].str.replace(',','.','')
#car['Price'] = car['Price'].astype(str)
car['Price'] = car['Price'].str.replace(',', '.', regex=False)
car['Price'] = pd.to_numeric(car['Price'], errors='coerce')
car['Price']


# In[9]:


car['Price'] = pd.to_numeric(car['Price'], errors='coerce')
car['Price']


# In[10]:


car['Kms_driven'] = car['Kms_driven'].astype(str)
car['Kms_driven']=car['Kms_driven'].str.split(' ').str.get(0).str.replace(',','').astype(int)
car['Kms_driven']


# In[11]:


car.info()


# In[12]:


car[car['Fuel_type'].isna()]


# In[13]:


#car['Name'] = car['Name'].astype(str)
car['Name'] = car['Name'].str.split().str.slice(0, 3).str.join('')
# slice is using for that to select first
#three words of the name remove other 


# In[14]:


car['Name']


# In[15]:


car


# In[16]:


car.info()


# In[17]:


car.describe()


# In[18]:


#car1=car[car['Price']<8e8].reset_index(drop=True)


# In[19]:


#car1


# In[20]:


car


# In[21]:


car.to_csv('cleaned car.csv')


# # model

# In[22]:


x=car.drop(columns='Price')
y=car['Price']


# In[23]:


x


# In[24]:


y


# In[25]:


print(car['Price'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




