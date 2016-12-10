from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.title)
driver.quit()
