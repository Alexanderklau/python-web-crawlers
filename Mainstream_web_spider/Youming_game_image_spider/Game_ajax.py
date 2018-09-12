from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://pic.ali213.net/list/tagList/4.html")
time.sleep(3)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.find("div",{"class":"ALi_m"}).get_text())