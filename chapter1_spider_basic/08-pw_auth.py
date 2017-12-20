# -*- coding:utf-8 -*-
import urllib2
import cookielib


def send_request():
    user_name = 'bigcat'
    password = '123456'
    url = "http://192.168.93.57"

    # 1. 创建密码管理器对象
    pw_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 2. 添加账户密码信息，分别表示域服务器信息（一般写None），服务器url，账户名，密码
    pw_manager.add_password(None, url, user_name, password)
    # 3. 构建一个HTTP web 验证的处理器对象，构建自定义opener对象，发送请求即可
    auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr=pw_manager)
    # 4.定义opener对象
    opener = urllib2.build_opener(auth_handler)
    response = opener.open(url)

    return response.read()

if __name__ == '__main__':
    print send_request()
