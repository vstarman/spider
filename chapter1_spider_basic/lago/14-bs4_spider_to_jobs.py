# -*- coding:utf-8 -*-
"""
用JsonPath解析数据,将需要爬取的数据保存为Json格式
"""
import urllib
import requests
import json
import time
import jsonpath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderJobsLaGo(object):
    """此类用来爬取拉钩网的工作信息"""
    def __init__(self):
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "27",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "user_trace_token=20171215185341-7505ee61-3a30-477f-b96c-0bf88e31655a; LGUID=20171215185343-37aa595c-e186-11e7-9d71-5254005c3644; _ga=GA1.2.1490965250.1513335302; _gid=GA1.2.111135875.1513685875; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAACBHABBIF0653C06CFF6DDE8D5F0C0C943C1FE37; LGSID=20171220225917-59c7ecef-e596-11e7-a337-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513335302,1513685876,1513782041; TG-TRACK-CODE=index_search; SEARCH_ID=c94a77fab6dd445e96479bb62d19c1be; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513782296; LGRID=20171220230335-f38fc62f-e596-11e7-9df5-5254005c3644",
            "DNT": "1",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.proxy_list = []
        # self.position_name = raw_input("请输入需要抓取的职位:")
        # self.city_name = raw_input("请输入需要抓取的城市:")
        # self.want_page = int(raw_input("请输入需要抓取的页数:"))
        self.page = 1
        self.item_list = []

        self.position_name = 'python'
        self.city_name = '北京'
        self.want_page = 1

    def send_request(self):
        """发送请求,返回响应"""
        # 编辑查询参数,和表单数据
        query_params = {
            "px": "default",
            "city": self.city_name,
            "needAddtionalResult": "false",
            "isSchoolJob": 0,
        }
        form_data = {
            "first": "false",
            "pn": self.page,
            "kd": self.position_name,
        }
        form_data = urllib.urlencode(form_data)
        response = requests.post(self.url, params=query_params, data=form_data, headers=self.headers)
        # print type(response.json())    # -->dict
        # print type(response.content)   # -->str
        return response

    def parse_page(self, response):
        """负责对数据进行解析"""
        # html = response.content
        # dict_obj = json.loads(html)

        try:
            # 转为字典对象
            dict_obj = response.json()
            # 解析出json的result数据列表,
            # result是列表,json path返回也是列表: [[]]
            result_list = jsonpath.jsonpath(dict_obj, '$..result')[0]

            for result in result_list:
                item = dict()
                item["positionName"] = result["positionName"]
                item["workYear"] = result["workYear"]
                item["education"] = result["education"]
                item["createTime"] = result["createTime"]
                item["city"] = result["city"]
                item["salary"] = result["salary"]
                item["positionAdvantage"] = result["positionAdvantage"]
                item["financeStage"] = result["financeStage"]
                item["industryField"] = result["industryField"]
                item["companySize"] = result["companySize"]
                item["companyLabelList"] = result["companyLabelList"]
                item["district"] = result["district"]
                item["positionLables"] = result["positionLables"]
                item["companyFullName"] = result["companyFullName"]
                item["firstType"] = result["firstType"]
                self.item_list.append(item)
        except Exception as e:
            print "[ERROR]: 数据解析失败..."

    def run(self):
        """程序主逻辑函数"""
        # 1.循环发送请求
        while self.page <= self.want_page:
            response = self.send_request()
            # 2.解析响应
            self.parse_page(response)
            time.sleep(0.3)
            self.page += 1

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


if __name__ == '__main__':
    # 爬取拉钩招聘信息
    zh_spider = SpiderJobsLaGo()
    zh_spider.run()
