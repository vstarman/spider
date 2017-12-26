# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Teachers.items import TeachersItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # with open('itcast.html', 'w') as f:
        #     f.write(response.text)

        node_list = response.xpath('//div[@class="li_txt"]')
        # item_list = []
        for node in node_list:
            item = TeachersItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            # item_list.append(item)
            yield item
        # return item_list
