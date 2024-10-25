from django.urls import path

# 当前目录导入 views 模块
from . import views

app_name = "balls"

# 列表（存储 URL 和视图函数的映射关系）
urlpatterns = [
    # "" 表示 URL 为空字符串，也就是根路径，通常代表网站的主页（如 http://localhost:8000/）
    # <int:question_id>: 从URL中捕获一个整数值，然后赋值给 question_id
    # 如果用户访问 /5/vote/ ，5 就会被捕获并赋值给 question_id
    # 然后question_id传递给对应的函数
    # detail(request=<HttpRequest object>, question_id=34)
    
    # path("路径表达式", 视图函数, name="名称")
    path("", views.my_view, name="my_view"),
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]