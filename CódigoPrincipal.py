import json
import serial

# Leitura da porta serial
Arduino = serial.Serial('COM9', baudrate=9600) #conectando com leitura do RFID e dos botões.

#leitura do crachá
tag_lida = Arduino.readline() #leitura da ID
tag_decode = tag_lida.decode('utf-8')
tag_decode = tag_decode.replace('\r\n', '')

# envio do feedback
tetoansioso = 4
tetotriste = 4
tetoestressado = 4
tetoneutro = 4
tetofeliz = 4

def enviaremailansioso():
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
    textansioso = """\
        Olá, notamos vários reports mostrando que você está bastante ansioso(a). Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante ansioso(a). Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textansioso, "plain")
    part2 = MIMEText(htmlansioso, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    print('banana')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def enviaremailtriste():
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
    textansioso = """\
        Olá, notamos vários reports mostrando que você está bastante triste recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te 
        ajudar, ela pode te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante triste recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textansioso, "plain")
    part2 = MIMEText(htmlansioso, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    print('banana')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def enviaremailestressado():
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
    textansioso = """\
        Olá, notamos vários reports mostrando que você está bastante estressado recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te 
        ajudar, ela pode te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante estressado recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato com ela através da própria School ou pelo ramal.
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textansioso, "plain")
    part2 = MIMEText(htmlansioso, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    print('banana')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def enviaremailneutro():
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
    textansioso = """\
        Para nós, sentimento de neutralidade é quase satisfação, mas estamos dispostos a melhorar isso! Entre em contato com 
        algum de nossos coordenadores/professores para juntos melhorarmos sua experiência Cesar School!
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Para nós, sentimento de neutralidade é quase satisfação, mas estamos dispostos a melhorar isso! Entre em contato com 
        algum de nossos coordenadores/professores para juntos melhorarmos sua experiência Cesar School!
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textansioso, "plain")
    part2 = MIMEText(htmlansioso, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    print('banana')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def enviaremailfeliz():
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
    textansioso = """\
        Ficamos muito contentes em saber que está sendo proporcionada felicidade dentro da School, continue 
                utilizando nosso sistema de reports e sinta-se a vontade para reportar qualquer outro sentimento para gente!
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Ficamos muito contentes em saber que está sendo proporcionada felicidade dentro da School, continue 
                utilizando nosso sistema de reports e sinta-se a vontade para reportar qualquer outro sentimento para gente!
                </p>

            </body>
        </html>
        """
    part1 = MIMEText(textansioso, "plain")
    part2 = MIMEText(htmlansioso, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    print('banana')
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
        if data[y]['Estressado'] == tetoestressado:
            enviaremailestressado()
            tetoestressado += 4

    if buttonpress == "2":
        data[y]['Ansioso'] += 1
        print('Ansioso')
        if data[y]['Ansioso'] == tetoansioso:
            enviaremailansioso()
            tetoansioso += 4
        

    if buttonpress == "3":
        data[y]['Neutro'] += 1
        print('Neutro')
        if data[y]['Neutro'] == tetoneutro:
            enviaremailneutro()
            tetoneutro += 4

    if buttonpress == "4":
        data[y]['Triste'] += 1
        print('Triste')
        if data[y]['Triste'] == tetotriste:
            enviaremailtriste()
            tetotriste += 4
        

    if buttonpress == "5":
        data[y]['Feliz'] += 1
        print('Feliz')
        if data[y]['Feliz'] == tetofeliz:
            enviaremailfeliz()
            tetofeliz += 4
        

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
