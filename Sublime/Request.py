# coding: utf-8

import requests
import json

postData = {
	'username':'admin',
	'password':'123456'
	}
getData=None
postUrl = "http://127.0.0.1:8000/login/"
# fiddler抓的接口为：https://www.imooc.com/index/getstarlist
getUrl = "http://www.imooc.com/index/getstarlist"#为什么在代码中的url要去掉s，加s就报错
def send_get(url,data):
	response=requests.get(url=url, data=data).json()
	return json.dumps(response,indent=2,ensure_ascii=False)
def send_post(url,data):
	response=requests.post(url=url, data=data).json()
	return json.dumps(response,indent=2,ensure_ascii=False)
def run_main(url,data,method):
	if method =='GET':
		return send_get(url,data)
	else:
		return send_post(url,data)

if __name__ =="__main__":
	# print(run_main(getUrl,getData,'GET'))
	print(run_main(postUrl,postData,'POST'))