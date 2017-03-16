# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from urllib import request

def download(url,num_retries=2,user_agent = 'wswp'):
    print('Downloading:',url)
    headers = {'User-agent:',user_agent}
    requests = request.Request(url,headers = headers)
    try:
        html = request.urlopen(requests).read()
    except request.URLError as e:
        print('Download error:',e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url,user_agent,num_retries-1)
    return html










# if __name__ == '__main__':