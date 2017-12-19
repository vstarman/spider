# -*- coding:utf-8 -*-
import random
import requests
from my_user_poll import MY_USER_AGENT
from lxml import etree


class TBSpider:
    """贴吧类"""
    def __init__(self):
        self.bar_name = '欧洲'#raw_input('请输入贴吧名: ')
        self.begin_page = 1#int(raw_input('起始页: '))
        self.end_page = 1#int(raw_input('终止页: '))

        # http://tieba.baidu.com/f?kw=%E7%A9%B7%E6%B8%B8&ie=utf-8&pn=50
        self.url_base = 'http://tieba.baidu.com/f?'
        # 使用google chrome user_agent文本会失败
        self.ua_header = {'User_Agent': MY_USER_AGENT[6]}

    def run(self):
        """项目启动函数"""
        # 1.遍历贴吧页面,获取每个帖子链接
        for page in range(self.begin_page, self.end_page + 1):
            pn = (page - 1) * 50
            dict_obj = {
                'kw': self.bar_name,
                'pn': pn
            }
            # 1.1 取到页面字节流
            html = self.send_request(self.url_base, dict_obj, self.ua_header)
            # 1.2.获取每页帖子链接: //a[@class='j_th_tit']/@href
            link_xpath = "//div[@class='t_con cleafix']/div/div/div/a/@href"
            link_list = self.load_page(html, link_xpath)
            # 2.打开每个页面,获取每个图片链接
            for link in link_list:
                link_url = self.url_base[:-3] + link
                # 2.1返回每页帖子文本
                page_html = self.send_request(link_url)
                pic_xpath = "//img[@class='BDE_Image']/@src"
                # 2.2.获取每页图片链接
                pic_link_list = self.load_page(page_html, pic_xpath)
                # 3.打开每个图片链接,保存图片
                for pic_link in pic_link_list:
                    data = self.send_request(pic_link)
                    pic_name = pic_link[-20:]
                    self.save_pic(data, 'tieba_pics/%s' % pic_name)
                    print '------->图片保存成功: %s' % pic_name

    def send_request(self, url, params=None, headers=None):
        """
        请求发送函数, 返回响应字节流
        :param url: To access the url
        :param params: query string
        :param headers: request headers
        :return: response
        """
        try:
            html = requests.get(url, params=params, headers=headers).content
            # print html
        except Exception as e:
            print e
            html = None
        return html

    def load_page(self, html, xpath_rule):
        """
        处理html文本, 提取帖子详情链接
        :param html: 传入的文本
        :param xpath_rule: xpath规则
        :return: 帖子链接列表
        """
        # 将html字符串转为HTML_DOM对象
        html_obj = etree.HTML(html)
        # link_list = html_obj.xpath("//a[@class='j_th_tit']/@href")
        link_list = html_obj.xpath(xpath_rule)
        return link_list

    def save_pic(self, data, file_name):
        """保存图片"""
        # http://imgsrc.baidu.com/forum/w%3D580/
        # sign=58d7e0c662d0f703e6b295d438f85148/c4a2abec8a136327b01474e2918fa0ec0afac7e0.jpg
        with open(file_name, 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    spider = TBSpider()
    spider.run()
