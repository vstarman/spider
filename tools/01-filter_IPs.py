# -*- coding:utf-8 -*-
import os
import urllib2
import time
import json
from bs4 import BeautifulSoup
from my_ips_poll import MY_IP_POLL


# 过滤ip
def filter_ip(proxy, res):
    """
    匹配ip和port
    :param proxy: 容器
    :param res: 文本内容
    :return:
    """
    try:
        # 制作soup找出<tr></tr>标签块,作为列表一个元素
        soup = BeautifulSoup(res, "html5lib")
        ips = soup.findAll('tr')
        # 遍历tr标签块,找出<td></td>标签块
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            # print tds
            """
            [<td class="country"><img alt="Cn" src="http://fs.xicidaili.com/images/flag/cn.png"/></td>,
             <td>223.241.78.157</td,
             <td>8010</td,
             <td>\n        <a href="/2017-12-16/anhui">\u5b89\u5fbd\u829c\u6e56</a>\n      </td,
             <td class="country">\u9ad8\u533f</td,
             <td>HTTPS</td,
             <td class="country">\n        <div class="bar" title="6.481\u79d2">\n          <div class="bar_inner slow" style="width:51%">\n            \n          </div>\n        </div>\n      </td,
             <td class="country">\n        <div class="bar" title="1.296\u79d2">\n          <div class="bar_inner medium" style="width:88%">\n            \n          </div>\n        </div>\n      </td,
             <td>1\u5206\u949f</td,
             <td>17-12-16 18:44</td>]"""
            ip_temp = dict()
            ip_temp[tds[5].contents[0]] = tds[1].contents[0] + ":" + tds[2].contents[0]
            proxy.append(ip_temp)
            # print ip_temp

    except Exception as e:
        print e


# 保存列表到文件
def save_ips(obj, filename):
    with open(filename, 'w+') as w:
        w.write(repr(obj))
        w.close()


# 测试ip是否可用
def test_alive_ip(obj):
    """
    遍历测试列表内的ip是否可用
    :param obj: 传入的列表对象
    :return:
    """
    list_obj = []  # 用来保存验证通过的代理ip
    for ip_dict in obj:
        # 1.验证代理
        proxy_handler = urllib2.ProxyHandler(ip_dict)
        opener = urllib2.build_opener(proxy_handler)
        response = None
        try:
            response = opener.open('http://www.httpbin.org/ip', timeout=1)
        except Exception, err:
            pass
        if response:
            try:
                res_dict = json.loads(response.read())
                if res_dict:
                    print res_dict.encode('utf-8')
            except Exception as e:
                pass


def main():
    """主函数"""
    # 新文件名
    new_file_name = 'my_ips_poll.py'
    # 获取文件列表
    folder_name = '../ip_socks'
    dir_list = os.listdir(folder_name)
    # 定义容器保存ip和端口
    vessel = []
    # 遍历文件,追加到新文件中
    for file_name in dir_list:
        f = open(file_name)
        # print f
        # 过滤ip神器
        filter_ip(vessel, f.read())
        # 保存列表文件到py文件
        save_ips(vessel, new_file_name)
        f.close()


if __name__ == '__main__':
    # 1.验证代理
    # proxy_handler = urllib2.ProxyHandler({'http': 'mr_mao_hacker:sffqry9r@120.27.218.32:16816'})
    # opener = urllib2.build_opener(proxy_handler)
    # response = opener.open('http://www.httpbin.org/ip')
    # print response.read()
    test_alive_ip(MY_IP_POLL)
