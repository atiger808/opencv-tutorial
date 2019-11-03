"""book_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front import views
urlpatterns = [
    path('', views.index, name='index'),
    path('book_add/', views.book_add, name='book_add'),
    # re_path('book_detail/(?P<book_id>\d+)/', views.book_detail, name='book_detail'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_delete/', views.book_delete, name="book_delete"),
    path('book_edit/', views.book_edit, name='book_edit'),

]
