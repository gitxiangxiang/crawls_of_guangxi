import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from scrapy.utils.project import get_project_settings
from guangxi_by_sxp.spiders.universal import UniversalSpider
from guangxi_by_sxp.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():

    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()
