from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookOrder
from django.db.models.manager import Manager
from django.db.models import Q, F, Count
from django.db import connection

def index(request):
    print(type(Book.objects))
    return HttpResponse('index')

def index2(request):
    # id 大于2的图书
    # books = Book.objects.filter(id__gte=2)
    # # id 大于2 并且不包含id=3 de 图书
    # books = books.filter(~Q(id=3))
    # 链式调用:
    # books = Book.objects.filter(id__gte=2).filter(~Q(id=3))
    # 上面一句等同于下面这句
    # books = Book.objects.filter(id__gte=2).exclude(id=3)
    # print(books)
    # print(type(books))

    # annotate 给模型添加字段
    books = Book.objects.annotate(author_name=F('author__name'))
    print(books.query)
    for i in books:
        print('%s, %s' % (i.name, i.author_name))
    print(connection.queries)
    return HttpResponse('Index2')

def inser_book_order(request):
    # 添加订单
    # 方式一：
    # book = Book.objects.get(pk=4)
    # book_order = BookOrder(price=288)
    # book_order.book_id = book.id
    # book_order.save()

    # 方式二
    book = Book.objects.get(pk=4)
    book_order = BookOrder(price=199)
    book.bookorder_set.add(book_order, bulk=False)
    return HttpResponse('inser order success')

def index3(request):
    # 1 根据create_time 从小到大排序
    orders= BookOrder.objects.order_by('create_time')
    # 2 根据create_time 从大到小排序
    # orders = BookOrder.objects.order_by('-create_time')
    # 3 首先根据create_time从大到小, 如果create_time是一样的，
    # 那么根据price从大到小
    # orders = BookOrder.objects.order_by('-create_time', '-price')
    # 4 根据订单的评分来排序, 从小到大
    # orders = BookOrder.objects.order_by('book__rating')

    # 5 根据图书销量从大到小进行排序
    books = Book.objects.annotate(order_nums=Count('bookorder')).order_by('-order_nums')
    for book in books:
        print('%s %s ' % (book.name, book.order_nums))
    return HttpResponse('Index3')