from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'
