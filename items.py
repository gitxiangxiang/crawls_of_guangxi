# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinhphuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title = scrapy.Field()
    public_date = scrapy.Field()
    news_content = scrapy.Field()
    site = scrapy.Field()
    author = scrapy.Field()
    media = scrapy.Field()
    type = scrapy.Field()
    abstract = scrapy.Field()
    url = scrapy.Field()
    sourceContent = scrapy.Field()


