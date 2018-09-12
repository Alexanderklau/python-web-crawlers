#encoding: utf-8

import scrapy
import re
from scrapy.selector import Selector
from ..items import WynewsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class ExampleSpider(CrawlSpider):
    name = "news"
    allow_domains = ["tech.163.com"]
    start_urls = ['http://tech.163.com']
    rules = (
        Rule(LinkExtractor(allow=r"/14/08\d+/\d+/*"),
        callback = "parse_news",follow=True),
    )

    def printcn(suni):
        for i in suni:
            print(suni.encode('utf-8'))

    def parse_news(self,response):
        item = WynewsItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:-5]
        self.get_title(response, item)
        self.get_source(response, item)
        self.get_url(response, item)
        self.get_news_from(response, item)
        self.get_from_url(response, item)
        self.get_text(response, item)
        return item

