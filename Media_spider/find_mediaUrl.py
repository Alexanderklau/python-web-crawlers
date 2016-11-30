#-*-coding:utf-8-*-
from urllib.request import urlopen,urlretrieve,Request
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
url = "http://open.163.com/special/opencourse/magazinewriting.html"
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get(url)
print(driver.find_element_by_id('content').text())
driver.close()