import scrapy


class ComapnyspiderSpider(scrapy.Spider):
    name = "comapnySpider"
    allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://www.topcv.vn"]

    def parse(self, response):
        pass
