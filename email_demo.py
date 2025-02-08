# Technology:
# A gmail account
# SMTP e-mail server
# SSL (Secure Sockets Layer) or TLS (Transport Layer Security) - protocols for encrypted connections

import smtplib
import ssl

smtp_server = 'smtp.gmail.com'
port = 465
sender = 'pytraining2019@gmail.com'
password = input("Enter your password >: ")
receiver = 'azakharov16@gmail.com'

message = """
From: {}
To: {}
Subject: Hello there!

This is Python speaking.
""".format(sender, receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print("Connection established.")
    server.sendmail(sender, receiver, message)
    print("Message sent.")
    server.quit()

# Opportunistic encryption: make an unencrypted connection, then upgrade it to encrypted connection.
# port = 587 (Google will be watching this port)
# try:
#    server = smtplib.SMTP(smtp_server, port)
#    server.ehlo()
#    server.starttls(context=context)
#    server.ehlo()
#    server.login(sender, password)
#    print("Connection established.")
# except Exception as e:
#    pass
# finally:
#    server.quit()
