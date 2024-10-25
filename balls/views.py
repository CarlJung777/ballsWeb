              ### 视图 ###
# 在 Django 中，网页和其他内容都是从视图派生而来
# 视图函数,处理用户的 HTTP 请求，并返回一个 HTTP 响应
# request 对象包含了用户的所有请求信息
# 用户通过浏览器访问此试图函数对应的url时，Djangojiu hui就会调用这个函数 

# ！！每个视图必须做到：返回一个包含被请求页面内容的 HttpResponse 对象或者抛出一个异常 ！！


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# 视图函数构建后，在 urls urlpatterns 中添加调用
def my_view(request):
    return HttpResponse("Hello, lllll. balls")

# 如果找不到数据库中的对象，则抛出错误
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "balls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# 载入 index.html 模板文件，给它传递一个上下文(context)
# 这个上下文是一个字典，它将模板内的变量映射为 Python 对象
def index(request):
    # ORM 对象关系映射 (Object–relational mapping)
    # 按 pub_date 字段降序排列（“-”表示降序）
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # 构建字典
    context = {"latest_question_list": latest_question_list}
    # render("请求对象", "模板文件路径", context="上下文数据字典", content_type="内容类型", status="状态码", using="模板引擎")
    return render(request, "balls/index.html", context)