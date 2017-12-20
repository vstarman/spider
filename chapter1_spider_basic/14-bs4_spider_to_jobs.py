# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib2
import urllib
import json
import time
from my_user_poll import MY_USER_AGENT
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderJobsLaGo(object):
    """此类用来爬取拉钩网的工作信息"""
    def __init__(self):
        pass

    def run(self):
        # https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0
        pass

    @staticmethod
    def _property(self):
        """此类用于测试property方法
           property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

           fget is a function to be used for getting an attribute value, and likewise
           fset is a function for setting, and fdel a function for del'ing, an
           attribute.  Typical use is to define a managed attribute x:

           class C(object):
               def getx(self): return self._x
               def setx(self, value): self._x = value
               def delx(self): del self._x
               x = property(getx, setx, delx, "I'm the 'x' property.")

           Decorators make defining new properties or modifying existing ones easy:

           class C(object):
               @property
               def x(self):
                   "I am the 'x' property."
                   return self._x
               @x.setter
               def x(self, value):
                   self._x = value
               @x.deleter
               def x(self):
                   del self._x

           # (copied from class doc)
           """
        pass


class SpiderJobsTenCent(object):
    """用来爬取腾讯网招聘信息,存储为json信息"""
    def __init__(self):
        self.base_url = 'http://hr.tencent.com/position.php?&start='
        self.detail_url = 'http://hr.tencent.com/position_detail.php?id=27267&keywords=python&tid=0&lid=2156'
        self.want_pages = raw_input('请输入要爬取的页数(不输默爬取整站): ')
        self.headers = {'User-Agent': MY_USER_AGENT[1]}
        self.job_list = []   # 保存职位信息
        self.page = 1  # 页面

    def send_request(self, url):
        """发送请求,返回html"""
        try:
            html = requests.get(url, headers=self.headers).content
            return html
        except Exception as e:
            print "[ERROR]: %s 请求发送失败..." % url
            return None

    def parse_html(self, html):
        """用来解析html数据"""
        # 1.2 创建BeautifulSoup解析器对象: str-->obj
        soup = BeautifulSoup(html, 'lxml')
        job_list = soup.find_all('tr', {'class': ['odd', 'even']})

        # 1.4 遍历列表将每个职位信息存入列表
        for job in job_list:
            item = dict()
            item['position_name'] = job.find('a').get_text()                 # 职位名称
            item['position_link'] = 'http://hr.tencent.com/' + job.find('a').get('href')     # 详情地址
            item['position_category'] = job.find_all('td')[1].get_text()     # 职位类别
            item['hiring_number'] = job.find_all('td')[2].get_text()         # 招聘人数
            item['work_location'] = job.find_all('td')[3].get_text()         # 工作地点
            item['publish_time'] = job.find_all('td')[4].get_text()          # 发布时间
            # 保存每条职位信息
            self.job_list.append(item)

            # 如果到最后一页,返回False
            if soup.find('a', {'id': 'next', 'class': 'noactive'}):
                return False

            # 否则,提取下一页链接
            next_link = 'http://hr.tencent.com/' + soup.find('a', {'id': 'next'}).get('href')
            return next_link

    def save_list_to_json(self):
        """用来将python列表存储为json数据"""
        # 存储为json数据,禁用ascii编码处理中文
        # json_data = json.dumps(self.job_list, ensure_ascii=False)
        # with open('14-tecent.json', 'w') as f:
        #     f.write(json_data.encode('utf-8'))

        json.dump(self.job_list, open('14-tecent.json', 'w'))
        print '[INFO]Json数据保存成功!'

    def run(self):
        """启动函数"""
        # 1.获取第一页链接
        html = self.send_request(self.base_url)
        while True:
            # 1.2解析页面,返回下一页链接
            next_link = self.parse_html(html)
            print '[INFO]第%d页爬取完毕...' % self.page

            # 1.3判断是否有下一页,是否输入页码,如果有,按页码爬取
            if self.want_pages:
                if self.page >= int(self.want_pages):
                    break
            if not next_link:
                print '[INFO]已到最后一页'
                break
            # 否则获取下一页
            html = self.send_request(next_link)

            # time.sleep(0.5)
            self.page += 1

        # 存储数据
        self.save_list_to_json()


class SpiderZhiHu(object):

    def run(self):
        url = 'https://www.zhihu.com/'
        headers = {'User_Agent': MY_USER_AGENT[1]}
        html = requests.get(url, headers=headers).content
        print html


if __name__ == '__main__':
    # 爬取腾讯招聘信息
    tx_spider = SpiderJobsTenCent()
    tx_spider.run()

    # 爬取知乎招聘信息
    # zh_spider = SpiderZhiHu()
    # zh_spider.run()

    # 爬取拉钩招聘信息
    # zh_spider = SpiderZhiHu()
    # zh_spider.run()
