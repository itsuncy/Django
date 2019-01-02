import unittest
from RunMain import RunMain

class TestMethod(unittest.TestCase):

    def test_01(self):
        url = "http://www.imooc.com/index/getstarlist"  # 为什么在代码中的url要去掉s，加s就报错
        data = None
        run = RunMain
        res = run.run_main(url,"GET",data)
        print("这是个测试方法1")

    def test_02(self):
        print("这是个测试方法2")


if __name__ == '__main__':
    unittest.main()
