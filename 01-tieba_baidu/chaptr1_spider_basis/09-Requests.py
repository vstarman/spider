# -*- coding:utf-8 -*-
import os
import sys
import random
import requests
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from tools import MY_IP_POLL, MY_USER_AGENT


# 测试百度
def rest_baidu():
    kw = {'wd': '长春'}
    headers = {"User-Agent": random.choice(MY_IP_POLL)}

    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print type(response.text)

    # 查看响应内容，response.content返回的字节流数据
    print type(response.content)

    print response.url

    print response.encoding

    print response.status_code


# 测试有道
def test_youdao():
    form_data = {
        'i': '我爱你',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1513422483031',
        'sign': '8196a8760ea7656ec30548ddae197d77',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'true',
    }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=form_data, headers=headers)
    print response.text


# 测试代理
def test_proxies():
    proxies = {'http': 'mr_mao_hacker:sffqry9r@120.27.218.32:16816'}
    # export HTTP_PROXY = {'http': 'mr_mao_hacker:sffqry9r@120.27.218.32:16816'}

    response = requests.get("http://www.baidu.com", proxies=proxies)
    print response.text


# 测试coolie
def test_cookie():
    response = requests.get("http://www.baidu.com/")
    # 获取cookie对象
    cookie_jar = response.cookies
    # 将对象转为字典
    cookie_dic = requests.utils.dict_from_cookiejar(cookie_jar)
    print cookie_jar
    print '-' * 100
    print cookie_dic


# 测试session
def test_session():
    # 1. 创建session对象，可以保存Cookie值
    session = requests.session()

    # 2. 处理 headers
    headers = {
        "User-Agent": random.choice(MY_USER_AGENT)}

    # 3. 需要登录的用户名和密码
    data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

    # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
    session.post("http://www.renren.com/PLogin.do", data=data)

    # 5. session包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = session.get("http://www.renren.com/410043129/profile")
    print response.text


# 检查ssl证书
def test_ssl():
    # response = requests.get('https://www.baidu.com', verify=False)
    response = requests.get("https://www.12306.cn/mormhweb/", verify=False)
    print response.text

if __name__ == '__main__':
    # youdao_trans()
    # test_proxies()
    # test_cookie()
    # test_session()
    test_ssl()
