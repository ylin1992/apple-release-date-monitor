import abc
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDER_EMAIL, RECEIVER_EMAIL, SENDGRID_API_KEY, SSL_PORT, SENDER_PWD
import smtplib, ssl

class Email(abc.ABC):
    
    @abc.abstractmethod
    def set_email():
        return NotImplemented
    
    @abc.abstractmethod
    def get_email_info():
        return NotImplemented
    
    @abc.abstractmethod
    def send_email():
        return NotImplemented
    

class SendGridEmail(Email):
    
    def __init__(self, sender, receiver, subject="", content=""):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
    
    def set_email(self, **kwargs):
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])
            else:
                raise ValueError('"%s" is not defined'%k) 
    
    def get_email_info(self):
        return self.__repr__()
    
    def send_email(self):
        message = Mail(
        from_email=self.sender,
        to_emails=self.receiver,
        subject=self.subject,
        html_content=self.content)
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.body)
    
    def __repr__(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'subject': self.subject,
            'content': self.content
        }

class SSLEmail(SendGridEmail):


    def send_email(self):
        context = ssl.create_default_context()
        message = """\
        Subject: %s!

        %s."""%(self.subject, self.content)

        with smtplib.SMTP_SSL("smtp.gmail.com", SSL_PORT, context=context) as server:
            server.login(self.sender, SENDER_PWD)
            server.sendmail(self.sender, self.receiver, message)
        
if __name__ == '__main__':
    email = SendGridEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject='test subject', content='test content')
    print(email.get_email_info())
    email.set_email(content='modified content')
    print(email.get_email_info())
    email.send_email()
    
    # email = SSLEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject='test subject', content='test content')
    # email.send_email()