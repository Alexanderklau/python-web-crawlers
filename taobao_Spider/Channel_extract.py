import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

start_urls = 'https://www.taobao.com/tbhome/page/market-list'
uaList = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586']
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (uaList)

def Find_urls(url):
    driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs',
                                 desired_capabilities=dcap)
    driver.get(start_urls)
    wb_data = driver.page_source
    soup = BeautifulSoup(wb_data)
    links = soup.select('div.category-items > a')
    for link in links:
        href = link.get_text()
        url = link.get('href')
        data = {
            'Name' : href,
            'Link' : url,
        }
        print(data)
Find_urls(start_urls)

