                              |___/    

import scrapy
from items import Article
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser
from scrapy import Request

class newzspider(scrapy.Spider):
    name = 'newzspider'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/uk/']
    custom_settings = {'FEEDS':{'results1.csv':{'format':'csv'}}}

    def parse(self, response):

        # get links for 8 most popular articles
        links = response.xpath('//*[@class="most-popular__item tone-news--most-popular fc-item--pillar-news"]/a/@href')
        for link in links:
            url = (link.get())
            yield Request(url, callback=self.parse_detail)            
#            article = Article()
#            article['link'] = link.get()
#            yield article

    def parse_detail(self, response):
        
        title = response.xpath('//*[@itemprop="headline"]/text()').get()
        story = response.xpath('//p/text()').getall()
        yield {'title' : title, 'story' : story}

# main driver

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider)
    process.start()
