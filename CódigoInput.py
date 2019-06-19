import json


with open("data_file.json", "r+") as f:
    data = json.load(f)
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
        te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante ansioso(a). Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
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
        ajudar, ela pode te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante triste recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
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
        ajudar, ela pode te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
        """
    htmlansioso = """\
        <html>
            <body>
                <p>Olá, notamos vários reports mostrando que você está bastante estressado recentemente e isso não é nada bom. Nossa psicóloga está disponível para tentar te ajudar, ela pode 
        te dar ótimas dicas! Entre em contato indo até ela ou pelo número XXXXX-XXXX
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
        FALTA ESCREVER
        """
    htmlansioso = """\
        <html>
            <body>
                <p>FALTA ESCREVER!
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
        FALTA ESCREVER
        """
    htmlansioso = """\
        <html>
            <body>
                <p>FALTA ESCREVER
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


y = input('Qual a sua ID? ')



if y in data:
    x = input('Como você está se sentindo? ')
    if x == 'Estressado':
        data[y]['Estressado'] += 1
        if data[y]['Estressado'] == tetoestressado:
            enviaremailestressado()
            tetoestressado += 4
    if x == 'Ansioso':
        data[y]['Ansioso'] += 1
        if data[y]['Ansioso'] == tetoansioso:
            enviaremailansioso()
            tetoansioso += 4
    if x == 'Neutro':
        data[y]['Neutro'] += 1
        if data[y]['Neutro'] == tetoneutro:
            enviaremailneutro()
            tetoneutro += 4
    if x == 'Triste':
        data[y]['Triste'] += 1
        if data[y]['Triste'] == tetotriste:
            enviaremailtriste()
            tetotriste += 4
    if x == 'Feliz':
        data[y]['Feliz'] += 1
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
        "Nome": nome,
        "E-mail": email,
        "Estressado": 0,
        "Ansioso": 0,
        "Neutro": 0,
        "Feliz": 0,
        "Triste": 0,
    }
    if y in data:
        x = input('Como você está se sentindo? ')
        if x == 'Estressado':
            data[y]['Estressado'] += 1
        if x == 'Ansioso':
            data[y]['Ansioso'] += 1
        if x == 'Neutro':
            data[y]['Neutro'] += 1
        if x == 'Triste':
            data[y]['Triste'] += 1
        if x == 'Feliz':
            data[y]['Feliz'] += 1


    with open("data_file.json", "a") as jsonFile:
        json.dump(data, jsonFile, indent=4)



print(data[y])


with open("data_file.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)

