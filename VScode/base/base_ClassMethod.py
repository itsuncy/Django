# coding: utf-8
# @Author: WuKong.Sun
# @Date:2018.10.20
# @Describe: setup类，方法和teardown类，方法的使用

import unittest

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后的方法")

    # 每次方法 之前执行
    # def setUp(self):
    # 	print('test-->setup')
    # 每次方法 之后执行
    # def tearDown(self):
    # 	print('test-->teardown')
    def test_01(self):
        print("这是个测试方法1")

    def test_02(self):
        print("这是个测试方法2")


if __name__ == '__main__':
    unittest.main()
