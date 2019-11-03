# _*_ coding: utf-8 _*_
# @Time     : 2019/5/10 18:14
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm
from django.shortcuts import render

class Person(object):
    def __init__(self, username):
        self.username = username

def index(request):
    p = Person('张三')
    context = {
        'username':'shuaibin',
        'person': p,
        'person_dic': {
            'username': '李四',
            'age': 19,
            'keys': 'ppww',
        },
        'persons': [
            '红楼梦',
            '西游记',
            '三国演义',
        ]
    }
    return render(request, 'index.html', context=context)