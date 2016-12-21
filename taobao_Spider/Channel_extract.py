import requests
from bs4 import BeautifulSoup
start_urls = 'https://www.taobao.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
}
def Find_urls(url):
    wb_data = requests.get(start_urls,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    print(soup)
Find_urls(start_urls)

