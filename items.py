#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy


class NewzzItem(scrapy.Item):

    publication = scrapy.Field()
    headline = scrapy.Field()
    author = scrapy.Field()
    story = scrapy.Field()
