# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
time.sleep(3)
driver.maximize_window()

driver.find_element_by_id("lbNormal").click()
time.sleep(3)

driver.find_element_by_class_name("u-input box").send_keys("13281101982")
time.sleep(3)

driver.find_element_by_name("j-inputtext dlpwd").send_keys("lwb13999510103")
driver.find_element_by_id("dologin").send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()