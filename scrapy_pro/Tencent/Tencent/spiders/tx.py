# -*- coding: utf-8 -*-
import scrapy
import time
from Tencent.items import PositionItem
from scrapy.spiders import CrawlSpider, Rule


class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?keywords=&lid=0&start='
    start_urls = [base_url + str(i) for i in range(0, 2681, 10)]

    # 1. 通过偏移量处理多个页面的规律情况
    # offset = 0
    # start_urls = [base_url + str(0)]

    def parse(self, response):
        """制作item传给pipelines做最后处理"""
        node_list = response.xpath("//tr[@class='odd'] | //tr[@class='even']")
        # print '-' * 100
        for node in node_list:
            item = PositionItem()
            item['position_link'] = node.xpath('./td/a/@href').extract_first()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_type'] = node.xpath('./td[2]/text()').extract_first()
            item['position_nums'] = node.xpath('./td[3]/text()').extract_first()
            item['work_location'] = node.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = node.xpath('./td[5]/text()').extract_first()
            time.sleep(1)
            yield item

        """
        # 1. 适用于确定页码，一直循环判断并自增
        # 优点是写法简单，缺点是并没有用到scrapy的并发
        if self.offset < 2681:
                self.offset += 10
                yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)
        """
        """
        # 2. 通过点击下一页控制页面跳转
        # 如果到了最后一页，返回非None值
        # 如果没有到最后一页，返回None
        if not response.xpath("//a[@class='noactive' and @id='next']/@href").extract_first():
            next_link = "http://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract_first()
            yield scrapy.Request(url=next_link, callback=self.parse)
        """
