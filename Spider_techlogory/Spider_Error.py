# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from urllib import request

def download(url,num_retries=2):
    print('Downloading:',url)
    try:
        html = request.urlopen(url).read()
    except request.URLError as e:
        print('Download Error:',e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 400 <= e.code < 600:
                return download(url,num_retries-1)
    return html
if __name__ == '__main__':
    download('https://www.google.com')









# if __name__ == '__main__':