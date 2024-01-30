# My first successful spider with scrapy 

import scrapy

# Simple code to crawl spider by (scrapy.spider)
class MotaSpider(scrapy.Spider):
    name = "mota"
    allowed_domains = ["priceoye.pk"]
    start_urls = ["https://priceoye.pk/mobiles"]


    def parse(self, response):

        products= response.css('div.productBox')

        for product in products:

            item = {
            'price':product.css('div.price-box.p1::text').get().replace('Rs.',' ').strip(),
            'link':product.css('a::attr(href)').get(),
            'brand':product.css('div::attr(data-brand)').get().strip(),
            'nomenclature':product.css('div::attr(data-slug)').get().strip()
            }
        
            yield item

        next_page = response.css('div.pagination a[href]:last-child::attr(href)').get()


        if next_page is not None:
                yield response.follow(next_page, callback=self.parse)