# coding: utf-8
# @Author: WuKong.Sun
# @Date:2018.11.01
# @Describe: 1.提取响应结果做为其他方法的入参
#            2.通过添加注解和容器，实现对用例执行的管理

import unittest
import json
from base_RunMain import RunMain


class testMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://127.0.0.1:8000/login/"  # django项目接口
        data = {
            "username": "suncy",
            "password": "123456"
        }
        res = self.run.run_main(url, "POST", data)
        self.assertEqual(res["retCode"], 200, "测试失败")
        # 通过定义全局变量的方法，提取响应中的字段结果
        globals()['userid'] = res["retCode"]
        # print(res)

    # @unittest.skip("test_02")
    # 通过给方法添加注解，skip容器，实现跳过对应的用例不执行
    def test_02(self):
        print(userid)
        url = "http://127.0.0.1:8000/login/"  # django项目接口
        data = {
            "username": "admin_123",
            "password": "123456_abc"
        }
        res = self.run.run_main(url, "POST", data)
        self.assertEqual(res["retCode"], 200, "测试失败")
        # print(res)


if __name__ == "__main__":
    # 通过创建TestSuite这个容器，往里添加case名字，来实现执行部份用例的控制
    suite = unittest.TestSuite()
    suite.addTest(testMethod("test_01"))
    suite.addTest(testMethod("test_02"))
    unittest.TextTestRunner().run(suite)
    # unittest.main()
