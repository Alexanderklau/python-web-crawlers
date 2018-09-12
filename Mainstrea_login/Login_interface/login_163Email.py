from selenium import webdriver
from urllib.request import urlopen
import time

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
time.sleep(3)
print(driver.get('http://mail.163.com'))
driver.close()