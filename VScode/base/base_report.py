# coding: utf-8
# @Author: WuKong.Sun
# @Date:2018.11.01
# @Describe: 通过HTMLTestRunner生成测试报告

import unittest
import HTMLTestRunner
import time
import sys
sys.path.append('D:\\Program Files\\Django\\VScode\\report')
from base_RunMain import RunMain
from reports_path import testReports_path
class testMethod(unittest.TestCase):
    
    print(sys.path)
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
        # globals()['userid'] = res["retCode"]
        # print(res)

    # @unittest.skip("test_02")
    # 通过给方法添加注解，skip容器，实现跳过对应的用例不执行
    def test_02(self):
        # print(userid)
        url = "http://127.0.0.1:8000/login/"  # django项目接口
        data = {
            "username": "admin_123",
            "password": "123456_abc"
        }
        res = self.run.run_main(url, "POST", data)
        self.assertEqual(res["retCode"], 200, "测试失败")
        # print(res)


if __name__ == "__main__":
    # setPath = "D:/Program Files/Django/VScode/report/"
    # 获取生成报告文件的存储路径
    setPath = testReports_path()
    # 获取系统日期+时间
    getTime = time.strftime('/%Y-%m-%d %H%M%S', time.localtime(time.time()))
    # 将测试报告以路径+日期的格式生成
    fileName = setPath + getTime + "测试报告.html"
    fp = open(fileName, "wb")  # wb 读写格式打开
    # 通过创建TestSuite这个容器，往里添加case名字，来实现执行部份用例的控制
    suite = unittest.TestSuite()
    # 将test_01和test_02两个用例放到容器里
    suite.addTest(testMethod("test_01"))
    suite.addTest(testMethod("test_02"))
    # 通过HTMLTestRunner将测试结果，生成测试报告
    report = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title="测试报告", verbosity=1, description="Django登录接口测试", tester="WuKong.Sun")
    report.run(suite)
    # unittest.TextTestRunner().run(suite)
    # unittest.main()
