import scrapy
class SinaSpider(scrapy.Spider):
    name = "Sina"
    allowed_domains = ["sina.com"]
    start_urls = [
        "http://www.sina.com.cn/",
    ]

    def parse(self,response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print(title ,link , desc)