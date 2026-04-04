import scrapy


class Douban2Spider(scrapy.Spider):
    name = "douban2"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        print(response.url)

x =Douban2Spider()
x.parse