# -*- coding:utf-8 -*-
import requests
import random
import requests
from my_user_poll import MY_USER_AGENT
from lxml import etree


class TBSpider:
    """贴吧类"""
    def __init__(self):
        self.bar_name = '欧洲'#raw_input('请输入贴吧名: ')
        self.begin_page = 1#int(raw_input('起始页: '))
        self.end_page = 3#int(raw_input('终止页: '))

        # http://tieba.baidu.com/f?kw=%E7%A9%B7%E6%B8%B8&ie=utf-8&pn=50
        self.url_base = 'http://tieba.baidu.com/'
        self.ua_header = {'User_Agent': MY_USER_AGENT[0]}

    def run(self):
        # 1.遍历贴吧页面
        for page in range(self.begin_page, self.end_page + 1):
            pn = (page - 1) * 50
            dict_obj = {
                'kw': self.bar_name,
                'pn': pn
            }
            html = requests.get(self.url_base, params=dict_obj, headers=self.ua_header).content
            # 2.获取每页帖子链接: //a[@class='j_th_tit']/@href


    def send_request(self, url):
        pass


if __name__ == '__main__':
    spider = TBSpider()
    spider.run()
