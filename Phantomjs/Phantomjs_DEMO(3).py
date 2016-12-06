from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get("http://www.quanshu.net/")
time.sleep(3)
print(driver.find_element_by_id("container").text)
driver.close()