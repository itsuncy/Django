# coding: utf-8
# @Author: WuKong.Sun
# @Date:2018.10.31
# @Describe: unittest测试案例及断言的使用

import unittest
import json
from base_RunMain import RunMain

class testMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://www.imooc.com/index/getstarlist"
        data = None
        res = self.run.run_main(url, "GET", data)
        self.assertEqual(res["msg"], '成功', "测试失败")
        # print(res)

    def test_02(self):
        url = "http://127.0.0.1:8000/login/"  # django项目接口
        # url = "http://dev-hanzi.lqdzj.cn/ajax_stroke_search?q=%E4%B8%80%E2%BF%B1&mode=1"
        data = {
            "username": "admin_123",
            "password": "123456_abc"
        }
        res = self.run.run_main(url, "POST", data)
        # if res["retCode"] == 200:
        #     print("测试通过")
        # else:
        #     print('测试失败')
        self.assertEqual(res["retCode"], 200, "测试失败")
        # self.assertEqual(res["retMessage"], "成功", "测试通过")
        # print(res)


if __name__ == "__main__":
    unittest.main()
