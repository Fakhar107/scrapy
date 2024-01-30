import scrapy

class BhaiSpider(scrapy.Spider):
    name = "bhai"
    allowed_domains = ["priceoye.pk"]
    start_urls = ["https://priceoye.pk/mobiles"]

    def parse(self, response):
        for product in response.css('div.productBox'):
            yield {
                'name': product.css('div.detail-box div.p-title::text').get(),
                'brand': product.css('div.productBox::attr(data-brand)').get(),
                'price': product.css('div.price-box.p1::text').get()
            }

        next_page = response.css('div.pagination a[href]:last-child::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


