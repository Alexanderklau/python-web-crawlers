# coding: utf-8

__author__ = "lau.wenbo"


import requests

r = requests.get("http://www.baidu.com/")
# 下载图像

headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:63.0) Gecko/20100101 Firefox/63.0",

}
c = requests.get("https://www.zhihu.com/explore",headers=headers)
print(c.text)
z = requests.get("http://github.com/favicon.ico")
with open("favicon.ico", "wb") as f:
    f.write(z.content)



