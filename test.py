import crawler

driver = crawler.init_driver()
crawler.crawl(driver=driver, duration=5, iter_time=1)