# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


if __name__ == '__main__':
    person = Person('徐', '伟')
    print person.first_name
    print person.last_name
    print person.full_name

