# coding = utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")


browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()
browser.quit()