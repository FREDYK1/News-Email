import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username="frederickkankam7@gmail.com"
    password="atww gjwj isbr xbtb"

    receiver = "frederickkankam7@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))