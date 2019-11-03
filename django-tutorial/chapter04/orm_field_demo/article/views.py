from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Person

def index(request):
    # article = Article()
    # article.save()
    # article = Article.objects.get(pk=2)
    # article.title = '背影'
    # article.removed = False
    # article.save()
    from datetime import datetime
    article = Article.objects.get(pk=2)
    create_time = article.create_time
    print(create_time)
    print('==='*30)
    # print(localtime(create_time))
    return render(request, 'index.html', context={'create_time': create_time})
    return HttpResponse('Success')

def email_view(request):
    p = Person(email='qq.com')
    p.save()
    return HttpResponse('Success')