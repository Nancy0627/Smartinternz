#!/usr/bin/env python
# coding: utf-8

# Assignment 1
# 
# 
# `
# 
# 
# 
# 
# 
# 
# 

# ### 1. Assign your Name to variable name and Age to variable age. Make a Python program that prints your name and age.

# In[1]:


name="NANCY SINHA"
age=20
print(name,age)


# ### 2. X="Datascience is used to extract meaningful insights." Split the string

# In[3]:


X="Datascience is used to extract meaningful insights."
X.split("a")


# ### 3. Make a function that gives multiplication of two numbers
# 

# In[6]:


def func(a,b):
    c=a*b
    print("The product of a and b is ")
    print(c)
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
func(n,m)



# ### 4. Create a Dictionary of 5 States with their capitals. also print the keys and values.

# In[9]:


dict={'Himachal Pradesh':"Shimla","Bihar":"Patna","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Jharkhand":"Ranchi"}
print(dict)
dict.keys()


# In[10]:


dict.values()


# ### 5. Create a list of 1000 numbers using range function.
# 

# In[4]:


num=list(range(1,1001))
print(num)


# ### 6. Create an identity matrix of dimension 4 by 4

# In[11]:


import numpy as np
var2=np.identity(4,dtype="int")
var2


# ### 7. Create a 3x3 matrix with values ranging from 1 to 9
# 

# In[16]:


import numpy as np
matrix =  np.arange(9).reshape(3,3)
print(matrix)


# ### 8. Create 2 similar dimensional array and perform sum on them.

# In[26]:


a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("1st array is ")
print(a1)
print("2nd array is ")
print(a2)
sum=a1+a2
print("the sum of 2 arrays ")
print(sum)


# ### 9. Generate the series of dates from 1st Feb, 2023 to 1st March, 2023 (both inclusive)

# In[33]:


import pandas as pd

start_date = "2023-02-01"
end_date = "2023-03-01"

date_range = pd.date_range(start= start_date, end =  end_date)

for date in date_range:
    print(date)


# ### 10. Given a dictionary, convert it into corresponding dataframe and display it dictionary = {'Brand': ['Maruti', 'Renault', 'Hyndai'], 'Sales' : [250, 200, 240]}

# In[13]:


import pandas as pd
dictionary = {'Brand': ['Maruti', 'Renault', 'Hyndai'], 'Sales' : [250, 200, 240]}
print(dictionary)
df=pd.DataFrame(dictionary)
print(df)

