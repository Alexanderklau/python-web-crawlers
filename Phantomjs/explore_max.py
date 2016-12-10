from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://baidu.com")
print("最大化浏览器")
browser.maximize_window()
time.sleep(2)

browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()