from django.shortcuts import render, redirect, reverse
from django.db import connection
# Create your views here.

def get_cursor():
    return connection.cursor()

def index(request):
    cur = get_cursor()
    cur.execute("select id, name, author from book")
    books = cur.fetchall()
    # for i in books:
    #     print(i)
    return render(request, 'index.html', context={'books': books})

def book_add(request):
    if request.method == 'GET':
        return render(request, 'book_add.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into book(id, name, author) values(null, '%s', '%s')" % (name, author))
        return redirect(reverse('index'))

def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select id, name, author from book where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request, 'book_detail.html', context={'book': book})

def book_delete(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id='%s'" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError('删除图书method错误')

def book_edit(request):
    if request.method == 'GET':
        book_id = request.GET.get('book_id')
        cursor = get_cursor()
        cursor.execute("select id, name, author from book where id='%s'" % book_id)
        book = cursor.fetchone()
        return render(request, 'book_edit.html', context={'book': book, 'msg':''})
    elif request.method == 'POST':
        book_id = request.POST.get('book_id')
        name = request.POST.get('name')
        author = request.POST.get('author')
        if name and author:
            cursor = get_cursor()
            cursor.execute("update book set name='%s', author='%s' where id='%s'" % (name, author, book_id))
            return redirect(reverse('index'))
        else:
            print('内容不能为空')
            return render(request, 'error_msg.html', context={'msg': '内容不能为空'})
    else:
        raise RuntimeError('method 错误')





