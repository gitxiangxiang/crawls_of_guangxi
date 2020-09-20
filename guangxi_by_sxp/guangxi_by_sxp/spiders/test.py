import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from guangxi_by_sxp.items import ChinhphuItem
from lxml import etree

class TestSpider(CrawlSpider):
    """
    用于预先测试的半通用爬虫
    """
    name = 'test'
    allowed_domains = ['dangcongsan.vn']
    start_urls = ['http://cn.dangcongsan.vn/']

    rules = (
        # Rule(LinkExtractor(allow=r'/Home/%+.*', restrict_xpaths='//div[@class="hotNewRight"]'), callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="menuItem"]'), follow=True)
    )

    def parse_item(self, response):
        item = {}
        print(response.text)
        # item['title'] = response.xpath('//div[@class="dtContentHl"]//text()').extract_first().strip()
        # item['news_title'] = response.xpath('//div[@class="dtContentHl"]/span[@id="ctl00_mainContent_bodyContent_lbHeadline"]/text()').extract_first().strip()
        # item['news_content'] = ''.join([i.strip() for i in response.xpath('//div[@class="dtContentTxt"]//text()').extract()])
        # item['public_date'] = response.xpath('//div[@class="dtContentDate"]/span[@id="ctl00_mainContent_bodyContent_lbDate"]/text()').extract_first().strip()
        # item['site'] = "http://cn.news.chinhphu.vn/"
        # item['author'] = ""
        # item['media'] = "chinhphu"
        # item['type'] = ""
        # item['abstract'] = ""
        # item['url'] = response.url
        # item['sourceContent'] = response.xpath('//div[@class="dtContentTxt"]').extract_first()
        yield {}
