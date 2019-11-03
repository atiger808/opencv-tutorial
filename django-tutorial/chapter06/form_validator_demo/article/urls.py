# _*_ coding: utf-8 _*_
# @Time     : 2019/5/18 1:41
# @Author   : Ole211
# @Site     : 
# @File     : urls.py    
# @Software : PyCharm
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('s/<article_id>/', views.detail, name='detail'),
]