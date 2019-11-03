from django.shortcuts import render
from django.http  import HttpResponse
from django.db.models import Avg
from .models import Book
from django.db import connection

def index(request):
    # 获取图书的定价平均价
    result = Book.objects.aggregate(Avg('price'))
    print(result)
    # 聚合函数aggregate 获取sql语句方法
    # 先引入 from django.db import connection
    # 再执行 connection.queries
    print(connection.queries)
    return HttpResponse('Success')