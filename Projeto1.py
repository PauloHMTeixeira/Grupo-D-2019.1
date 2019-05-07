import serial
buttonState = serial.Serial('COM4', baudrate = 9600, timeout = 0.3)
arq = open ('arq1.txt', 'w+')
while True:

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
		
arq.close()
