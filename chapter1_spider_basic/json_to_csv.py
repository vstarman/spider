# -*- coding:utf-8 -*-
import json
# 用来处理csv文件的模块
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def json_to_csv(filename=None):
    if not filename:
        filename = '14-tecent'

    # 创建json文件对象
    json_file = file(filename + '.json', 'r')
    # 创建csv文件对象
    csv_file = file(filename + '.csv', 'w')

    # 从内存读取文件,返回list对象
    list_obj = json.load(json_file)
    # 创建cvs读写对象,参数为需要处理的文件对象
    csv_writer = csv.writer(csv_file)

    # 将json中的key坐表头,存入csv第一行
    sheet = list_obj[0].keys()
    # 获取所有的数据部分，二维嵌套列表
    data = [i.values() for i in list_obj]

    # 先写入表头部分，一行数据，参数是一个一维列表
    csv_writer.writerow(sheet)
    # 再写入数据部分，多行数据，参数是一个二维的列表
    csv_writer.writerows(data)

    # 关闭文件对象
    csv_file.close()
    json_file.close()

if __name__ == '__main__':
    json_to_csv()
