import serial #conexão com porta serial
leitura_byte_rfid = 12 #limita tamanho da tag lida??

#leitura dos botões
buttonState = serial.Serial('COM6', baudrate = 9600, timeout = 0.3) #lê estado dos butões  

#leitura do RFID
RFID = serial.Serial('COM6', baudrate = 9600) #conectando com leitura do RFID

while True: 
	tag_lida = RFID.read(leitura_byte_rfid) #lê tag do crachá
	#if tag_lida != 0:
	if len(tag_lida) != 0: #alternativo: == (leitura_byte_rfid - 1)
		print("Olá, ", tag_lida, "como está se sentindo hoje?") 

		buttonpress = buttonState.read()

		if buttonpress == b'1':

			print("Estressado")

			arq.writelines('Estressado')

			break

		elif buttonpress == b'2':

			print("Ansioso")

			arq.writelines('Ansioso')

			break

		elif buttonpress == b'3':

			print("Neutro")

			arq.writelines('Neutro')

			break

		elif buttonpress == b'4':

			print("Feliz")

			arq.writelines('Feliz')

			break

		elif buttonpress == b'5':

			print("Triste")

			arq.writelines('Triste')

			break

print("obrigado(a)!")
