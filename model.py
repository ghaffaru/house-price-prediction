#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Predicting the price of a house
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# In[2]:


house = pd.read_csv('home_data.csv')


# In[3]:


house.head()


# In[4]:


house.tail()


# In[5]:


house.info()


# In[6]:


house.describe()


# In[7]:


plt.figure(figsize=(10,6))
plt.scatter(house.sqft_living,house.price)
plt.xlabel('Sqft')
plt.ylabel('Price')


# In[8]:


#getting line of best fit
sns.lmplot('sqft_living','price', data=house)


# In[9]:


sns.heatmap(house.corr())


# In[10]:


sns.distplot(house.price, color='red')


# In[11]:


house.info()


# In[12]:


features = house[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','sqft_above','sqft_lot15','yr_built','condition',
                 'zipcode']]

labels = house['price']


# In[13]:


from sklearn.model_selection import train_test_split


# In[14]:


#training and testing, 75% for training, 25
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.1, random_state=7)


# In[15]:


#verify size of feature training set

print (features_train.shape)


# In[16]:


#verify size of label training set
print(labels_train.shape)


# In[17]:


print(features_test.shape)


# In[18]:


print(labels_test.shape)


# In[19]:


from sklearn.linear_model import LinearRegression


# In[20]:


model = LinearRegression()


# In[21]:


model.fit(features_train,labels_train)


# In[22]:


prediction = model.predict(features_test)


# In[34]:


model.predict(features_test)[1]


# In[32]:


features_test


# In[43]:


label_actual = pd.DataFrame(labels_test)


# In[46]:


label_actual.price
# print(labels_test)


# In[38]:


model.predict([features_test.loc[12640]])


# In[40]:


from sklearn.metrics import mean_squared_error


# In[52]:


labels_test


# In[56]:


from math import sqrt
sqrt(mean_squared_error(labels_test, model.predict(features_test)))


# In[54]
test_predict = pd.DataFrame({
    "bedrooms" : 5,
    "bathrooms" : 2,
    "sqft_living" : 1000,
    "sqft_lot" : 20456,
    "floors" : 2.0,
    "sqft_above" : 1480,
    "sqft_lot15" : 6005,
    "yr_built" : 1996,
    "condition" : 4,
    "zipcode" : 98064
},index=[0])

# print(str(model.predict(test_predict)).strip('[]'))

#save the model
#serialize model to json
model_json = model.to_json()
with open('model.json','w') as json_file:
    json_file.write(model_json)

#save weights to HDF5
model.save_weights('model.h5')