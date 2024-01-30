import scrapy


class J2storeSpider(scrapy.Spider):
    name = "j2store"
    allowed_domains = ["j2store.net"]
    start_urls = ["https://j2store.net/demo/index.php/shop"]

    def parse(self, response):
        products = response.css("div.col-sm-9 div[itemprop=itemListElement]")
        for item in products:
            yield{
                'name': item.css("h2.product-title a::text").get().strip(),
                'price': item.css("div.sale-price::text").get().strip()
            }

