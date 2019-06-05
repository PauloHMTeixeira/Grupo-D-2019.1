import json
import serial

# Leitura da porta serial
Arduino = serial.Serial('COM9', baudrate=9600) #conectando com leitura do RFID e dos botões.

#leitura do crachá
tag_lida = Arduino.readline() #leitura da ID
tag_decode = tag_lida.decode('utf-8')
tag_decode = tag_decode.replace('\r\n', '')

y = tag_decode

print('Sua ID é: {}' .format(y))

buttonpress = Arduino.readline()
buttonpress = buttonpress.decode('utf-8') #decodificação
buttonpress = buttonpress.replace('\r\n', '')

with open("data_file.json", "r+") as f:
    data = json.load(f)


if y in data:
    print('Como você está se sentindo? ')
    if buttonpress == "1":
        data[y]['Estressado'] += 1
        print('Estressado')

    if buttonpress == "2":
        data[y]['Ansioso'] += 1
        print('Ansioso')

    if buttonpress == "3":
        data[y]['Neutro'] += 1
        print('Neutro')

    if buttonpress == "4":
        data[y]['Triste'] += 1
        print('Triste')

    if buttonpress == "5":
        data[y]['Feliz'] += 1
        print('Feliz')
else:
    data[y] = {
        "Estressado": 0,
        "Ansioso": 0,
        "Neutro": 0,
        "Feliz": 0,
        "Triste": 0,
    }
    
    print('Como você está se sentindo? ')
    if buttonpress == "1":
        data[y]['Estressado'] += 1
        print('Estressado')

    if buttonpress == "2":
        data[y]['Ansioso'] += 1
        print('Ansioso')

    if buttonpress == "3":
        data[y]['Neutro'] += 1
        print('Neutro')

    if buttonpress == "4":
        data[y]['Triste'] += 1
        print('Triste')

    if buttonpress == "5":
        data[y]['Feliz'] += 1
        print('Feliz')

    with open("data_file.json", "a") as jsonFile:
        json.dump(data, jsonFile, indent=4)

print(data[y])

with open("data_file.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)
