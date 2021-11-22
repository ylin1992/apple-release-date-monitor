import smtplib, ssl
import os
port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = os.getenv('SENDER_EMAIL', None) 
receiver_email = os.getenv('RECEIVER_EMAIL', None) 
message = """\
Subject: Release date is updated!

The release date has updated, check it on the website!."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
