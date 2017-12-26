# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PositionItem(scrapy.Item):
    """Position info"""
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_nums = scrapy.Field()
    work_location = scrapy.Field()
    publish_time = scrapy.Field()
    # 爬取时间
    crawl_time = scrapy.Field()


class RequireItem(scrapy.Item):
    """Position require"""
    # define the fields for your item here like:
    position_require = scrapy.Field()
    position_duty = scrapy.Field()
    # 爬取时间
    crawl_time = scrapy.Field()