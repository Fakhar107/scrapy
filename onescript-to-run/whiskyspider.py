import scrapy
from scrapy.crawler import CrawlerProcess

class WhiskySpider(scrapy.Spider):
    name = 'mobiles'

    def start_requests(self):
        yield scrapy.Request('https://priceoye.pk/mobiles')
        
    def parse(self, response):
        products = response.css('div.productBox')
        for item in products:
            yield {
                'name' : response.css('div::attr(data-slug)').get().strip(),
                'brand' : response.css('div::attr(data-brand)').get().strip(),
                'price' : response.css('div.price-box.p1::text').get().strip()
            }
        for x in range(2,16):
            yield (scrapy.Request(f'https://priceoye.pk/mobiles?page={x}',callback = self.parse))
                   
process = CrawlerProcess(settings = {
    'FEED_URI' : 'whisky.csv',
    'FEED_FORMAT' : 'csv'
    })
process.crawl(WhiskySpider)
process.start()
