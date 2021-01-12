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
    allowed_domains =["independent.co.uk"]
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
        # use not contains to exclude voucher offers! 
        links = response.xpath('//a[@class="title"][not(contains(@href,"https://www.independent.co.uk/vouchercodes"))]/@href')
        for url in links:     
            url = url.get()
            print(url)
            next_page = url
            if next_page:
                yield response.follow(next_page, headers=self.headers, callback=self.parse_details)
        
    def parse_details(self, response):
    
        items = NewzzItem()
        
        try:
            story = response.xpath('//p/text()').get()
        except:
            pass
           
        title = response.xpath('//h1/text()').get()
            
        print("\n")
        print("######")
        print(story)
        url = response.url
        print(url)
        
        items['publication'] = self.allowed_domains[0]
        
        if title:
            items['title'] = title
        else:
            items['title'] = 'no title'

        # use 2 predicates together to single out the Author name
        try:
            items['author'] = response.xpath('//*[@id="articleHeader"]//a[contains(@href,"/author/")]/text()')[0].get()
        except:
            pass
        items['story'] = story
        items['url'] = url

        yield items
                
# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider3)
    process.start()
