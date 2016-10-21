# -*- coding: UTF-8 -*-

from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import random

def load_html(url):
    ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110']
    header = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
              'X-Forwarded-For':ip[random.randint(0, 2)]}
    request = Request(url, None, header)
    response = urlopen(request)
    return response.read()

def find_html(url,html):
    data = {}
    soup = BeautifulSoup(html,"html.parser")
    body = soup.find('div',id='newsContent03')
    data['body'] = body.get_text()
    return data

def output_html(data):
    print(data['body'])

if __name__ == '__main__':
    url = "http://www.qq.com"
    html = load_html(url)
    data = find_html(url,html)
    output_html(data)






