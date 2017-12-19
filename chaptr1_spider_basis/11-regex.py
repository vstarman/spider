# -*- coding:utf-8 -*-
import re


def test_re():
    """测试re模块"""
    s = 'hello world, this is so beautiful!'
    s_list = s.split(" ")
    print s_list
    s2 = "`".join(s_list)
    print s2
    p = re.compile(r'(o+ )')
    print p.sub(r"\1`\1`\1", s)
    print p.sub(r"\1`\1`\1", s, 1)


def test_unicode():
    s = u'hello, bad 这是一道光 bad world. '
    # \u4e00 - \9fa5 中文范围
    p = re.compile(ur'[^\u4e00-\u9fa5]+')
    s_list = p.findall(s)
    print s_list   # unicode str list
    for i in s_list:
        print i.encode('utf-8')

    # 将字符串非中文部分都删除
    print p.sub('', s)


def filter_chinese():
    """过滤中文"""
    s = u'hello, 中国, you are so 美丽'
    pattern = re.compile(ur'[\u4e00-\u9fa5]+')
    chinese_list = pattern.findall(s)
    print ''.join(chinese_list)

if __name__ == '__main__':
    # test_re()
    # test_unicode()
    filter_chinese()
