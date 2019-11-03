from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import MessageBordForm
from django.views.generic import View

class IndexViews(View):
    def get(self, request):
        form = MessageBordForm()
        return render(request, 'index.html', context={'form': form})

    def post(self, request):
        form = MessageBordForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print(title)
            print(content)
            print(email)
            print(reply)
            return HttpResponse('post sucess')
        else:
            print(form.errors)
            return HttpResponse('post fail')