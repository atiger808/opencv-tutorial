# _*_ coding: utf-8 _*_
# @Time     : 2019/5/10 19:43
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm
from django.shortcuts import render

def index(request):
    context = {
        'age': 13
    }
    return render(request, 'index.html', context=context)