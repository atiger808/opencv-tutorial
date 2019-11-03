from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price= models.FloatField(null=False, default=0)

# 1 makemigrations命令 生成迁移脚本文件
# python manage.py makemigrations
# 2 migrate命令 将生成的迁移脚本文件映射到数据库
# python manage.py migrate

class Published(models.Model):
    name = models.CharField(max_length=100, null=False)
    address =  models.CharField(max_length=100, null=False)