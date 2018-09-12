# -*- coding: utf-8 -*-
import scrapy
from ..items import sinaItem
class DmozSpider(scrapy.Spider):

    name = "sina"
    allowed_domians = ["sina.com"]
    start_urls = [
        "http://www.sina.com.cn/",]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = sinaItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item


    def parse_dir_contents(self,response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url,href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)

        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

        # for sel in response.xpath('//ul/li'):
        #     item = DomzItem()
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     yield item
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
         #   f.write(response.body)
