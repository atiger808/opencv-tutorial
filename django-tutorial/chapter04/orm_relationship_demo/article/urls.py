# _*_ coding: utf-8 _*_
# @Time     : 2019/5/14 18:05
# @Author   : Ole211
# @Site     : 
# @File     : urls.py    
# @Software : PyCharm
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/', views.delete_view, name='delete_view'),
    path('one_to_many/', views.one_to_manay, name='one_to_many'),
]
