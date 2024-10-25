# from django.shortcuts import render

# Create your views here.
# 视图函数,处理用户的 HTTP 请求，并返回一个 HTTP 响应
# request 对象包含了用户的所有请求信息
# 用户通过浏览器访问此试图函数对应的url时，Djangojiu hui就会调用这个函数 
# def my_view(request):
#     return render(request, 'index.html', {"message": "Hello, world. balls"})


from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world. balls")
