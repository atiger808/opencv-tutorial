from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    '''
    在windows 操作系统中mysql的排序规则(collation)是utf8-genneral
    无论什么都是大小写不敏感
    在linux 系统下 mysql的排序规则(collation)是utf8-bin
    则大小写敏感
    exact 和 iexact 区别就是=和like 的区别，
    exact会被翻译成=, iexact会被翻译成LIKE
    '''
    article = Article.objects.filter(title__exact='Hello World')
    print(article.query)
    print(article)
    article2 = Article.objects.filter(title__iexact='Hello World')
    # 获取sql语句：article.query
    print('=='*30)
    print(article2.query)
    print(article2)
    return HttpResponse('success')

def index1(request):
    # get 返回的是orm模型， filter返回的是QuerySet
    article = Article.objects.filter(pk=1)
    print(type(article))
    print(article)
    return HttpResponse('success')

def index2(request):
    # contains 区分大小写
    # icontains 不区分大小写
    result = Article.objects.filter(title__icontains='背')
    print(result)
    return HttpResponse('success')