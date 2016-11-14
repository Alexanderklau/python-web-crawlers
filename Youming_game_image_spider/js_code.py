from selenium import webdriver
import time

drive = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
drive.get("http://www.mmkao.net/")
time.sleep(10)
print(drive.find_element_by_id('content').text)
drive.close()