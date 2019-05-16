import csv
import os
import serial

buttonState = serial.Serial('entrada', baudrate=9600, timeout=0.3)
estressado = 0
ansioso = 0
neutro = 0
feliz = 0
triste = 0
identificacao = ''
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Untitled.csv')


def criar_perfil(identificacao, estressado, ansioso, neutro, feliz, triste):
    perfil = {"id": identificacao, "estressado": estressado, "ansioso": ansioso, "neutro": neutro, "feliz": feliz, "triste": triste}
    return perfil


perfil1 = criar_perfil('Alicia', 0, 0, 0, 0, 0)
perfil2 = criar_perfil('caio', 0, 0, 0, 0, 0)


while True:
    ide = input('digite o usuario ')
    emc = input('digite sua emocao ')

    if ide == 'Alicia':


        buttonpress = buttonState.read()
        open(csvfile, "w")
        if buttonpress == b'1':
            perfil1['estressado'] += 1
            if buttonpress == b'2':
                perfil1['ansioso'] += 1
            if buttonpress == b'3':
                perfil1['neutro'] += 1
            if buttonpress == b'4':
                perfil1['feliz'] += 1
            if buttonpress == b'5':
                perfil1['triste'] += 1
            if buttonpress == b'6':
                break

        if buttonpress == b'2':
            perfil1['ansioso'] += 1
            if buttonpress == b'1':
                perfil1['estressado'] += 1
            if buttonpress == b'3':
                perfil1['neutro'] += 1
            if buttonpress == b'4':
                perfil1['feliz'] += 1
            if buttonpress == b'5':
                perfil1['triste'] += 1
            if buttonpress == b'6':
                break

        if buttonpress == b'3':
            perfil1['neutro'] += 1
            if buttonpress == b'1':
                perfil1['estressado'] += 1
            if buttonpress == b'2':
                perfil1['ansioso'] += 1
            if buttonpress == b'4':
                perfil1['feliz'] += 1
            if buttonpress == b'5':
                perfil1['triste'] += 1
            if buttonpress == b'6':
                break

        if buttonpress == b'4':
            perfil1['feliz'] += 1
            if buttonpress == b'1':
                perfil1['estressado'] += 1
            if buttonpress == b'2':
                perfil1['ansioso'] += 1
            if buttonpress == b'3':
                perfil1['neutro'] += 1
            if buttonpress == b'5':
                perfil1['triste'] += 1
            if buttonpress == b'6':
                break

        if buttonpress == b'5':
            perfil1['triste'] += 1
            if buttonpress == b'1':
                perfil1['estressado'] += 1
            if buttonpress == b'2':
                perfil1['ansioso'] += 1
            if buttonpress == b'3':
                perfil1['neutro'] += 1
            if buttonpress == b'4':
                perfil1['feliz'] += 1
            if buttonpress == b'6':
                break

        if buttonpress == b'6':
            break

        csvData = [['ID', 'Estressado', 'Ansioso', 'Neutro', 'Feliz', 'Triste'],
                   [ide, estressado, ansioso, neutro, feliz, triste]]

        with open('Untitled.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)

        csvFile.close()