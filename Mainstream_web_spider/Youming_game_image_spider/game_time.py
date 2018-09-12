from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://pic.ali213.net/list/tagList/4.html")
time.sleep(7)
driver.get_screenshot_as_file("1.jpg")
driver.close()