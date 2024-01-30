from typing import Iterable
import scrapy
from scrapy.http import Request


class ArgSpider(scrapy.Spider):
    name = "arg"
    allowed_domains = ["priceoye.pk"]

    def start_requests(self):
        yield scrapy.Request(f'https://priceoye.pk/motorcycle/{self.company}/')

    def parse(self, response):
        for product in response.css('div.productBox'):
            yield {
                'name': product.css('div.detail-box div.p-title::text').get(),
                'brand': product.css('div.productBox::attr(data-brand)').get(),
                'price': product.css('div.price-box.p1::text').get()
            }

        next_page = response.css('div.pagination a[href]:last-child::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
