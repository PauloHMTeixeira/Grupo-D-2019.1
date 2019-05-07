import serial

buttonState = serial.Serial('COM4', baudrate=9600, timeout=0.3)
arq = open('arq1.txt', 'w+')
while True:
    mt = 0
    t = 0
    i = 0
    f = 0
    mf = 0
    buttonpress = buttonState.read()
    if buttonpress == b'1':
        mt = mt + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(mt, t, i, f, mf))
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(mt, t, i, f, mf))
        break
    elif buttonpress == b'2':
        t = t + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(mt, t, i, f, mf)
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(mt, t, i, f, mf)
        break
    elif buttonpress == b'3':
        i = i + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(mt, t, i, f, mf)
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(mt, t, i, f, mf)
        break
    elif buttonpress == b'4':
        f = f + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(mt, t, i, f, mf)
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(mt, t, i, f, mf)
        break
    elif buttonpress == b'5':
        mf = mf + 1
        print("identificacao, {}, {}, {}, {}, {}" .format(mt, t, i, f, mf)
        arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(mt, t, i, f, mf)
        break

arq.close()