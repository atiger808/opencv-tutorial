# _*_ coding: utf-8 _*_
# @Time     : 2019/5/10 19:57
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm

from django.shortcuts import render

def index(request):
    context = {
        'books':[
            '三国演义',
            '红楼梦',
            '西游记'
        ],
        'book_lists':[
            {
                'name': '水浒传',
                'auth': '施耐庵',
                'price': 155
            },
            {
                'name': '西游记',
                'auth': '吴承恩',
                'price': 199
            },
            {
                'name': '三国演义',
                'auth': '罗贯中',
                'price': 209
            },
            {
                'name': '红楼梦',
                'auth': '曹雪芹',
                'price': 188
            }
        ],
        'persons':{
            'age': 25,
            'username': 'jack',
        },
        'comments':[
            '非常好！',
            'good! 不错',
            '加油！',
            None

        ]
    }
    return render(request, 'index.html', context=context)