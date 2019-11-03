from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return "<Article(id:%s, title:%s)>" % (self.pk, self.title)

    # 更改表名
    class Meta:
        db_table = 'article'