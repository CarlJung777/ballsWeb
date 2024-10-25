# from django.shortcuts import render

# Create your views here.
# 视图函数,处理用户的 HTTP 请求，并返回一个 HTTP 响应
# request 对象包含了用户的所有请求信息
# 用户通过浏览器访问此试图函数对应的url时，Djangojiu hui就会调用这个函数 
# def my_view(request):
#     return render(request, 'index.html', {"message": "Hello, world. balls"})


from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def my_view(request):
    return HttpResponse("Hello, world. balls")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "balls/index.html", context)