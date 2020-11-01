import sys
import os
import io
from guangxi_by_sxp.utils import add_unique_index

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from scrapy.utils.project import get_project_settings
from guangxi_by_sxp.spiders.universal import UniversalSpider
from guangxi_by_sxp.utils import get_config
from scrapy.crawler import CrawlerProcess
from guangxi_by_sxp import settings as init_settings


def run():
    # 传入一个参数：网站名称
    name = sys.argv[1]
    custom_settings = get_config(name)
    # 为数据库添加唯一值索引
    add_unique_index([name])
    spider = custom_settings.get('spider')
    # spider = 'enter-navigations'
    project_settings = get_project_settings()
    try:
        if init_settings.LOG_TO_FILE is True:
            project_settings.update({"LOG_FILE": name+".log"})
    except:
        pass
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start(stop_after_crawl=False)


if __name__ == '__main__':
    run()
