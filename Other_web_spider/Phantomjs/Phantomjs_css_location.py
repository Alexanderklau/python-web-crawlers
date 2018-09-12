from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_css_selector("#kw").send_keys("Python")
time.sleep(30)
browser.quit()