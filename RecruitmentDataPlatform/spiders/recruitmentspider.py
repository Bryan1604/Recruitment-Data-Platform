import scrapy


class RecruitmentspiderSpider(scrapy.Spider):
    name = "recruitmentspider"
    # allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://itviec.com/it-jobs"]
    count = 0
    # def parse(self, response):
    #         # Thiết lập User-Agent trong yêu cầu
    #         headers = {
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    #         }
    #         yield scrapy.Request(response.url, headers=headers, callback=self.parse_page)
    def updateCounter(self):
        count = count +1 

    def parse(self, response):
        jobs = response.css('div.ipy-2')
        for job in jobs:
            yield {
                "job_name": job.css('h3.imt-3 a::text').get(),
                "job_url": "https://itviec.com" + job.css('h3.imt-3 a').attrib['href'],
            }
        
        next_page = "https://itviec.com/it-jobs?job_selected=product-designer-ninja-van-tech-lab-5957&page=" + str(self.count +1)
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            
            yield scrapy.Request(next_page, callback=self.parse)
        pass
