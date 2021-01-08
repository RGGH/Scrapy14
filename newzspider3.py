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

class newzspider3(scrapy.Spider):

    name = 'newzspider3'
    start_urls = ['https://www.independent.co.uk/']
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip,',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

    def start_requests (self):
        request = Request(url='https://www.independent.co.uk', headers=self.headers, callback=self.parse,dont_filter=True)
        yield request

    def parse(self, response):
    
        items = NewzzItem()
        
        links = response.xpath('//a/@href').getall()

        for url in links[20:30]:
            items['url'] = url
            items['publication'] = 'independent'
            items['author'] = 'author'
            items['story'] = 'story'
            items['title'] = 'title'
            yield items


# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider3)
    process.start()
