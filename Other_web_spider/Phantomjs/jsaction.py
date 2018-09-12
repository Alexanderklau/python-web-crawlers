# coding=utf-8

from selenium import webdriver
import os,time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://mail.163.com/?msg=authfail#return")
time.sleep(3)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.findAll('password'))

