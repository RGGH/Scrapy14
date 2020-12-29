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

class newzspider2(scrapy.Spider):

    name = 'newzspider2'
    start_urls = ['https://www.express.co.uk/']
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip,', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'cache-control': 'max-age=0', 'cookie': '_ga=GA1.3.1482438053.1609251185;', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    def start_request (self):
        request = Request(start_urls, headers=headers, callback=self.parse)
        yield request

    def parse(self, response):
    
        items = NewzzItem()
        
        links = response.xpath("//a/@href").getall()
    
        # Just send the URL to INSERT MySQL initially to test if pipelines work
        # use dummy values for others
        for url in links[30:40]:
            items['url'] = url
            items['author'] = "author"
            items['story'] = "story"
            items['title'] = "title"
            yield items
            

# main driver
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(newzspider2)
    process.start()
