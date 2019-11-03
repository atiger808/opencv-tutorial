# _*_ coding: utf-8 _*_
# @Time     : 2019/5/18 2:03
# @Author   : Ole211
# @Site     : 
# @File     : urls.py    
# @Software : PyCharm
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]