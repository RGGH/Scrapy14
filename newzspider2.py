#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request
import sys
sys.path.insert(0,'..')
from items import NewzzItem

class newzspider2(scrapy.Spider):

    name = 'newzspider2'
    start_urls = ['https://www.express.co.uk/']
    download_delay = 10 
    
    headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'accept-encoding': 'gzip,', 
    'accept-language': 'en-US,en;q=0.9', 
    'cache-control': 'max-age=0', 
    'cookie': '_cb_ls=1;', 
    'sec-fetch-dest': 'document', 
    'sec-fetch-mode': 'navigate', 
    'sec-fetch-site': 'cross-site', 
    'sec-fetch-user': '?1', 
    'upgrade-insecure-requests': '1', 
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    
    #custom_settings = {'FEEDS':{'results2.csv':{'format':'csv'}}}  # replace with MySQL
    
    def start_request (self):
        request = Request(start_urls, headers=headers, callback=self.parse)
        yield request
          
        
    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        
        # get links for most popular articles
        links = response.xpath('//h4/text()').getall()
        print(links[:5])
#            url = (link.get())
#            yield Request(url)            
#
#    def parse_detail(self, response, url):
#        
#        title = response.xpath('//*[@itemprop="headline"]/text()').get()
#        story = response.xpath('//p/text()').getall()
#        url = url
#
#        yield {'title' : title, 'story' : story, 'url' : url}

# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider2)
    process.start()
