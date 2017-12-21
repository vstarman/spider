# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


from decimal import Decimal


########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None

    # ----------------------------------------------------------------------
    @property
    def fee(self):
        """
        Return the current fee
        """
        return self._fee

    # ----------------------------------------------------------------------
    @fee.setter
    def fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
    # fee = property(get_fee, set_fee)




if __name__ == '__main__':
    f = Fees()
    f.fee('809880')
    print f.fee
    # person = Person('徐', '伟')
    # print person.first_name
    # print person.last_name
    # print person.full_name
    # isinstance()

