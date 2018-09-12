# coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com/")
browser.find_element_by_name("wd").send_keys("Python")
time.sleep(20)
browser.quit()