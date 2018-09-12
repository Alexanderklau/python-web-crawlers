from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_xpath("//input[@id='kw']").send_keys("python")
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()