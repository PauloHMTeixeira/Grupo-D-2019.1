import json
import serial

leitura_byte_rfid = 12 

#leitura do RFID
Arduino = serial.Serial('COM9', baudrate = 9600) #conectando com leitura do RFID

d = {}
'''with open("data_file.json", "w") as write_file:
    json.dump(d, write_file, indent=4)'''

while True:
	tag_lida = Arduino.read(leitura_byte_rfid)
	print(tag_lida)

	with open("data_file.json", "r+") as f: #abre o arquivo para modificar leitura do botão
		data = json.load(f) #talvez esteja errado!!

	y = tag_lida
	y = str(int.from_bytes(y, byteorder='big')) #transforma em string a identificação do crachá

	if y in data:
		print('Como você está se sentindo? ')

		#leitura do botão
		buttonpress = Arduino.read() 

		if buttonpress == b'1':
			data[y]['Estressado'] += 1
			print('Estressado')
		if buttonpress == b'2':
			data[y]['Ansioso'] += 1
			print('Ansioso')
		if buttonpress == b'3':
			data[y]['Neutro'] += 1
			print('Neutro')
		if buttonpress == b'4':
			data[y]['Triste'] += 1
			print('Triste')
		if buttonpress == b'5':
			data[y]['Feliz'] += 1
			print('Feliz')

	else:
		data[(y)] = {
		"Estressado": 0,
		"Ansioso": 0,
		"Neutro": 0,
		"Feliz": 0,
		"Triste": 0,
		}

		if y in data:
			print('Como você está se sentindo? ')

			buttonpress = Arduino.read()

			if buttonpress == b'1':
				data[y]['Estressado'] += 1
				print('Estressado')
			if buttonpress == b'2':
				data[y]['Ansioso'] += 1
				print('Ansioso')
			if buttonpress == b'3':
				data[y]['Neutro'] += 1
				print('Neutro')
			if buttonpress == b'4':
				data[y]['Triste'] += 1
				print('Triste')
			if buttonpress == b'5':
				data[y]['Feliz'] += 1
				print('Feliz')

		with open("data_file.json", "a") as jsonFile: #adiciona nova leitura de botão
			json.dump(data, jsonFile, indent=4)

print(data[y])

with open("data_file.json", "w") as jsonFile:
	json.dump(data, jsonFile, indent=4)
