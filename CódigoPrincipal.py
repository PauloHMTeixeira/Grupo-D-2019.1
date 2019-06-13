import json
import serial

# Leitura da porta serial
Arduino = serial.Serial('COM9', baudrate=9600) #conectando com leitura do RFID e dos botões.

#leitura do crachá
tag_lida = Arduino.readline() #leitura da ID
tag_decode = tag_lida.decode('utf-8')
tag_decode = tag_decode.replace('\r\n', '')

# envio do feedback
teto = 4

def enviaremail():
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    port = 465
    password = 'cesarschool123'
    sender_email = 'humorcesar@gmail.com'
    receiver_email = data[y]['E-mail']
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    textestressado = """\
        Estamos cientes da sua situação e gostaria bastante de poder ajudar de forma mais presente, entre em contato com a nossa psicóloga,
         Ana Carolina, via número de telefone 00000-0000
        """
    htmlestressado = """\
        <html>
            <body>
                <p>Estamos cientes da sua situação e gostaria bastante de poder ajudar de forma mais presente, entre em contato com a nossa psicóloga,
         Ana Carolina, via número de telefone 00000-0000
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textestressado, "plain")
    part2 = MIMEText(htmlestressado, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

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
        
    # precisa ajeitar aqui!!
    if data[y][x] == teto:
        enviaremail()
        teto += 4
else:
    nome = input('Qual seu nome completo (sem "de" e "e")? ')
    nome2 = nome.lower().split(" ")
    email = ""
    for i in nome2:
        email += i[0]
    email += "@cesar.school"
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
