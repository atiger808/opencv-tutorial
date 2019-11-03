# Generated by Django 2.0 on 2019-05-15 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190515_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='article.Category'),
            preserve_default=False,
        ),
    ]
