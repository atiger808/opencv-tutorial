from django.shortcuts import render
from .models import Article, Category
from bs4 import BeautifulSoup as bs
import requests
import re


def get_article(article_url):
    res = requests.get(article_url)
    soup = bs(res.text, 'html.parser')
    content = soup.find_all('div', class_='topic-content')[0].text
    title = soup.find(class_='topic-title-main').find('h1').text
    return title, content, article_url

pages = set()
def crawl(offset):
    global pages
    base_url = 'http://ism002.com'
    url = 'http://ism002.com/story/p/{}'.format(offset)
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    for link in soup.findAll('a', href=re.compile('(/story/s/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                pages.add(base_url + link.attrs['href'])
    return pages


def crawl_main(request):
    pages = crawl(1)
    for article_url in pages:
        title, content, url = get_article(article_url)
        exists = Article.objects.filter(title=title).exists()
        if exists:
            continue
        else:
            Article(title=title, content=content, url=article_url).save()
            print('%s----保存成功' % (article_url))
    return render(request, 'article/index.html')

def index(request):
    articles = Article.objects.all()
    for i in articles:
        print(i.title)
        print(i.url)
    return render(request, 'article/index.html', context={'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'article/detail.html', context=context)


