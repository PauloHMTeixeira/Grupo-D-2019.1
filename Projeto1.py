import serial
buttonState = serial.Serial('COM4', baudrate = 9600, timeout = 0.3)
arq = open ('arq1.txt', 'w+')
while True:

	buttonpress = buttonState.read()
	if buttonpress == b'1':
		print("Muito triste")
		arq.writelines('Muito triste')
		break
	elif buttonpress == b'2':
		print("Triste")
		arq.writelines('Triste')
		break 
	elif buttonpress == b'3':
		print("Indiferente")
		arq.writelines('Indiferente')
		break
	elif buttonpress == b'4':
		print("Feliz")
		arq.writelines('Feliz')
		break
	elif buttonpress == b'5':
		print("Muitop feliz")
		arq.writelines('Muito feliz')
		break
		
arq.close()
