from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join, Compose, MapCompose, Identity


class UniversalLoader(ItemLoader):
    default_output_processor = TakeFirst()


def batch_strip(strs):
    new_str = [s.strip() for s in strs]
    return new_str


class ChinhphuLoader(UniversalLoader):
    # news_content_in = MapCompose(lambda s: s.strip)
    news_content_out = Compose(batch_strip, Join())
    public_date_out = Compose(Join(), lambda s: s.strip())
    # public_date = Compose(lambda s: s.strip)
