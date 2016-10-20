# -*- coding:utf-8 -*-
import scrapy
import re
import os
import urllib
from urllib.request import urlretrieve
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request

class Xiaohuar_spider(scrapy.spiders.Spider):

    name="girl"#定义爬虫名

    allowed_domains=["xiaohuar.com"]    #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页

    start_urls=["http://www.xiaohuar.com/list-1-1.html"]

    #该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        current_url=response.url    #爬取时请求的url
        body=response.body  #返回的html
        unicode_body=response.body_as_unicode() #返回的html unicode

        hxs=Selector(response) #创建查询对象，HtmlXPathSelector已过时

        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):#如果url能够匹配到需要爬取的url，就爬取
            items=hxs.xpath('//div[@class="item_list infinite_scroll"]/div')#匹配到大的div下的所有小div（每个小div中包含一个图片）

            for i in range(len(items)):#遍历div个数
                src=hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src'%i).extract() #查询所有img标签的src属性，即获取校花图片地址
                name=hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()'%i).extract() #获取span的文本内容，即校花姓名
                school=hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()'%i).extract()#校花学校

                if src:
                    absoluteSrc="http://www.xiaohuar.com"+src[0] #拼接实际路径,因为.extract()会返回一个list，但是我们是依次取得div，所以是取第0个
                    file_name="%s_%s.jpg"%(school[0],name[0])#拼接文件名，学校_姓名
                    file_path=os.path.join("/home/lau/PycharmProjects/python-web-crawlers/GIrl/image",file_name)#拼接这个图片的路径，我是放在F盘的pics文件夹下
                    urlretrieve(absoluteSrc,file_path)#接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径

            all_urls = hxs.xpath('//a/@href').extract()#提取界面所有的url
            for url in all_urls:#遍历获得的url，如果满足条件，继续爬取
                if url.startswith('http://www.xiaohuar.com/list-1-'):
                    yield Request(url, callback=self.parse)