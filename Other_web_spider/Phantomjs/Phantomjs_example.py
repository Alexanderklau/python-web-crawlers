# coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
url = driver.get('http://pic.ali213.net/list/dongman/')
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
driver.execute_script(js)
time.sleep(3)
driver.execute_script(js)
time.sleep(3)
html = driver.page_source
Bsobj = BeautifulSoup(html)
for link in Bsobj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])



