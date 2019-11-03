# _*_ coding: utf-8 _*_
# @Time     : 2019/5/11 22:10
# @Author   : Ole211
# @Site     : 
# @File     : views.py    
# @Software : PyCharm
from django.shortcuts import render
from django.db import connection


def index(request):
    cur = connection.cursor()
    # cur.execute("insert into book(id, name, author) values(null, '西游记', '施耐庵')")
    cur.execute("select * from book")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')