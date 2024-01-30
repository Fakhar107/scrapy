from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import FullprojectItem
from scrapy.loader import ItemLoader


class AmazonSpider(CrawlSpider):
    name = "amazon"
    allowed_domains = ["www.amazon.co.uk"]
    start_urls = ["https://www.amazon.co.uk/s?k=monitors"]

    rules = (
        Rule(LinkExtractor(allow='s?k=monitor&page=', restrict_css='a.s-pagination-next')),
        Rule(LinkExtractor(allow='/dp/'), callback='parse_item')
    )

    def parse(self, response):
        l = ItemLoader(item = FullprojectItem(), response=response)
        l.add_css('name', 'a-size-medium a-color-base a-text-normal')
        l.add_css('asin', 'div.data-asin')
        l.add_css('price', 'a-size-base.s-underline-text')
        l.add_css('totalviews', 'a-size-base s-underline-text')
        yield l.loader_item()
