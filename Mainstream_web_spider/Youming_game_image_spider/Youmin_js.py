#-*- coiding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get('http://pic.ali213.net/')
time.sleep(3)
chart = driver.page_source
bsObj = BeautifulSoup(chart)
print(bsObj)

