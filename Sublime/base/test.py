# -*- coding: utf-8 -*-
# @Author: Suncy
# @Date:   2018-10-30 10:36:21
# @Last Modified by:   Suncy
# @Last Modified time: 2018-10-30 11:22:47
import unittest
from base_RunMain import RunMain

class testMethod(unittest.TestCase):
	def test_01(self):
		url = "http://www.imooc.com/index/getstarlist"  # 为什么在代码中的url要去掉s，加s就报错
		data = None
		run = RunMain(url,"GET",data).request
		print(run)

if __name__ == "__main__":
	unittest.main()
