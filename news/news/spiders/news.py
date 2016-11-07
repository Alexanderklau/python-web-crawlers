import scrapy
from ..items import newsItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"    #唯一标识，启动spider时即指定该名称
    #allowed_domains = ["jiu-tuo.com"]
    start_urls = [
        #"http://www.sina.com.cn/"
        #"http://www.qq.com/"
        "http://www.jiu-tuo.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = newsItem()
            item['Phone'] = sel.xpath('a/@href').extract()
            item['name'] = sel.xpath('span/a/@href').extract()
            #item['phone'] = sel.xpath('//td[@class="stdrt show65"]').extract()
            #item['goby'] = sel.xpath('//td[@class="stdrt show48"]').extract()
            yield item

    def parse_dir_contents(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)