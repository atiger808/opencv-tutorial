from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False, default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        # <Book: (name, author, price, date)>
        return "<Book: ({name}, {author}, {price}, {date})>".format(name=self.name, author=self.author,
                                                                    price=self.price, date=self.date)