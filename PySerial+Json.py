import json
import serial
leitura_byte_rfid = 12 #limita tamanho da tag lida??

#leitura dos botões
buttonState = serial.Serial('COM6', baudrate = 9600, timeout = 0.3) #lê estado dos butões

#leitura do RFID
RFID = serial.Serial('COM6', baudrate = 9600) #conectando com leitura do RFID

tag_lida = RFID.read(leitura_byte_rfid)
buttonpress = buttonState.read()

d = {}

with open("data_file.json", "r+") as f:
    data = json.load(f)


y = tag_lida

if y in data:
    buttonpress = input('Como você está se sentindo? ')
    if buttonpress == b'1':
        data[y]['Estressado'] += 1
    if buttonpress == b'2':
        data[y]['Ansioso'] += 1
    if buttonpress == b'3':
        data[y]['Neutro'] += 1
    if buttonpress == b'4':
        data[y]['Triste'] += 1
    if buttonpress == b'5':
        data[y]['Feliz'] += 1

else:
    data[y] = {
        "Estressado": 0,
        "Ansioso": 0,
        "Neutro": 0,
        "Feliz": 0,
        "Triste": 0,
    }

    with open("data_file.json", "a") as jsonFile:
        json.dump(data, jsonFile, indent=4)



print(data[y])


with open("data_file.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)
