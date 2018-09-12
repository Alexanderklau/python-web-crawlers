import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            fill_url = response.urljoin(href.extract())
            yield scrapy.Request(fill_url,callback=self.parse_question)

    def parse_question(self,response):
        yield {
            'title': response.css('h1 a::text ').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body' : response.css('.question .post-text').extract_first(),
            'tags' : response.css('.question .post-tag::text').extract(),
            'link' : response.url,
        }