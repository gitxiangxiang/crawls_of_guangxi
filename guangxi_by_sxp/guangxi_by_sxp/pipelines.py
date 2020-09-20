# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymongo
import datetime
from guangxi_by_sxp.settings import DatetimeParse


class GuangxiBySxpPipeline:
    def process_item(self, item, spider):
        return item


class DateParsePipeline:
    pass


class MongoPipeline:
    """
    将数据存到mongoDB中
    """
    def __init__(self, mongo_url, mongo_db, collection):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        self.mongo_collection = collection
        self.expired_cnt = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def process_item(self, item, spider):
        try:
            item['news_title']
        except:
            return DropItem('invalidate article')
        if item['news_title'] != '' and item['news_title'] is not None:
            try:
                item['public_date'] = datetime.datetime.strptime(item['public_date'], DatetimeParse[item['media']])
                self.expired_cnt = self.expired_cnt + 1
                print('----------', self.expired_cnt, '-----------')
            except Exception as e:
                print('无时间属性')
            self.collection.insert(dict(item))
            return item
        else:
            return DropItem('invalidate article')


