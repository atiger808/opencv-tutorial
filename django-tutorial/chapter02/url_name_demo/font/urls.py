# _*_ coding: utf-8 _*_
# @Time     : 2019/5/9 18:02
# @Author   : Ole211
# @Site     : 
# @File     : urls.py    
# @Software : PyCharm


from django.urls import path
from . import  views

# 应用命名空间
# 应用命名空间的变量叫做app_name
app_name = 'font'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.login, name='login'),
]