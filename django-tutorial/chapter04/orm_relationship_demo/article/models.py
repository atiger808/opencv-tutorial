from django.db import models
from frontuser.models import FrontUser


class Category(models.Model):
    name = models.CharField(max_length=100)

# 如果想要引用其他app的模型
# app.模型名字
def default_category():
    return Category.objects.get(pk=2)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name='articles')
    author = models.ForeignKey('frontuser.FrontUser', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'Article:(id: %s, title: %s)' % (self.id, self.title)

class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=False)
    # 或者
    # origin_comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)