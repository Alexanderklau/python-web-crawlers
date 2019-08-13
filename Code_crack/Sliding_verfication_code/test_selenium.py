# coding: utf-8

__author__ = 'lau.wenbo'


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


EMAIL = "test@test.com"
PASSWORD = '123456'


class CrackGeettest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button


if __name__ == "__main__":
    z = CrackGeettest()
    x = z.get_geetest_button()
    x.click()