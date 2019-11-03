from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        return redirect(reverse('font:login'))


def login(request):
    return HttpResponse('前台登录页面')