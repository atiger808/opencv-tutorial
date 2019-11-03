from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categpry'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    url = models.URLField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'

