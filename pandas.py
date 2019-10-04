#!/usr/bin/env python
# coding: utf-8

# # What is pandas-python? Introduction and Installation

# Pandas is python module that makes data science easy and effective

# Weather dataset

# Questions?
# 
# 1. What was the maximum temparature in new york in the month of january?
# 
# 2. On which days did it rains?
# 
# 3. What was the average speed of wind during the month?
# 

# First we will see in python code

# In[27]:


# now we will see in pandas 
import pandas as pd
df = pd.read_csv("C://Users/Apolloniann/Desktop/data science/7.1/nyc_weather.csv")
df.tail()


# In[6]:


from google.colab import drive
drive.mount('https://drive.google.com/file/d/1KxwFsL6IF7OD_XN28kjxl0-amnELIhZ8/view?usp=sharing')


# In[ ]:


#get the maximum temparature 
df['Temperature'].max()


# In[25]:


#to know which day it rains
df['EST'][df['Events'] == 'Rain']


# In[21]:


#3. average wind speed
df['WindSpeedMPH'].mean()


# # Installation

# 
# pip3 install pandas
