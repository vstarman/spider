# -*- coding:utf-8 -*-
"""
用JsonPath解析数据,将需要爬取的数据保存为Json格式
"""
import urllib
import requests
import json
import time
import csv
import jsonpath
import sys
import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')


class SpiderJobsLaGo(object):
    """此类用来爬取拉钩网的工作信息
    包含:
    1.循环爬取拉勾网数据;
    2.并可选择将数据保存为json文件,csv文件,和MongoDB数据库
    """
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
        self.position_name = raw_input("请输入需要抓取的职位:")
        self.city_name = raw_input("请输入需要抓取的城市:")
        self.want_page = raw_input("请输入需要抓取的页数:")
        if not self.want_page:
            self.want_page = 'all'
        self.page = 1
        self.item_list = []
        self.position_num = 0

        # self.position_name = 'python'
        # self.city_name = '北京'
        # self.want_page = 1

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

            # 判断有无数据
            if len(result_list):
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
                    item["companyLabelList"] = self.list_to_str(result["companyLabelList"])
                    item["district"] = result["district"]
                    item["positionLables"] = self.list_to_str(result["positionLables"])
                    item["companyFullName"] = result["companyFullName"]
                    item["firstType"] = result["firstType"]
                    self.item_list.append(item)

            print "[INFO]: 第%d页数据保存成功!" % self.page
            return len(result_list)
        except Exception as e:
            print "[ERROR]: 数据解析失败..."

    @staticmethod
    def list_to_str(list_pro):
        """将内层列表转为字符串"""
        if not list_pro:
            return ''
        s = ''
        for i in list_pro:
            s += i + ','
        return s

    def save_to_json(self):
        """保存文件到磁盘"""
        file_name = self.city_name + '_' + self.position_name + '_' + self.want_page
        json.dump(self.item_list, open(file_name + '_jobs.json', 'w'))
        print "[INFO]: 数据写入成功"

    def save_to_csv(self):
        """保存文件为csv格式"""
        file_name = self.city_name + '_' + self.position_name + '_' + self.want_page

        csv_file = file(file_name + '_jobs.csv', 'w')

        # 创建cvs读写对象,参数为需要处理的文件对象
        csv_writer = csv.writer(csv_file)

        # 将json中的key坐表头,存入csv第一行
        sheet = self.item_list[0].keys()
        # 获取所有的数据部分，二维嵌套列表
        data = [i.values() for i in self.item_list]

        # 先写入表头部分，一行数据，参数是一个一维列表
        csv_writer.writerow(sheet)
        # 再写入数据部分，多行数据，参数是一个二维的列表
        csv_writer.writerows(data)

        # 关闭文件对象
        csv_file.close()

    def save_to_MongoDB(self, set_name=None):
        """存储数据到MongoDB数据库"""
        try:
            # 创建链接对象
            client = pymongo.MongoClient()
            # 建库对象
            db = client['MongoDB_LaGou']
            # 建集合对象
            if not set_name:
                set_name = self.city_name + '_' + self.position_name + '_' + self.want_page
            collections = db[set_name]
            # 插入数据
            collections.insert(self.item_list)

            print '[叮咚]数据存储成功...'
        except Exception as e:
            print e
            print '[叮咚]数据存储失败...'

    def run(self):
        """程序主逻辑函数"""
        # 1.循环发送请求
        while str(self.page) <= self.want_page:
            response = self.send_request()

            # 2.解析响应,返回职位长度
            data_len = self.parse_page(response)
            self.position_num += data_len

            print "[INFO]已抓取数据%d条..." % self.position_num
            if not data_len:
                print "[INFO]抓取数据完毕"
                break

            time.sleep(0.3)
            self.page += 1

        # 写入磁盘文件
        # self.save_to_csv()
        # self.save_to_json()

        # 写入数据库
        self.save_to_MongoDB()


if __name__ == '__main__':
    # 爬取拉钩招聘信息
    zh_spider = SpiderJobsLaGo()
    zh_spider.run()
