# coding:utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_link_text("贴吧").click()
browser.find_element_by_id("")
browser.implicitly_wait(30)
browser.quit()