#import serial

#buttonState = serial.Serial('COM4', baudrate=9600, timeout=0.3)
e = 0
a = 0
id = 0
y = 0
tr = 0
#arq = open('arq1.txt', 'w+')
x = int(input('Como tem sido sua experiência Cesar School?'))
#while True:
   # buttonpress = buttonState.read()
if x == 1:
    e = e + 1
    print("identificacao, {}, {}, {}, {}, {}" .format(e, a, id, y, tr))
    #arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t))
       # break
if x == 2:
    a = a + 1
    print("identificacao, {}, {}, {}, {}, {}" .format(e, a, id, y, tr)
    #arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t)
       # break
if x == 3:
    id = id + 1
    print("identificacao, {}, {}, {}, {}, {}" .format(e, a, id, y, tr)
    #arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t)
      #  break
if x == 4:
    y = y + 1
    print("identificacao, {}, {}, {}, {}, {}" .format(e, a, id, y, tr)
    #arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t)
       # break
if x == 5:
    tr = tr + 1
    print("identificacao, {}, {}, {}, {}, {}" .format(e, a, id, y, tr)
    #arq.writelines('identificacao, {}, {}, {}, {}, {}' .format(e, a, n, f, t)
       # break

#arq.close()