#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy
from items import Article
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser
from scrapy import Request

class newzspider(scrapy.Spider):
    name = 'newzspider'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/uk/']
    custom_settings = {'FEEDS':{'results1.csv':{'format':'csv'}}} # replace with MySQL

    def parse(self, response):

        # get links for 8 most popular articles
        links = response.xpath('//*[@class="most-popular__item tone-news--most-popular fc-item--pillar-news"]/a/@href')
        for link in links:
            url = (link.get())
            yield Request(url, callback=self.parse_detail, cb_kwargs={'url': url})            

    def parse_detail(self, response, url):
        
        title = response.xpath('//*[@itemprop="headline"]/text()').get()
        story = response.xpath('//p/text()').getall()
        url = url

        yield {'title' : title, 'story' : story, 'url' : url}

# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider)
    process.start()
