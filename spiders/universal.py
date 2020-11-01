import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from guangxi_by_sxp.utils import get_config
from guangxi_by_sxp.rules import rules
from guangxi_by_sxp.items import ChinhphuItem
from guangxi_by_sxp.loaders import ChinhphuLoader


class UniversalSpider(CrawlSpider):
    name = 'universal'
    # allowed_domains = ['universal']
    # start_urls = ['http://universal/']
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def __init__(self, name, uniq_name, start_urls, *args, **kwargs):
        self.name = uniq_name
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules')).get('articles')
        self.start_urls = start_urls
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider, self).__init__(*args, **kwargs)

    # def start_requests(self):
    #     url = 'https://nhandan.org.vn/article/Paging?categoryId=1171&pageIndex=2&pageSize=15&fromDate=18/09/2020&toDate=19/09/2020&displayView=PagingPartial'
    #     yield scrapy.Request(url=url)

    def parse_item(self, response):
        # print(response.text)
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
            yield loader.load_item()
        else:
            yield {}
