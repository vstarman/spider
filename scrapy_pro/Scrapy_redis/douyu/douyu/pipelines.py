# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class ImgPipeline(ImagesPipeline):
    # 获取设置中的存储路径
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        img_url = item['image_url']
        yield Request(url=img_url)

    def item_completed(self, results, item, info):
        img_path = [x['path'] for ok, x in results if ok]
        new_path = self.IMAGES_STORE + item['name'] + '.jpg'
        # print new_path
        item['image_path'] = new_path
        os.rename(self.IMAGES_STORE + img_path[0], new_path)
        # print img_path
        return item
