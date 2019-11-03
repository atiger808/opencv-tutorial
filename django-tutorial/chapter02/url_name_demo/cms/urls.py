# _*_ coding: utf-8 _*_
# @Time     : 2019/5/9 18:02
# @Author   : Ole211
# @Site     : 
# @File     : urls.py    
# @Software : PyCharm
from django.urls import path
from . import  views

app_name = 'cms'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]