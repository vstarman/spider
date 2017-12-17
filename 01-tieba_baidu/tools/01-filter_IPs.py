# -*- coding:utf-8 -*-
import os
import re
import logging
from bs4 import BeautifulSoup

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug("debug")
logging.warning('warning')
logging.info('info')


# 废弃代码
def regex_filter(file_context):
    """
    正则匹配文件内容
    :param file_context: 文件内容
    :return: 匹配后的ip数据
    """
    comp = """      <td>(\d+\.\d+\.\d+\.\d+)</td>
      <td>(\d+)</td>
      <td>
        <a href="(.+)">(.+)</a>
      </td>
      <td class="country">(.+)</td>
      <td>([HTTP|HTTPS])</td>"""
    # re.findall()
    # comp = "<td>(.+)</td>"
    new_file_name = "MY_IPs.py"
    with open(new_file_name, 'a') as w:
        w.write("\n".join(re.findall(comp, file_context)))

    # return ip_list


# 保存列表到文件
def save_ips(lst, filename):
    with open(filename, 'w+') as w:
        w.write(repr(lst))
        w.close()


# 过滤ip神器
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


if __name__ == '__main__':
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
