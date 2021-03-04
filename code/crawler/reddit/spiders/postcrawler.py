import scrapy
from scrapy.selector import Selector

from reddit.items import RedditItem


class PostcrawlerSpider(scrapy.Spider):
    name = 'postcrawler'
    allowed_domains = ['www.techcrunch.com/startups/']
    start_urls = ['https://techcrunch.com/startups/']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    custom_settings = {
        'DEPTH_LIMIT': 10
    }

    def parse(self, response):
        
        title = response.xpath('//h2/a/text()').extract()
        author = response.xpath('//span/a/text()').extract()
        date = response.xpath('//div/time/text()').extract()
        for (title, author, date) in zip(title, author, date):
            
            post = RedditItem()
            post['title'] = title
            post['author'] = author
            post['date'] = date
            
            yield post
                  
        next_page = response.css('.load-more::attr(href)').extract()[0]
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)