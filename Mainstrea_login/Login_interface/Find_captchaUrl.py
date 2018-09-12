#-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://210.41.224.117/Login/xLogin/Login.asp")
chart = driver.page_source
bsObj = BeautifulSoup(chart)
captcha = bsObj.findAll("img")
