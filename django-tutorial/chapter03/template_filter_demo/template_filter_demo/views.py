# _*_ coding: utf-8 _*_
# @Time     : 2019/5/11 15:43
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm
from django.shortcuts import render
from datetime import datetime

def greet(word):
    return 'hello, %s' % word

def index(request):
    context = {
        'greet': greet('lucy')
    }
    return render(request, 'index.html', context=context)

def add_views(request):
    context = {
        'value1': [1, 2, 3, 45,],
        'value2': [20, 30, 40, '50']
    }
    return render(request, 'add.html', context=context)

def cut_views(request):
    return render(request, 'cut.html')

def date_views(request):
    context = {
        'today': datetime.now()
    }
    return render(request, 'date.html', context=context)