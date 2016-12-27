import requests
from bs4 import BeautifulSoup
from selenium import webdriver

start_urls = 'http://cd.zu.anjuke.com/'
def Find_url():
    wb_data = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
    wb_data.get(start_urls)
    pageSource = wb_data.page_source
    soup = BeautifulSoup(pageSource,'lxml')
    areaUrl = soup.select('span.elems-l > a')
    print(areaUrl)
    # for link in areaUrl:
    #     href = link.get('href')
    #     print(href)




Find_url()
