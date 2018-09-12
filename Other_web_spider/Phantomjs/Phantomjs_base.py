# coding = utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://github.com/Alexanderklau')
print(driver.title)
driver.quit()