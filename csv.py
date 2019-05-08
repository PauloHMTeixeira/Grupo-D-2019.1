import serial

buttonState = serial.Serial('COM4', baudrate=9600, timeout=0.3)
arq = open('arq1.txt', 'w+')
while True:
    e = 0
    a = 0
    n = 0
    f = 0
    t = 0
    buttonpress = buttonState.read()
    if buttonpress == b'1':
        e = e + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(e, a, n, f, t))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
        break
    elif buttonpress == b'2':
        a = a + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(e, a, n, f, t))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
        break
    elif buttonpress == b'3':
        n = n + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(e, a, n, f, t))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
        break
    elif buttonpress == b'4':
        f = f + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(e, a, n, f, t))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
        break
    elif buttonpress == b'5':
        t = t + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(e, a, n, f, t))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
        break

arq.close()
