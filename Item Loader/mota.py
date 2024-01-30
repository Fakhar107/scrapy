import scrapy

from priceoye.items import PriceoyeItem
from scrapy.loader import ItemLoader

class MotaSpider(scrapy.Spider):
    name = "mota"
    allowed_domains = ["priceoye.pk"]
    start_urls = ["https://priceoye.pk/mobiles"]

    def parse(self, response):
        for product in response.css('div.productBox'):
            loader = ItemLoader(item=PriceoyeItem(), selector=product)
            loader.add_css('name', 'div::attr(data-slug)')
            loader.add_css('brand', 'div::attr(data-brand)')
            loader.add_css('price', 'div.price-box.p1::text')  # Fix the CSS selector
            loader.add_css('link', 'a::attr(href)')  # Add the missing closing parenthesis

            yield loader.load_item()

        next_page = response.css('div.pagination a[href]:last-child::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)