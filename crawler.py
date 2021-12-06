from selenium import webdriver
import time
from config import RECEIVER_EMAIL, SENDER_EMAIL
import os
import datetime
from emails import Email, SendGridEmail, SSLEmail
import email_fetcher


START_TIME          = time.time()
FEEDS_DURATION      = 2 # hours
CRAWL_URL           = "https://www.apple.com/tw/macbook-pro/"
TARGET_CLASS_NAME   = 'bottom-intro'
MONITORED_TEXT      = '購買'
MONITORED_TITLE     = 'buy - macbook pro 14'
is_checked          = False
def feeds_timer():
    global START_TIME
    end_time = time.time()
    elasped = (end_time - START_TIME)  / 60 / 60
    print(elasped)
    if elasped > FEEDS_DURATION:
        START_TIME = time.time()
        return True
    else:
        return False

def check_feeds(f):
    def wrapper(*args, **kwargs):
        is_time_up = feeds_timer()
        f(is_time_up, *args, **kwargs)
        return is_time_up
    return wrapper

def print_info(t, text):
    print('[FETCH %d]: %s' %(t, text))
    
def init_driver():
    try:
        # local
        driver = webdriver.Chrome('./chromedriver')
    except:
        # heroku
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    return driver

@check_feeds
def crwaler_helper(is_time_up, driver, i=0, send_email=False, emails=None):
    global is_checked
    driver.get(CRAWL_URL)
    try:
        es = driver.find_elements_by_class_name(TARGET_CLASS_NAME)
        print(es)
        try:
            iterator = iter(es)
            for e in es:
                print_info(i + 1, e.text)
                title = e.get_attribute("data-analytics-title")
                if title is not None:
                    print_info(i + 1, title)
                    if is_time_up and send_email or i == 0:
                        for email in emails:
                            email.set_email(subject="Feeds on %s"%(str(datetime.datetime.now())), content='Status: %s'%title)
                    if MONITORED_TITLE in title and not is_checked and send_email:
                        is_checked = True
                        for email in emails:
                            email.set_email(subject="Status has been updated!", content='Status: %s'%title)
                            email.send_email()

        except:
            print_info(i + 1, es.text)
            print(is_time_up)
            if is_time_up and send_email or i == 0:
                for email in emails:
                    email.set_email(subject="Feeds on %s"%(str(datetime.datetime.now())), content='Status: %s'%es.text)
                    # email.send_email()
                    #sg_email.send_feed(datetime.datetime.now(), es.text)
            if not is_checked and MONITORED_TEXT not in es.text  and send_email or i == 0:
                is_checked = True
                for email in emails:
                    email.set_email(subject="Status has been updated!", content='Status: %s'%es.text)
                    email.send_email()
                #sg_email.send_email(es.text)
    except Exception as e:
        print(e)

def crawl(driver, duration=60):
    i = 0
    email = SendGridEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject="", content="")
    while(True):
        reciever_emails_address = email_fetcher.get_all_users()
        emails = [SendGridEmail(sender=SENDER_EMAIL, receiver=r, subject="", content="") for r in reciever_emails_address]
        crwaler_helper(driver=driver, i=i, send_email=True, emails=emails)
        i += 1
        time.sleep(duration)
    driver.close()  

