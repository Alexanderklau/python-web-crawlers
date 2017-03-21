# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from urllib.request import *
from urllib.parse import *
from http import cookiejar
from bs4 import BeautifulSoup

#设置代理IP
# proxy_support = ProxyHandler({'http':'120.197.234.164:80'})


#设置cookie
cookie_support = HTTPCookieProcessor(cookiejar.LWPCookieJar())
opener = build_opener(cookie_support,HTTPHandler)
install_opener(opener)

#开始的URL
#hosturl = "http://www.renren.com"
hosturl = "http://mail.163.com/"

#接受表单数据的URL
#posturl = "http://www.renren.com/ajaxLogin/login"
posturl = "https://mail.163.com/entry/cgi/ntesdoor?df=mail163_letter&from=web&funcid=loginone&iframe=1&language=-1&passtype=1&product=mail163&net=e&style=-1&race=118_35_39_bj&uid=Thinkgamer@163.com"

#发送表单数据
postdata = urlencode(
    {
    "username":"13281101982@163.com",
    "password":"lwb13999510103"
    }
)

#设置表头
headers = {
    #'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0/',
    #'Referer':'http://www.renren.com/'
    'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
    'Referer':'http://mail.163.com/'
}

#生成HTTP请求
req =Request(
    url = posturl,
    data = postdata,
    headers = headers
)
print (req)
page = urlopen(req).read()
print (page)

listvalue = page.split(";")

url = listvalue[0].split("op.location.href = ")[1]
href = url[1:-1]
print (href)
soup = BeautifulSoup(urlopen(href))
print (soup.title)









# if __name__ == '__main_