import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'list.jd.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
url = 'https://list.jd.com/list.html?cat=9987,653,655&page=1'
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)
drive = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs',
                            desired_capabilities=dcap)

print(drive.get(url))

# soup = BeautifulSoup(wb_data.text,'lxml')
# name = soup.select('div.p-name > a > em')
# price = soup.select('strong.J_price > i')
# print(soup)
# name = soup.select('div.p-name em')

