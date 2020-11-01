import datetime
from guangxi_by_sxp.utils import create_date_list


def nhandan():
    now = datetime.datetime.today()
    now_year = now.year
    page_nums = 100
    url = "https://nhandan.org.vn/article/Paging?categoryId={0}&pageIndex={1}&pageSize=15&fromDate=01/01/"+str(now_year)+"&toDate="+now.strftime('%d/%m/%Y')+"&displayView=PagingPartial"
    category_ids = [1171, 1185, 1251, 1211, 1287, 1257, 1231, 1224, 1303, 1309, 1292, 1315]
    for page in range(page_nums):
        for category_id in category_ids:
            yield url.format(category_id, page)


def banmuang():
    urls = [
        "https://www.banmuang.co.th/news/ajax/politic/{0}/208167:208161:208148:208136",
        "https://www.banmuang.co.th/news/ajax/crime/{0}/208213:208196:208178:208173",
        "https://www.banmuang.co.th/news/ajax/economy/{0}/208203:208201:208190:208189",
        "https://www.banmuang.co.th/news/ajax/auto/{0}/207955:207957:207954:207937",
        "https://www.banmuang.co.th/news/ajax/entertain/{0}/208159:208156:208149:208141",
        "https://www.banmuang.co.th/news/ajax/sport/{0}/208202:207775:207774:207726",
        "https://www.banmuang.co.th/news/ajax/education/{0}/208212:208092:208091:208090",
        "https://www.banmuang.co.th/news/ajax/bangkok/{0}/208195:208186:207913:207851",
        "https://www.banmuang.co.th/news/ajax/region/{0}/208215:208216:208214:208207",
        "https://www.banmuang.co.th/news/ajax/social/{0}/208154:208146:207864:207862",
        "https://www.banmuang.co.th/news/ajax/promotion/{0}/208160:208113:208079:208038"
    ]
    page_nums = 100
    for page in range(1, page_nums+1):
        for url in urls:
            yield url.format(page)


def thejakartapost():
    yield "https://www.thejakartapost.com/index"


def guojiribao():
    url = "http://www.guojiribao.com/shtml/gjrb/{0}/index.shtml"
    date_list = create_date_list()
    # 逆序构造URL
    for date in date_list[::-1]:
        yield url.format(date)
