# _*_ coding: utf-8 _*_
# @Time     : 2019/5/17 16:32
# @Author   : Ole211
# @Site     : 
# @File     : forms.py    
# @Software : PyCharm
from django import forms

class MessageBordForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='标题：', error_messages={'min_length': '最少不能少于一个字符'})
    content = forms.CharField(widget=forms.Textarea, label='内容：', error_messages={'required':'内容不能为空'})
    email = forms.EmailField(label='邮箱：', error_messages={'required': '邮箱格式不正确'})
    reply = forms.BooleanField(required=False, label='是否回复：')