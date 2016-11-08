#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
from urllib.request import urlopen,urlretrieve
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'#正则表达式，得到图片地址
    imgre = re.compile(reg) #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html) #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    for imgurl in imglist:
        urlretrieve(imgurl,'/home/lau/PycharmProjects/python-web-crawlers/girlspider/down' % x)
        x+=1


html = getHtml("http://www.mmkao.net/Sityle/2.html")
print(getImg(html))