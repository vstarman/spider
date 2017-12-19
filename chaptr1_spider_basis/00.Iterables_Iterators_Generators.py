# -*- coding:utf-8 -*-
# 详解python数据结构
import cmath
# from BitVector import BitVector
from itertools import islice


class DataStructure(object):
    """详解迭代对象,迭代器,生成器"""
    @staticmethod
    def assert_container():
        """判断是否是容器"""
        assert 1 in [1, 2, 3], AssertionError('容器不包含该元素')
        assert 4 not in [1, 2, 3], AssertionError('容器不包含该元素')
        assert 1 in {1, 2, 3}, AssertionError('容器不包含该元素')
        assert 1 in (1, 2, 3), AssertionError('容器不包含该元素')
        assert 1 in {1: 'foo', 2: 'bar', 3: 'qux'}, AssertionError('容器不包含该元素')
        assert 'foo' in 'book info', AssertionError('容器不包含该元素')


class Fib:
    @staticmethod  # known case of __new__
    def __new__(cls, *more):  # known special case of object.__new__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def next(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

    @classmethod
    def run(cls):
        f = Fib()
        list(islice(f, 0, 10))


class BloomFilter(object):
    """布隆过滤器"""
    def __init__(self, error_rate, elementNum):
        #计算所需要的bit数
        self.bit_num = -1 * elementNum * cmath.log(error_rate) / (cmath.log(2.0) * cmath.log(2.0))

        #四字节对齐
        self.bit_num = self.align_4byte(self.bit_num.real)

        #分配内存
        self.bit_array = BitVector(size=self.bit_num)

        #计算hash函数个数
        self.hash_num = cmath.log(2) * self.bit_num / elementNum

        self.hash_num = self.hash_num.real

        #向上取整
        self.hash_num = int(self.hash_num) + 1

        #产生hash函数种子
        self.hash_seeds = self.generate_hashseeds(self.hash_num)

    def insert_element(self, element):
        for seed in self.hash_seeds:
            hash_val = self.hash_element(element, seed)
            #取绝对值
            hash_val = abs(hash_val)
            #取模，防越界
            hash_val = hash_val % self.bit_num
            #设置相应的比特位
            self.bit_array[hash_val] = 1

    #检查元素是否存在，存在返回true，否则返回false
    def is_element_exist(self, element):
        for seed in self.hash_seeds:
            hash_val = self.hash_element(element, seed)
            #取绝对值
            hash_val = abs(hash_val)
            #取模，防越界
            hash_val = hash_val % self.bit_num

            #查看值
            if self.bit_array[hash_val] == 0:
                return False
        return True

    #内存对齐
    def align_4byte(self, bit_num):
        num = int(bit_num / 32)
        num = 32 * (num + 1)
        return num

    #产生hash函数种子,hash_num个素数
    def generate_hashseeds(self, hash_num):
        count = 0
        #连续两个种子的最小差值
        gap = 50
        #初始化hash种子为0
        hash_seeds = []
        for index in xrange(hash_num):
            hash_seeds.append(0)
        for index in xrange(10, 10000):
            max_num = int(cmath.sqrt(1.0 * index).real)
            flag = 1
            for num in xrange(2, max_num):
                if index % num == 0:
                    flag = 0
                    break

            if flag == 1:
                #连续两个hash种子的差值要大才行
                if count > 0 and (index - hash_seeds[count - 1]) < gap:
                    continue
                hash_seeds[count] = index
                count = count + 1

            if count == hash_num:
                break
        return hash_seeds

    def hash_element(self, element, seed):
        hash_val = 1
        for ch in str(element):
            chval = ord(ch)
            hash_val = hash_val * seed + chval
        return hash_val


def fib():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, curr + prev

if __name__ == '__main__':
    # data_structure = DataStructure()
    # data_structure.assert_container()
    f = Fib()
    print list(islice(f, 0, 10))
    # f = fib()
    # print list(islice(f, 0, 10))

