from scrapy.item import Item, Field

class Article(Item):
    title = Field()
    url = Field()
    story = Field()
