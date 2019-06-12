# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:26:49 2019

@author: Aluno
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

i=0
Estressado=[]
Ansioso=[]
Neutro=[]
Feliz=[]
Triste=[]


file = 'data_file.xlsx'
emo = 'Estressado', 'Ansioso', 'Neutro', 'Feliz','Triste'
df = pd.ExcelFile(file)
df1 = df.parse('Transformed by JSON-CSV.COM')
jonas = df1.shape

while i < jonas[0]:
    Estressado.append(df1.loc[i,'|__Estressado'])
    Ansioso.append(df1.loc[i,'|__Ansioso'])
    Neutro.append(df1.loc[i,'|__Neutro'])
    Feliz.append(df1.loc[i,'|__Feliz'])
    Triste.append(df1.loc[i,'|__Triste'])
    i+=1

sizes = sum(Estressado),sum(Ansioso),sum(Neutro),sum(Feliz),sum(Triste)
fig, ax = plt.subplots()
ax.pie(sizes,labels=emo, autopct='%1.1f%%',startangle=90)
ax.axis('equal')
plt.show()