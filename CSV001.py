import csv
import os

estressado = 0
ansioso = 0
neutro = 0
feliz = 0
triste = 0
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Untitled.csv')

open(csvfile, "w")

csvData = [['ID', 'Estressado', 'Ansioso', 'Neutro', 'Feliz', 'Triste'],
           ['Pedro', '0', '0', '0', '0', '0'],
           ['Davi', '0', '0', '0', '0', '0']]

with open('Untitled.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()