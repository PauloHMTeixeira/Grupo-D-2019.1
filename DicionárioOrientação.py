import csv
import os


estressado = 0
ansioso = 0
neutro = 0
feliz = 0
triste = 0
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Untitled.csv')




def criar_perfil(identificacao, estressado, ansioso, neutro, feliz, triste):
    perfil = {"id": identificacao, "estressado": estressado, "ansioso": ansioso, "neutro": neutro, "feliz": feliz, "triste": triste}
    return perfil

perfil1 = criar_perfil('alicia', 0, 0, 0, 0, 0)
perfil2 = criar_perfil('caio', 0, 0, 0, 0, 0)


while True:
    ide = input('digite o usuario ')
    emc = input('digite sua emocao ')
    # ide = identificacao do usuario (RFID), emc = emoção do usuário
    if ide == 'caio':
        if emc == '1':
            perfil2['estressado'] += 1
        if emc == '2':
            perfil2['ansioso'] += 1
        if emc == '3':
            perfil2['neutro'] += 1
        if emc == '4':
            perfil2['feliz'] += 1
        if emc == '5':
            perfil2['triste'] += 1
    if ide == 'alicia':
        if emc == '1':
            perfil1['estressado'] += 1
        if emc == '2':
            perfil1['ansioso'] += 1
        if emc == '3':
            perfil1['neutro'] += 1
        if emc == '4':
            perfil1['feliz'] += 1
        if emc == '5':
            perfil1['triste'] += 1
    if ide == 'fim':
        break
    print(perfil1)
    print('----------------')
    print(perfil2)

open(csvfile, "w")


csvData = [['ID',  'Estressado', 'Ansioso', 'Neutro', 'Feliz', 'Triste'],
            [perfil1['id'],  perfil1['estressado'], perfil1['ansioso'], perfil1['neutro'], perfil1['feliz'], perfil1['triste']],
            [perfil2['id'],  perfil2['estressado'], perfil2['ansioso'], perfil2['neutro'], perfil2['feliz'], perfil2['triste']]]

with open('Untitled.csv', "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()