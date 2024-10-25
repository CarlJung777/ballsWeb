from django.urls import path

# 当前目录导入 views 模块
from . import views

# 列表  存储 URL 和视图函数的映射关系
urlpatterns = [
    # "" 表示 URL 为空字符串，也就是根路径，通常代表网站的主页（如 http://localhost:8000/）
    path("", views.my_view, name="my_view"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]