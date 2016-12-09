from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random,time
url = 'http://www.ali213.net/'
browser = webdriver.Firefox()
browser.get(url)
time.sleep(3)
browser.maximize_window()
browser.quit()