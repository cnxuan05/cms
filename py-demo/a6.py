import scrapy
# conda install -c scrapinghub scrapy

class StackOverflowSpider(scrapy.Spider):

    name = 'stackoverflow'
    start_urls = ['https://stackoverflow.com/questions?sort=votes']
    # start_urls = ['http://www.zaobao.com/finance/realtime']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
        #for href in response.css('.section-sub-list h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }