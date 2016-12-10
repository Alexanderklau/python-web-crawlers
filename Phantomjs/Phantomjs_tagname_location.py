# coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com/")
browser.find_element_by_tag_name("input").send_keys("python")
time.sleep(30)
browser.quit()