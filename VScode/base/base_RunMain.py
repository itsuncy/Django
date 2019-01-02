# coding: utf-8
# @Author: WuKong.Sun
# @Date:2018.10.28
# @Describe: 接口请求方法的封装

import requests
import json


class RunMain:
    def send_get(self, url, data):
        response = requests.get(url=url, data=data).json()  # 将结果转换成了dict格式
        return response

    def send_post(self, url, data):
        response = requests.post(url=url, data=data).json()
        return response

    def run_main(self, url, method, data):
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

if __name__ == "__main__":

    url = "http://127.0.0.1:8000/login/"
    data = {
        'username': 'admin',
        'password': '123456'
    }
    response = RunMain().run_main(url, "POST", data)
    result = json.dumps(response, indent=4, ensure_ascii=False)
    print(result)

    # fiddler抓的接口为：https://www.imooc.com/index/getstarlist
    # url = "http://www.imooc.com/index/getstarlist"  # 为什么在代码中的url要去掉s，加s就报错
    # data = None
    # result = RunMain().run_main(url, "GET", data)
    # print(result)
