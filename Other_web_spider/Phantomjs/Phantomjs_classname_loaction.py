# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_class_name("s_ipt").send_keys("Python")
browser.implicitly_wait(60)
browser.quit()
