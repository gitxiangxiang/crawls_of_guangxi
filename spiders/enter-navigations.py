from scrapy.spiders import CrawlSpider, Rule
from guangxi_by_sxp.utils import get_config
from guangxi_by_sxp.rules import rules
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from guangxi_by_sxp import settings as init_settings


class EnterNavigationsSpider(CrawlSpider):
    name = 'enter-navigations'
    # allowed_domains = ['navigations.com']
    # start_urls = ['http://navigations.com/']

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.spider_name = name
        self.config = config
        self.rules = rules.get(config.get('rules')).get('navigations')
        self.start_urls = config.get('start_urls')
        self.allowed_domains = config.get('allowed_domains')
        self.spider_cnt = 1
        super(EnterNavigationsSpider, self).__init__(*args, **kwargs)

    def gen_spider(self, response):
        url = response.url
        print(url)
        spider_name = self.spider_name+'_'+str(self.spider_cnt)
        self.spider_cnt = self.spider_cnt + 1
        project_settings = get_project_settings()
        try:
            if init_settings.LOG_TO_FILE is True:
                project_settings.update({"LOG_FILE": self.spider_name + ".log"})
        except:
            pass
        settings = dict(project_settings.copy())
        # 合并配置
        settings.update(self.config.get('settings'))
        process = CrawlerProcess(settings)
        # 启动爬虫
        process.crawl('universal', **{'name': self.spider_name, 'uniq_name': spider_name, 'start_urls': [url]})
        # process.start()
        self.logger.info("spider："+spider_name+" 启动")
        return None
