#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.untitled_csv 

# block 1 - simple stats
mean1 = df['Salary'].mean()
sum1 = df['Salary'].sum()
max1 = df['Salary'].max()
min1 = df['Salary'].min()
count1 = df['Salary'].count()
median1 = df['Salary'].median() 
std1 = df['Salary'].std() 
var1 = df['Salary'].var()  

# block 2 - group by
groupby_sum1 = df.groupby(['Country']).sum() 
groupby_count1 = df.groupby(['Country']).count()

# print block 1
print ('Mean salary: ' + str(mean1))
print ('Sum of salaries: ' + str(sum1))
print ('Max salary: ' + str(max1))
print ('Min salary: ' + str(min1))
print ('Count of salaries: ' + str(count1))
print ('Median salary: ' + str(median1))
print ('Std of salaries: ' + str(std1))
print ('Var of salaries: ' + str(var1))

# print block 2
print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
print ('Count of values, grouped by the Country: ' + str(groupby_count1))

