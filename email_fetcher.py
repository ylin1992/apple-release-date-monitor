import requests
import os
from config import DB_SERVER_HOST
def get_all_users():
    try:
        res = requests.get(DB_SERVER_HOST+'/users?subscribed=true')
    except Exception as e:
        print(e)
    if res.status_code == 200:
        users = res.json().get('users')
        emails = [u['email'] for u in users]
        print(emails)
        return emails
    else:
        print("Error, status code: " + str(res.status_code))
        return None