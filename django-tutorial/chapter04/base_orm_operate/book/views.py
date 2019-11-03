from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    # 1. 使用ORM添加一条数据到数据库
    # book = Book(name='三国演义', author='罗贯中', price=199)
    # book.save()

    # 2. 查询
    # 2.1. pk根据主键进行查找
    # book = Book.objects.get(pk=1)
    # print(book)
    # 2.2 根据其他条件进行查找
    # books = Book.objects.filter(name='西游记').first()
    # print(books)

    # 3. 删除数据
    # book = Book.objects.get(pk=2)
    # book.delete()

    # 4. 修改数据
    book = Book.objects.get(pk=3)
    book.price = 300
    book.save()
    return HttpResponse('图书添加成功')
    # return render(request, 'index.html')
