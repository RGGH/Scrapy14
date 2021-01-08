#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request
from scrapy.loader import ItemLoader
import sys
sys.path.insert(0,'..')
from items import NewzzItem

class newzspider(scrapy.Spider):

    name = 'newzspider'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/uk/']

    def parse(self, response):

        # get links for 8 most popular articles
        links = response.xpath('//*[@class="most-popular__item tone-news--most-popular fc-item--pillar-news"]/a/@href')
        for link in links:
            url = (link.get())
            yield Request(url, callback=self.parse_detail, cb_kwargs={'url': url})            

    def parse_detail(self, response, url):
    
        items = NewzzItem()
        
        title = response.xpath('//*[@itemprop="headline"]/text()').get()
        story = response.xpath('//p/text()').getall()
        url = url
        
        items['publication'] = self.allowed_domains[0]
        
        if title:
            items['title'] = title
        else:
            items['title'] = 'no title'
        items['publication'] = 'theguardian'    
        items['author'] = 'author'
        items['story'] = story[0]
        items['url'] = url
                     
    #Todo : 
        yield items

# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider)
    process.start()
    
    
