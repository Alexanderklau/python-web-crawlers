# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import requests

url = 'http://123.com/seadr'
params = {
    'pn':1,
    'rn':20,
}
r = requests.get(url,params=params)
print(r.url)

#http://image.baidu.com/search/index
# ?ct=&z=&tn=baiduimage&ipn=r&word=%E9%A3%8E%E6%99%AF&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=&lm=-1&st=-1&fr=&fmq=1459502303089_R&ic=0&se=&sme=&width=1920&height=1080&face=0





# if __name == '__main__':