from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://hotel.qunar.com/")
data = driver.title
print(data)