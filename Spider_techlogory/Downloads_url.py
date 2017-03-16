# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from urllib import request

def download(url):
    print('Downloading:',url)
    try:
        html = request.urlopen(url).read()
    except request.URLError as e:
        print('Download Error:',e.reason)
        html = None
    return html
if __name__ == '__main__':
    download('https://1234')