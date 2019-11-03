from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import MyForm, RegisterForm
from .models import User
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return render(request, 'front/index.html')

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # price = form.cleaned_data.get('price')
            # personal_website = form.cleaned_data.get('website')
            telephone = form.cleaned_data.get('telephone')
            print(email)
            # print(price)
            # print(personal_website)
            print(telephone)
            return HttpResponse('success')
        else:
            msg = form.errors
            print(msg)
            return render(request, 'front/index.html', context={'msg': msg})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'front/register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.cleaned_data.get('password')
            telephone = form.clean_telephone()
            user = User(username=username, password=password, telephone=telephone)
            user.save()
            return HttpResponse('register success')
        else:
            msg = form.errors
            print(msg)
            return render(request, 'front/msg.html', context={'msg': msg})

class LoginView(View):
    def get(self, request):
        return render(request, 'front/login.html')

    def post(self, request):
        if self.request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username__exact=username)
            print(user.username, user.password)
            print(user)
            if user and password==user.password:
                return HttpResponse('login success')
            else:
                return HttpResponse('login fail')

