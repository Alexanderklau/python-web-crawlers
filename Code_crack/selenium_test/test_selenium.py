# coding: utf-8

__author__ = "lau.wenbo"

from selenium import webdriver
import time

path = "/Users/yemilice/Desktop/work/python-web-crawlers/Code_crack/chromedriver/chromedriver"
driver = webdriver.Chrome(path)
url = "https://www.baidu.com"
driver.get(url)
time.sleep(2)
driver.find_element_by_id('kw').send_keys('site:zjj7.com')
driver.find_element_by_id('su').click()
time.sleep(2)
result = driver.find_element_by_xpath("//div[@class='result c-container ']/h3/a")
result.click()
time.sleep(20)
driver.close()