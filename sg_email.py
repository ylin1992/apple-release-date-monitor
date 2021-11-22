import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDER_EMAIL, RECEIVER_EMAIL, SENDGRID_API_KEY
def send_email(text):
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=RECEIVER_EMAIL,
        subject='The release date has been updated',
        html_content='<strong>Check it out on the website!</strong><p>'+text+'</p>')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)

