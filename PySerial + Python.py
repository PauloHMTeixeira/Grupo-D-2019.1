import csv
import os
import serial

buttonState = serial.Serial('entrada', baudrate = 9600, timeout = 0.3)
estressado = 0
ansioso = 0
neutro = 0
feliz = 0
triste = 0
identificacao = ''
userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'PyCharmProjects', 'Untitled.csv')

# if identificacao == 'Pedro':
while True:

    buttonpress = buttonState.read()
    open(csvfile, "w")
    if buttonpress == b'1':
        estressado = estressado + 1
        if buttonpress == b'2':
            ansioso = ansioso + 1
        if buttonpress == b'3':
            neutro = neutro + 1
        if buttonpress == b'4':
            feliz = feliz + 1
        if buttonpress == b'5':
            triste = triste + 1
        if buttonpress == b'6':
            break

    if buttonpress == b'2':
        ansioso = ansioso + 1
        if buttonpress == b'1':
            estressado = estressado + 1
        if buttonpress == b'3':
            neutro = neutro + 1
        if buttonpress == b'4':
            feliz = feliz + 1
        if buttonpress == b'5':
            triste = triste + 1
        if buttonpress == b'6':
            break

    if buttonpress == b'3':
        neutro = neutro + 1
        if buttonpress == b'1':
            estressado = estressado + 1
        if buttonpress == b'2':
            ansioso = ansioso + 1
        if buttonpress == b'4':
            feliz = feliz + 1
        if buttonpress == b'5':
            triste = triste + 1
        if buttonpress == b'6':
            break

    if buttonpress == b'4':
        feliz = feliz + 1
        if buttonpress == b'1':
            estressado = estressado + 1
        if buttonpress == b'2':
            ansioso = ansioso + 1
        if buttonpress == b'3':
            neutro = neutro + 1
        if buttonpress == b'5':
            triste = triste + 1
        if buttonpress == b'6':
            break

    if buttonpress == b'5':
        triste = triste + 1
        if buttonpress == b'1':
            estressado = estressado + 1
        if buttonpress == b'2':
            ansioso = ansioso + 1
        if buttonpress == b'3':
            neutro = neutro + 1
        if buttonpress == b'4':
            feliz = feliz + 1
        if buttonpress == b'6':
            break

    if buttonpress == b'6':
        break

    csvData = [['ID', 'Estressado', 'Ansioso', 'Neutro', 'Feliz', 'Triste'],
               ['Pedro', estressado, ansioso, neutro, feliz, triste]]

    with open('Untitled.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)

    csvFile.close()