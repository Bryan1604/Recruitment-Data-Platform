# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitmentdataplatformItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RecruitmentItem(scrapy.Item):
    job_name = scrapy.Field()
    job_url = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    tag = scrapy.Field()
    post_time = scrapy.Field()
    
class CompanyItem(scrapy.Item):
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    type = scrapy.Field()
    size = scrapy.Field() 
    country = scrapy.Field()
    overview = scrapy.Field()
    key_skill = scrapy.Field()
    location = scrapy.Field()
    job_quantity = scrapy.Field()
    
    