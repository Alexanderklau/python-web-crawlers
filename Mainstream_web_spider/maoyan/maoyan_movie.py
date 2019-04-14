# coding: utf-8

__author__ = "lau.wenbo"


import requests
from requests.exceptions import RequestException
import re
import time
import json

"""
获取到页面信息，并且爬取
"""

def get_url_page(url):
    try:
        headers = {
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_url_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*data-src="(.*?)".*?name">')
    return pattern

def write_file(text):
    with open('resule.txt', "a+", encoding='utf-8') as f:
        f.write(text)


def main():
    url = 'https://maoyan.com/board/4?offset=0'
    html = get_url_page(url=url)
    write_file(html)

main()
