import crawler

driver = crawler.init_driver()
crawler.crawl(driver=driver, duration=60)