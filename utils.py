from os.path import realpath, dirname
import json
import logging
import pymongo
import threading
import datetime
from guangxi_by_sxp.settings import MONGO_DB, MONGO_URL
# logging.basicConfig(filename='guangxi.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')


def get_config(name):
    path = dirname(realpath(__file__)) + '/spiders/website_config/' + name + '/config.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


# 日志装饰器
def logger(fn):
    def logger_in(*args):
        logging.info("begin")
        result = fn(*args)
        logging.info("end")
        return result
    return logger_in


def add_unique_index(collections):
    """
    为每个集合的url字段添加唯一值索引，确保不出现重复文章。
    collections为集合的列表
    """
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    collist = db.list_collection_names()
    for collection in collections:
        if collection not in collist:
            db[collection].create_index([('url', pymongo.ASCENDING)], unique=True)


def synchronized(func):
    """
    线程加锁
    """
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


def singleton(cls):
    """
    单例模式
    """
    instances = {}

    @synchronized
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


@singleton
class SpiderCounter:
    """
    爬虫计数器，用于关闭twisted引擎
    """
    spider_cnt = 0

    def open_spider(self):
        self.spider_cnt  = self.spider_cnt + 1

    def close_spider(self):
        self.spider_cnt  = self.spider_cnt - 1
        if self.spider_cnt == 0:
            from twisted.internet import reactor
            try:
                reactor.stop()
            except RuntimeError:  # raised if already stopped or in shutdown stage
                pass


def create_date_list(date_start=None, date_end=None, format='%Y%m%d'):
    """
    生成日期列表
    format表示日期格式
    """

    if date_start is None:
        date_start = '20200101'
    if date_end is None:
        date_end = datetime.datetime.now().strftime(format)

    # 转为日期格式
    date_start = datetime.datetime.strptime(date_start, format)
    date_end = datetime.datetime.strptime(date_end, format)
    date_list = [date_start.strftime(format)]
    while date_start < date_end:
        # 日期叠加一天
        date_start += datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(date_start.strftime(format))
    return date_list
