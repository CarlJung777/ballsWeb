"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 用户发起请求时，Django 找到名为 urlpatterns 的变量并按顺序遍历这些模式
# 例如找到 balls/ 之后，会剥离匹配的文本（"polls/"）
# 然后将剩余的文本发送给 'balls.urls' URL 配置
urlpatterns = [
    # path 最少要两个参数 route 和 view
    path('balls/', include('balls.urls')),
    path('admin/', admin.site.urls),

]
