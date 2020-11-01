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
        spider.crawler.engine.close_spider(spider, 'closespider')
        return item


class DateParsePipeline:
    pass


class MongoPipeline:
    """
    将数据存到mongoDB中
    """
    def __init__(self, mongo_url, mongo_db, user, password, collection):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        self.user = user
        self.password = password
        # self.mongo_collection = collection
        self.expired_cnt = 0  # 当前过期和重复文章数
        self.max_drop = 100  # 最大过期和重复文章数，超出即停止爬取

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            user=crawler.settings.get('USER'),
            password=crawler.settings.get('PASSWORD'),
            collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_url)
        self.db = self.client[self.mongo_db]
        # self.collection = self.db[self.mongo_collection]

    def process_item(self, item, spider):
        # 每个网站的文章持久化到各自的集合中，集合名对应于‘media’字段的值
        # 由于设计原因，请保持‘media’字段的值与网站名称相同。
        mongo_collection = self.db[item['media']]
        try:
            item['news_title']
        except:
            return DropItem('invalidate article')
        if item['news_title'] != '' and item['news_title'] is not None:
            try:
                try:
                    item['public_date'] = datetime.datetime.strptime(item['public_date'], DatetimeParse[item['media']])
                except Exception as e:
                    item['public_date'] = datetime.datetime.now()
                # 如果积攒了足够多（多于100篇）往年的文章，就自动停止抓取。
                if item['public_date'].year < datetime.datetime.today().year:
                    self.expired_cnt = self.expired_cnt + 1
                    spider.logger.info('----------'+str(self.expired_cnt)+'过期-----------')
                    if self.expired_cnt > self.max_drop:
                        spider.crawler.engine.close_spider(spider, '最新数据爬取完毕')
            except Exception as e:
                spider.logger.info('无时间属性')
                return item
                # return DropItem('lack of date')
            try:
                mongo_collection.insert_one(dict(item))
            except:
                self.expired_cnt = self.expired_cnt + 1
                spider.logger.info('----------'+str(self.expired_cnt)+'重复-----------')
                if self.expired_cnt > self.max_drop:
                    spider.crawler.engine.close_spider(spider, '最新数据爬取完毕')
            return item
        else:
            return DropItem('invalidate article')


