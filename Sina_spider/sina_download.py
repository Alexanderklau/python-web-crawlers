# -*- coding: UTF-8 -*-  

import random
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def parser(url, html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    # <span property="v:summary" class="">
    summary = soup.find('div', id="syncad_0")

    data['summary'] = summary.get_text()

    return data

def download_html(url):
    ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110']
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'X-Forwarded-For': ip[random.randint(0, 2)]}
    request = Request(url, None, header)
    response = urlopen(request)
    return response.read()


def output(data):
    fout = open("output.txt", "w")
    fout.write("%s" % data['summary'])
    fout.close()


if __name__ == "__main__":
    url = "http://www.sina.com.cn/"
    html = download_html(url)
    data = parser(url, html)
    output(data)