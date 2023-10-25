import scrapy


class RecruitmentspiderSpider(scrapy.Spider):
    name = "recruitmentspider"
    # allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://itviec.com/it-jobs?gclid=CjwKCAjw-eKpBhAbEiwAqFL0mr7rB3hs8ZMO0wucEzAG0bXUOMmtdxzOocTb4rj5216_awW1jx31hRoCYa0QAvD_BwE&utm_campaign=gsn_brand_hn&utm_medium=cpc&utm_source=google&utm_term=it+vi%E1%BB%87c&job_selected=it-security-engineer-english-fintech-kbtg-vietnam-1200"]

    # def parse(self, response):
    #         # Thiết lập User-Agent trong yêu cầu
    #         headers = {
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    #         }
    #         yield scrapy.Request(response.url, headers=headers, callback=self.parse_page)
    def parse(self, response):
        jobs = response.css('div.ipy-2')
        for job in jobs:
            yield {
                "job_name": job.css('h3.imt-3 a::text').get(),
                "job_url": "https://itviec.com" + job.css('h3.imt-3 a').attrib['href'],
                
            }
        pass
