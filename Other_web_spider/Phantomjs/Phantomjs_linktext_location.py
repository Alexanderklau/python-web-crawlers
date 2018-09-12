# coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
#browser.find_element_by_link_text("贴吧").click()
browser.find_element_by_partial_link_text("贴").click()
time.sleep(20)
browser.quit()
