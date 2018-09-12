# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup


def parser(url, html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    # <span property="v:summary" class="">
    artibody = soup.find('section', id="artibody")

    data['artibody'] = artibody.get_text()
    return data


def download_html(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


def output(data):
    fout = open("output.txt", "w")
    fout.write("%s" % data['artibody'].encode('utf8'))
    fout.close()


if __name__ == "__main__":
    url = "http://news.sina.com.cn/c/2016-10-19/doc-ifxwvpqh7848254.shtml"
    html = download_html(url)
    data = parser(url, html)
    output(data)