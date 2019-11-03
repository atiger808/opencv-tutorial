from django.db import models

# Create your models here.
class Article(models.Model):
    # 如果想使用自己定义的field作为主键， 必须设置primary_key=True
    id = models.BigAutoField(primary_key=True)
    # 在定义字段的时候，如果没有指定null=True, 那么默认情况下， null=False
    # 就是不能为空
    # 如果要使用可以为null的BooleanField, 那么应该使用NullBooleanField (可以为空)
    # 来代替BooleanField
    removed = models.NullBooleanField()
    # CharField, 默认必须定义max_length属性， 如果超过254个字符， 就不建议使用了
    # 就推荐使用TextField,
    title = models.CharField(max_length=200)
    # auto_now_add: 是在第一次添加数据进去的时候会自动获取当前时间
    # auto_now: 每次这个对象调用save方法的时候会将当前的时间更新
    # 创建时间 auto_now_add = True
    # 更新时间 auto_now = True
    create_time = models.DateTimeField(auto_now=True)

class Person(models.Model):
    # ModelForm
    # EmailField 在数据库层面并不会限制字符串一定要满足邮箱格式
    # 只是在以后使用ModelForm等表单相关的操作的时候会起作用
    email = models.EmailField()
    signature = models.TextField()

