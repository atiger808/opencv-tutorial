# _*_ coding: utf-8 _*_
# @Time     : 2019/5/17 17:32
# @Author   : Ole211
# @Site     : 
# @File     : forms.py    
# @Software : PyCharm
from django import forms
from .models import User
from django.core import validators

class MyForm(forms.Form):
    # email = forms.EmailField(error_messages={'invalid': '请输入一个有用的邮箱地址'})
    # price = forms.FloatField(error_messages={'invalid': '请输入浮点类型数据'})
    # personal_website = forms.URLField(error_messages={'invalid':'请输入正确格式的个人网站', 'required': '请输入个人网站！'})
    # 验证器
    # 验证手机号格式
    email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确的邮箱！')])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号！')])

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=40, min_length=2, label='账户')
    password = forms.CharField(max_length=40, min_length=6, label='密码')
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号')], label='手机号')

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError('手机号已经存在')
        return telephone

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('账户已经被注册')
        return username