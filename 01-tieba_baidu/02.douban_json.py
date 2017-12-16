# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
import random
from tieba_floder.settings import MY_USER_AGENT
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"
    headers = {"User-Agent": random.choice(MY_USER_AGENT)}

    # 变动的是这两个参数，从start开始往后显示limit个
    form_data = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '10'
    }
    # 参数编码
    params = urllib.urlencode(form_data)

    request = urllib2.Request(url + params, headers=headers)
    response = urllib2.urlopen(request)

    resp_str = response.read()
    print type(repr(resp_str)),
    resp_list = json.loads(resp_str)
    # print resp_list
    print resp_str

