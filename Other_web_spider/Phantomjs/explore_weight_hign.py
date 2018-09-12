# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com/")
time.sleep(2)

print("explore height 480,weight 800")
browser.set_window_size(480,800)
time.sleep(3)
browser.quit()
