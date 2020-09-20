import datetime


def dangcongsan_yn():
    now = datetime.datetime.today()
    now_year = now.year
    page_nums = 100
    url = "https://nhandan.org.vn/article/Paging?categoryId={0}&pageIndex={1}&pageSize=15&fromDate=01/01/"+str(now_year)+"&toDate="+now.strftime('%d/%m/%Y')+"&displayView=PagingPartial"
    category_ids = [1171, 1185, 1251, 1211, 1287, 1257, 1231, 1224, 1303, 1309, 1292, 1315]
    for page in range(page_nums):
        for category_id in category_ids:
            yield url.format(category_id, page)
