from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose, MapCompose, Identity


class UniversalLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinhphuLoader(UniversalLoader):
    # news_content_in = MapCompose(lambda s: s.strip)
    news_content_out = Compose(Join(), lambda s: s.strip())
    public_date_out = Compose(Join(), lambda s: s.strip())
    # public_date = Compose(lambda s: s.strip)
