import csv
import os
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Teste.csv')


open(csvfile, "w")

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
    if ide == 'alicia':
        if emc == '1':
            perfil1['estressado'] += 1

    csvData = [['ID', 'Estressado'],
                [ide, perfil1['estressado'],]]
    print(perfil1)
    print('----------------')
    print(perfil2)
