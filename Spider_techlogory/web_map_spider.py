# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import re
from urllib import request
def download(url):
    print('Downloading:',url)
    try:
        html = request.urlopen(url).read()
    except request.URLError as e:
        print('Download Error:',e.reason)
        html = None
    return html
def crawl_sitemap(url):
    sitemap = download(url)
    # <a class="" page-data="1" target="_blank" suda-uatrack="key=index_new_guess&value=c_click" href="\d" title="\d">()\d</a>
    links = re.findall('<a class="" page-data="1" \d>(\d)</a>',sitemap)
    for link in links:
        html = download(link)
if __name__ == '__main__':
    crawl_sitemap('http://www.sina.com.cn/')