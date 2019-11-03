from django.shortcuts import render
from .models import Article, Category
from django.http import HttpResponse
from frontuser.models import FrontUser
# Create your views here.

def index(request):
    category = Category(name='最新文章')
    category.save()
    author = FrontUser(username='莫言')
    author.save()
    article = Article(title='红高粱', content=r'相对湿度是的深V烦得很11wd')
    article.category = category
    article.author = author
    article.save()

    article = Article.objects.first()

    print(article.title, article.content, article.category.name)
    return HttpResponse('Success')

def delete_view(request):
    category = Category.objects.get(pk=1)
    category.delete()
    category.save()
    return HttpResponse('delete success')

def one_to_manay(request):
    # 1. 添加文章
    # article = Article(title='流浪地球', content='十大是的菜市场删除')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    # article.category = category
    # article.author = author
    # print(category.name)
    # print(author.username)
    # article.save()
    # return HttpResponse('Success')

    # 2. 获取某分类下的所有文章
    # category = Category.objects.first()
    # 2.1 使用category_article_set.all()
    # articles = category.article_set.all()
    # 2.2如果要使用category.articles 需要在Article模型里category添加related_name='articles' 属性
    # articles = category.articles.all()
    # for article in articles:
    #     print(article.id,article.title)
    # return HttpResponse('sucess')

    # 3.1 另一种方式添加文章 category_id 可以为空的情况 null=True的情况
    # category = Category.objects.first()
    # print(category)
    # article = Article(title='爷爷', content='sdffea22122')
    # article.author = FrontUser.objects.first()
    # article.save()
    # category.articles.add(article)
    # category.save()
    # return HttpResponse('Success')

    # 3.2 category_id 不能为空 null=False的情况
    category = Category.objects.first()
    print(category)
    article = Article(title='爷爷', content='sdffea22122')
    article.author = FrontUser.objects.first()
    # 加上 参数bulk=False 不用.save就直接保存数据库
    category.articles.add(article, bulk=False)
    return HttpResponse('Success')

