import scrapy
from ..items import DomzItem
class DmozSpider(scrapy.Spider):
    name = "domz"
    allowed_domians = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",]

        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)

    def parse_dir_contents(self,response):
        for sel in response.xpath('//ul/li'):
            item = DomzItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

        # for sel in response.xpath('//ul/li'):
        #     item = DomzItem()
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     yield item
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
         #   f.write(response.body)
