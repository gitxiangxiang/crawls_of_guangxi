from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


# 键值对应json配置文件中‘rules’的值
rules = {
    'chinhphu-cn': [
        # 提取首页文章链接
        Rule(LinkExtractor(allow=r'/Home/%+.*', restrict_xpaths=r'//div[@class="hotNewRight"]'), callback='parse_item'),
        # 提取导航栏链接
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="menuItem"]'), follow=True),
        # 提取文章链接
        Rule(LinkExtractor(allow=r'/Home/%+.*', restrict_xpaths=r'//a[@class="catItemTitle"]'), callback='parse_item'),
        # 提取下一页链接
        Rule(LinkExtractor(restrict_xpaths=r'//span[@class="pageViewNoItemSelected"]/following-sibling::a[1]'), follow=True),
    ],
    'chinhphu-en': [
        Rule(LinkExtractor(allow=r'/Home/.*', restrict_xpaths=r'//div[@class="hotNewRight"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="menuItem"]'), follow=True),
        Rule(LinkExtractor(allow=r'/Home/.*', restrict_xpaths=r'//a[@class="catItemTitle"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=r'//span[@class="pageViewNoItemSelected"]/following-sibling::a[1]'), follow=True),
    ],
    'dangcongsan-cn': [
        Rule(LinkExtractor(allow=r'.*.html', restrict_xpaths=r'//div[@id="contentLastest"]//div[@class="w-item-w"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'.*.html', restrict_xpaths=r'//div[@class="category-list"]//a[@class="item-title"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/.*.html', deny=r'//.*/.*/.*.html', restrict_xpaths=r'//div[@class="main-menu-cn"]//li[@class="main-li"]'), follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="phanPage"]//li[@class="active"]/following-sibling::li[1]'), follow=True)
    ],
    'dangcongsan-en': [
        Rule(LinkExtractor(allow=r'.*.html', restrict_xpaths=r'//div[@class="category-list"]//a[@class="item-title"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/.*.html', deny=r'//.*/.*/.*.html', restrict_xpaths=r'//div[@class="main-menu"]//li'), follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="phanPage"]//li[@class="active"]/following-sibling::li[1]'), follow=True)
    ],
    'dangcongsan-yn': [
        # 提取文章链接
        Rule(LinkExtractor(allow=r'.*', restrict_xpaths=r'//div[@class="box-widget-loaded"]//div[@class="box-title"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'.*', restrict_xpaths=r'//div[@class="box-widget-other"]//div[@class="box-title"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'.*', restrict_xpaths=r'//article//div[@class="box-title"]'), callback='parse_item'),
        # 提取导航栏链接
        Rule(LinkExtractor(allow=r'.*', restrict_xpaths=r'//div[contains(@class, "main-menu")]//li[@class="parent-menu"]/a'), follow=True),
        # 提取下一页链接

    ]
}
"""
猜测“dangcongsan-yn”（越南人民网越南语版）网站通过此请求来追加文章
https://nhandan.org.vn/article/Paging?categoryId=1171&pageIndex=2&pageSize=15&fromDate=18/09/2020&toDate=19/09/2020&displayView=PagingPartial
"""