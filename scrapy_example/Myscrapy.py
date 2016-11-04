import scrapy
class mySpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['tieba.baidu.com']
    start_urls = [
        'http://tieba.baidu.com',
    ]

    def parse(self, response):
        #self.logger.info('A response from %s just arrived!',response.url)
        for h3 in response.xpath('//h3').extrace():
            yield { "title" : h3}
        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url,callback=self.parse)