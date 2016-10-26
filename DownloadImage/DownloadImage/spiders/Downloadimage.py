# coding=utf-8
import scrapy
import re
import os
import urllib
from urllib.request import urlretrieve
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request

class Girl_spider(scrapy.spiders.Spider):
    name = "Girl"
    allowed_domains = ["pic.yesky.com"]

    start_urls = ["http://pic.yesky.com/c/6_20498_1.shtml"]
    def parse(self,response):
        currnet_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        hxs = Selector(response)
        if re.match('http://pic.yesky.com/c/6_20498_\d+.shtml',response.url):
            items = hxs.xpath('//div[@class="lb_box"]/dl')
            for i in range(len(items)):
                src = hxs.xpath('//div[@class="lb_box"]/dl/dt/img/@src' % i).extract
                name = hxs.xpath('//div[@class="lb_box"]/dl/dd/a/text()' % i).extract()
                if src:
                    absoluteSrc = "http://pic.yesky.com" + src[0]
                    file_name = "%s.jpg" %(name[0])
                    file_path = os.path.join("/home/lau/PycharmProjects/python-web-crawlers/DownloadImage/Download",file_name)
                    urlretrieve(absoluteSrc,file_path)

            all_urls = hxs.xpath('//a/@href').extract()
            for url in all_urls:
                if url.startswith('http://pic.yesky.com/c/6_20498_'):
                    yield Request(url,callback=self.parse)
