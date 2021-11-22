from selenium import webdriver
import time
import send_email
import os
def print_info(t, text):
    print('[FETCH: %d]: %s' %(t, text))
    
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

def crawl(driver, duration=5, iter_time=10):
    for i in range(iter_time):
        driver.get("https://www.apple.com/tw/macbook-pro/")
    es = driver.find_element_by_class_name('typography-body')
    try:
        iterator = iter(es)
        for e in es:
            print_info(i + 1, e.text)
    except:
        print_info(i + 1, es.text)
        if es.text == '推出日期，敬請期待。':
            send_email.send_email()
    time.sleep(duration)
    driver.close()  