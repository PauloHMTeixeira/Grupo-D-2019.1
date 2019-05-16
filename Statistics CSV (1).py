#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('untitled.csv')

# block 1 - simple stats
sum1 = df['Estressado'].sum()
count1 = df['Estressado'].count()
median1 = df['Estressado'].median() 
std1 = df['Estressado'].std() 
var1 = df['Estressado'].var()
media1= sum1/(len('Estressado'))

# block 2 - group by
groupby_sum1 = df.groupby(['Feliz']).sum() 
groupby_count1 = df.groupby(['Feliz']).count()

# print block 1
print ('Sum of salaries: ' + str(sum1))
print ('Count of salaries: ' + str(count1))
print ('Median salary: ' + str(median1))
print ('Std of salaries: ' + str(std1))
print ('Var of salaries: ' + str(var1))
print ('Arithmetic average: ' + str(media1))

# print block 2
print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
print ('Count of values, grouped by the Country: ' + str(groupby_count1))


# In[ ]:




