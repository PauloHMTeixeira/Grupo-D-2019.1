# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:26:49 2019

@author: Aluno
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

i=0
oi=list()
y=list()


file = 'data_file.xlsx'
emo = 'Estressado', 'Ansioso', 'Neutro', 'Feliz','Triste'
df = pd.ExcelFile(file)
df1 = df.parse('Transformed by JSON-CSV.COM')
jonas = df1.shape

gur=int(input())
gur-=2



while i < jonas[0]:
    oi.append(df1.loc[gur,'|__Estressado'])
    oi.append(df1.loc[gur,'|__Ansioso'])
    oi.append(df1.loc[gur,'|__Neutro'])
    oi.append(df1.loc[gur,'|__Feliz'])
    oi.append(df1.loc[gur,'|__Triste'])
    i+=1

sizes = oi[0],oi[1],oi[2],oi[3],oi[4]
fig, ax = plt.subplots()
ax.pie(sizes,labels=emo, autopct='%1.1f%%',startangle=90)
ax.axis('equal')
plt.show()  