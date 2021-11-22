from selenium import webdriver
import time

def print_info(t, text):
    print('[FETCH: %d] %s' %(t, text))

driver = webdriver.Chrome('./chromedriver')

for i in range(10):
    driver.get("https://www.apple.com/tw/macbook-pro/")
    es = driver.find_element_by_class_name('typography-body')
    try:
        iterator = iter(es)
        for e in es:
            print_info(i + 1, e.text)
    except:
        print_info(i + 1, es.text)
    time.sleep(2)
driver.close()

