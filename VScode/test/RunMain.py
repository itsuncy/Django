
# coding: utf-8

import requests
import json


class RunMain:
    def __init__(self, url, method, data):
        self.request = self.run_main(url, method, data)

    def send_get(self, url, data):
        response = requests.get(url=url, data=data).json() #将结果转换成了dict格式
        return json.dumps(response, indent=2, ensure_ascii=False) #dumps将结果转换成了str格式

    def send_post(self, url, data):
        response = requests.post(url=url, data=data).json()
        return json.dumps(response, indent=2, ensure_ascii=False)

    def run_main(self, url, method, data):
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == "__main__":
    # fiddler抓的接口为：https://www.imooc.com/index/getstarlist
    url = "http://www.imooc.com/index/getstarlist"  # 为什么在代码中的url要去掉s，加s就报错
    data = None
    result = RunMain(url, 'GET', data)
    print(result.request)
    
# data = {
#   'username':'admin',
#   'password':'123456'
#   }
# url = "http://127.0.0.1:8000/login/"
# result = RunMain(url,'POST',data)
# print(result.request)
