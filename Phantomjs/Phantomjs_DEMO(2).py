from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.set_window_size(1120, 550)
driver.get("http://www.quanshu.net/")
driver.find_element_by_id('search_form_input_homepage').send_keys("Nirvana")
driver.find_element_by_id("search_button_homepage").click()
print(driver.current_url)
driver.close()  