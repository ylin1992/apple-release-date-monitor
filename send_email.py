import smtplib, ssl
import os
from config import SENDER_PWD, SENDER_EMAIL, RECEIVER_EMAIL, SSL_PORT
port = SSL_PORT

def send_email():
    context = ssl.create_default_context()
    message = """\
    Subject: Release date is updated!

    The release date has updated, check it on the website!."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PWD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
