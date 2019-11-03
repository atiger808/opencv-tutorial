# _*_ coding: utf-8 _*_
# @Time     : 2019/5/11 14:45
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def login(request):
    next = request.GET.get('next')
    text = '登录页面， 登录完成后要跳转的url： %s' % next
    return HttpResponse(text)

def book(request):
    return HttpResponse('读书页面')

def book_detail(request, book_id, category):
    text = '你的图书ID是 %s 图书分类：%s' % (book_id, category)
    return HttpResponse(text)

def movie(request):
    return HttpResponse('电影页面')

def city(request):
    return HttpResponse('同城页面')