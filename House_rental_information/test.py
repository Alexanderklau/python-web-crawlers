from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://210.41.224.117/Login/xLogin/Login.asp")
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj)
