import csv
import os
# biblioteca csv para criação do arquivo csv e os apenas para Mac/Apple
estressado = 0
ansioso = 0
neutro = 0
feliz = 0
triste = 0
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Untitled.csv')
# userhome e csvfile também são apenas para Mac/Apple
open(csvfile, "w")
# aqui comando para o Python abrir o arquivo csv (previamente criado)
csvData = [['ID', 'Estressado', 'Ansioso', 'Neutro', 'Feliz', 'Triste'],
           ['Pedro', '0', '0', '0', '0', '0'],
           ['Davi', '0', '0', '0', '0', '0']]
# aqui como as informações vão ficar organizadas, ID e as opções dos botões
with open('Untitled.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
# comandos para mexer no arquivo csv 
csvFile.close()
# comando para fechar o arquivo csv
