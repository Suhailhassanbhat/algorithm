#!/usr/bin/env python
# coding: utf-8

# # Executing a linear regression
#purpose: to execute a linear regression on a dataset to see how age, sex, bmi, region, children, smoking affect the cost of insurance.
#Eventually, to figure out what are the best variables to predict insurance cost.

# In[25]:


#import libraries needed for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
import statsmodels.api as sm


# In[9]:


# Read in data that has columns such as age, sex, bmi, insurance cost etc.
data = pd.read_csv('insurance.csv')


# In[10]:


#view our data
data.head(2)


# In[11]:


#what do our columns look like
data.columns


# In[127]:


#number of men who smoke
data[(data['smoker']==1) & (data['sex']==1)].count()


# In[128]:


#number of women who are smokers
data[(data['smoker']==1) & (data['sex']==0)].count()


# # Labelling
# Since three columns have text, we need to convert those into numerals.Importing labelencoder here to convert text into numbers. It labels yes as 1 and no as 0. This code borrowed from https://www.kaggle.com/hely333/eda-regression

# In[129]:


from sklearn.preprocessing import LabelEncoder

#sex
le = LabelEncoder()
le.fit(data.sex.drop_duplicates()) 
data.sex = le.transform(data.sex)
# smoker or not
le.fit(data.smoker.drop_duplicates()) 
data.smoker = le.transform(data.smoker)
#region
le.fit(data.region.drop_duplicates()) 
data.region = le.transform(data.region)


# In[130]:


#let us see if it worked
data.head()


# In[116]:


data['sex'].value_counts()
#our data set has nearly equal count of men and women


# In[118]:


data['smoker'].value_counts()
#we have nearly five times non-smokers versus smokers in this data. Who are they? 


# What is the correlation between charges and independent variables

# In[131]:


data.corr()['charges'].sort_values()


# In[132]:


data.plot(x='smoker', y = 'charges', kind='scatter')
#smoker pay way higher than non-smokers


# As it is clear that the insurance cost is greatly dependent on smoking. A smoker pays more than a non-smoker

# In[141]:


#what about bmi
data.plot(x='bmi', y = 'charges', kind='scatter')


# 
# People with bmi above 30 end up paying more because bmi of 30 or above is considered obese

# In[142]:


# what about region
data.plot(x='region', y = 'charges', kind='scatter')


# 
# Hard to tell how insurance costs depend on region

# In[146]:


#children
data.plot(x='children', y = 'charges', kind='scatter')


# # 
# Our data set consists of a lot of people who don't have children. But how many

# In[161]:


data.children.value_counts().plot(kind='bar')


# # Basic linear regression 

# In[133]:


#Make a linear regression between charges and age

#setting variables
x = data[['age']].values
y = data[['charges']].values

### init the regression
my_regression = LinearRegression()

### fit our variables into it
my_regression.fit(x,y)

### make the scatter in Blue
plt.scatter(x,y,color='dodgerblue',alpha=.4)

### draw regression in red
## predict where the y is based on x
plt.plot(x, my_regression.predict(x), color='indianred', linewidth='2')


# # Set up our stats model

# In[134]:


## set up for stats models
x_stats = data[['age']].values
y_stats = data[['charges']].values

x_stats = sm.add_constant(x_stats)

## create and print the linear model
my_model = sm.OLS(y_stats, x_stats).fit()
my_predictions = my_model.predict(x_stats)

my_model.summary()


# In[135]:


#setting up the model for multiple regression
x_stats = data[['age', 'sex', 'bmi', 'children', 'smoker', 'region']].values
y_stats = data[['charges']].values

x_stats = sm.add_constant(x_stats)

## create and print the linear model
my_model = sm.OLS(y_stats, x_stats).fit()
my_predictions = my_model.predict(x_stats)

## r-squared explains the strength of the relationship between our model and the outcome
## so here the relationship is 9%, which is not good at all

my_model.summary()


# # We gathered from above that smoking, children and region are stronger variables than age, sex and bmi in our insurance cost prediction. Let us try those three variables out in our analysis.
# 

# In[164]:


#setting up the model for multiple regression
x_stats = data[['children', 'smoker', 'region']].values
y_stats = data[['charges']].values

x_stats = sm.add_constant(x_stats)

## create and print the linear model
my_model = sm.OLS(y_stats, x_stats).fit()
my_predictions = my_model.predict(x_stats)

## r-squared explains the strength of the relationship between our model and the outcome
## so here the relationship is 9%, which is not good at all

my_model.summary()


# #In our region variable, p-value is more than what we would like it to be. Let us get rid of it.

# In[165]:


#setting up the model for multiple regression
x_stats = data[['children', 'smoker']].values
y_stats = data[['charges']].values

x_stats = sm.add_constant(x_stats)

## create and print the linear model
my_model = sm.OLS(y_stats, x_stats).fit()
my_predictions = my_model.predict(x_stats)

## r-squared explains the strength of the relationship between our model and the outcome
## so here the relationship is 9%, which is not good at all

my_model.summary()


# In this analysis, our p-value, R-squared, coef look good. Our t-values might be a little off, but I don't know how to read those values at this point. When I ran the first analysis with all the variables, I could see that children and smokers are the two variables with a greater impact on our dependent variables.  That is why I choose those two variables for my model.

# In[ ]:




