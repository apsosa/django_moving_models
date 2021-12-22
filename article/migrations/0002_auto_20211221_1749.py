# Generated by Django 2.2 on 2021-12-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
