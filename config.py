import os

SENDER_EMAIL = os.getenv('SENDER_EMAIL', None)
SENDER_PWD = os.getenv('SENDER_PWD', None)
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', None)
SSL_PORT = 465