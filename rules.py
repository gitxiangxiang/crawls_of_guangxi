from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

# 键值对应json配置文件中‘rules’的值
rules = {
    'chinhphu-cn': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(restrict_xpaths=r'//div[@class="menuItem"]'), callback='gen_spider', follow=False)
        ],
        "articles": [
            # 提取首页文章链接
            Rule(LinkExtractor(allow=r'/Home/%+.*', restrict_xpaths=r'//div[@class="hotNewRight"]'),
                 callback='parse_item'),
            # 提取文章链接
            Rule(LinkExtractor(allow=r'/Home/%+.*', restrict_xpaths=r'//a[@class="catItemTitle"]'),
                 callback='parse_item'),
            # 提取下一页链接
            Rule(LinkExtractor(restrict_xpaths=r'//span[@class="pageViewNoItemSelected"]/following-sibling::a[1]'),
                 follow=True),
        ]
    },
    'chinhphu-en': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(restrict_xpaths=r'//div[@class="menuItem"]'), callback='gen_spider', follow=False),
        ],
        "articles": [
            Rule(LinkExtractor(allow=r'/Home/.*', restrict_xpaths=r'//div[@class="hotNewRight"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'/Home/.*', restrict_xpaths=r'//a[@class="catItemTitle"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(restrict_xpaths=r'//span[@class="pageViewNoItemSelected"]/following-sibling::a[1]'),
                 follow=True),
        ]
    },
    'dangcongsan-cn': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'/.*.html', deny=r'//.*/.*/.*.html',
                               restrict_xpaths=r'//div[@class="main-menu-cn"]//li[@class="main-li"]'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            Rule(
                LinkExtractor(allow=r'.*.html', restrict_xpaths=r'//div[@id="contentLastest"]//div[@class="w-item-w"]'),
                callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*.html',
                               restrict_xpaths=r'//div[@class="category-list"]//a[@class="item-title"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(
                restrict_xpaths=r'//div[@class="phanPage"]//li[@class="active"]/following-sibling::li[1]'),
                follow=True),
            Rule(LinkExtractor(
                restrict_xpaths=r'//div[@class="phanPage"]//li[2]'), follow=True)
        ]
    },
    'dangcongsan-en': {
        "navigations": [
            # 提取导航栏链接
            Rule(
                LinkExtractor(allow=r'/.*.html', deny=r'//.*/.*/.*.html',
                              restrict_xpaths=r'//div[@class="main-menu"]//li'), callback='gen_spider',
                follow=False),
        ],
        "articles": [
            Rule(LinkExtractor(allow=r'.*.html',
                               restrict_xpaths=r'//div[@class="category-list"]//a[@class="item-title"]'),
                 callback='parse_item'),
            # 下一页
            Rule(LinkExtractor(
                restrict_xpaths=r'//div[@class="phanPage"]//li[@class="active"]/following-sibling::li[1]'),
                follow=True),
            Rule(LinkExtractor(
                restrict_xpaths=r'//div[@class="phanPage"]//li[2]'), follow=True)
        ]
    },
    'nhandan': {
        """
        “nhandan”（越南人民网越南语版）网站通过此请求来追加文章
        https://nhandan.org.vn/article/Paging?categoryId=1171&pageIndex=2&pageSize=15&fromDate=18/09/2020&toDate=19/09/2020&displayView=PagingPartial
        """
        "navigations": [
            # 提取导航栏链接（没用到）
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[contains(@class, "main-menu")]//li[@class="parent-menu"]/a'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="box-widget-loaded"]//div[@class="box-title"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="box-widget-other"]//div[@class="box-title"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*', restrict_xpaths=r'//article//div[@class="box-title"]'),
                 callback='parse_item'),
        ]
    },
    'siamrath': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'.*', deny=r'.*/h',
                               restrict_xpaths=r'//div[@class="styleline-inner"]//li'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="view-content"]//a'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//ul[@class="pagination"]//li[@class="next"]'),
                 follow=True),
        ]
    },
    'matichon': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="menu-main-menu2-container"]/ul[@id="menu-main-menu2-1"]/li/a'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="td-pb-row"]//div[@class="td-ss-main-content"]//div[@class="item-details"]//h3'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[contains(@class, "page-nav")]//span[@class="current"]/following-sibling::a[1]'),
                 follow=True),
        ]
    },
    'banmuang': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="mainmenu"]/div[@id="myslidemenu"]/ul/li/a/@href'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[contains(@class, "list") and contains(@class, "block")]//h4'),
                 callback='parse_item'),
            # "https://www.banmuang.co.th/news/ajax/politic/"+page+"/208167:208161:208148:208136"
        ]
    },
    'thejakartapost': {
        "navigations": [
            # 提取导航栏链接(没用到)
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="col-xs-12 tjp-header channelHeader"]'
                                               r'//div[@class="container tjp-page"]//div[@class="row"]/ul/li'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="col-xs-12 columns main-single-page channelSearch"]'
                                               r'//div[contains(@class, "listNews")]//div[@class="newsWord"]/a[2]'),
                 callback='parse_item'),
            # 获取下一页
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="navigation-page"]//a[@class="jp-last"]'),
                 follow=True),
        ]
    },
    'guojiribao': {
        "navigations": [
            # 提取导航栏链接(没用到)
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="col-xs-12 tjp-header channelHeader"]'
                                               r'//div[@class="container tjp-page"]//div[@class="row"]/ul/li'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//table//div[@class="lefta"]//div[@class="rconf"]'
                                               r'//dl[@class="Rcon"]/dd/a[@title!="广告"]'),
                 callback='parse_item'),
            # 获取下一页
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//table//div[@id="scrollDiv"]/ul/li'),
                 follow=True),
        ]
    },
    'kompas': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="row clearfix nav"]//ul[contains(@class, "nav__row")]'
                                               r'/li[@class="nav__item"]/a'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//a[@class="article__link"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//a[@class="tren__link"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//a[@class="hype__link"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//a[@class="food__link"]'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//a[@class="sains__link"]'),
                 callback='parse_item'),
            # 获取下一页
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[contains(@class, "paging__wrap")]//div[@class="paging__item"]'
                                               r'/a[@class="paging__link paging__link--next"]'),
                 follow=True),
        ]
    },
    'singaporenews': {
        "navigations": [
            # 提取导航栏链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="row expanded header"]//div[@id="navigation-menu"]'
                                               r'//ul[@class="dropdown menu"]/li'),
                 callback='gen_spider', follow=False),
        ],
        "articles": [
            # 提取文章链接
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="row expanded content"]//div[@class="large-8 columns"]//h2'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="row expanded content"]//div[@class="large-4 columns"]//h6'),
                 callback='parse_item'),
            Rule(LinkExtractor(allow=r'.*',
                               restrict_xpaths=r'//div[@class="row column headline"]//div[@class="single_head"]//h6'),
                 callback='parse_item'),
        ]
    },
}
