# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib2
import urllib
import json
from my_user_poll import MY_USER_AGENT


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
        self.base_url = 'http://hr.tencent.com/'
        self.detail_url = 'http://hr.tencent.com/position_detail.php?id=27267&keywords=python&tid=0&lid=2156'

    def send_request(self, url, params, **kwargs):
        requests.get(url, params, **kwargs)
        pass

    def run(self):
        """启动函数"""
        # 1.爬取职位详情链接
        # 1.1 爬取职位页面信息: 查询参数,头信息
        url = self.base_url + "position.php?"
        params = {'keywords': 'python'}
        params = urllib.urlencode(params)
        headers = {'UserAgent': MY_USER_AGENT[1]}
        request = urllib2.Request(url + params, headers=headers)
        response = urllib2.urlopen(request)
        resp_html = response.read()

        # 1.2 解析页面数据,返回字典数据

        # 1.2 创建BeautifulSoup解析器对象: str-->obj
        soup_html = BeautifulSoup(resp_html, 'lxml')

        # 1.3 用css选择器选出每页的10个职位对象
        job_list = soup_html.select('tr[class="even"],tr[class="odd"]')
        print '获取了%d个职位信息...' % len(job_list)

        # 1.4 遍历列表将每个职位信息存入列表
        items = []
        for job in job_list:
            item = dict()
            item['name'] = job.select('td a')[0].get_text()           # 职位名称
            item['detailLink'] = job.select('td a')[0].attrs['href']  # 详情地址
            item['category'] = job.select('td')[1].get_text()         # 职位类别
            item['recruitNumber'] = job.select('td')[2].get_text()    # 招聘人数
            item['workLocation'] = job.select('td')[3].get_text()     # 工作地点
            item['publishTime'] = job.select('td')[4].get_text()      # 发布时间
            items.append(item)

        # 2.存储为json数据,禁用ascii编码处理中文
        json_data = json.dumps(items, ensure_ascii=False)
        with open('14-tecent.json', 'w') as f:
            f.write(json_data.encode('utf-8'))
        print '存储成功...'


class SpiderZhiHu(object):

    def run(self):
        url = 'https://www.zhihu.com/'
        headers = {'User_Agent': MY_USER_AGENT[1]}
        html = requests.get(url, headers=headers).content
        print html


if __name__ == '__main__':
    # tx_spider = SpiderJobsTenCent()
    # tx_spider.run()
    zh_spider = SpiderZhiHu()
    zh_spider.run()
