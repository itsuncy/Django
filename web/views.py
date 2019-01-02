from django.shortcuts import render_to_response
from django.http.response import HttpResponse
import json


# Create your views here.
def login(request):
    # POST请求
    # http://127.0.0.1:8000/login/
    if request.method == 'POST':
        result = {

        }
        username = request.POST.get('username')
        password = request.POST.get('password')        
        result['isSuccess'] = 'S'
        result['retCode'] = 200
        result['retMessage'] = '成功'
        result['username'] = username
        result['password'] = password
        response = json.dumps(result)
        return HttpResponse(response, content_type='application/json;charset=utf-8')
    # GET请求
    # http://127.0.0.1:8000/login?username=admin&mobile=131123&date=20181025
    # elif request.method == 'GET':
    #     result = {}
    #     username = request.GET.get('username')
    #     mobile = request.GET.get('mobile')
    #     data = request.GET.get('date')
    #     result['user'] = username
    #     result['moblienum'] = mobile
    #     result['data'] = data
    #     response = json.dumps(result)
    #     return HttpResponse(response, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')
