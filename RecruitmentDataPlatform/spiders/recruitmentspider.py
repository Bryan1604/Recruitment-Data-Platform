import scrapy


class RecruitmentspiderSpider(scrapy.Spider):
    name = "recruitmentspider"
    # allowed_domains = ["www.topcv.vn"]
    start_urls = [
        "https://itviec.com/it-jobs?gclid=CjwKCAjw-eKpBhAbEiwAqFL0mr7rB3hs8ZMO0wucEzAG0bXUOMmtdxzOocTb4rj5216_awW1jx31hRoCYa0QAvD_BwE&utm_campaign=gsn_brand_hn&utm_medium=cpc&utm_source=google&utm_term=it+vi%E1%BB%87c&job_selected=senior-it-quality-control-officer-mb-ageas-life-4701&page=3",
    ]

    def parse(self, response):
        jobs = response.css('div.ipy-2')
        for job in jobs:
            yield {
                "job_name": job.css('h3.imt-3 a::text').get(),
                "job_url": "https://itviec.com" + job.css('h3.imt-3 a').attrib['href'],
                "type": job.css('div.d-flex.align-items-center.text-dark-grey.imt-1 span::text')[0].get(),
                "location": job.css('div.d-flex.align-items-center.text-dark-grey.imt-1 span::text')[1].get(),
                "company": job.css('div.imy-3.d-flex.align-items-center span.ims-2.small-text a.text-rich-grey::text').get(),
                "tag": job.css('div.imt-3.imb-2 a.text-reset div.itag.itag-light.itag-sm::text').get()
            }
        
        next_page =  response.css("div.page.next a::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://itviec.com" + next_page
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page_url,callback=self.parse)
            
        pass
