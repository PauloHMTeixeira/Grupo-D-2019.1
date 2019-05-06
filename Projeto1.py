import serial
buttonState = serial.Serial('COM4', baudrate = 9600, timeout = 0.3)
arq = open ('arq1.txt', 'w+')
while True:

	buttonpress = buttonState.read()
	if buttonpress == b'1':
		print("Sou lindo")
		arq.writelines('Sou lindo')
		break
	elif buttonpress == b'2':
		print("Estou Feliz")
		arq.writelines('Estou Feliz')
		break 
	elif buttonpress == b'3':
		print("to puto")
		arq.writelines('to puto')
		break
	elif buttonpress == b'4':
		print("triste")
		arq.writelines('triste')
		break
	elif buttonpress == b'5':
		print("nervouser")
		arq.writelines('nervouser')
		break
		
arq.close()